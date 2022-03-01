'''stretch

音声データの時間伸縮を扱います。

'''

import numpy as np
from typing import Tuple

def calc_velocity_rate(velocity: int) -> float:
    '''
    | 子音速度から、固定範囲の長さをどのように変更するか求めます。
    | velocity=200で0.5、velocity=0で2、velocity=100で1を返します。

    Notes
    -----

    >>> rate = 2 ** ((100-velocity)/100)

    Parameters
    ----------
    velocity: int
        子音速度(0～200)

    Returns
    -------
    rate: float
    '''
    return 2 ** ((100-velocity)/100)


def world_stretch(target_frames:int, f0: np.ndarray, sp: np.ndarray, ap: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    '''

    | worldデータを全体を引き延ばす方式で伸縮します。
    | 元データが[ABCDE]を2倍に引き延ばすとき[AABBCCDDEE]となります。

    Parameters
    ----------
    target_frames: int
        伸縮後のworldフレーム数

    f0: np.ndarray of float64
        
        | wavのf0(音高)データの1次元配列。
        | settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。

    sp: np.ndarray of float64

        | wavのスペクトル包絡(声質)データの2次元配列。
        | 1次元目は時間軸で、settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。
        | 2次元目は周波数軸で、fft_sizeに基づき決定する。

    ap: np.ndarray of float64

        | wavの非周期性指標データの2次元配列。
        | 1次元目は時間軸で、settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。
        | 2次元目は周波数軸で、fft_sizeに基づき決定する。

    Returns
    -------
    new_f0: np.ndarray of float64
        
        | wavのf0(音高)データの1次元配列。

    new_sp: np.ndarray of float64

        | wavのスペクトル包絡(声質)データの2次元配列。

    new_ap: np.ndarray of float64

        | wavの非周期性指標データの2次元配列。

    '''

    if target_frames == f0.shape[0]:
        return f0, sp, ap

    new_f0: np.ndarray = np.zeros(target_frames)
    new_sp: np.ndarray = np.zeros((target_frames,sp.shape[1]))
    new_ap: np.ndarray = np.zeros((target_frames,ap.shape[1]))

    if target_frames > f0.shape[0]:
        #伸ばす
        multinum: int = int(target_frames / f0.shape[0]) + 1
        border: int = f0.shape[0] - (multinum*f0.shape[0] - target_frames)
        #0～borderの要素はmultinum回、border～の要素はmultinum-1回繰り返す
        for i in range(f0.shape[0]):
            if i<= border:
                s = i*multinum
                e = (i+1)*multinum
            else:
                s = border*multinum + (i-border) * (multinum-1)
                e = border*multinum + (i-border+1) * (multinum-1)
            new_f0[s:e]=f0[i]
            new_sp[s:e]=sp[i]
            new_ap[s:e]=ap[i]
    else:
        #縮める
        leavereat: float = 1-(target_frames / f0.shape[0])
        border:float = 0
        leaves:int = 0
        for i in range(f0.shape[0]):
            border = border + leavereat
            if border >= 1:
                border = border - 1
                leaves = leaves + 1
            elif i-leaves < new_f0.shape[0]:
                new_f0[i-leaves]=f0[i]
                new_sp[i-leaves]=sp[i]
                new_ap[i-leaves]=ap[i]
    return new_f0[:target_frames], new_sp[:target_frames], new_ap[:target_frames]

def world_loop(target_frames:int, f0: np.ndarray, sp: np.ndarray, ap: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    '''

    | worldデータを全体を引き延ばす方式で伸縮します。
    | 元データが[ABCDE]を2倍に引き延ばすとき[ABCDEDCBAB]となります。

    Parameters
    ----------
    target_frames: int
        伸縮後のworldフレーム数

    f0: np.ndarray of float64
        
        | wavのf0(音高)データの1次元配列。
        | settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。

    sp: np.ndarray of float64

        | wavのスペクトル包絡(声質)データの2次元配列。
        | 1次元目は時間軸で、settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。
        | 2次元目は周波数軸で、fft_sizeに基づき決定する。

    ap: np.ndarray of float64

        | wavの非周期性指標データの2次元配列。
        | 1次元目は時間軸で、settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。
        | 2次元目は周波数軸で、fft_sizeに基づき決定する。

    Returns
    -------
    new_f0: np.ndarray of float64
        
        | wavのf0(音高)データの1次元配列。

    new_sp: np.ndarray of float64

        | wavのスペクトル包絡(声質)データの2次元配列。

    new_ap: np.ndarray of float64

        | wavの非周期性指標データの2次元配列。

    '''
    if target_frames == f0.shape[0]:
        return f0, sp, ap
    elif target_frames < f0.shape[0]:
        return f0[:target_frames], sp[:target_frames], ap[:target_frames]

    new_f0 = np.pad(f0, (0, target_frames - f0.shape[0]), "reflect")
    new_sp = np.pad(sp, [(0, target_frames - sp.shape[0]),(0,0)], "reflect")
    new_ap = np.pad(ap, [(0, target_frames - ap.shape[0]),(0,0)], "reflect")
    
    return new_f0, new_sp[:target_frames], new_ap[:target_frames]