"""
/***************************************************************************
Name                 : Test StdmModule Instances
Description          : Sample StdmModule instances for testing.
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
from stdm.gui.module import StdmModule


class ConfigurationModule(StdmModule):
    def name(self):
        return 'STDM Configuration'

    def key(self):
        return 'STDM_CONF'


ConfigurationModule.register()


class SecurityModule(StdmModule):
    def name(self):
        return 'System Security'

    def key(self):
        return 'STDM_SEC'


SecurityModule.register()