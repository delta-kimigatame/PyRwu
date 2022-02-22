import re
import warnings

class Flag:
    '''Flag

    各フラグの詳細を扱うクラス
    
    Attributes
    ----------
    name: str
        フラグのキー
    descriptions: list of str
        説明文の配列。1要素毎に改行して出力される。
    isBool: bool, default False
        オンオフを切り替えるタイプならTrue。範囲を指定するタイプならFalse
    min: int, default 0
        範囲を指定するフラグの最小値
    max: int, default 100
        範囲を指定するフラグの最大値
    flag: bool, default False
        isBoolがTrueの時の値
    value: int, default 50
        isBoolがFalseの時の値
    default_bool: bool, default False
        self._flagの初期値
    default_value: int, default 50
        self._valueの初期値
    '''

    _name: str
    _descriptions: list
    _isBool: bool = False
    _min: 0
    _max: 100
    _flag: bool = False
    _value: int = 50
    _default_bool :bool = False
    _default_value :int = 50

    @property
    def name(self) -> str:
        return self._name

    @property
    def descriptions(self) -> list:
        return self._descriptions

    @property
    def isBool(self) -> bool:
        return self._isBool

    @property
    def min(self) -> int:
        return self._min
    
    @property
    def max(self) -> int:
        return self._max
    
    @property
    def flag(self) -> bool:
        return self._flag

    @property
    def value(self) -> int:
        return self._value
    
    @property
    def default_bool(self) -> bool:
        return self._default_bool

    @property
    def default_value(self) -> int:
        return self._default_value

    @value.setter
    def value(self, value: int):
        '''
        value値が適正かチェックして、self._valueを更新します。

        Parameters
        ----------
        value: int

        Warnings
        --------
        flag is boolean.
            self._isBoolがTrueの時。代入は無視される
        value's out of range
            与えられたvalueがmin以上max以下でないとき。代入は無視される。
        
        '''
        if self._isBool:
            warnings.warn("flag is boolean. name:{}".format(self._name))
        elif self._min> value:
            warnings.warn("value's out of range.key:{}, min:{}, value:{}".format(self._name, self._min, value))
        elif self._max< value:
            warnings.warn("value's out of range.key:{}, max:{}, value:{}".format(self._name, self._max, value))
        else:
            self._value = value
            
    @flag.setter
    def flag(self, value: bool):
        '''
        value値が適正かチェックして、self._flagを更新します。

        Parameters
        ----------
        value: flag

        Warnings
        --------
        flag is boolean.
            self._isBoolがFalseの時。代入は無視される
        
        '''
        if not self._isBool:
            warnings.warn("flag is not boolean. name:{}".format(self._name))
        else:
            self._flag = value


    def __init__(self, name, descriptions=[], isBool=False, min=0, max=100, default_bool=False, default_value=50):
        '''
        Parameters
        ----------
        name: str
            フラグのキー
        descriptions: list of str
            説明文の配列。1要素毎に改行して出力される。
        isBool: bool, default False
            オンオフを切り替えるタイプならTrue。範囲を指定するタイプならFalse
        min: int, default 0
            範囲を指定するフラグの最小値
        max: int, default 100
            範囲を指定するフラグの最大値
        default_bool: bool, default False
            self._flagの初期値
        default_value: int, default 50
            self._valueの初期値
        '''
        self._name = name
        self._descriptions = descriptions
        self._isBool = isBool
        self._min = min
        self._max = max
        self._flag = default_bool
        self._value = default_value
        self._default_value = default_value
        self._default_bool = default_bool

class Flags:
    '''Flags

    フラグに関するクラス

    Attributes
    ----------
    params: dict or Flag
        フラグで使う文字をキーとする辞書
    '''

    _params: dict

    @property
    def params(self) -> dict:
        return self_params

    def __init__(self):
        self._params = {}

    def add(self, flag: Flag):
        '''
        扱うフラグの種類を追加する。

        Parameters
        ----------
        flag: Flag
            扱うフラグのパラメータ
        '''
        self._params[flag.name] = flag

    def getDetail(self) -> str:
        '''
        各フラグの詳細を結合した文字列を返す。

        Returns
        -------
        description: str
        '''
        description: str = ""

        for flag in self._params.values():
            description += "\t"+flag.name + "\t"
            if not flag.isBool:
                description += str(flag.min) + " ～ " + str(flag.max) + "\t default:" + str(flag.default_value) + "\n\t\t"
            else:
                description += "\t\t default:" + str(flag.default_bool) + "\n\t\t"
            description += "\n\t\t".join(flag.descriptions)+"\n\n"
        return description


    def parse(self, value: str):
        '''
        フラグ文字列をパースして、各フラグの値を更新する。

        Parameters
        ----------
        value: str
            フラグ文字列。B50、g-5B30、eg+5B70Aなどのように、与えられる。
        '''
        keys = sorted(self.params.keys(),key=len, reverse==True) #文字数が長い順にキーを並べる
        for k in keys:
            if k not in value:
                continue
            m = re.search(k + r'+?(-?[0-9]*)', value) #boolタイプのフラグにも後ろに文字があれば、ほかのフラグの異常値を避けるために抽出する。
            if self.params[k].isBool:
                self.params[k].flag = True
            else:
                self.params[k].value = int(m.group(1))
            value = value.replace(m.group(0),"")

