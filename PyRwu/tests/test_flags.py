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
        
class TestFlags(unittest.TestCase):
    def setUp(self):
        self.flags = flags.Flags()
        self.flags.add(flags.Flag("B", descriptions=["range1","newline"]))
        self.flags.add(flags.Flag("g", descriptions=["range2"], min=-100, max=100))
        self.flags.add(flags.Flag("e", descriptions=["bool"], isBool=True))
        self.flags.add(flags.Flag("Mg", descriptions=["2character1"]))
        self.flags.add(flags.Flag("Me"))


    def test_getDetail(self):
        result = self.flags.getDetail()
        self.assertEqual(result,"\tB\t0 ～ 100\t default:50\n\t\trange1\n\t\tnewline\n\n" + 
                         "\tg\t-100 ～ 100\t default:50\n\t\trange2\n\n" +
                         "\te\t\t\t default:False\n\t\tbool\n\n" +
                         "\tMg\t0 ～ 100\t default:50\n\t\t2character1\n\n" + 
                         "\tMe\t0 ～ 100\t default:50\n\t\t\n\n")

    def test_parse_range_simple(self):
        self.assertEqual(self.flags.params["B"].value, 50)
        self.flags.parse("B30")
        self.assertEqual(self.flags.params["B"].value, 30)
        
    def test_parse_range_positive(self):
        self.assertEqual(self.flags.params["B"].value, 50)
        self.flags.parse("B+30")
        self.assertEqual(self.flags.params["B"].value, 30)
        
    def test_parse_range_negative(self):
        self.assertEqual(self.flags.params["g"].value, 50)
        self.flags.parse("g-20")
        self.assertEqual(self.flags.params["g"].value, -20)
        
    def test_parse_range_not_match_only_character(self):
        self.assertEqual(self.flags.params["B"].value, 50)
        self.flags.parse("B")
        self.assertEqual(self.flags.params["B"].value, 50)
        
    def test_parse_bool_simple(self):
        self.assertFalse(self.flags.params["e"].flag)
        self.flags.parse("e")
        self.assertTrue(self.flags.params["e"].flag)
        
    def test_parse_bool_with_number(self):
        self.assertFalse(self.flags.params["e"].flag)
        self.flags.parse("e30")
        self.assertTrue(self.flags.params["e"].flag)
        
    def test_parse_range_Multi(self):
        self.assertEqual(self.flags.params["g"].value, 50)
        self.assertEqual(self.flags.params["Mg"].value, 50)
        self.flags.parse("Mg0")
        self.assertEqual(self.flags.params["g"].value, 50)
        self.assertEqual(self.flags.params["Mg"].value, 0)
        
    def test_parse_range_Multi_with_bool(self):
        self.assertFalse(self.flags.params["e"].flag)
        self.assertEqual(self.flags.params["Me"].value, 50)
        self.flags.parse("Me0")
        self.assertFalse(self.flags.params["e"].flag)
        self.assertEqual(self.flags.params["Me"].value, 0)

        
    def test_parse_multi(self):
        self.assertEqual(self.flags.params["g"].value, 50)
        self.assertEqual(self.flags.params["Mg"].value, 50)
        self.assertEqual(self.flags.params["B"].value, 50)
        self.assertEqual(self.flags.params["Me"].value, 50)
        self.assertFalse(self.flags.params["e"].flag)
        self.flags.parse("Mg0g-20B30eMe15")
        self.assertEqual(self.flags.params["g"].value, -20)
        self.assertEqual(self.flags.params["Mg"].value, 0)
        self.assertEqual(self.flags.params["B"].value, 30)
        self.assertEqual(self.flags.params["Me"].value, 15)
        self.assertTrue(self.flags.params["e"].flag)