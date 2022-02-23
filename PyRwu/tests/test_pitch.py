import unittest
import math

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