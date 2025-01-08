import module_12_1
import module_12_2
import unittest

TestSuit = unittest.TestSuite()
TestSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
TestSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

unittest.TextTestRunner(verbosity=2).run(TestSuit)