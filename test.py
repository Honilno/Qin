import os
import unittest

from tests.character_test import CharacterTest
from tests.runda_test import RundaTest

print(os.getcwd())
test_array = [
    unittest.TestLoader().loadTestsFromTestCase(CharacterTest),
    unittest.TestLoader().loadTestsFromTestCase(RundaTest)
    ]

tests = unittest.TestSuite(test_array)

unittest.TextTestRunner().run(tests)
