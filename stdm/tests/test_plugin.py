import unittest
import sys
# import utils
import os

import psycopg2


class PluginTest(unittest.TestCase):
    def setUp(self):
        self.conn = psycopg2.connect('')

    def test_general(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        self.conn.close()


def run_all():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(PluginTest))
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite)
