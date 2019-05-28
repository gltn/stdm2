"""
/***************************************************************************
Name                 : STDM Module
Description          : Abstract container that contains information for
                       specific functionality.
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

from abc import (
    ABC,
    abstractmethod
)

from qgis.gui import QgisInterface


class StdmModule(ABC):
    """Abstract class containing specific information for an STDM module e.g.
    Data Profile Customization module, Users and Roles module etc.

    Requires to be sub-classed for specific modules.
    """
    m_types = {}

    def __init__(self, iface):
        """Class constructor.
        :param iface: Reference to QGIS interface exposing QGisApp. See
        :class: qgis.gui.QgisInterface
        :type iface: QgisInterface
        """
        self._iface = iface
        self._icon = ''

    @property
    def qgis_iface(self):
        """
        :return: Returns an instance of the Qgis interface object.
        :rtype: QgisInterface
        """
        return self._iface

    @property
    def icon(self):
        """
        :return: Returns the path to the icon file.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, path):
        """
        Sets path to the icon file.
        :param path: File path to the icon image.
        :type path: str
        """
        if path and path != self._icon:
            self._icon = path

    @classmethod
    @abstractmethod
    def name(cls):
        """
        :return: Returns the friendly display name of the module that will
        appear in the menu and/or action tooltip in the corresponding action.
        Should be overridden by sub-classes.
        :rtype: str
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def key(cls):
        """
        :return: Returns a unique name that identifies this module. It can,
        for instance, be a code or shortened display name.
        Should be overridden by sub-classes.
        :rtype: str
        """
        raise NotImplementedError

    def __hash__(self):
        """
        :return: Returns a hash value computed from the module key. If the
        key is empty then it will return -1.
        :rtype: int
        """
        if not self.key():
            return -1

        return hash(self.key())

    def __str__(self):
        return self.name()

    @classmethod
    def register(cls):
        """Registers a new module into the collection."""
        if issubclass(cls, StdmModule):
            mod_key = cls.key()
            if mod_key:
                StdmModule.m_types[mod_key] = cls
            else:
                # Log this
                pass

    @classmethod
    def get(cls, key):
        """
        :param key: Key (unique identifier) of the module.
        :type key: str

        :return: Returns the module with the given key from the collection.
        :rtype: StdmModule or None
        """
        return StdmModule.m_types.get(key, None)

    @classmethod
    def all(cls):
        """
        :return: Returns a list of all of the registered modules.
        :rtype: list
        """
        return StdmModule.m_types.values()
