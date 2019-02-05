"""
/***************************************************************************
Name                 : STDM QGIS Loader
Description          : STDM QGIS Loader
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
# Import Python stuff
import os

import errno
import shutil
from string import Template
import codecs
import configparser
import subprocess

# Import the PyQt and QGIS libraries
from PyQt5.QtCore import QFileInfo, QUrl, QFile, QDir, QSettings
from PyQt5.QtWidgets import (
    QAction, QFileDialog, QMessageBox)

from PyQt5.QtGui import (QIcon,
                         QDesktopServices,
                         QStandardItemModel,
                         QStandardItem
                         )
from qgis.core import QgsApplication
# Initialize Qt resources from file resources.py
# Do not remove this import even though your IDE / pylint may report it unused
# noinspection PyUnresolvedReferences
from .resources import *  #pylint: disable=W0401,W0614


class STDMQGISLoader:
    def __init__(self, iface):
        """Constructor

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface

        """
        # Save reference to the QGIS interface
        self.iface = iface
        # noinspection PyArgumentList
        self.user_plugin_dir = QFileInfo(
            QgsApplication.qgisUserDatabaseFilePath()).path() + \
            '/python/plugins'
        self.plugin_builder_path = os.path.dirname(__file__)

        # class members
        self.action = None
        self.dialog = None
        self.plugin_path = None
        self.template = None
        self.shared_dir = None
        self.template_dir = None

    # noinspection PyPep8Naming
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(':/plugins/stdm/icon.png'),
            'Placeholder', self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu('&STDM', self.action)

    def run(self):
        pass

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu('&STDM', self.action)
        self.iface.removeToolBarIcon(self.action)
