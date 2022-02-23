'''pitch

音高関係のデータを扱います

'''

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
    return settings.A4FRQ * 2 ** ((notenum - base_notenum)/12)
    