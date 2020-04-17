import unittest
from cases.resolve_game import ResolveGameTest

if __name__ == "__main__":
    test_cases = [ResolveGameTest]

    suites = []
    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        suites.append(suite)

    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suites))