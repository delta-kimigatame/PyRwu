import numpy as np
'''interpolate

線形補完を扱います。

'''


def interp1d(t: np.ndarray, new_t: np.ndarray, value:np.ndarray) -> np.ndarray:
    '''

    | tに従属するvalueを、new_t間隔で線形補完したarrayを返します。

    Parameters
    ----------
    t: np.ndarray of float64
        valueのデータ間隔。等間隔である必要があります。
    new_t: np.ndarray of float64
        新しいデータの間隔。等間隔である必要があります。
    value: np.ndarray of float64
        現在のデータ

    Returns
    -------
    new_value: np.ndarray of float64
        valueをnew_t間隔で線形保管したデータ
    '''
    new_value: np.ndarray = np.zeros_like(new_t, dtype=np.float64)
    index: int
    span: float = t[1] - t[0]
    for i in range(new_value.shape[0]):
        index = int(new_t[i] / span)
        if t[index] == new_t[i]:
            new_value[i] = value[index]
        else:
            new_value[i] = (value[index] * (t[index+1] - new_t[i])+ value[index+1] * (new_t[i] - t[index])) / span

    return new_value
