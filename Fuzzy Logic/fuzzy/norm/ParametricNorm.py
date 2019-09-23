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
    Base class for any kind of parametric fuzzy norm.
"""

__revision__ = "$Id: ParametricNorm.py,v 1.16 2010-10-29 19:24:41 rliebscher Exp $"

from fuzzy.norm.Norm import Norm
from fuzzy.utils import prop

class ParametricNorm(Norm):
    """Abstract base class for any parametric fuzzy norm
    
    @ivar p: parameter for norm
    @type p: float
    """
    _range = None

    def __init__(self, type, param):
        """Initialize type and parameter
        
        @param param: parameter for norm
        @type param: float
        """
        super(ParametricNorm, self).__init__(type)
        self.p = param

    # pylint: disable=E0202,E0211
    #ID:E0202 ParametricNorm.p: An attribute inherited from ParametricNorm hide this method
    #ID:E0211 TParametricNorm.p: Method has no argument
    @prop
    def p(): #@NoSelf
        """x
        @type: float"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._p
        def fset(self, value): # pylint: disable=W0612,C0111
            self._checkParam(value)
            self._p = value
        return locals()

    # pylint: disable=E0211
    #ID:E0211 TParametricNorm.p_range: Method has no argument
    @prop
    def p_range(): #@NoSelf
        """range(s) of valid values for p"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._range
        return locals()

    def _checkParam(self, value):
        """check parameter if allowed for paramter p
        @param value: the value to be checked 
        @type value: float"""
        from fuzzy.utils import checkRange
        if not checkRange(value, self._range):
            from fuzzy.Exception import FuzzyException
            raise FuzzyException("Parameter value %s is not allowed" % str(value))

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s(param=%s)" % (self.__class__.__module__, self.__class__.__name__, self._p)
