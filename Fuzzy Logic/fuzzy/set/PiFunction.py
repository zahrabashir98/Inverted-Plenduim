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

"""Realize a Pi-shaped fuzzy set"""

__revision__ = "$Id: PiFunction.py,v 1.19 2010-03-28 18:44:46 rliebscher Exp $"


from fuzzy.set.Function import Function
from fuzzy.set.SFunction import SFunction
from fuzzy.set.ZFunction import ZFunction

class PiFunction(Function):
    r"""
    Realize a Pi-shaped fuzzy set::
        
                _
               /|\
              / | \
            _/  |  \_
             |  a  |
             |     |
              delta

    See also U{http://pyfuzzy.sourceforge.net/demo/set/PiFunction.png}

    
    @ivar a: center of set.
    @type a: float
    @ivar delta: absolute distance between x-values for minimum and maximum.
    @type delta: float
    """

    def __init__(self, a=0.0, delta=1.0):
        """Initialize a Pi-shaped fuzzy set.

        @param a: center of set
        @type a: float
        @param delta: absolute distance between x-values for minimum and maximum
        @type delta: float
        """
        super(PiFunction, self).__init__()
        self.a = a
        self.delta = delta
        self._sfunction = SFunction(a - delta/2., delta/2)
        self._zfunction = ZFunction(a + delta/2., delta/2)

    def __call__(self, x):
        """Return membership of x in this fuzzy set.
           This method makes the set work like a function.
           
           @param x: value for which the membership is to calculate
           @type x: float
           @return: membership
           @rtype: float
           """
        if x < self.a:
            return self._sfunction(x)
        else:
            return self._zfunction(x)

    def getCOG(self):
        """Return center of gravity."""
        return self.a

    def getValuesX(self):
        """Return sequence of x-values so we get a smooth function."""
        for x in self._sfunction.getValuesX():
            yield x
        # first value is equal the last of the previous sequence    
        skippedFirst = False 
        for x in self._zfunction.getValuesX():
            if not skippedFirst:
                skippedFirst = True
            else:
                yield x

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s(a=%s, delta=%s)" % (self.__class__.__module__, self.__class__.__name__, self.a, self.delta)
        