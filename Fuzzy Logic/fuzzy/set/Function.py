# -*- coding: utf-8 -*-
#
# Copyright (C) 2009  Rene Liebscher
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free 
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>. 
#

"""Base class for any fuzzy set defined by a function (not a polygon)."""

__revision__ = "$Id: Function.py,v 1.13 2010-03-28 18:44:46 rliebscher Exp $"


from fuzzy.set.Set import Set

class Function(Set):
    """Base class for any fuzzy set defined by a function (not a polygon)."""

    # if converted in linear polygon form use
    # at least x pieces
    _resolution = 25 #: segments when converting into a polygon
