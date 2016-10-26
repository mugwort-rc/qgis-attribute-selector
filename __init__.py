# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeSelector
                                 A QGIS plugin
 AttributeSelector
                             -------------------
        begin                : 2016-10-26
        copyright            : (C) 2016 by mugwort_rc
        email                : mugwort.rc@gmail.com
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
    """Load AttributeSelector class from file AttributeSelector.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .AttributeSelector import AttributeSelector
    return AttributeSelector(iface)
