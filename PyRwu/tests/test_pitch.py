import unittest
import math

import numpy as np

import pitch

class TestGetFrqFromStr(unittest.TestCase):
    def test_getfrq_a4(self):
        self.assertEqual(440.0, pitch.getFrqFromStr("A4"))
        
    def test_getfrq_a5(self):
        self.assertEqual(880.0, pitch.getFrqFromStr("A5"))
        
    def test_getfrq_a3(self):
        self.assertEqual(220.0, pitch.getFrqFromStr("A3"))
        
    def test_getfrq_c4(self):
        self.assertEqual(261.626, round(pitch.getFrqFromStr("C4"),3))
        
    def test_getfrq_csharp6(self):
        self.assertEqual(1108.731, round(pitch.getFrqFromStr("C#6"),3))
        
    def test_getfrq_csharp6_zen(self):
        self.assertEqual(1108.731, round(pitch.getFrqFromStr("C♯6"),3))
        
    def test_getfrq_Dflat6(self):
        self.assertEqual(1108.731, round(pitch.getFrqFromStr("Db6"),3))
        
    def test_getfrq_Dflat6_zen(self):
        self.assertEqual(1108.731, round(pitch.getFrqFromStr("D♭6"),3))
        
    def test_getfrq_c1(self):
        self.assertEqual(32.703, round(pitch.getFrqFromStr("C1"),3))

class TestDecodeRunLength(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(pitch.decodeRunLength("AA#3#"),"AAAAAAAA")
        
    def test_sandwich(self):
        self.assertEqual(pitch.decodeRunLength("AA#3#BBAA#5#"),"AAAAAAAABBAAAAAAAAAAAA")
        
    def test_twice(self):
        self.assertEqual(pitch.decodeRunLength("AA#3#BBAA#5#CCAA#3#"),"AAAAAAAABBAAAAAAAAAAAACCAAAAAAAA")

class TestDecodeBase64(unittest.TestCase):
    def test_zero(self):
        np.testing.assert_array_equal(pitch.decodeBase64(pitch.decodeRunLength("AA#6#")), np.array([0,0,0,0,0,0,0]))
        
    def test_max(self):
        np.testing.assert_array_equal(pitch.decodeBase64(pitch.decodeRunLength("AA#6#f/#3#")), np.array([0,0,0,0,0,0,0,2047,2047,2047,2047]))
        
    def test_min(self):
        np.testing.assert_array_equal(pitch.decodeBase64(pitch.decodeRunLength("AA#6#gA#3#")), np.array([0,0,0,0,0,0,0,-2048,-2048,-2048,-2048]))

class TestGetPitchRange(unittest.TestCase):
    def test_get_pitch_range(self):
        prange = pitch.getPitchRange("!100", 30.0, 2500)
        np.testing.assert_array_equal(prange, np.array([0, 6.4, 6.4*2, 6.4*3, 6.4*4, 6.4*5]))
        
    def test_get_pitch_range_tempo_float(self):
        prange = pitch.getPitchRange(100.0, 30.0, 2500)
        np.testing.assert_array_equal(prange, np.array([0, 6.4, 6.4*2, 6.4*3, 6.4*4, 6.4*5]))
        
    def test_bad_tempo(self):
        with self.assertRaises(ValueError) as cm:
            prange = pitch.getPitchRange("!a100", 30.0, 2500)
        self.assertEqual(cm.exception.args[0], "{} is not utau tempo format.".format("!a100"))
        
class TestInterpPitch(unittest.TestCase):
    def test_interp_wide(self):
        base = np.array([0,4,8,12,16,20], dtype=np.float64)
        utau_t = np.array([0,2,4,6,8,10], dtype=np.float64)
        world_t = np.array([0,5,10], dtype=np.float64)
        interp_data = pitch.interpPitch(base, utau_t, world_t)
        np.testing.assert_array_equal(interp_data, np.array([0,10,20]) )
        
    def test_interp_narrow(self):
        base = np.array([0,4,8,12,16,20], dtype=np.float64)
        utau_t = np.array([0,2,4,6,8,10], dtype=np.float64)
        world_t = np.arange(11, dtype=np.float64)
        interp_data = pitch.interpPitch(base, utau_t, world_t)
        np.testing.assert_array_equal(interp_data, np.array([0,2,4,6,8,10,12,14,16,18,20]) )
        
    def test_interp_narrow_with_pad(self):
        base = np.array([0,4,8,12,16,20], dtype=np.float64)
        utau_t = np.array([0,2,4,6,8,10,12], dtype=np.float64)
        world_t = np.arange(13, dtype=np.float64)
        interp_data = pitch.interpPitch(base, utau_t, world_t)
        np.testing.assert_array_equal(interp_data, np.array([0,2,4,6,8,10,12,14,16,18,20,10,0]) )
