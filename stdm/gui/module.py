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
from PyQt5.QtGui import QIcon
from PyQt.QtWidgets import QAction
from qgis.gui import QgisInterface
from stdm.core.security import PermissionInfo


def create_qaction(stdm_module):
    """
    Helper method that creates a QAction from an STDM module object.
    :param stdm_module: Instance of StdmModule object.
    :type stdm_module: StdmModule
    :return: QAction object associated with the StdmModule.
    :rtype: QAction
    """
    sm_act = QAction(stdm_module.qgis_iface)
    sm_act.setData(stdm_module)
    icon = stdm_module.icon()
    if icon is not None:
        sm_act.setIcon(stdm_module.icon())

    sm_act.setText(stdm_module.name())

    # Further adapt it based on module-defined properties
    stdm_module.adapt_qaction(sm_act)

    return sm_act


class StdmModule(ABC):
    """Abstract class containing specific information for an STDM module e.g.
    Data Profile Customization module, Users and Roles module etc.

    Requires to be sub-classed for specific modules.
    """
    m_types = {}
    qaction_creator = create_qaction

    def __init__(self, iface):
        """Class constructor.
        :param iface: Reference to QGIS interface exposing QGisApp. See
        :class: qgis.gui.QgisInterface
        :type iface: QgisInterface
        """
        self._iface = iface

    def adapt_qaction(self, qaction):
        """
        Provides the option for sub-classes to further customize the QAction
        object that will be created from the module. Default implementation
        does nothing.
        :param qaction: QAction object that will be customized further.
        :type qaction: QAction
        """
        pass

    def qaction(self):
        """
        :return: Return a QAction object associated with this module.
        Functions can be swapped accordingly for more flexibility, see
        class attribute.
        :rtype: QAction
        """
        return self.qaction_creator()

    @property
    def qgis_iface(self):
        """
        :return: Returns an instance of the Qgis interface object.
        :rtype: QgisInterface
        """
        return self._iface

    @abstractmethod
    def icon(self):
        """
        :return: Returns the QIcon corresponding to the module. Needs
        to be overridden by sub-classes.
        :rtype: QIcon
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def name(cls):
        """
        :return: Returns the friendly display name of the module that will
        appear in the menu and/or action tooltip in the corresponding action.
        This should be translatable text.

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

    def show_in_menu(self):
        """
        :return: Returns True/False if the module should appear in the QGIS
        menu. Default implementation is True.
        :rtype: bool
        """
        return True

    def show_in_toolbar(self):
        """
        :return: Returns True/False if the module should appear in the QGIS
        toolbar. Default implementation is True.
        :rtype: bool
        """
        return True

    @abstractmethod
    def permissions(self):
        """
        :return: Returns the security permission object that defines access
        to this module. This information will be persisted in the database
        once configuration of the module has been initiated by a user in the
        STDM_ADMIN role. Return None if the module will not require any
        user authentication before accessing it.
        :rtype: PermissionInfo or None
        """
        raise NotImplementedError
