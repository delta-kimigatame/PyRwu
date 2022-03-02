import numpy as np

import effects.base
import interpolate

class LargeAFlag(effects.base.WorldEffectBase):
    @staticmethod
    def apply(params) -> np.ndarray:
        '''
        | ピッチ変動にあわせて音量が変化します。
        | 1～100では、基準より高いとき音量が小さくなります。
        | -1～-100では、基準より低いとき音量が小さくなります。

        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        Returns
        -------
        new_values: np.ndarray of float64
            
            | 処理後の値

        '''
        if params.flags.params["A"].value == params.flags.params["A"].default_value:
            return params.output_data
        A: int = params.flags.params["A"].value
        try:
            bpm: float = float(params.tempo)
        except:
            try:
                if params.tempo[:2]=="0Q":
                    bpm: float = float(params.tempo[2:])
                else:
                    bpm: float = float(params.tempo[1:])
            except:
                raise ValueError("{} is not utau tempo format.".format(params.tempo))
        nframes: int = int(params.target_ms / 1000 * params.framerate)
        frame_step: int = int(round(60 / 96 / bpm * params.framerate,0)) #ピッチ列1つあたりが影響を与えるwavフレーム数
        pitch_length: int = int(nframes / frame_step) + 1
        wave_t: np.ndarray = np.arange(0, frame_step * (pitch_length + 1), frame_step)[:pitch_length + 1]
        if(wave_t.shape[0] > params.pitches.shape[0]):
            pitches: np.ndarray = np.pad(params.pitches, (0,wave_t.shape[0]-params.pitches.shape[0]))
        else:
            pitches: np.ndarray = params.pitches[:wave_t.shape[0]]
        
        effect: np.ndarray = interpolate.interp1d(wave_t, np.arange(params.output_data.shape[0]),pitches)/ 100

        effect_max: int = np.amax(np.abs(effect))
        if effect_max > 1:
            effect = effect / effect_max

        effect = np.ones_like(effect) - effect * A / 100

        return params.output_data * effect

