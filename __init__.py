# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LocalSoftware
                                 A QGIS plugin
 Connecting CAD and GIS software
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-10-12
        copyright            : (C) 2021 by LocalSoftware
        email                : csandova@mit.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LocalSoftware class from file LocalSoftware.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .local_software import LocalSoftware
    return LocalSoftware(iface)
