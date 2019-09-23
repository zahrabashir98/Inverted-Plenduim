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
"""Complement after Yager"""
__revision__ = "$Id: Yager.py,v 1.7 2010-03-28 18:39:02 rliebscher Exp $"

from fuzzy.complement.Parametric import Parametric
from fuzzy.utils import inf_p

class Yager(Parametric):
    """Complement after Yager"""

    _range = [ (0., inf_p) ]

    def __init__(self, omega=1., *args, **keywords):
        """Initialize instance with given parameter
        @param omega: The parameter
        @type omega: float  
        """
        super(Yager, self).__init__(omega, *args, **keywords)

    def __call__(self, value):
        """calculate the complement of the value
        @param value: the value to complement
        @type value: float
        @return: the complemented value
        @rtype: float  
        """
        return pow(1. - pow(float(value), self.p), 1. / self.p)

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s(omega=%s)" % (self.__class__.__module__, self.__class__.__name__, self.p)
