import numpy as np
from typing import Tuple

class PitchEffectBase:
    '''
    | ピッチに影響を与える処理の抽象型
    | 周波数に変換する前の、cent単位のピッチ列を加工する場合、このクラスを継承する。
    '''
    @staticmethod
    def apply(params, pitches: np.ndarray) -> np.ndarray:
        '''
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
        return pitches
    

class EffectBase:
    '''
    | f0,sp,ap,output_dataに影響を与える処理の抽象型
    | 各パラメータを加工する場合、このクラスを継承する。
    '''
    @staticmethod
    def apply(params) -> np.ndarray:
        '''
        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        Returns
        -------
        new_values: np.ndarray of float64
            
            | 処理後の値

        '''
        return np.array([])

    
class WorldEffectBase:
    '''
    | f0,sp,apの複数に影響を与える処理の抽象型
    | 各パラメータを加工する場合、このクラスを継承する。
    '''
    @staticmethod
    def apply(params) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        '''
        Parameters
        ----------
        params: resamp.Resamp

            伸縮機の各パラメータ

        Returns
        -------
        f0: np.ndarray of float64
            
            | 処理後のf0
            
        sp: np.ndarray of float64
            
            | 処理後のsp

        ap: np.ndarray of float64
            
            | 処理後のap

        '''
        return np.array([]), np.array([]), np.array([])