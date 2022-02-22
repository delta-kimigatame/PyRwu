import unittest

import flags

class TestFlag(unittest.TestCase):
    def test_default_init(self):
        flag = flags.Flag("B")
        self.assertEqual(flag.name, "B")
        self.assertEqual(flag.descriptions, [])
        self.assertFalse(flag.isBool)
        self.assertEqual(flag.min, 0)
        self.assertEqual(flag.max, 100)
        self.assertEqual(flag.default_value, 50)
        self.assertFalse(flag.default_bool)
        self.assertEqual(flag.value, 50)
        self.assertFalse(flag.flag)

    def test_init(self):
        flag = flags.Flag("B", descriptions=["test1","test2"],min=30,max=70,default_value=40)
        self.assertEqual(flag.name, "B")
        self.assertEqual(flag.descriptions, ["test1","test2"])
        self.assertFalse(flag.isBool)
        self.assertEqual(flag.min, 30)
        self.assertEqual(flag.max, 70)
        self.assertEqual(flag.default_value, 40)
        self.assertFalse(flag.default_bool)
        self.assertEqual(flag.value, 40)
        self.assertFalse(flag.flag)

        
    def test_init_bool(self):
        flag = flags.Flag("B", descriptions=["test1","test2"],isBool=True)
        self.assertEqual(flag.name, "B")
        self.assertEqual(flag.descriptions, ["test1","test2"])
        self.assertTrue(flag.isBool)
        self.assertEqual(flag.min, 0)
        self.assertEqual(flag.max, 100)
        self.assertEqual(flag.default_value, 50)
        self.assertFalse(flag.default_bool)
        self.assertEqual(flag.value, 50)
        self.assertFalse(flag.flag)

        
    def test_init_bool_and_default(self):
        flag = flags.Flag("B", descriptions=["test1","test2"],isBool=True, default_bool=True)
        self.assertEqual(flag.name, "B")
        self.assertEqual(flag.descriptions, ["test1","test2"])
        self.assertTrue(flag.isBool)
        self.assertEqual(flag.min, 0)
        self.assertEqual(flag.max, 100)
        self.assertEqual(flag.default_value, 50)
        self.assertTrue(flag.default_bool)
        self.assertEqual(flag.value, 50)
        self.assertTrue(flag.flag)

    def test_change_value(self):
        flag = flags.Flag("B")
        self.assertEqual(flag.value, 50)
        flag.value = 80
        self.assertEqual(flag.value, 80)
        
    def test_change_value_missing_reason_bool(self):
        flag = flags.Flag("B", isBool=True)
        self.assertEqual(flag.value, 50)
        with self.assertWarns(UserWarning) as cm:
            flag.value = 80
        self.assertEqual(flag.value, 50)
        self.assertEqual(str(cm.warning), "flag is boolean. name:{}".format("B"))
        
    def test_change_value_missing_reason_underflow(self):
        flag = flags.Flag("B")
        self.assertEqual(flag.value, 50)
        with self.assertWarns(UserWarning) as cm:
            flag.value = -10
        self.assertEqual(flag.value, 50)
        self.assertEqual(str(cm.warning), "value's out of range.key:{}, min:{}, value:{}".format("B", 0, -10))
        
    def test_change_value_missing_reason_overflow(self):
        flag = flags.Flag("B")
        self.assertEqual(flag.value, 50)
        with self.assertWarns(UserWarning) as cm:
            flag.value = 120
        self.assertEqual(flag.value, 50)
        self.assertEqual(str(cm.warning), "value's out of range.key:{}, max:{}, value:{}".format("B", 100, 120))
        
    def test_change_bool(self):
        flag = flags.Flag("B", isBool=True)
        self.assertFalse(flag.flag)
        flag.flag = True
        self.assertTrue(flag.flag)
        
    def test_change_bool_missing_reason_not_bool(self):
        flag = flags.Flag("B")
        self.assertFalse(flag.flag)
        
        with self.assertWarns(UserWarning) as cm:
            flag.flag = True
        self.assertFalse(flag.flag)
        self.assertEqual(str(cm.warning), "flag is not boolean. name:{}".format("B"))