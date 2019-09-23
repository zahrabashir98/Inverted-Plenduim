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
    Calculate value for fuzzy rule.
    
    Used to build fuzzy rules.
"""

__revision__ = "$Id: Operator.py,v 1.15 2010-10-29 19:24:41 rliebscher Exp $"

class Operator(object): # pylint: disable=R0903
    """Abstract base class for any kind of operator."""

    def __init__(self):
        """Dummy initialization, so it is safe to call it
           from any sub class."""
        pass

    def __call__(self):
        """Return current value.
        
        @return: result of operator calculation
        @rtype: float
        @raise fuzzy.FuzzyException.FuzzyException: any problem in calculation
        """
        raise NotImplementedError("abstract class %s can't be called" % self.__class__.__name__)
