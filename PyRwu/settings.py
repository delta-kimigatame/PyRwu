'''Settings
各種定数や初期値の設定

Attributes
----------
FLAGS: flags.Flags
    使用するフラグの設定。

PYWORLD_F0_FLOOR: float, default pw.default_f0_floor

    | worldでの分析するf0の下限
    | デフォルトでは71.0

PYWORLD_F0_CEIL: float, default pw.default_f0_ceil

    | worldでの分析するf0の上限
    | デフォルトでは800.0

PYWORLD_PERIOD: float, default pw.default_frame_period

    | worldデータの1フレーム当たりの時間(ms)
    | デフォルトでは5.0

PYWORLD_Q1:float default -0.15

    | worldでスペクトル包絡抽出時の補正値
    | 通常は変更不要
    
PYWORLD_THRESHOLD: float, default 0

    | worldで非周期性指標抽出時に、有声/無声を決定する閾値(0 ～ 1)
    | 値が0の場合、音声のあるフレームを全て有声と判定します。
    | 値が0超の場合、一部のフレームを無声音として判断します。
    | 本来の初期値0.85はharvestと組み合わせる前提で調整されていますが、
    | UTAUでの合成では1回でも判定ミスがあるとストレスなので0にしています。

A4FRQ: float, default 440
    基準となる音高

TONE_NUM: dict
    
    | UTAUから渡される音高名をnotenumに変換するための辞書
    | notenumはC1=24、C#1=25...B7=107で、以下の式で与えられる。

    >>> notenum = (octave+1) * 12 + TONE_NUM[key]

PITCH_EFFECTS: list of effects.base.PitchEffectBase
    
    | ピッチ処理時に適用するエフェクトのクラスを指定する。
    
F0_EFFECTS: list of effects.base.EffectBase

    | synthesizeでf0に適用するエフェクトのクラスを指定する。

SP_EFFECTS: list of effects.base.EffectBase

    | synthesizeでspに適用するエフェクトのクラスを指定する。

AP_EFFECTS: list of effects.base.EffectBase

    | synthesizeでapに適用するエフェクトのクラスを指定する。

WORLD_EFFECTS: list of effects.base.WorldEffectBase

    | synthesizeで適用するエフェクトのうち、f0,sp,apの複数のパラメータを変更するクラスを指定する。

OUT_WAVE_EFFECTS: list of effects.base.EffectBase

    | synthesize後のwaveに適用するエフェクトのクラスを指定する。

OUTPUT_BITDEPTH: int, default 16

    | 出力するwavのビット深度。8, 16, 24, 32のいずれかでなければなりません。
'''

from effects import large_b_flag, large_p_flag
import flags
import pyworld as pw
from effects import *

FLAGS = flags.Flags()
FLAGS.add(flags.Flag("B",
                     descriptions=["息成分の強さ(ブレシネス)。大きいほど息っぽい",
                                    "0～49ではB0の時非周期性指標が全て0になるように乗算します。",
                                    "51～100ではB100の時、1000Hz～5000Hz帯の非周期性指標が全て1になるように加算します。"],
                     isBool=False,
                     min=0,
                     max=100,
                     default_value=50))
FLAGS.add(flags.Flag("g",
                     descriptions=["疑似ジェンダー値",
                                    "負の数で女声化・若年化",
                                    "正の数で男声化・大人化します。"],
                     isBool=False,
                     min=-100,
                     max=100,
                     default_value=0))
FLAGS.add(flags.Flag("t",
                     descriptions=["音程の補正。1cent単位"],
                     isBool=False,
                     min=-100,
                     max=100,
                     default_value=0))
FLAGS.add(flags.Flag("P",
                     descriptions=["ピークコンプレッサー。",
                                   "P100の時volume適用前の音量最大値が-6dBになるように正規化",
                                   "P0の時は何もしない。"],
                     isBool=False,
                     min=0,
                     max=100,
                     default_value=86))
FLAGS.add(flags.Flag("e",
                     descriptions=["wavの伸縮方法。",
                                   "通常はループ方式で、このフラグを設定するとストレッチ式になる。"],
                     isBool=True,
                     default_bool=False))
FLAGS.add(flags.Flag("A",
                     descriptions=["ピッチ変動にあわせて音量が変化します。",
                                    "1～100では、基準より高いとき音量が小さくなります。",
                                    "-1～-100では、基準より低いとき音量が小さくなります。"],
                     isBool=False,
                     min=-100,
                     max=100,
                     default_value=0))
FLAGS.add(flags.Flag("gw",
                     descriptions=["うなり声、グロウル",
                                   "グロウルが"],
                     isBool=False,
                     min=0,
                     max=500,
                     default_value=0))
FLAGS.add(flags.Flag("gws",
                     descriptions=["ノート前半部分のグロウルがかからない時間を5ms単位で指定します。",
                                   "負の数を指定するとノート末尾からの時間になります。"],
                     isBool=False,
                     min=-1000,
                     max=1000,
                     default_value=0))
FLAGS.add(flags.Flag("gwa",
                     descriptions=["gwフラグのアタックタイムを5ms単位で指定します。"],
                     isBool=False,
                     min=0,
                     max=1000,
                     default_value=0))


PYWORLD_PERIOD: float = pw.default_frame_period
PYWORLD_F0_FLOOR: float = pw.default_f0_floor
PYWORLD_F0_CEIL: float = pw.default_f0_ceil
PYWORLD_Q1: float = -0.15
PYWORLD_THRESHOLD: float = 0

A4FRQ: float = 440.0
TONE_NUM: dict = {"C":0, "C#":1, "C♯":1, "Db":1, "D♭":1,
                  "D":2, "D#":3, "D♯":3, "Eb":3, "E♭":3,
                  "E":4, 
                  "F":5, "F#":6, "F♯":6, "Gb":6, "G♭":6,
                  "G":7, "G#":8, "G♯":8, "Ab":8, "A♭":8,
                  "A":9, "A#":10, "A♯":10, "Bb":10, "B♭":10,
                  "B":11}

PITCH_EFFECTS = [t_flag.TFlag,
                 gw_flag.GwFlag]
F0_EFFECTS = []
SP_EFFECTS = [g_flag.GFlag]
AP_EFFECTS = [large_b_flag.LargeBFlag]
WORLD_EFFECTS = []
OUT_WAVE_EFFECTS = [large_a_flag.LargeAFlag,
                    large_p_flag.LargePFlag,
                    ]

OUTPUT_BITDEPTH = 16