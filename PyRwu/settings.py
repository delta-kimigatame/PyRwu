'''Settings
各種定数や初期値の設定

Attributes
----------
FLAGS : flags.Flags
    使用するフラグの設定。
'''

import flags

FLAGS = flags.Flags()
FLAGS.add(flags.Flag("B",
                     descriptions=["息成分の強さ(ブレシネス)。大きいほど息っぽい",
                                    "0～49ではB=0の時非周期性指標が全て0になるように乗算します。",
                                    "51～100ではB=100の時非周期性指標が全て1になるように加算します。"],
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
FLAGS.add(flags.Flag("e",
                     descriptions=["wavの伸縮方法。",
                                   "通常はループ方式で、このフラグを設定するとストレッチ式になる。"],
                     isBool=True,
                     default_bool=False))


