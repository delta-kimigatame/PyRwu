import unittest

import os.path
import os
import shutil
import wave
import numpy as np
import pyworld

import wave_io

class TestWaveRead(unittest.TestCase):
    '''
    エラーなく読み込むことは確認できているが、読み込み値が適正であるかのチェックは不十分
    '''
    def test_read_44100_16_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,0)
        self.assertEqual(fs, 44100)
        self.assertEqual(data.shape[0], 44100)
        self.assertEqual(str(type(data[0])), "<class 'numpy.float64'>")
        
    def test_read_44100_16_stereo(self):
        #Rchは0のwavを読み込んで、Lchだけ読み込んでいるかのチェック
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","stereo44_1-16.wav"),0,0)
        self.assertEqual(fs, 44100)
        self.assertEqual(data.shape[0], 44100)
        self.assertNotEqual(data[100],0)
        self.assertNotEqual(data[101],0)
        self.assertEqual(str(type(data[0])), "<class 'numpy.float64'>")
        
    def test_read_8000_8_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono8-8.wav"),0,0)
        self.assertEqual(fs, 8000)
        self.assertEqual(data.shape[0], 8000)
        self.assertEqual(str(type(data[0])), "<class 'numpy.float64'>")
        
    def test_read_48000_16_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono48-16.wav"),0,0)
        self.assertEqual(fs, 48000)
        self.assertEqual(data.shape[0], 48000)
        self.assertEqual(str(type(data[0])), "<class 'numpy.float64'>")
        
    def test_read_44100_24_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-24.wav"),0,0)
        self.assertEqual(fs, 44100)
        self.assertEqual(data.shape[0], 44100)
        self.assertEqual(str(type(data[0])), "<class 'numpy.float64'>")
        
    def test_read_96000_32_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono96k-32.wav"),0,0)
        self.assertEqual(fs, 96000)
        self.assertEqual(data.shape[0], 96000)
        self.assertEqual(str(type(data[0])), "<class 'numpy.float64'>")
        
    def test_not_wav_raise_error(self):
        with self.assertRaises(TypeError) as cm:
            data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","notwav.txt"),0,0)
        self.assertEqual(cm.exception.args[0], "{} can't read. this file isn't wave format.".format(os.path.join("tests","testdata","inputwav","notwav.txt")))
    
    def test_input_file_not_found(self):
        with self.assertRaises(FileNotFoundError) as cm:
            data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","hogehoge"),0,0)
        self.assertEqual(cm.exception.args[0], "{} not found.".format(os.path.join("tests","testdata","inputwav","hogehoge")))
        
    def test_read_44100_16_mono_offset(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,0)
        data2, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),500,0)
        self.assertEqual(fs, 44100)
        self.assertEqual(data2.shape[0], 22050)
        self.assertEqual(data[22050], data2[0])
        
    def test_read_44100_16_mono_end_offset(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,0)
        data2, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,500)
        self.assertEqual(fs, 44100)
        self.assertEqual(data2.shape[0], 22050)
        self.assertEqual(data[22050-1], data2[-1])
        
    def test_read_44100_16_mono_end_negative_offset(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,0)
        data2, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,-250)
        self.assertEqual(fs, 44100)
        self.assertEqual(data2.shape[0], 11025)
        self.assertEqual(data[11025-1], data2[-1])

        
    def test_read_44100_16_mono_range(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,0)
        data2, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),500,-250)
        self.assertEqual(fs, 44100)
        self.assertEqual(data2.shape[0], 11025)
        self.assertEqual(data[22050], data2[0])
        self.assertEqual(data[22050+11025-1], data2[-1])
        
    def test_read_8000_8_mono_range(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono8-8.wav"),0,0)
        data2, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono8-8.wav"),500,-250)
        self.assertEqual(fs, 8000)
        self.assertEqual(data2.shape[0], 2000)
        self.assertEqual(data[4000], data2[0])
        self.assertEqual(data[6000-1], data2[-1])
        
class TestWaveWrite(unittest.TestCase):
    def setUp(self):
        if os.path.isdir(os.path.join("tests","testdata","outputwav")):
            shutil.rmtree(os.path.join("tests","testdata","outputwav"))

    def test_read_44100_16_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),0,0)
        self.assertFalse(os.path.isfile(os.path.join("tests","testdata","outputwav","mono44_1-16.wav")))
        wave_io.write(os.path.join("tests","testdata","outputwav","mono44_1-16.wav"),data, fs, 2)
        self.assertTrue(os.path.isfile(os.path.join("tests","testdata","outputwav","mono44_1-16.wav")))
        
    def test_read_48000_16_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono48-16.wav"),0,0)
        self.assertFalse(os.path.isfile(os.path.join("tests","testdata","outputwav","mono48-16.wav")))
        wave_io.write(os.path.join("tests","testdata","outputwav","mono48-16.wav"),data, fs, 2)
        self.assertTrue(os.path.isfile(os.path.join("tests","testdata","outputwav","mono48-16.wav")))

    def test_read_96000_32_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono96k-32.wav"),0,0)
        self.assertFalse(os.path.isfile(os.path.join("tests","testdata","outputwav","mono96k-32.wav")))
        wave_io.write(os.path.join("tests","testdata","outputwav","mono96k-32.wav"),data, fs, 2)
        self.assertTrue(os.path.isfile(os.path.join("tests","testdata","outputwav","mono96k-32.wav")))
        
    def test_read_44100_24_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono44_1-24.wav"),0,0)
        self.assertFalse(os.path.isfile(os.path.join("tests","testdata","outputwav","mono44_1-24.wav")))
        wave_io.write(os.path.join("tests","testdata","outputwav","mono44_1-24.wav"),data, fs, 2)
        self.assertTrue(os.path.isfile(os.path.join("tests","testdata","outputwav","mono44_1-24.wav")))
        
    def test_read_8000_8_mono(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","mono8-8.wav"),0,0)
        self.assertFalse(os.path.isfile(os.path.join("tests","testdata","outputwav","mono8-8.wav")))
        wave_io.write(os.path.join("tests","testdata","outputwav","mono8-8.wav"),data, fs, 2)
        self.assertTrue(os.path.isfile(os.path.join("tests","testdata","outputwav","mono8-8.wav")))
        
    def test_read_44100_16_stereo(self):
        data, fs = wave_io.read(os.path.join("tests","testdata","inputwav","stereo44_1-16.wav"),0,0)
        self.assertFalse(os.path.isfile(os.path.join("tests","testdata","outputwav","stereo44_1-16.wav")))
        wave_io.write(os.path.join("tests","testdata","outputwav","stereo44_1-16.wav"),data, fs, 2)
        self.assertTrue(os.path.isfile(os.path.join("tests","testdata","outputwav","stereo44_1-16.wav")))