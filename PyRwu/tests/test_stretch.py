import unittest
import numpy as np

import stretch

class TestWorldStretch(unittest.TestCase):
    def setUp(self):
        self._f0 = np.arange(10, dtype=np.float64)
        self._sp = np.zeros((10,12))
        self._ap = np.zeros((10,12))
        for i in range(self._f0.shape[0]):
            self._sp[i,:]=i
            self._ap[i,:]=i

    def test_stretch_2(self):
        new_f0, new_sp, new_ap = stretch.world_stretch(20, self._f0, self._sp, self._ap)
        self.assertEqual(new_f0.shape[0], 20)
        np.testing.assert_array_equal(new_f0, np.array([0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]))
        self.assertEqual(new_sp.shape[0], 20)
        self.assertEqual(new_sp.shape[1], 12)
        
    def test_stretch_1_5(self):
        new_f0, new_sp, new_ap = stretch.world_stretch(15, self._f0, self._sp, self._ap)
        self.assertEqual(new_f0.shape[0], 15)
        np.testing.assert_array_equal(new_f0, np.array([0,0,1,1,2,2,3,3,4,4,5,6,7,8,9]))
        self.assertEqual(new_sp.shape[0], 15)
        self.assertEqual(new_sp.shape[1], 12)
        
    def test_stretch_0_5(self):
        new_f0, new_sp, new_ap = stretch.world_stretch(5, self._f0, self._sp, self._ap)
        self.assertEqual(new_f0.shape[0], 5)
        np.testing.assert_array_equal(new_f0, np.array([0,2,4,6,8]))
        self.assertEqual(new_sp.shape[0], 5)
        self.assertEqual(new_sp.shape[1], 12)
        
    def test_stretch_0_7(self):
        new_f0, new_sp, new_ap = stretch.world_stretch(7, self._f0, self._sp, self._ap)
        self.assertEqual(new_f0.shape[0], 7)
        np.testing.assert_array_equal(new_f0, np.array([0,1,2,4,5,7,8]))
        self.assertEqual(new_sp.shape[0], 7)
        self.assertEqual(new_sp.shape[1], 12)

        
class TestWorldLoop(unittest.TestCase):
    def setUp(self):
        self._f0 = np.arange(10, dtype=np.float64)
        self._sp = np.zeros((10,12))
        self._ap = np.zeros((10,12))
        for i in range(self._f0.shape[0]):
            self._sp[i,:]=i
            self._ap[i,:]=i
            
    def test_stretch_2(self):
        new_f0, new_sp, new_ap = stretch.world_loop(20, self._f0, self._sp, self._ap)
        self.assertEqual(new_f0.shape[0], 20)
        np.testing.assert_array_equal(new_f0, np.array([0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,1]))
        self.assertEqual(new_sp.shape[0], 20)
        self.assertEqual(new_sp.shape[1], 12)
        
    def test_stretch_1_5(self):
        new_f0, new_sp, new_ap = stretch.world_loop(15, self._f0, self._sp, self._ap)
        self.assertEqual(new_f0.shape[0], 15)
        np.testing.assert_array_equal(new_f0, np.array([0,1,2,3,4,5,6,7,8,9,8,7,6,5,4]))
        self.assertEqual(new_sp.shape[0], 15)
        self.assertEqual(new_sp.shape[1], 12)
        
    def test_stretch_0_5(self):
        new_f0, new_sp, new_ap = stretch.world_loop(5, self._f0, self._sp, self._ap)
        self.assertEqual(new_f0.shape[0], 5)
        np.testing.assert_array_equal(new_f0, np.array([0,1,2,3,4]))
        self.assertEqual(new_sp.shape[0], 5)
        self.assertEqual(new_sp.shape[1], 12)