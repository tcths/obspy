# -*- coding: utf-8 -*-
"""
obspy.io.hyposat - HYPOSAT file formats support for ObsPy
=========================================================

This module provides read/write support for some file formats used by
`HYPOSAT <ftp://ftp.norsar.no/pub/outgoing/johannes/hyposat/>`_.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)


Usage Example
-------------

The PHA reader hooks into the standard ObsPy event handling
mechanisms including format autodetection.

>>> from obspy import read_events
>>> cat = read_events('/path/to/nlloc.qml')
>>> print(cat)
2 Event(s) in Catalog:
2025-05-14T14:35:35.510000Z | +40.225,  +10.450 | 3.5 None
2025-05-14T15:43:05.280000Z | +40.223,  +10.450 | 1.8 None

"""
if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)