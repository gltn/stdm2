"""
/***************************************************************************
Name                 : StdmModule Unit Tests
Description          : Unit tests for StdmModule class.
Date                 : 26-05-2019
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

from stdm.gui.module import StdmModule
from stdm.tests.gui.custom_modules import (
    ConfigurationModule
)


class TestStdmModule(unittest.TestCase):
    def test_get(self):
        conf_mod = StdmModule.get(ConfigurationModule.key())
        # self.assertIs(conf_mod, None)

    def test_all(self):
        self.assertEqual(len(StdmModule.all()), 2)

