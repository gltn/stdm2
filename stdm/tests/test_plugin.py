import unittest
import sys
import utils
import os


class PluginTest(unittest.TestCase):
    def test_general(self):
        self.assertEqual(1, 1)

def run_all():
    suite = unittest.testSuite()
    suite.addTests(unittest.makeSuite(PluginTest))
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite())
