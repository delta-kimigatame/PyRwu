import numpy as np

import effects.base

class GwFlag(effects.base.PitchEffectBase):
    @staticmethod
    def apply(params, pitches: np.ndarray) -> np.ndarray:
        '''
        うなり声、グロウル

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
        if params.flags.params["gw"].value == params.flags.params["gw"].default_value:
            return pitches
        gw: int = params.flags.params["gw"].value
        t: np.ndarray = np.arange(0, pitches.shape[0] * params.t[1], params.t[1])
        growl = np.sin(t*3) * gw
        return pitches + growl
