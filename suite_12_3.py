import unittest
import test12_3

casesST = unittest.TestSuite()

casesST.addTest(unittest.TestLoader().loadTestsFromTestCase(test12_3.RunnerTest))
casesST.addTest(unittest.TestLoader().loadTestsFromTestCase(test12_3.TournamentTest))

rt_runner = unittest.TextTestRunner(verbosity=2)
rt_runner.run(casesST)