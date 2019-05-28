"""
/***************************************************************************
Name                 : GUI tests
Description          : Suite for running tests in the GUI module.
Date                 : 28-05-2019
copyright            : (C) 2019 by UN-Habitat and implementing partners.
                       See the accompanying file CONTRIBUTORS.txt in the root
email                : stdm@unhabitat.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import unittest
import sys
from stdm.tests.gui.test_stdm_module import TestStdmModule


def run_all():
    suite = unittest.TestSuite()
    # Add your tests here
    suite.addTests(unittest.makeSuite(TestStdmModule))
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite)