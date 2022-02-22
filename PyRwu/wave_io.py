'''wave_io

waveのIO関係のデータを扱います。

'''
import os
import os.path
import wave
from typing import Tuple

import numpy as np

def read(input_path: str, offset: float, end_ms: float) -> Tuple[np.ndarray, int]:
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
    data: np.ndarray or np.float64
        指定された区間のwaveのデータ。1次元
    framerate: int
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
            channels: int = wr.getnchannels()
            framerate: int = wr.getframerate()
            sampwidth: int = wr.getsampwidth()
            nframes: int = wr.getnframes() #フレーム数
            bytes_data: byte = wr.readframes(nframes)
    except:
        raise TypeError("{} can't read. this file isn't wave format.".format(input_path))
    
    wave_ms: float = nframes / framerate * 1000
    offset_frame: int = int(offset * framerate / 1000) * channels
    end_frame: int
    data: np.ndarray
    if end_ms >= 0:
        end_frame = int((wave_ms - end_ms) * framerate / 1000) * channels
    else:
        end_frame = int((offset - end_ms) * framerate / 1000) * channels
        
    bytes_data = bytes_data[offset_frame*sampwidth*channels:end_frame*sampwidth*channels]
    
    if sampwidth == 1:
        data = np.frombuffer(bytes_data, dtype="int8")
    elif sampwidth == 2:
        data = np.frombuffer(bytes_data, dtype="int16")
    elif sampwidth == 3:
        data = np.zeros(int((end_frame-offset_frame)), dtype = "int32")
        for i in range(int(len(bytes_data)/sampwidth)):
            data[i] = int.from_bytes(bytes_data[i*sampwidth:(i+1)*sampwidth], "little", signed=True)
    elif sampwidth == 4:
        data = np.frombuffer(bytes_data, dtype="int32")
    if channels==2:
        data = data [::2]
        
    return data/ 2**(sampwidth*8-1), framerate

def write(output_path: str,data: np.ndarray, framerate:int=44100, sampwidth: int=2):
    '''
    | waveファイルを保存します。
    | すでにwavファイルがある場合、上書きします。
    | もし、output_pathにいたるフォルダがなければ、再帰的に作成します。

    Parameters
    ----------
    output_path: str
        保存するwavのパス
    data: np.ndarray of np.float64
        保存するwavの波形データ
    framerate: int, default 44100
        保存するwavのサンプリング周波数
    sampwidth: int, default 2
        保存するwavのbit深度をバイト数で表したもの

    Raises
    ------
    OSError
        wavを書き出しする際、書き込み権限がなかった時。
    '''
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    byte_data: bytes = b""
    data = data * 2**(sampwidth*8-1)
    if sampwidth==1:
        data = data.astype("int8")
    elif sampwidth==2:
        data = data.astype("int16")
    elif sampwidth==3:
        data = data.astype("int32")
        for x in data:
            byte_data += x.to_bytes(3, "little", signed=True)
    elif sampwidth==4:
        data = data.astype("int32")
    with wave.open(output_path, "wb") as ww:
        ww.setparams((1, sampwidth, framerate, data.shape[0] * sampwidth, "NONE", "not compressed"))

        if sampwidth != 3:
            ww.writeframes(data.tobytes())
        else:
            ww.writeframes(byte_data)

