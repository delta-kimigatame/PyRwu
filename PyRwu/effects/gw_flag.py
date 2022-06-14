import numpy as np
from . import base

class GwFlag(base.PitchEffectBase):
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
        atack: int = params.flags.params["gwa"].value
        start: int = params.flags.params["gws"].value
        t: np.ndarray = np.arange(0, pitches.shape[0] * params.t[1], params.t[1])
        growl = np.sin(t*3) * gw
        if atack != 0:
            growl[start:start+atack] = growl[start:start+atack] * np.arange(0, 1, 1/atack)[:growl[start:start+atack].shape[0]]
        if start != 0:
            growl[:start] = 0
        return pitches + growl
