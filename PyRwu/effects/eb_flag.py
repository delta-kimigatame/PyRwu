import numpy as np
from . import base

class EBFlag(base.WorldEffectBase):
    @staticmethod
    def apply(params) -> np.ndarray:
        '''
        | 語尾の息成分の強さ(ブレシネス)。大きいほど息っぽい
        | eb100の時、1000Hz～5000Hz帯の非周期性指標が全て1になるように加算します。
        | あわせて、eb100の時スペクトル包絡が0になるように弱めます。
        | 語尾息がかかる範囲はebs、語尾息が最大になるまでの時間はebaで指定します。

        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        Returns
        -------
        new_values: np.ndarray of float64
            
            | 処理後の値

        '''
        if params.flags.params["eb"].value == params.flags.params["eb"].default_value:
            return params.f0, params.sp, params.ap
        
        value: int = params.flags.params["eb"].value
        atack: int = params.flags.params["eba"].value
        start: int = params.flags.params["ebs"].value
        
        sp: np.ndarray = params.sp.copy()
        ap: np.ndarray = params.ap.copy()

        effect: np.ndarray = np.ones_like(ap) - ap
        sp_effect: np.ndarray = np.ones_like(sp)- value / (params.flags.params["eb"].max + 1)
        mask: np.ndarray = np.zeros_like(ap)
        mask_len: int = int(1000 * (ap.shape[1]-1) / params.framerate)
        effect[:,:mask_len] = mask[:,:mask_len]
        mask_len: int = int(5000 * (ap.shape[1]-1) / params.framerate)
        effect[:,mask_len:] = mask[:,mask_len:]
        effect = effect * value / params.flags.params["eb"].max
        for i in range(atack):
            effect[start+i,:] = effect[start+i,:] * i/atack
            sp_effect[start + i,:] = 1- value / (params.flags.params["eb"].max + 1) * i / atack
        if start != 0:
            effect[:start] = 0
            sp_effect[:start] = 1
        sp = sp * sp_effect
        ap = ap + effect
        return params.f0, sp, ap

