import module_12_1
import unittest

class CalcTest(unittest.TestCase):
    def test_add(self):
        """
        Test for add function in calculator
        :return:
        """
        self.assertEqual(module_12_1.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(module_12_1.sub(5, 3), 2)

if __name__=="__main__":
    unittest.main()