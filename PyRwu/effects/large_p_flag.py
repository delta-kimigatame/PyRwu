import numpy as np
from . import base

class LargePFlag(base.WorldEffectBase):
    @staticmethod
    def apply(params) -> np.ndarray:
        '''
        | ピークコンプレッサー。
        | P100の時volume適用前の音量最大値が-6dBになるように正規化
        | P0の時は原音の音量に合わせて正規化します。

        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        Returns
        -------
        new_values: np.ndarray of float64
            
            | 処理後の値

        '''
        output_volume =  np.amax(np.abs(params.output_data))
        P: int = params.flags.params["P"].value/100
        
        return params.output_data / output_volume * 0.5 * P + params.output_data * (1-P)

