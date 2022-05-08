'''PyRwuIniquity

Py Resampler by World for UTAUの略です。
使用方法をUTAUからの直接起動に限定することで高速化を実現しています。

* 飴屋／菖蒲氏によって公開されている、
  Windows向けに作成された歌声合成ソフトウェア「UTAU」に同梱されている、
  wavファイル伸縮用ソフトresampler.exeの代替機能を提供するプロジェクトです。
'''

import sys
import os.path
import threading
import psutil

sys.path.append(os.path.dirname(__file__)) #embeddable pythonにimpot用のパスを追加
import resamp
import settings

def resamp_run(input_path: str, output_path: str, target_tone: str, velocity: 100,
               flag_value: str="", offset: float=0, target_ms: float=0, fixed_ms: float=0,
               end_ms: float=0, volume: int=100, modulation: int=0, tempo: str="!120", pitchbend: str=""):
    resamp.Resamp(input_path=input_path,
                  output_path=output_path,
                  target_tone=target_tone,
                  velocity=velocity,
                  flag_value=flag_value,
                  offset=offset,
                  target_ms=target_ms,
                  fixed_ms=fixed_ms,
                  end_ms=end_ms,
                  volume=volume,
                  modulation=modulation,
                  tempo=tempo,
                  pitchbend=pitchbend).resamp()


if __name__=="__main__":
    proc: psutil.Process = psutil.Process()
    while not proc.cmdline()[-1].endswith("temp.bat"):
        proc = proc.parent()
        if proc is None:
            raise ValueError("実行方法が不正です。")
    bat_path: str = proc.cmdline()[-1]
    with open(bat_path, "r", encoding="cp932") as fr:
        datas = fr.read().replace("\r","").split("\n")
    oto: str = ""
    cachedir: str = ""
    flags: str = ""
    velocity: int = 100
    tempfile: str = ""
    params: list = []
    resamp_args: list = []
    threads: list = []
    for line in datas:
        if line == "":
            continue
        elif "@set oto=" in line:
            oto = line.replace("@set oto=","")
        elif "@set cachedir=" in line:
            cachedir = line.replace("@set cachedir=","")
        elif "@set flag=" in line:
            flags = line.replace("@set flag=","")
        elif "@set vel=" in line:
            velocity = int(line.replace("@set vel=",""))
        elif "@set temp=" in line:
            tempfile = line.replace("@set temp=","")
            tempfile = tempfile.replace("%cachedir%", cachedir).replace("\"","")
        elif "@set params=" in line:
            params = line.replace("@set params=","").split(" ")
        elif "@call %helper% " in line:
            resamp_args = line.replace("@call %helper% ","").split(" ")
            threads.append(threading.Thread(target=resamp_run,
                                            args=(" ".join(resamp_args[:-8]).replace("\"","").replace("%oto%", oto),
                                            tempfile,
                                            resamp_args[-8],
                                            velocity,
                                            flags,
                                            float(resamp_args[-5]),
                                            float(resamp_args[-4]),
                                            float(resamp_args[-3]),
                                            float(resamp_args[-2]),
                                            int(params[0]),
                                            int(params[1]),
                                            params[2],
                                            params[3],)))
            threads[-1].start()
        for t in threads:
            t.join()

