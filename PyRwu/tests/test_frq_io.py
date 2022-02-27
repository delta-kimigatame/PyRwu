import unittest


import os.path
import os
import shutil
import numpy as np
import pyworld as pw

import frq_io
import wave_io

class TestFrqRead(unittest.TestCase):
    '''
    エラーなく読み込むことは確認できているが、読み込み値が適正であるかのチェックは不十分
    '''
    def test_read_frq(self):
        data, t = frq_io.read(os.path.join("tests","testdata","inputwav","a_wav.frq"),0,0,44100,5.0)
        self._input_data, self._framerate = wave_io.read(os.path.join("tests","testdata","inputwav","a.wav"), 0,0)
        self._f0, self._t = pw.harvest(self._input_data, self._framerate, frame_period=5.0)
        self.assertEqual(data.shape[0], self._f0.shape[0])
        self.assertEqual(t.shape[0], self._t.shape[0])
        self.assertEqual(t[-1], self._t[-1])
        
    def test_read_frq_with_emdms(self):
        data, t = frq_io.read(os.path.join("tests","testdata","inputwav","a_wav.frq"),0,10,44100,5.0)
        self._input_data, self._framerate = wave_io.read(os.path.join("tests","testdata","inputwav","a.wav"), 0,10)
        self._f0, self._t = pw.harvest(self._input_data, self._framerate, frame_period=5.0)
        self.assertEqual(data.shape[0], self._f0.shape[0])
        self.assertEqual(t.shape[0], self._t.shape[0])
        self.assertEqual(t[-1], self._t[-1])
        
    def test_read_frq_with_emdms_negative(self):
        data, t = frq_io.read(os.path.join("tests","testdata","inputwav","a_wav.frq"),0,-10,44100,5.0)
        self._input_data, self._framerate = wave_io.read(os.path.join("tests","testdata","inputwav","a.wav"), 0,-10)
        self._f0, self._t = pw.harvest(self._input_data, self._framerate, frame_period=5.0)
        self.assertEqual(data.shape[0], self._f0.shape[0])
        self.assertEqual(t.shape[0], self._t.shape[0])
        self.assertEqual(t[-1], self._t[-1])
