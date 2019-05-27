import unittest
from unittest import (
    TestCase
)
import sys


class TestStdmModule(TestCase):
    def test_register(self):
        self.fail()

    def test_get(self):
        self.fail()

    def test_all(self):
        self.fail()


def run_all():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestStdmModule))
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite)
