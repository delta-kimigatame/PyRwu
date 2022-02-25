import numpy as np
import effects.base

class LargeBFlag(effects.base.WorldEffectBase):
    @staticmethod
    def apply(params) -> np.ndarray:
        '''
        | 息成分の強さ(ブレシネス)。大きいほど息っぽい
        | 0～49ではB0の時非周期性指標が全て0になるように乗算します。
        | 51～100ではB100の時、1000Hz～5000Hz帯の非周期性指標が全て1になるように加算します。

        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        Returns
        -------
        new_values: np.ndarray of float64
            
            | 処理後の値

        '''
        if params.flags.params["B"].value == params.flags.params["B"].default_value:
            return params.ap
        
        ap: np.ndarray = params.ap.copy()
        if params.flags.params["B"].value < params.flags.params["B"].default_value:
            ap = ap * params.flags.params["B"].value / (params.flags.params["B"].default_value - params.flags.params["B"].min)
        else:
            effect: np.ndarray = np.ones_like(ap) - ap
            mask: np.ndarray = np.zeros_like(ap)
            #1000Hz以下をマスク
            mask_len: int = int(1000 * (ap.shape[1]-1) / params.framerate)
            effect[:,:mask_len] = mask[:,:mask_len]
            mask_len: int = int(5000 * (ap.shape[1]-1) / params.framerate)
            effect[:,mask_len:] = mask[:,mask_len:]
            ap = ap + effect * (params.flags.params["B"].value - params.flags.params["B"].default_value) / (params.flags.params["B"].max - params.flags.params["B"].default_value)
            
        return ap

