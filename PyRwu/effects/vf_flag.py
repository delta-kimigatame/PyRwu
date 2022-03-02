import numpy as np

import effects.base
import stretch

class VfFlag(effects.base.WorldEffectBase):
    @staticmethod
    def apply(params) -> np.ndarray:
        '''
        | 疑似エッジ
        | vfフラグでエッジがかかる長さを5ms単位で指定します。
        | vfフラグが正の場合冒頭から、負の場合固定範囲の末尾からです。
        | vfwフラグは、エッジ1回の長さを1000フレームに対する割合で指定します。
        | vfpは、エッジ1回あたりの無音部分の長さをエッジ部分の長さに対する割合で指定します。

        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        Returns
        -------
        new_values: np.ndarray of float64
            
            | 処理後の値

        '''
        if params.flags.params["vf"].value == params.flags.params["vf"].default_value:
            return params.output_data
        if params.flags.params["vfw"].value == 0:
            return params.output_data
        vf: int = params.flags.params["vf"].value
        velocity_rate: float = stretch.calc_velocity_rate(params.velocity)
        fixed_ms: float = velocity_rate * params.fixed_ms
        if vf >0:
            vfs: int =0
            length: int =int(44100 / 1000 * vf *5)
        elif fixed_ms + vf * 5 <= 0:
            vfs: int =0
            length: int =int(44100 / 1000 * fixed_ms)
        else:
            vfs: int = int(fixed_ms + vf * 5)
            length: int =int(44100 / 1000 * abs(vf) *5)
        effects: np.ndarray = np.ones_like(params.output_data)
        edge_length: int =int(1000 * params.flags.params["vfw"].value / 100)
        pad_length:int = int(edge_length * params.flags.params["vfp"].value / 100)
        sicle_length: int = edge_length + pad_length
        n: int = int(length / sicle_length)
        for i in range(n):
            effects[vfs + i*sicle_length:vfs + i*sicle_length + edge_length] = np.arange(1, 0 , -1/edge_length) * i/n
            effects[vfs + i*sicle_length + edge_length:vfs + (i+1) * sicle_length] = 0

        lasteffect: np.ndarray = np.arange(0, 1 , 1/(length-n*sicle_length))[:length -n*sicle_length]
        lasteffect = np.pad(lasteffect,(0,(length -n*sicle_length - lasteffect.shape[0])),"edge")
        effects[vfs + n*sicle_length:vfs + length] = lasteffect

        return params.output_data * effects

