"""
/***************************************************************************
Name                 : Social Tenure Domain Model
Description          : QGIS Entry Point for Social Tenure Domain Model
Date                 : 04-01-2015
copyright            : (C) 2015 by UN-Habitat and implementing partners.
                       See the accompanying file CONTRIBUTORS.txt in the root
email                : stdm@unhabitat.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import sys
import os


def classFactory(iface):
    """
    Load STDMQGISLoader class.
    """
    from .plugin import STDMQGISLoader
    return STDMQGISLoader(iface)
