'''frq_io

frqのIO関係のデータを扱います。

'''
import os
import os.path
from typing import Tuple

import numpy as np

import pitch

def read(input_path: str, offset: float, end_ms: float, framerate: int, world_period: float) -> Tuple[np.ndarray, np.ndarray]:
    '''
    frqファイルを読み込み、指定された区間のworld時間軸のf0列に変換して返します。

    Parameters
    ----------
    input_path: str
        | frqファイルのパス
        | 事前にファイルがあることを確認すること
        
    offset: float, default 0
        入力ファイルの読み込み開始位置(ms)
    end_ms: float, default 0

        | 入力ファイルの読み込み終了位置(ms)(省略可 default:0)
        | 正の数の場合、ファイル末尾からの時間
        | 負の数の場合、offsetからの時間

    framerate: int
    
        | wavのサンプリング周波数

    world_period: float

            | worldデータの1フレーム当たりの時間(ms)
            | 初期設定では5.0
        
    Returns
    -------
    data: np.ndarray or np.float64
        指定された区間のf0のデータ。1次元
    t: np.ndarray
        worldの時間配列。0からworld_period間隔の等差数列
    '''
    with open(input_path, "rb") as fr:
        bytes_data = fr.read()[40:] #冒頭40バイトはヘッダなので不要
    base_data: np.ndarray = np.frombuffer(bytes_data, dtype="float64")[::2] #音量はいらない
    frq_span = 1 / framerate * 256
    start_frame: int = int(offset / frq_span /1000)
    if end_ms > 0:
        end_frame:int = base_data.shape[0] - int(end_ms / frq_span /1000) - 1
        base_data = base_data[start_frame:end_frame]
    elif end_ms ==0 :
        base_data = base_data[start_frame:]
    else:
        end_frame:int = start_frame - int(end_ms / frq_span /1000) + 2
        base_data = base_data[start_frame:end_frame]
        
    frq_t: np.ndarray= np.arange(0, frq_span * (base_data.shape[0]+1), frq_span)[:base_data.shape[0]]
    world_t: np.ndarray= np.arange(0, frq_t[-1], world_period/1000)
    data: np.ndarray = pitch.interp1d(frq_t, world_t, base_data)
    return data, world_t