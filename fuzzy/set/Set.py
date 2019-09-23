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

"""
Base class for all fuzzy sets.
"""

__revision__ = "$Id: Set.py,v 1.24 2010-10-29 19:24:41 rliebscher Exp $"

class Set(object):
    """Base class for all types of fuzzy sets."""

    def __call__(self, x):
        """Return membership of x in this fuzzy set.
           This method makes the set work like a function.
           
           @param x: value x
           @type x: float
           @return: membership for value x
           @rtype: float
           """
        return 0.

    def getValuesXY(self, flat = True):
        """Internal helper function to help convert arbitrary fuzzy sets in 
        fuzzy sets represented by a polygon."""
        return ((x,self(x)) for x in self.getValuesX())

    def getValuesX(self):
        """Internal helper function to help convert arbitrary fuzzy sets in 
        fuzzy sets represented by a polygon."""
        raise NotImplementedError("Set has no values defined")

    def getCOG(self):
        """Returns center of gravity.
           
           @return: x-value of center of gravity
           @rtype: float
           """
        raise NotImplementedError("abstract class %s has no center of gravity." % self.__class__.__name__)

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s()" % (self.__class__.__module__, self.__class__.__name__)

# pylint: disable=W0611
# too make old code happy
from fuzzy.set.operations import norm,merge #@UnusedImport
