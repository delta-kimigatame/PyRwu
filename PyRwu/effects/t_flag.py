import numpy as np
from . import base

class TFlag(base.PitchEffectBase):
    @staticmethod
    def apply(params, pitches: np.ndarray) -> np.ndarray:
        '''
        "音程の補正。1cent単位"

        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        pitches: np.ndarray of float64
            
            | world時間軸のピッチ数列(cent単位)
            | settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。

        Returns
        -------
        pitches: np.ndarray of float64
            
            | world時間軸のピッチ数列(cent単位)
            | settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。

        '''
        return pitches + params.flags.params["t"].value
