'''pitch

音高関係のデータを扱います

'''
import re

import numpy as np

import interpolate
import settings

def getFrqFromStr(tone: str) -> float:
    '''
    settings.TONE_NUMとsettings.A4FRQと与えられた文字列から周波数を返す。

    Parameters
    ----------
    tone :str
    
        | 音高を表す文字列。C4、B3、A#2のように与えられる。
        | 半音記号は、#,♯,b,♭の4種類が認識可能

    Returns
    -------
    frq :float
        周波数

    Raises
    ------
    ValueError
        toneの書式が適正でない場合
    '''
    try:
        notenum :int = settings.TONE_NUM[tone[:-1]] + (int(tone[-1]) + 1) * 12
    except:
        raise ValueError("{} is not tone-name.".format(tone))
    base_notenum: int = settings.TONE_NUM["A"] + 60
    return settings.A4FRQ * (2 ** ((notenum - base_notenum)/12))
    
def decodeRunLength(value :str) -> str:
    '''
    | UTAUピッチ用のランレングス圧縮を展開します。
    | 2文字一組とし、#num#はひとつ前の組の繰り返し回数を表します。
    
    >>> AAABAC → [AA, AB, AC]
    >>> AA#3# → [AA, AA, AA, AA]

    Parameters
    ----------
    value: str
        ランレングス圧縮された文字列

    Returns
    -------
    decode_data: str
        展開後の文字列
    '''
    repl :str
    reg = re.compile("(..)#([0-9]+)#")
    m = re.search(reg, value)
    while m is not None:
        repl = m.group(1) * (int(m.group(2))+1)
        value=value.replace(m.group(0), repl)
        m = re.search(reg, value)
    return value

def decodeBase64Core(value :str) -> int:
    '''
    base64文字をデコードします。

    Parameters
    ----------
    value :str
        
       | 1文字の文字列
       | 2文字以上でも2文字目以降は無視されます。

    Returns
    -------
    decode_value :int

    '''
    value = ord(value[0])
    if value >= ord("A") and value <= ord("Z"):
        return value - ord("A")
    elif value >= ord("a") and value <= ord("z"):
        return value - ord("a") + 26
    elif  value >= ord("0") and value <= ord("9"):
        return value - ord("0") + 52
    elif value=="+":
        return 62
    else:
        return 63

def decodeBase64(value :str) -> np.ndarray:
    '''
    base64文字列をデコードし、-2048～2047のndarrayを返します。

    Parameters
    ----------
    value: str

        Base64でエンコードされた文字列

    Returns
    -------
    decode_data: np.ndarray of int16

        | -2047 ～ 2048の整数列
        | データ数は、与えられたvalueの半分になります。
    '''

    decode_data: np.ndarray = np.zeros(int(len(value)/2), dtype="int16")
    for i in range(decode_data.shape[0]):
        decode_data[i]= decodeBase64Core(value[i*2]) * 64 + decodeBase64Core(value[i*2+1])
        if decode_data[i] >= 2048:
            decode_data[i] -= 4096

    return decode_data

def getPitchRange(tempo: str, target_ms: float, framerate: int)-> np.ndarray:
    '''
    | 出力長さに対する、UTAUピッチのタイミング列を求めます。
    | UTAUピッチ列は、4部音符あたり96個を基本とし、
    | ピッチ列の間隔をwaveのフレームで表したとき整数となるようにします。
    | 全フレーム数をピッチ列間隔で除した数を切り上げた整数になります。

    Parameters
    ----------
    tempo: str

        | ピッチのテンポ
        | floatに変換可能な文字列もしくは、数字の頭に!がついた文字列

    target_ms: float

        | 出力ファイルの長さ(ms)
        | UTAUでは通常50ms単位に丸めた値が渡される。
        
    framerate: int
        wavのサンプリング周波数

    Returns
    -------
    range: np.ndarray of float64
        UTAUピッチのタイミング列を求めます。

    Raises
    ------
    ValueError
        tempoに有効な文字列が渡されなかったとき
    '''
    try:
        bpm: float = float(tempo)
    except:
        try:
            bpm: float = float(tempo[1:])
        except:
            raise ValueError("{} is not utau tempo format.".format(tempo))
    nframes: int = int(target_ms / 1000 * framerate)
    frame_step: int = int(round(60 / 96 / bpm * framerate,0))
    pitch_length: int = int(nframes / frame_step) + 1
    ms_step: float = frame_step / framerate * 1000
    return np.arange(0, ms_step * (pitch_length + 1), ms_step)[:pitch_length + 1]

def interpPitch(base: np.ndarray, utau_t: np.ndarray, world_t: np.ndarray) -> np.ndarray:
    '''
    | UTAUピッチ列をworld時間軸に線形補完します。
    | UTAUピッチ列が必要長さに満たない場合、後ろ側を0埋めをします。

    Parameters
    ----------
    base: np.ndarray
        UTAUピッチ列

    utau_t: np.ndarray
        UTAUピッチのタイミング列

    world_t: no.ndarray
        world時間軸のタイミング列

    Returns
    -------
    interp_data: np.ndarray
        world時間軸のピッチ列
    '''
    if(utau_t.shape[0] > base.shape[0]):
        base = np.pad(base, (0,utau_t.shape[0]-base.shape[0]))
    else:
        base = base[:utau_t.shape[0]]
        
    return interpolate.interp1d(utau_t, world_t, base)
