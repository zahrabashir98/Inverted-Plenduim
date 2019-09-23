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
"""Special operator class which returns a constant value."""
__revision__ = "$Id: Const.py,v 1.15 2010-10-29 19:24:41 rliebscher Exp $"

from fuzzy.operator.Operator import Operator

class Const(Operator): # pylint: disable=R0903
    """Special operator which returns a constant value.
       
       @ivar value: value returned at call of __call__().
       @type value: float
    """

    def __init__(self, value):
        """Constructor.
        
        @param value: value returned at call of __call__().
        @type value: float
        """
        super(Const, self).__init__()
        self.value = value

    def __call__(self):
        """Return stored constant value."""
        return self.value

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s(%s)" % (self.__class__.__module__, self.__class__.__name__, self.value)
