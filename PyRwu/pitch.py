'''pitch

音高関係のデータを扱います

'''
import re
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
