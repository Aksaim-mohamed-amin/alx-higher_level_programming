import unittest

class TestDebug(unittest.TestCase):
    def test_debug(self):
        loader = unittest.TestLoader()
        suite = loader.discover('tests', pattern='test*.py')
        for test in suite:
            print(test)
