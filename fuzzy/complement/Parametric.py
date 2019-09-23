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
"""Abstract base class for any parametric fuzzy complement"""
__revision__ = "$Id: Parametric.py,v 1.9 2010-10-29 19:24:41 rliebscher Exp $"

from fuzzy.complement.Base import Base
from fuzzy.utils import prop

class Parametric(Base):
    """Abstract base class for any parametric fuzzy complement
    
    @ivar p: parameter for complement
    @type p: float
    """
    _range = None

    def __init__(self, p, *args, **keywords):
        """Initialize type and parameter
        
        @param p: parameter for complement
        @type p: float
        """
        super(Parametric, self).__init__(*args, **keywords)
        self.p = p

    # pylint: disable=E0211,E0202
    #ID:E0211 Parametric.p: Method has no argument
    #ID:E0202 Parametric.p: An attribute inherited from Parametric hide this method
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
    #ID:E0211 Parametric.p_range: Method has no argument
    @prop
    def p_range(): #@NoSelf
        """range(s) of valid values for p"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._range
        return locals()

    def _checkParam(self, value):
        """check parameter if allowed for parameter p
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
        return "%s.%s(p=%s)" % (self.__class__.__module__, self.__class__.__name__, self._p)
    