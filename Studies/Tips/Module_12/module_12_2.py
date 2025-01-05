import module_12_1
import unittest

class CalcTest(unittest.TestCase):
    def setUp(self):                    # создаётся в начале каждый раз при запуске проверки
        print("setUp")


    @classmethod
    def setUpClass(cls):                # создаётся в самом начале (ещё до setUp) только 1 раз
        print("MegaSetUp")


    def tearDown(self):                 # аналогично setUp только в конце
        pass


    @classmethod
    def tearDownClass(cls):             # аналогично setUp только в конце 1 раз
        pass


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