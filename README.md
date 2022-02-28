# PyRwu

### これは何?
* 飴屋／菖蒲氏によって公開されている、Windows向けに作成された歌声合成ソフトウェア「UTAU」に同梱されている、wavファイル伸縮用ソフトresampler.exeの互換プロジェクトです。

    UTAU公式サイト(http://utau2008.web.fc2.com/)

* プロジェクト名はPy Resampler by world for utauの略でPyRwu(ぱいるぅ)と読みます。
* 音声処理のコアな部分はPyWORLDを使用しています。

    PyWORLD(https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder)

* 改造や組み込みを歓迎しますが、それらのためのドキュメントは準備中です。
* 合成処理時に、worldの解析結果のうち最も時間がかかる非周期性指標をwavフォルダと同じ場所に.d4cの拡張子で生成します。ファイルサイズがwavの20倍ぐらいあります。
* 兄弟プロジェクト

    PyWavTool(https://github.com/delta-kimigatame/PyWavTool)

***

### 免責事項
* 本ソフトウェアを使用して生じたいかなる不具合についても、作者は責任を負いません。
* 作者は、本ソフトウェアの不具合を修正する責任を負いません。

***

### 使用できるフラグ
使用できるフラグは

```PyRwuExe.Exe --show-flags```

でも確認できます。

    B       0 ～ 100         default:50
            息成分の強さ(ブレシネス)。大きいほど息っぽい
            0～49ではB0の時非周期性指標が全て0になるように乗算します。
            51～100ではB100の時、1000Hz～5000Hz帯の非周期性指標が全て1になるように加算します。

    eb      0 ～ 100         default:0
            語尾の息成分の強さ。大きいほど息っぽい

    ebs     -1000 ～ 1000    default:0
            ノート前半部分の語尾息がかからない時間を5ms単位で指定します。
            負の数を指定するとノート末尾からの時間になります。

    eba     0 ～ 1000        default:0
            ebフラグのアタックタイムを5ms単位で指定します。

    g       -100 ～ 100      default:0
            疑似ジェンダー値
            負の数で女声化・若年化
            正の数で男声化・大人化します。

    t       -100 ～ 100      default:0
            音程の補正。1cent単位

    P       0 ～ 100         default:86
            ピークコンプレッサー。
            P100の時volume適用前の音量最大値が-6dBになるように正規化
            P0の時は何もしない。

    e                        default:False
            wavの伸縮方法。
            通常はループ方式で、このフラグを設定するとストレッチ式になる。

    A       -100 ～ 100      default:0
            ピッチ変動にあわせて音量が変化します。
            1～100では、基準より高いとき音量が小さくなります。
            -1～-100では、基準より低いとき音量が小さくなります。

    gw      0 ～ 500         default:0
            うなり声、グロウル
            グロウルが

    gws     -1000 ～ 1000    default:0
            ノート前半部分のグロウルがかからない時間を5ms単位で指定します。
            負の数を指定するとノート末尾からの時間になります。

    gwa     0 ～ 1000        default:0
            gwフラグのアタックタイムを5ms単位で指定します。

***

### 技術仕様
* 全体の処理の流れについては(https://delta-kimigatame.github.io/PyRwu/resamp.html)
* 各種設定項目については(https://delta-kimigatame.github.io/PyRwu/settings.html)

***

### リンク
* twitter(https://twitter.com/delta_kuro)
* github(https://github.com/delta-kimigatame/MakeOtoTemp)