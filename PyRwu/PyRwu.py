'''PyRwu

Py Resampler by World for UTAUの略です。

* 飴屋／菖蒲氏によって公開されている、
  Windows向けに作成された歌声合成ソフトウェア「UTAU」に同梱されている、
  wavファイル伸縮用ソフトresampler.exeの代替機能を提供するプロジェクトです。

Usage
-----
>>> usage: PyRwu.py [-h] [--show-flag]
                input_path output_path target_tone velocity [flags] [offset] [target_ms] [fixed_ms] [end_ms]
                [volume] [modulation] [pitchbend]

Parameters
----------
input_path: str
    原音のファイル名
output_path: str
    wavファイルの出力先パス
target_tone: str
    音高名(A4=440Hz)。
    半角上げは#もしくは♯ 
    半角下げはbもしくは♭で与えられます。
velocity: int
    子音速度
flags: str, default ""
    フラグ(省略可)
offset: float, default 0
    入力ファイルの読み込み開始位置(ms)
target_ms: float, default 0
    出力ファイルの長さ(ms)
    UTAUでは通常50ms単位に丸めた値が渡される。
fixed_ms: float, default 0
    offsetからみて通常伸縮しない長さ(ms)
end_ms: float, default 0
    入力ファイルの読み込み終了位置(ms)(省略可 default:0)
    正の数の場合、ファイル末尾からの時間
    負の数の場合、offsetからの時間
volume: int, default 100
    音量。0～200(省略可)
modulation: int, default 0
    モジュレーション。0～200(省略可)
pitchbend: str, default ""
    ピッチベンド。(省略可)
    -2048～2047までの12bitの2進数をbase64で2文字の文字列に変換し、
    同じ数字が続く場合ランレングス圧縮したもの
'''

import sys
import os.path
import argparse

import settings

class ShowFlagAction(argparse.Action):
    '''ShowFlagAction

    --show-flagオプションで実行された際に、フラグの詳細を表示します。

    '''
    def __init__(self, option_strings, dest, **kwargs):
        super(ShowFlagAction, self).__init__(option_strings, dest=dest, nargs=0, help="使用できるフラグの詳細を表示", **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(settings.FLAGS.getDetail())
        parser.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This module is Resampler for UTAU powered by world")
    parser.add_argument("input_path", help="原音のファイル名", type=str)
    parser.add_argument("output_path", help="wavファイルの出力先パス", type=str)
    parser.add_argument("target_tone", help="音高名(A4=440Hz)。" + 
                        "半角上げは#もしくは♯" + 
                        "半角下げはbもしくは♭で与えられます。", type=str)
    parser.add_argument("velocity", help="子音速度", type=int)
    parser.add_argument("flags", help="フラグ(省略可 default:\"\")。詳細は--show-flags参照", type=str, nargs="?", default="")
    parser.add_argument("offset", help="入力ファイルの読み込み開始位置(ms)(省略可 default:0)", type=float, nargs="?", default=0)
    parser.add_argument("target_ms", help="出力ファイルの長さ(ms)(省略可 default:0)"+
                        "UTAUでは通常50ms単位に丸めた値が渡される。", type=int, nargs="?", default=0)
    parser.add_argument("fixed_ms", help="offsetからみて通常伸縮しない長さ(ms)", type=float, nargs="?", default=0)
    parser.add_argument("end_ms", help="入力ファイルの読み込み終了位置(ms)(省略可 default:0)"+
                        "正の数の場合、ファイル末尾からの時間" + 
                        "負の数の場合、offsetからの時間", type=float, nargs="?", default=0)
    parser.add_argument("volume", help="音量。0～200(省略可 default:100)", type=int, nargs="?", default=100)
    parser.add_argument("modulation", help="モジュレーション。0～200(省略可 default:0)", type=int, nargs="?", default=0)
    parser.add_argument("pitchbend", help="ピッチベンド。(省略可 default:\"\")"+
                        "-2048～2047までの12bitの2進数をbase64で2文字の文字列に変換し、" + 
                        "同じ数字が続く場合ランレングス圧縮したもの", type=str, nargs="?", default="")
    parser.add_argument("--show-flag", action=ShowFlagAction)
    args = parser.parse_args()