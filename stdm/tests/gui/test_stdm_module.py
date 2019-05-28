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
from qgis.utils import iface
from stdm.gui.module import StdmModule
from stdm.tests.gui.custom_modules import (
    ConfigurationModule,
    SecurityModule
)


class TestStdmModule(unittest.TestCase):
    def test_get_conf_module(self):
        conf_mod = StdmModule.get(ConfigurationModule.key())
        self.assertIsNotNone(conf_mod)

    def test_get_sec_module(self):
        sec_mod = StdmModule.get(SecurityModule.key())
        self.assertIsNotNone(sec_mod)

    def test_get_none_module(self):
        ne_mod = StdmModule.get('NON_EXISTENT')
        self.assertIsNone(ne_mod)

    def test_action(self):
        conf_mod_obj = ConfigurationModule(iface)
        conf_act = conf_mod_obj.qaction()
        self.assertTrue(conf_act.isCheckable())

    def test_all(self):
        self.assertEqual(len(StdmModule.all()), 2)

