import numpy as np
import pyworld as pw

import flags
import wave_io
import stretch
import pitch
import settings
class Resamp:
    '''Resamp

    | 伸縮機の実際の動作を規定します。
    | 処理の順序は下記の通り

    1. フラグをパース
    2. 入力ファイルのworldパラメータを取得

        1. wavファイルの読み込み
        2. harvestでf0取得
        3. stonemaskでf0補正
        4. cheaptrickでスペクトル包絡取得
        5. d4cで非周期性指標取得

    3. worldパラメータの伸縮(長さ)
    4. 音高・モジュレーションの適用(ピッチ)
    5. ピッチの適用
    6. worldパラメーター用の加工処理

        1. f0に影響するフラグ(tフラグ)
        2. スペクトル包絡に影響するフラグ(gフラグ)
        3. 非周期性指標に影響するフラグ(Bフラグ)

    7. 音声合成
    8. wav波形の加工処理

        1. 音量に関するフラグ(Pフラグ)

    9. 音量の適用
    10. wavファイルの出力

    Attributes
    ----------
    input_path: str
        原音のファイル名

    input_data: np.ndarray of float64
        wavから読み込んだ波形データ

    framerate: int
        wavのサンプリング周波数

    f0: np.ndarray of float64
        
        | wavのf0(音高)データの1次元配列。
        | settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。

    t: np.ndarray of float64
        | 各フレームの時間的位置(sec)
        | settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。
        | 例えば、settings.PYWORLD_PERIOD=5のとき、t[100]=0.5

    sp: np.ndarray of float64

        | wavのスペクトル包絡(声質)データの2次元配列。
        | 1次元目は時間軸で、settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。
        | 2次元目は周波数軸で、fft_sizeに基づき決定する。

    ap: np.ndarray of float64

        | wavの非周期性指標データの2次元配列。
        | 1次元目は時間軸で、settings.PYWORLD_PERIOD(デフォルト5ms)毎に生成される。
        | 2次元目は周波数軸で、fft_sizeに基づき決定する。

    output_data: np.ndarray of float64
        worldのパラメータから合成した波形データ

    output_path: str
        wavファイルの出力先パス

    target_tone: str

        | 音高名(A4=440Hz)。
        | 半角上げは#もしくは♯ 
        | 半角下げはbもしくは♭で与えられます。

    target_frq: float
        音高の周波数

    velocity: int
        子音速度

    flag_value: str, default ""
        フラグ(省略可)

    flags: flags.Flags, default settings.FLAGS
        入力されたフラグをパースしたもの

    offset: float, default 0
        入力ファイルの読み込み開始位置(ms)

    target_ms: float, default 0

        | 出力ファイルの長さ(ms)
        | UTAUでは通常50ms単位に丸めた値が渡される。
        
    target_frames: int
        target_msをworld仕様のフレーム数に変換したもの

    fixed_ms: float, default 0
        offsetからみて通常伸縮しない長さ(ms)

    fixed_frames: int
        worldパラメータのうち、前から何フレームが固定範囲に入るか?

    end_ms: float, default 0

        | 入力ファイルの読み込み終了位置(ms)(省略可 default:0)
        | 正の数の場合、ファイル末尾からの時間
        | 負の数の場合、offsetからの時間

    volume: int, default 100
        音量。0～200(省略可)

    modulation: int, default 0
        モジュレーション。0～200(省略可)

    tempo: str, default "!120"

        | ピッチのテンポ
        | 数字の頭に!がついた文字列

    pitchbend: str, default ""

        | ピッチベンド。(省略可)
        | -2048～2047までの12bitの2進数をbase64で2文字の文字列に変換し、
        | 同じ数字が続く場合ランレングス圧縮したもの

    pitches: np.ndarray of float64

        | 与えられたピッチ配列を数値配列に変換したもの

    '''

    _input_path: str
    _output_path: str
    _target_tone: str
    _velocity: int
    _flag_value: str
    _offset: float
    _target_ms: float
    _fixed_ms: float
    _end_ms: float
    _volume: int
    _modulation: int
    _tempo: str
    _pitchbend: str

    _input_data: np.ndarray
    _framerate: int
    _f0: np.ndarray
    _t: np.ndarray
    _sp: np.ndarray
    _ap: np.ndarray

    _target_frames :int
    _fixed_frames :int

    _output_data: np.ndarray

    _target_frq: float

    _flags: flags.Flags = settings.FLAGS

    _pitches: np.ndarray

    @property
    def input_path(self) -> str:
        return self._input_path
    
    @property
    def output_path(self) -> str:
        return self._output_path

    @property
    def velocity(self) -> int:
        return self._velocity
    
    @property
    def flag_value(self) -> str:
        return self._flag_value
    
    @property
    def offset(self) -> float:
        return self._offset
    
    @property
    def target_ms(self) -> float:
        return self._target_ms
    
    @property
    def target_frames(self) -> int:
        return self._target_frames

    @property
    def fixed_ms(self) -> float:
        return self._fixed_ms
    
    @property
    def fixed_frames(self) -> int:
        return self._fixed_frames

    @property
    def end_ms(self) -> float:
        return self._end_ms
    
    @property
    def volume(self) -> int:
        return self._volume
    
    @property
    def modulation(self) -> int:
        return self._modulation
    
    @property
    def tempo(self) -> str:
        return self._tempo

    @property
    def pitchbend(self) -> str:
        return self._pitchbend
    
    @property
    def input_data(self) -> np.ndarray:
        return self._input_data
    
    @property
    def framerate(self) -> int:
        return self._framerate
    
    @property
    def f0(self) -> np.ndarray:
        return self._f0
    
    @property
    def t(self) -> np.ndarray:
        return self._t
    
    @property
    def sp(self) -> np.ndarray:
        return self._sp
    
    @property
    def ap(self) -> np.ndarray:
        return self._ap
    
    @property
    def output_data(self) -> np.ndarray:
        return self._output_data
    
    @property
    def target_frq(self) -> float:
        return self._target_frq
    
    @property
    def flags(self) -> flags.Flags:
        return self._flags
    
    @property
    def pitches(self) -> np.ndarray:
        return self._pitches
    
    def __init__(self, input_path: str, output_path: str, target_tone: str, velocity: 100,
                 flag_value: str="", offset: float=0, target_ms: float=0, fixed_ms: float=0,
                 end_ms: float=0, volume: int=100, modulation: int=0, tempo: str="!120", pitchbend: str=""):
        self._input_path = input_path
        self._output_path = output_path
        self._target_tone = target_tone
        self._velocity = velocity
        self._flag_value = flag_value
        self._offset = offset
        self._target_ms = target_ms
        self._fixed_ms = fixed_ms
        self._end_ms = end_ms
        self._volume = volume
        self._modulation = modulation
        self._tempo = tempo
        self._pitchbend = pitchbend

    def parseFlags(self):
        '''
        与えられたフラグをパースし、self.flagsを更新します。
        
        Notes
        -----
        フラグの取得方法を変更したい場合、このメソッドをオーバーライドしてください。
        '''
        self._flags.parse(self._flag_value)

    def getInputData(self,
                     f0_floor: float=settings.PYWORLD_F0_FLOOR,
                     f0_ceil: float=settings.PYWORLD_F0_CEIL,
                     frame_period: float=settings.PYWORLD_PERIOD,
                     q1: float=settings.PYWORLD_Q1,
                     threshold: float=settings.PYWORLD_THRESHOLD):
        '''
        入力された音声データからworldパラメータを取得し、self._input_data, self._framerate, self._f0, self._sp, self._apを更新します。

        Notes
        -----
        | 音声データの取得方法を変更したい場合、このメソッドをオーバーライドしてください。
        | オーバーライドする際、self._input_dataはこれ以降の処理で使用しないため、更新しなくても問題ありません。

        Parameters
        ----------
        f0_floor: float, default settings.PYWORLD_F0_FLOOR

            | worldでの分析するf0の下限
            | デフォルトでは71.0

        f0_ceil: float, default settings.PYWORLD_F0_CEIL

            | worldでの分析するf0の上限
            | デフォルトでは800.0

        frame_period: float, default settings.PYWORLD_PERIOD

            | worldデータの1フレーム当たりの時間(ms)
            | 初期設定では5.0
            
        q1: float, default settings.PYWORLD_Q1

            | worldでスペクトル包絡抽出時の補正値
            | 通常は変更不要
            | 初期設定では-15.0

        threshold: float, default settings.PYWORLD_THRESHOLD

            | worldで非周期性指標抽出時に、有声/無声を決定する閾値(0 ～ 1)
            | 値が0の場合、音声のあるフレームを全て有声と判定します。
            | 値が0超の場合、一部のフレームを無声音として判断します。
            | 初期値0.85はharvestと組み合わせる前提で調整されています。
        
        Raises
        ------
        FileNotFoundError
            input_pathにファイルがなかったとき
        TypeError
            input_pathで指定したファイルがwavではなかったとき
        '''

        self._input_data, self._framerate = wave_io.read(self._input_path, self._offset, self._end_ms)
        self._f0, self._t = pw.harvest(self._input_data, self._framerate, f0_floor=f0_floor, f0_ceil=f0_ceil, frame_period=frame_period)
        self._f0 = pw.stonemask(self._input_data, self._f0, self._t, self._framerate)
        self._sp = pw.cheaptrick(self._input_data, self._f0, self._t, self._framerate, q1=q1, f0_floor=f0_floor, frame_period=frame_period)
        self._ap = pw.d4c(self._input_data, self._f0, self._t, self._framerate, threshold=threshold)

    def stretch(self):
        '''
        | self._target_ms, self._fixed_ms, self._velocityに基づいて、self._f0,self._sp,self._apを更新します。
        | 計算途中結果のうち、後ほど活用できそうなself._target_framesとself._fixed_framesも記憶します。

        Notes
        -----
        | 音声の伸縮方法を変更したい場合、このメソッドをオーバーライドしてください。
        '''

        vel_f0 :np.ndarray
        vel_sp :np.ndarray
        vel_ap :np.ndarray
        
        s_f0 :np.ndarray
        s_sp :np.ndarray
        s_ap :np.ndarray

        self._target_frames = int(self._target_ms / settings.PYWORLD_PERIOD)
        input_fix_frames: int = int(self._fixed_ms / settings.PYWORLD_PERIOD)

        if self._velocity != 100:
            _velocity_rate: float = stretch.calc_velocity_rate(self._velovity)
            self._fixed_frames = int(input_fix_frames * _velocity_rate)
            vel_f0, vel_sp, vel_ap = stretch.world_stretch(self._fixed_frames,
                                                           self._f0[:input_fix_frames],
                                                           self._sp[:input_fix_frames],
                                                           self._ap[:input_fix_frames])
        else:
            self._fixed_frames = input_fix_frames
            vel_f0 = self._f0[:input_fix_frames]
            vel_sp = self._sp[:input_fix_frames]
            vel_ap = self._ap[:input_fix_frames]

        if self.flags.params["e"].flag:
            s_f0, s_sp, s_ap = stretch.world_stretch(self._target_frames - self._fixed_frames,
                                                     self._f0[input_fix_frames:],
                                                     self._sp[input_fix_frames:],
                                                     self._ap[input_fix_frames:])
        else:
            s_f0, s_sp, s_ap = stretch.world_loop(self._target_frames - self._fixed_frames,
                                                  self._f0[input_fix_frames:],
                                                  self._sp[input_fix_frames:],
                                                  self._ap[input_fix_frames:])

        self._f0 = np.concatenate([vel_f0, s_f0], axis=0)
        self._sp = np.concatenate([vel_sp, s_sp], axis=0)
        self._ap = np.concatenate([vel_ap, s_ap], axis=0)

    def pitchShift(self):
        '''
        | self._tone, self._modulationを使用して、self._target_frq,self._f0を更新します。

        Notes
        -----
        | ノートの音程およびモジュレーションに関する処理を変更したい場合、このメソッドをオーバーライドしてください。
        | オーバーライドする際、self._target_frqはこれ以降の処理で使用しないため、更新しなくても問題ありません。
        
        Raises
        ------
        ValueError
            toneの書式が適正でない場合
        '''

        average_frq: float = np.average(self._f0)
        self._target_frq = pitch.getFrqFromStr(self._tone)
        self._f0 = self._f0 / average_frq * self._target_frq
        if self._modulation != 0:
            mod_f0: np.ndarray = np.stack([self._f0, np.full(self._f0.shape[0], self._target_frq)])
            self._f0 = np.average(mod_f0, axis=0, weight=[1-self._modulation, self._modulation])

    def applyPitch(self):
        '''
        | self._target_ms, self._tempo, self._framerate, self,_pitchbend, self._tを使用して、self._pitches, self._f0を更新します。
        
        Notes
        -----
        | ピッチの適用およびピッチに関するフラグの処理を変更したい場合、このメソッドをオーバーライドしてください。
        
        Notes
        -----
        | UTAUのピッチ数列および、tフラグは1cent単位で与えられます。
        | 100cent = 半音のため、1オクターブは1200cent
        | 1オクターブ上がると周波数が2倍になることから、
        | 音程を1cent上げる処理は、元の周波数 * 2^(1/1200)
        
        Raises
        ------
        ValueError
            toneの書式が適正でない場合
        
        ValueError
            tempoに有効な文字列が渡されなかったとき
        '''
        self._pitches = pitch.decodeBase64(self._pitchbend)
        utau_t: np.ndarray = pitch.getPitchRange(self._tempo, self._target_ms, self._framerate)
        interp_pitch = pitch.interpPitch(self._pitches, utau_t, self_t)

        #tフラグの処理
        interp_pitch += self.flags.params["t"].value

        #pitchの適用
        self._f0 = self._f0 * (np.full(self._f0.shape[0], 2) ** (interp_pitch / 1200))