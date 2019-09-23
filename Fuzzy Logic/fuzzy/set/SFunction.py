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

"""Realize a S-shaped fuzzy set."""

__revision__ = "$Id: SFunction.py,v 1.19 2010-03-28 18:44:46 rliebscher Exp $"


from fuzzy.set.Function import Function

class SFunction(Function):
    r"""
    Realize a S-shaped fuzzy set::
                 __
                /|
               / |
              /| |
            _/ | |
             | a |
             |   |
            2*delta

    See also U{http://pyfuzzy.sourceforge.net/demo/set/SFunction.png}
    
    @ivar a: center of set.
    @type a: float
    @ivar delta: absolute distance between x-values for minimum and maximum.
    @type delta: float
    """

    def __init__(self, a=0.0, delta=1.0):
        """Initialize a S-shaped fuzzy set.

        @param a: center of set
        @type a: float
        @param delta: absolute distance between x-values for minimum and maximum
        @type delta: float
        """
        super(SFunction, self).__init__()
        self.a = a
        self.delta = delta

    def __call__(self, x):
        """Return membership of x in this fuzzy set.
           This method makes the set work like a function.
           
           @param x: value for which the membership is to calculate
           @type x: float
           @return: membership
           @rtype: float
           """
        a = self.a
        d = self.delta
        if x <= a-d:
            return 0.0
        if x <= a:
            t = (x-a+d)/(2.0*d)
            return 2.0*t*t
        if x <= a+d:
            t = (a-x+d)/(2.0*d)
            return 1.0-2.0*t*t
        return 1.0

    def getCOG(self):
        """Return center of gravity."""
        from fuzzy.Exception import FuzzyException
        raise FuzzyException("COG of SFunction uncalculable")

    def getValuesX(self):
        """Return sequence of x-values so we get a smooth function."""
        a = self.a
        d = self.delta
        stepsize = 2. * d / Function._resolution
        x = a - d
        for _ in range(Function._resolution):
            yield x
            x += stepsize
        yield a + d

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s(a=%s, delta=%s)" % (self.__class__.__module__, self.__class__.__name__, self.a, self.delta)
