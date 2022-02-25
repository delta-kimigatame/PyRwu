Search.setIndex({docnames:["PyRwu","effects","flags","index","modules","pitch","resamp","settings","stretch","tests","wave_io"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["PyRwu.rst","effects.rst","flags.rst","index.rst","modules.rst","pitch.rst","resamp.rst","settings.rst","stretch.rst","tests.rst","wave_io.rst"],objects:{"":[[0,0,0,"-","PyRwu"],[1,0,0,"-","effects"],[2,0,0,"-","flags"],[5,0,0,"-","pitch"],[6,0,0,"-","resamp"],[7,0,0,"-","settings"],[8,0,0,"-","stretch"],[9,0,0,"-","tests"],[10,0,0,"-","wave_io"]],"effects.base":[[1,1,1,"","EffectBase"],[1,1,1,"","PitchEffectBase"],[1,1,1,"","WorldEffectBase"]],"effects.base.EffectBase":[[1,2,1,"","apply"]],"effects.base.PitchEffectBase":[[1,2,1,"","apply"]],"effects.base.WorldEffectBase":[[1,2,1,"","apply"]],"effects.g_flag":[[1,1,1,"","GFlag"]],"effects.g_flag.GFlag":[[1,2,1,"","apply"]],"effects.t_flag":[[1,1,1,"","TFlag"]],"effects.t_flag.TFlag":[[1,2,1,"","apply"]],"flags.Flag":[[2,3,1,"id0","default_bool"],[2,3,1,"id1","default_value"],[2,3,1,"id2","descriptions"],[2,3,1,"id3","flag"],[2,3,1,"id4","isBool"],[2,3,1,"id5","max"],[2,3,1,"id6","min"],[2,3,1,"id7","name"],[2,3,1,"id8","value"]],"flags.Flags":[[2,2,1,"","add"],[2,2,1,"","getDetail"],[2,3,1,"id9","params"],[2,2,1,"","parse"]],"resamp.Resamp":[[6,3,1,"id0","ap"],[6,2,1,"","applyPitch"],[6,3,1,"id1","end_ms"],[6,3,1,"id2","f0"],[6,3,1,"id3","fixed_frames"],[6,3,1,"id4","fixed_ms"],[6,3,1,"id5","flag_value"],[6,3,1,"id6","flags"],[6,3,1,"id7","framerate"],[6,2,1,"","getInputData"],[6,3,1,"id8","input_data"],[6,3,1,"id9","input_path"],[6,3,1,"id10","modulation"],[6,3,1,"id11","offset"],[6,3,1,"id12","output_data"],[6,3,1,"id13","output_path"],[6,2,1,"","parseFlags"],[6,2,1,"","pitchShift"],[6,3,1,"id14","pitchbend"],[6,3,1,"id15","pitches"],[6,3,1,"id16","sp"],[6,2,1,"","stretch"],[6,2,1,"","synthesize"],[6,3,1,"id17","t"],[6,3,1,"id18","target_frames"],[6,3,1,"id19","target_frq"],[6,3,1,"id20","target_ms"],[6,5,1,"","target_tone"],[6,3,1,"id21","tempo"],[6,3,1,"id22","velocity"],[6,3,1,"id23","volume"]],"tests.test_flags":[[9,1,1,"","TestFlag"],[9,1,1,"","TestFlags"]],"tests.test_flags.TestFlag":[[9,2,1,"","test_change_bool"],[9,2,1,"","test_change_bool_missing_reason_not_bool"],[9,2,1,"","test_change_value"],[9,2,1,"","test_change_value_missing_reason_bool"],[9,2,1,"","test_change_value_missing_reason_overflow"],[9,2,1,"","test_change_value_missing_reason_underflow"],[9,2,1,"","test_default_init"],[9,2,1,"","test_init"],[9,2,1,"","test_init_bool"],[9,2,1,"","test_init_bool_and_default"]],"tests.test_flags.TestFlags":[[9,2,1,"","setUp"],[9,2,1,"","test_getDetail"],[9,2,1,"","test_parse_bool_simple"],[9,2,1,"","test_parse_bool_with_number"],[9,2,1,"","test_parse_multi"],[9,2,1,"","test_parse_range_Multi"],[9,2,1,"","test_parse_range_Multi_with_bool"],[9,2,1,"","test_parse_range_negative"],[9,2,1,"","test_parse_range_not_match_only_character"],[9,2,1,"","test_parse_range_positive"],[9,2,1,"","test_parse_range_simple"]],"tests.test_pitch":[[9,1,1,"","TestDecodeBase64"],[9,1,1,"","TestDecodeRunLength"],[9,1,1,"","TestGetFrqFromStr"],[9,1,1,"","TestGetPitchRange"],[9,1,1,"","TestInterpPitch"]],"tests.test_pitch.TestDecodeBase64":[[9,2,1,"","test_max"],[9,2,1,"","test_min"],[9,2,1,"","test_zero"]],"tests.test_pitch.TestDecodeRunLength":[[9,2,1,"","test_sandwich"],[9,2,1,"","test_simple"],[9,2,1,"","test_twice"]],"tests.test_pitch.TestGetFrqFromStr":[[9,2,1,"","test_getfrq_Dflat6"],[9,2,1,"","test_getfrq_Dflat6_zen"],[9,2,1,"","test_getfrq_a3"],[9,2,1,"","test_getfrq_a4"],[9,2,1,"","test_getfrq_a5"],[9,2,1,"","test_getfrq_c1"],[9,2,1,"","test_getfrq_c4"],[9,2,1,"","test_getfrq_csharp6"],[9,2,1,"","test_getfrq_csharp6_zen"]],"tests.test_pitch.TestGetPitchRange":[[9,2,1,"","test_bad_tempo"],[9,2,1,"","test_get_pitch_range"],[9,2,1,"","test_get_pitch_range_tempo_float"]],"tests.test_pitch.TestInterpPitch":[[9,2,1,"","test_interp_narrow"],[9,2,1,"","test_interp_narrow_with_pad"],[9,2,1,"","test_interp_wide"]],"tests.test_resamp":[[9,1,1,"","TestResampInnit"]],"tests.test_resamp.TestResampInnit":[[9,2,1,"","test_applyPitch"],[9,2,1,"","test_applyPitch_2"],[9,2,1,"","test_applyPitch_with_t_flag"],[9,2,1,"","test_init"],[9,2,1,"","test_input_data"],[9,2,1,"","test_input_data_with_FileNotFoundError"],[9,2,1,"","test_input_data_with_TypeError"],[9,2,1,"","test_parse_flag"],[9,2,1,"","test_pitch_shift"],[9,2,1,"","test_stretch_data_long"],[9,2,1,"","test_stretch_data_long_with_e_flag"],[9,2,1,"","test_stretch_data_short"],[9,2,1,"","test_stretch_data_short_with_e_flag"],[9,2,1,"","test_synthesize"],[9,2,1,"","test_synthesize_g_minus"],[9,2,1,"","test_synthesize_g_plus"]],"tests.test_stretch":[[9,1,1,"","TestVelocity"],[9,1,1,"","TestWorldLoop"],[9,1,1,"","TestWorldStretch"]],"tests.test_stretch.TestVelocity":[[9,2,1,"","test_velocity_0"],[9,2,1,"","test_velocity_100"],[9,2,1,"","test_velocity_200"]],"tests.test_stretch.TestWorldLoop":[[9,2,1,"","setUp"],[9,2,1,"","test_stretch_0_5"],[9,2,1,"","test_stretch_1_5"],[9,2,1,"","test_stretch_2"]],"tests.test_stretch.TestWorldStretch":[[9,2,1,"","setUp"],[9,2,1,"","test_stretch_0_5"],[9,2,1,"","test_stretch_0_7"],[9,2,1,"","test_stretch_1_5"],[9,2,1,"","test_stretch_2"]],"tests.test_wave_io":[[9,1,1,"","TestWaveRead"],[9,1,1,"","TestWaveWrite"]],"tests.test_wave_io.TestWaveRead":[[9,2,1,"","test_input_file_not_found"],[9,2,1,"","test_not_wav_raise_error"],[9,2,1,"","test_read_44100_16_mono"],[9,2,1,"","test_read_44100_16_mono_end_negative_offset"],[9,2,1,"","test_read_44100_16_mono_end_offset"],[9,2,1,"","test_read_44100_16_mono_offset"],[9,2,1,"","test_read_44100_16_mono_range"],[9,2,1,"","test_read_44100_16_stereo"],[9,2,1,"","test_read_44100_24_mono"],[9,2,1,"","test_read_48000_16_mono"],[9,2,1,"","test_read_8000_8_mono"],[9,2,1,"","test_read_8000_8_mono_range"],[9,2,1,"","test_read_96000_32_mono"]],"tests.test_wave_io.TestWaveWrite":[[9,2,1,"","setUp"],[9,2,1,"","test_read_44100_16_mono"],[9,2,1,"","test_read_44100_16_stereo"],[9,2,1,"","test_read_44100_24_mono"],[9,2,1,"","test_read_48000_16_mono"],[9,2,1,"","test_read_8000_8_mono"],[9,2,1,"","test_read_96000_32_mono"]],PyRwu:[[0,1,1,"","ShowFlagAction"]],effects:[[1,0,0,"-","base"],[1,0,0,"-","g_flag"],[1,0,0,"-","t_flag"]],flags:[[2,1,1,"","Flag"],[2,1,1,"","Flags"]],pitch:[[5,4,1,"","decodeBase64"],[5,4,1,"","decodeBase64Core"],[5,4,1,"","decodeRunLength"],[5,4,1,"","getFrqFromStr"],[5,4,1,"","getPitchRange"],[5,4,1,"","interpPitch"]],resamp:[[6,1,1,"","Resamp"]],settings:[[7,5,1,"","A4FRQ"],[7,5,1,"","AP_EFFECTS"],[7,5,1,"","F0_EFFECTS"],[7,5,1,"","FLAGS"],[7,5,1,"","OUT_WAVE_EFFECTS"],[7,5,1,"","PITCH_EFFECTS"],[7,5,1,"","PYWORLD_F0_CEIL"],[7,5,1,"","PYWORLD_F0_FLOOR"],[7,5,1,"","PYWORLD_PERIOD"],[7,5,1,"","PYWORLD_Q1"],[7,5,1,"","PYWORLD_THRESHOLD"],[7,5,1,"","SP_EFFECTS"],[7,5,1,"","TONE_NUM"],[7,5,1,"","WORLD_EFFECTS"]],stretch:[[8,4,1,"","calc_velocity_rate"],[8,4,1,"","world_loop"],[8,4,1,"","world_stretch"]],tests:[[9,0,0,"-","test_flags"],[9,0,0,"-","test_pitch"],[9,0,0,"-","test_resamp"],[9,0,0,"-","test_stretch"],[9,0,0,"-","test_wave_io"]],wave_io:[[10,4,1,"","read"],[10,4,1,"","write"]]},objnames:{"0":["py","module","Python \u30e2\u30b8\u30e5\u30fc\u30eb"],"1":["py","class","Python \u30af\u30e9\u30b9"],"2":["py","method","Python \u30e1\u30bd\u30c3\u30c9"],"3":["py","property","Python \u30d7\u30ed\u30d1\u30c6\u30a3"],"4":["py","function","Python \u306e\u95a2\u6570"],"5":["py","attribute","Python \u306e\u5c5e\u6027"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:property","4":"py:function","5":"py:attribute"},terms:{"##":[],"'runtest":9,"((":8,"(a":[0,6],"(b":6,"(cent":1,"(g":6,"(ms":[0,5,6,7,10],"(p":6,"(sec":6,"(t":6,")(":[0,6,10],")/":8,")\u3002":[0,6],",\u266d":5,",\u266f":5,",_":6,"--":[1,2,5,6,8,10],"-flag":0,"-h":0,"-show":0,"...":7,"._":[2,6],".a":5,".action":0,".base":[3,4,7],".case":9,".default":7,".effectbase":[1,7],".exe":0,".flag":2,".flags":[6,7],".float":10,".g":[3,4],".ndarray":[1,5,6,8,10],".pitcheffectbase":[1,7],".py":0,".pyworld":[1,6,8],".resamp":1,".t":[3,4],".test":4,".testcase":9,".tone":5,".value":[],".worldeffectbase":7,"1cent":[1,6],"2\u500d":8,"4c":6,"4frq":[5,7],"5b":2,"5ms":[1,6,8],">>":[0,5,7,8],"[--":0,"[aabbccddee":8,"[abcde":8,"[abcdedcbab":8,"[key":7,"\u2192 [":5,"\u3001#":5,"\u3001-":5,"\u3002(":[0,6],"\u3002b":2,"\u3002c":5,"\u300cutau":0,"\u3042\u305f\u308a":5,"\u3042\u308a":6,"\u3042\u308b":[6,7,9,10],"\u3042\u308f\u305b":[],"\u3044\u308b":[0,9],"\u3046\u3061":[6,7],"\u304a\u3088\u3073":6,"\u304b\u3089":[0,5,6,7,8,10],"\u304b\u3089\u307f":[0,6],"\u304c\u3064\u3044":[0,5,6],"\u304c\u308b":6,"\u304f\u3060":6,"\u3053\u3068":[6,9],"\u3053\u306e":[1,6],"\u3053\u308c":6,"\u3055\u3044":6,"\u3059\u3067":10,"\u3059\u308b":[0,1,2,6,7,8,10],"\u305d\u3046":6,"\u305f\u3044":6,"\u305f\u3081":[6,7],"\u305f\u308b":10,"\u3067\u304d":[6,9],"\u3067\u3059":0,"\u3068\u304d":[5,6,8,10],"\u3068\u3057":5,"\u3068\u3057\u3066":[6,7],"\u3069\u306e":8,"\u306a\u3044":[0,5,6],"\u306a\u304b\u3063":[5,6,10],"\u306a\u304f":[6,9],"\u306a\u3051\u308c":10,"\u306a\u3069":2,"\u306a\u3089":2,"\u306a\u308a":[5,8],"\u306a\u308b":[5,6,7],"\u306b\u3044":10,"\u306b\u3064\u3044\u3066":6,"\u306b\u3088\u3063":0,"\u306b\u5bfe\u3059\u308b":5,"\u306b\u95a2\u3059\u308b":[2,6],"\u3072\u3068\u3064":5,"\u307e\u3059":[0,1,5,6,7,8,10],"\u307e\u305b":6,"\u307e\u305f":6,"\u307e\u3067":[0,6],"\u3082\u3057":10,"\u3082\u3057\u304f":[0,5,6],"\u3082\u306e":[0,6,10],"\u3088\u3046":[2,5,8],"\u3089\u308c":[0,5,6],"\u3089\u308c\u308b":[2,5,7],"\u308c\u308b":[0,1,2,5,6,7,8],"\u30a8\u30d5\u30a7\u30af\u30c8":7,"\u30a8\u30e9\u30fc":9,"\u30a8\u30f3\u30b3\u30fc\u30c9":5,"\u30aa\u30af\u30bf\u30fc\u30d6":6,"\u30aa\u30d7\u30b7\u30e7\u30f3":0,"\u30aa\u30f3\u30aa\u30d5":2,"\u30aa\u30fc\u30d0\u30fc\u30e9\u30a4\u30c9":6,"\u30ad\u30fc":2,"\u30af\u30e9\u30b9":[1,2,7],"\u30b5\u30f3\u30d7\u30ea\u30f3\u30b0":[5,6,10],"\u30b5\u30f3\u30d7\u30eb\u30ec\u30fc\u30c8":10,"\u30b8\u30a7\u30f3\u30c0\u30fc":1,"\u30b9\u30da\u30af\u30c8\u30eb":[6,7,8],"\u30bd\u30d5\u30c8\u30a6\u30a7\u30a2":0,"\u30bd\u30d5\u30c8resampler":0,"\u30bf\u30a4\u30d7":2,"\u30bf\u30a4\u30df\u30f3\u30b0":5,"\u30c1\u30a7\u30c3\u30af":9,"\u30c6\u30f3\u30dd":[0,5,6],"\u30c7\u30b3\u30fc\u30c9":5,"\u30c7\u30d5\u30a9\u30eb\u30c8":[1,6,7,8],"\u30c7\u30fc\u30bf":[5,6,7,8,10],"\u30ce\u30fc\u30c8":6,"\u30d0\u30a4\u30c8":10,"\u30d1\u30b9":[0,6,10],"\u30d1\u30e9\u30e1\u30fc\u30bf":[1,2,5,6,7,8,10],"\u30d1\u30e9\u30e1\u30fc\u30bf\u30fc":6,"\u30d1\u30fc\u30b9":[2,6],"\u30d4\u30c3\u30c1":[0,1,5,6,7],"\u30d4\u30c3\u30c1\u30d9\u30f3\u30c9":[0,6],"\u30d5\u30a1\u30a4\u30eb":[0,5,6,10],"\u30d5\u30a9\u30eb\u30c0":10,"\u30d5\u30e9\u30b0":[0,2,6,7],"\u30d5\u30ec\u30fc\u30e0":[5,6,7,8],"\u30d7\u30ed\u30b8\u30a7\u30af\u30c8":0,"\u30d9\u30fc\u30b9\u30af\u30e9\u30b9":[0,1,2,6,9],"\u30da\u30fc\u30b8":3,"\u30e1\u30bd\u30c3\u30c9":6,"\u30e1\u30e2":[6,8],"\u30e2\u30b8\u30e5\u30ec\u30fc\u30b7\u30e7\u30f3":[0,6],"\u30e2\u30b8\u30e5\u30fc\u30eb":3,"\u30e9\u30f3\u30ec\u30f3\u30b0\u30b9":[0,5,6],"\u30fb\u30e2\u30b8\u30e5\u30ec\u30fc\u30b7\u30e7\u30f3":6,"\u4e00\u7d44":5,"\u4e00\u90e8":[6,7],"\u4e0a\u3052":[],"\u4e0a\u3052\u308b":6,"\u4e0a\u66f8\u304d":10,"\u4e0a\u9650":[6,7],"\u4e0b\u8a18":6,"\u4e0b\u9650":[6,7],"\u4e0d\u8981":[6,7],"\u4e0e\u3048":[0,2,5,6,7],"\u4e0e\u3048\u308b":1,"\u4e38\u3081":[0,5,6],"\u4ed5\u69d8":6,"\u4ed5\u7d44\u307f":[],"\u4ee3\u66ff":0,"\u4ee5\u4e0a":5,"\u4ee5\u4e0b":7,"\u4ee5\u964d":6,"\u4f38\u7e2e":[0,6,8],"\u4f38\u7e2e\u5f8c":8,"\u4f38\u7e2e\u6a5f":[1,6],"\u4f4d\u7f6e":[0,6,10],"\u4f5c\u6210":[0,10],"\u4f7f\u3046":2,"\u4f7f\u7528":[6,7],"\u4f8b\u3048":6,"\u4f8b\u5916":[5,6,10],"\u4fdd\u5b58":10,"\u5143\u76ee":[6,8],"\u5143\u914d":[6,8],"\u5165\u308b":6,"\u5165\u529b":[0,6,10],"\u5168\u4f53":8,"\u516c\u958b":0,"\u518d\u5e30":10,"\u51e6\u7406":[1,6,7],"\u51e6\u7406\u5f8c":1,"\u51fa\u529b":[0,2,5,6],"\u51fa\u529b\u9577":5,"\u5206\u6790":[6,7],"\u5207\u308a":2,"\u5207\u308a\u4e0a\u3052":5,"\u5217\u9593":5,"\u521d\u671f":6,"\u521d\u671f\u5024":[2,7],"\u5224\u5b9a":[6,7],"\u5224\u65ad":[6,7],"\u524d\u63d0":[6,7],"\u52a0\u5de5":[1,6],"\u52d5\u4f5c":6,"\u5305\u7d61":[6,7,8],"\u533a\u9593":10,"\u5341\u5206":9,"\u534a\u5206":5,"\u534a\u89d2":[],"\u534a\u89d2\u4e0a\u3052":[0,6],"\u534a\u89d2\u4e0b\u3052":[0,6],"\u534a\u97f3":[5,6],"\u5358\u4f4d":[0,1,5,6],"\u539f\u97f3":[0,6,10],"\u53d6\u5f97":6,"\u53ef\u80fd":5,"\u5408\u6210":[0,6],"\u540c\u3058":[0,6],"\u540c\u68b1":0,"\u5411\u3051":0,"\u5468\u6ce2":[5,6,8,10],"\u5468\u6ce2\u6570":1,"\u554f\u984c":6,"\u56de\u6570":5,"\u56fa\u5b9a":[6,8],"\u5727\u7e2e":[0,5,6],"\u57cb\u3081":5,"\u57fa\u3065\u3044":6,"\u57fa\u3065\u304d":[6,8],"\u57fa\u672c":5,"\u57fa\u6e96":7,"\u5834\u5408":[0,1,5,6,7,10],"\u58f0\u8cea":[6,8],"\u5909\u63db":[0,1,5,6,7],"\u5909\u66f4":[6,7,8],"\u5927\u4eba":1,"\u5973\u58f0":1,"\u5b50\u97f3":[0,6,8],"\u5b57\u5217":5,"\u5b9f\u884c":0,"\u5b9f\u969b":6,"\u5c55\u958b":5,"\u5c55\u958b\u5f8c":5,"\u5f15\u304d\u5ef6\u3070":8,"\u5f53\u305f\u308a":[6,7],"\u5f71\u97ff":[1,6],"\u5f8c\u307b\u3069":6,"\u5f8c\u308d":5,"\u5fc5\u8981":5,"\u6210\u524d":6,"\u623b\u308a\u5024":[1,2,5,8,10],"\u6271\u3044":[5,8,10],"\u6271\u3046":2,"\u62bd\u51fa":[6,7],"\u62bd\u8c61":1,"\u6307\u5b9a":[2,6,7,10],"\u6307\u6a19":[6,7,8],"\u63d0\u4f9b":0,"\u6539\u884c":2,"\u6570\u5024":6,"\u6570\u5217":[1,6],"\u6570\u5b57":[0,5,6],"\u6570\u8ef8":[6,8],"\u6574\u6570":5,"\u6587\u5b57":[0,2,5,6],"\u6587\u5b57\u5217":[0,2,5,6],"\u65b9\u5f0f":8,"\u65b9\u6cd5":6,"\u6642\u9593":[0,1,5,6,7,8,10],"\u6642\u9593\u8ef8":[],"\u66f4\u65b0":[2,6],"\u66f8\u304d\u51fa\u3057":10,"\u66f8\u304d\u8fbc\u307f":10,"\u66f8\u5f0f":[5,6],"\u66ff\u3048\u308b":2,"\u6700\u5927":2,"\u6700\u5c0f\u5024":2,"\u6709\u52b9":[5,6],"\u6709\u58f0":[6,7],"\u671f\u5024":[6,7],"\u671f\u6027":[6,7,8],"\u672b\u5c3e":[0,6,10],"\u691c\u7d22":3,"\u6a29\u9650":10,"\u6a5f\u80fd":0,"\u6b21\u5143":10,"\u6b4c\u58f0":0,"\u6c42\u3081":[5,8],"\u6c7a\u5b9a":[6,7,8],"\u6ce2\u5f62":[6,10],"\u6d3b\u7528":6,"\u6df1\u5ea6":10,"\u6e21\u3055":[0,5,6,7],"\u6e80\u305f":5,"\u7121\u58f0":[6,7],"\u7121\u8996":5,"\u751f\u6210":[1,6,8],"\u7537\u58f0":1,"\u7591\u4f3c":1,"\u76ee\u4ee5\u964d":5,"\u7701\u7565":[0,6],"\u7701\u7565\u53ef":[0,6,10],"\u78ba\u8a8d":9,"\u7a2e\u5b9a":7,"\u7a2e\u985e":[2,5],"\u7bc4\u56f2":[2,6,8,10],"\u7d20\u6bce":2,"\u7d22\u5f15":3,"\u7d42\u4e86":[0,6,10],"\u7d44\u307f\u5408\u308f\u305b\u308b":[6,7],"\u7d50\u5408":2,"\u7d50\u679c":6,"\u7d99\u627f":1,"\u7d9a\u304f":[0,6],"\u7dda\u5f62":5,"\u7e70\u308a\u8fd4\u3057":5,"\u82e5\u5e74":1,"\u83d6\u84b2":0,"\u8868\u3057":[5,10],"\u8868\u3059":5,"\u8868\u793a":0,"\u88dc\u5b8c":5,"\u88dc\u6b63":[1,6,7],"\u8907\u6570":[1,7],"\u898f\u5b9a":6,"\u8a08\u7b97":6,"\u8a18\u53f7":5,"\u8a18\u61b6":6,"\u8a2d\u5b9a":[6,7],"\u8a73\u7d30":[0,2],"\u8a8d\u8b58":5,"\u8aac\u660e\u6587":2,"\u8aad\u307f\u8fbc\u307f":[0,6,9,10],"\u8aad\u307f\u8fbc\u3080":9,"\u8aad\u307f\u8fbc\u3093":6,"\u8abf\u6574":[6,7],"\u8f9e\u66f8":[2,7],"\u8fd4\u3057":[5,8,10],"\u8fd4\u3059":[2,5],"\u8ffd\u52a0":2,"\u9014\u4e2d":6,"\u901a\u308a":6,"\u901a\u5e38":[0,5,6,7],"\u901f\u5ea6":[0,6,8],"\u9032\u6570":[0,6],"\u9069\u6b63":[5,6,9],"\u9069\u7528":[6,7],"\u914d\u5217":[2,6],"\u9577\u3055":[0,5,6,8],"\u958b\u59cb":[0,6,10],"\u9593\u9694":5,"\u95a2\u4fc2":[5,10],"\u95be\u5024":[6,7],"\u9664\u3057":5,"\u975e\u5468":[6,7,8],"\u97f3\u58f0":[6,7,8],"\u97f3\u58f0\u5408":6,"\u97f3\u7a0b":[1,6],"\u97f3\u7b26":5,"\u97f3\u91cf":[0,6],"\u97f3\u9ad8":[5,6,7,8],"\u9806\u5e8f":6,"\u98f4\u5c4b":0,"\u9ad8\u540d":[0,6],"]=":6,"^(":6,"class":[0,1,2,6,9],"default":[0,2,6,7,10],"false":2,"float":[0,1,5,6,7,8,10],"for":[0,9],"int":[0,2,5,6,8,10],"new":[1,8],"package":[3,4],"static":1,"true":2,__:[],_a:9,_and:9,_ap:8,_applypitch:9,_bad:9,_bool:[2,9],_c:9,_call:[],_change:9,_character:9,_csharp:9,_data:[1,5,6,9],_default:9,_dflat:9,_e:9,_effects:7,_end:9,_error:9,_f:[6,7,8],_file:9,_filenotfounderror:9,_flag:[3,4,9],_flags:4,_float:9,_found:9,_frame:7,_frames:[6,8],_frq:6,_g:9,_get:9,_getdetail:9,_getfrq:9,_init:9,_input:9,_interp:9,_io:[3,4],_long:9,_loop:8,_match:9,_max:9,_min:9,_minus:9,_missing:9,_ms:[0,5,6,10],_multi:9,_narrow:9,_negative:9,_not:9,_num:[5,7],_number:9,_offset:9,_only:9,_overflow:9,_pad:9,_parse:9,_path:[0,6,10],_period:[1,6,7,8],_pitch:4,_plus:9,_positive:9,_q:[6,7],_raise:9,_range:9,_rate:8,_read:9,_reason:9,_resamp:4,_sandwich:9,_shift:9,_short:9,_simple:9,_size:[6,8],_sp:8,_stretch:[4,8],_strings:0,_synthesize:9,_t:[5,9],_tempo:9,_threshold:[6,7],_tone:[0,6],_twice:9,_typeerror:9,_underflow:9,_value:[2,5,6,9],_values:1,_velocity:[8,9],_wav:9,_wave:[4,7],_wide:9,_with:9,_zero:9,aa:5,aaabac:5,ab:5,ac:5,add:2,ap:[1,6,7,8],apply:1,applypitch:6,argparse:0,b7:7,base:[0,5,6],before:9,bit:[0,6,10],bool:2,by:0,calc:8,ceil:[6,7],cent:[1,6],cheaptrick:6,contents:4,core:5,data:10,decode:5,decodebase:5,decoderunlength:5,description:2,descriptions:2,dest:0,dict:[2,7],effectbase:1,effects:[3,4,7],eg:2,end:[0,6,10],exercising:9,f0:[6,7],fft:[6,8],filenotfounderror:[6,10],fixed:[0,6],fixture:9,flag:[2,6],flags:[0,3,4,6,7],floor:[6,7],frame:6,framerate:[5,6,10],frq:5,fs:6,getdetail:2,getfrqfromstr:5,getinputdata:6,getpitchrange:5,gflag:1,harvest:[6,7],hook:9,hz:[0,6],input:[0,6,10],interp:5,interppitch:5,io:10,isbool:2,it:9,kwargs:0,list:[2,7],max:2,method:9,methodname:9,min:2,modulation:[0,6],module:[3,4],mono:9,ms:[0,5,6],name:2,ndarray:5,no:5,notenum:7,np:[1,5,6,8,10],num:5,numpy:[1,5,6,8,10],object:[1,2,6],octave:7,of:[1,2,5,6,7,8,10],offset:[0,6,10],option:0,or:[2,10],oserror:10,out:7,output:[0,1,6,10],param:0,params:[1,2],parse:2,parseflags:6,pitch:[3,4,7],pitchbend:[0,6],pitcheffectbase:1,pitches:[1,6],pitchshift:6,property:[2,6],pw:7,py:0,pyworld:7,range:5,rate:8,read:10,resamp:[1,3,4],resampler:0,sampwidth:10,self:[2,6],setting:9,settings:[1,3,4,5,6,8],setup:9,show:0,showflagaction:0,sp:[1,6,7,8],stereo:9,stonemask:6,str:[0,2,5,6,10],stretch:[3,4,6],submodules:[3,4],synthesize:[6,7],target:[0,5,6,8],tempo:[0,5,6],test:9,testdecodebase:9,testdecoderunlength:9,testflag:9,testflags:9,testgetfrqfromstr:9,testgetpitchrange:9,testinterppitch:9,testresampinnit:9,tests:4,testvelocity:9,testwaveread:9,testwavewrite:9,testworldloop:9,testworldstretch:9,tflag:1,the:9,threshold:6,todo:[],tone:[5,6,7],tuple:[1,8,10],type:[0,2,6,7],typeerror:[6,10],unittest:9,up:9,usage:[3,4],utau:[0,5,6,7],value:[2,5],valueerror:[5,6],velocity:[0,6,8],volume:[0,6],wav:[0,5,6,8,10],wave:[3,4,5,7],windows:0,world:[0,1,5,6,7,8],worldeffectbase:1,write:10,wworld:[],zen:9},titles:["PyRwu module","effects package","flags module","Welcome to PyRwu's documentation!","PyRwu","pitch module","resamp module","settings module","stretch module","tests package","wave_io module"],titleterms:{"'s":3,".base":1,".g":1,".t":1,".test":9,"package":[1,9],_flag:1,_flags:9,_io:[9,10],_pitch:9,_resamp:9,_stretch:9,_wave:9,and:3,contents:[1,3,9],documentation:3,effects:1,flags:2,indices:3,module:[0,1,2,5,6,7,8,9,10],pitch:5,pyrwu:[0,3,4],resamp:6,settings:7,stretch:8,submodules:[1,9],tables:3,tests:9,to:3,usage:0,wave:10,welcome:3}})