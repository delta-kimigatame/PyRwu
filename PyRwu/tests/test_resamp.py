﻿import unittest
import os
import os.path
import numpy as np

import resamp
import wave_io

class TestResampInnit(unittest.TestCase):
    def test_init(self):
        resamp.Resamp(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "C4", 100, "", 0, 500, 0, 0, 100, 0, "!120", "AA#5#")

    def test_parse_flag(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "C4", 100, "g-20B30e15", 0, 500, 0, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.assertEqual(self.resamp.flags.params["g"].value, -20)
        self.assertEqual(self.resamp.flags.params["B"].value, 30)
        self.assertTrue(self.resamp.flags.params["e"].flag)

    def test_input_data(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "C4", 100, "g-20B30e15", 0, 500, 0, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.assertEqual(len(self.resamp.input_data), 44100)
        self.assertEqual(self.resamp.f0.shape[0], 201)
        self.assertEqual(self.resamp.sp.shape[0], 201)
        self.assertEqual(self.resamp.sp.shape[1], 1025)
        self.assertEqual(self.resamp.ap.shape[0], 201)
        self.assertEqual(self.resamp.ap.shape[1], 1025)
        
    def test_input_data_with_TypeError(self):
        with self.assertRaises(TypeError) as cm:
            self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","notwav.txt"),
                          os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                          "C4", 100, "g-20B30e15", 0, 500, 0, 0, 100, 0, "!120", "AA#5#")
            self.resamp.parseFlags()
            self.resamp.getInputData()
        self.assertEqual(cm.exception.args[0], "{} can't read. this file isn't wave format.".format(os.path.join("tests","testdata","inputwav","notwav.txt")))
        
    def test_input_data_with_FileNotFoundError(self):
        with self.assertRaises(FileNotFoundError) as cm:
            self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","hogehoge"),
                          os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                          "C4", 100, "g-20B30e15", 0, 500, 0, 0, 100, 0, "!120", "AA#5#")
            self.resamp.parseFlags()
            self.resamp.getInputData()
        self.assertEqual(cm.exception.args[0], "{} not found.".format(os.path.join("tests","testdata","inputwav","hogehoge")))

        
    def test_stretch_data_short(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "C4", 100, "", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.assertEqual(self.resamp.f0.shape[0], 201)
        self.assertEqual(self.resamp.sp.shape[0], 201)
        self.assertEqual(self.resamp.ap.shape[0], 201)
        self.resamp.stretch()
        self.assertEqual(self.resamp.f0.shape[0], 100)
        self.assertEqual(self.resamp.sp.shape[0], 100)
        self.assertEqual(self.resamp.ap.shape[0], 100)
        
        
    def test_stretch_data_long(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "C4", 100, "", 0, 2000, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.assertEqual(self.resamp.f0.shape[0], 201)
        self.assertEqual(self.resamp.sp.shape[0], 201)
        self.assertEqual(self.resamp.ap.shape[0], 201)
        self.resamp.stretch()
        self.assertEqual(self.resamp.f0.shape[0], 400)
        self.assertEqual(self.resamp.sp.shape[0], 400)
        self.assertEqual(self.resamp.ap.shape[0], 400)
        
    def test_stretch_data_short_with_e_flag(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "C4", 100, "e", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.assertEqual(self.resamp.f0.shape[0], 201)
        self.assertEqual(self.resamp.sp.shape[0], 201)
        self.assertEqual(self.resamp.ap.shape[0], 201)
        self.resamp.stretch()
        self.assertEqual(self.resamp.f0.shape[0], 100)
        self.assertEqual(self.resamp.sp.shape[0], 100)
        self.assertEqual(self.resamp.ap.shape[0], 100)
        
        
    def test_stretch_data_long_with_e_flag(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","mono44_1-16.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "C4", 100, "e", 0, 2000, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.assertEqual(self.resamp.f0.shape[0], 201)
        self.assertEqual(self.resamp.sp.shape[0], 201)
        self.assertEqual(self.resamp.ap.shape[0], 201)
        self.resamp.stretch()
        self.assertEqual(self.resamp.f0.shape[0], 400)
        self.assertEqual(self.resamp.sp.shape[0], 400)
        self.assertEqual(self.resamp.ap.shape[0], 400)
        
    def test_pitch_shift(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "A4", 100, "", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.assertEqual(self.resamp.target_frq,440)
        self.assertEqual(round(np.average(self.resamp.f0),3), 440)


        
    def test_applyPitch(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "A4", 100, "", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        np.testing.assert_array_equal(self.resamp.pitches, np.array([0,0,0,0,0,0]))
        
    def test_applyPitch_2(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "A4", 100, "", 0, 500, 100, 0, 100, 0, "!120", "Sw#100#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        np.testing.assert_array_equal(self.resamp.pitches[0],1200)
        self.assertEqual(round(np.average(self.resamp.f0),3), 880)
        
    def test_applyPitch_with_t_flag(self):
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      os.path.join("tests","testdata","outputresamp","mono44_1-16.wav"),
                      "A4", 100, "t100", 0, 500, 100, 0, 100, 0, "!120", "RM#100#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        np.testing.assert_array_equal(self.resamp.pitches[0],1100)
        self.assertEqual(round(np.average(self.resamp.f0),3), 880)

    def test_synthesize(self):
        output = os.path.join("tests","testdata","outputresamp","synthesize.wav")
        if os.path.isfile(output):
            os.remove(output)
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      output,
                      "A4", 100, "", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        self.assertFalse(os.path.isfile(output))
        self.resamp.synthesize()
        wave_io.write(output, self.resamp.output_data)
        self.assertTrue(os.path.isfile(output))

        
    def test_synthesize_g_minus(self):
        output = os.path.join("tests","testdata","outputresamp","synthesize_g_minus.wav")
        if os.path.isfile(output):
            os.remove(output)
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      output,
                      "A4", 100, "g-30", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        self.assertFalse(os.path.isfile(output))
        self.resamp.synthesize()
        wave_io.write(output, self.resamp.output_data)
        self.assertTrue(os.path.isfile(output))

        
    def test_synthesize_g_plus(self):
        output = os.path.join("tests","testdata","outputresamp","synthesize_g_plus.wav")
        if os.path.isfile(output):
            os.remove(output)
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      output,
                      "A3", 100, "g+30", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        self.assertFalse(os.path.isfile(output))
        self.resamp.synthesize()
        wave_io.write(output, self.resamp.output_data)
        self.assertTrue(os.path.isfile(output))
        
    def test_synthesize_B0(self):
        output = os.path.join("tests","testdata","outputresamp","synthesize_b0.wav")
        if os.path.isfile(output):
            os.remove(output)
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      output,
                      "A4", 100, "B0", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        self.assertFalse(os.path.isfile(output))
        self.resamp.synthesize()
        wave_io.write(output, self.resamp.output_data)
        self.assertTrue(os.path.isfile(output))
        
    def test_synthesize_B100(self):
        output = os.path.join("tests","testdata","outputresamp","synthesize_B100.wav")
        if os.path.isfile(output):
            os.remove(output)
        self.resamp = resamp.Resamp(os.path.join("tests","testdata","inputwav","a.wav"),
                      output,
                      "A4", 100, "B100", 0, 500, 100, 0, 100, 0, "!120", "AA#5#")
        self.resamp.parseFlags()
        self.resamp.getInputData()
        self.resamp.stretch()
        self.resamp.pitchShift()
        self.resamp.applyPitch()
        self.assertFalse(os.path.isfile(output))
        self.resamp.synthesize()
        wave_io.write(output, self.resamp.output_data)
        self.assertTrue(os.path.isfile(output))