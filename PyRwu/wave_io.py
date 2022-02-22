﻿'''wave_io

waveのIO関係のデータを扱います。

'''
import os
import os.path
import wave
from typing import Tuple

import numpy as np

def read(input_path: str, offset: float, end_ms: float) -> Tuple[np.ndarray, float]:
    '''

    指定された範囲のwavファイルを読み込み、データとサンプルレートを返します。

    Parameters
    ----------
    input_path: str
        原音のファイル名
    offset: float, default 0
        入力ファイルの読み込み開始位置(ms)
    end_ms: float, default 0
        入力ファイルの読み込み終了位置(ms)(省略可 default:0)
        正の数の場合、ファイル末尾からの時間
        負の数の場合、offsetからの時間

    Returns
    -------
    data: np.ndarray
        指定された区間のwaveのデータ。1次元
    framerate: float
        wavのサンプリング周波数

    Raises
    ------
    FileNotFoundError
        input_pathにwaveファイルがなかったとき
    TypeError
        input_pathで指定したファイルがwavではなかったとき
    '''
    if not os.path.exists(input_path):
        raise FileNotFoundError("{} not found.".format(input_path))
    try:
        with wave.open(input_path, "rb") as wr:
            channels: int = wr.getchannels()
            framerate: int = wr.getframerate()
            sampwidth: int = wr.getsampwidth()
            nframes: int = wr.getnframes() #フレーム数
            bytes_data: byte = wr.readframes()
    except:
        raise TypeError("{} can't read. this file isn't wave format.".format(input_path))
    
    byte_per_sec: int = channels * framerate * sampwidth
    wave_ms: float = nframes / byte_per_sec
    offset_frame: int = int(offset * 1000 / byte_per_sec)
    end_frame: int
    data: np.ndarray
    if end_frame >= 0:
        end_frame = int((wave_ms - end_ms) * 1000 / byte_per_sec)
    else:
        end_frame = int((offset - end_ms) * 1000 / byte_per_sec)
    bytes_data = bytes_data[offset_frame:end_frame]
    if sampwidth == 1:
        data= np.frombuffer(bytes_data, dtype = "int8")
    elif sampwidth == 2:
        data= np.frombuffer(bytes_data, dtype = "int16")
    elif sampwidth == 3:
        data = np.zeros(int((end_frame-offset_frame)/sampwidth), dtype = "int32")
        for i in range(len(int((end_frame-offset_frame)/sampwidth))):
            data[i] = int.from_bytes(bytes_data[i*sampwidth:(i+1)*sampwidth], "little", signed=True)
    elif sampwidth == 4:
        data= np.frombuffer(bytes_data, dtype = "int32")

    if channels==2:
        data = data [::2]

    return data, framerate