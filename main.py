import unittest
from cases.search_for_test import SearchForTest

if __name__ == "__main__":
    test_cases = [SearchForTest]

    suites = []
    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        suites.append(suite)

    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suites))