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
"""Complement after Zadeh"""
__revision__ = "$Id: Zadeh.py,v 1.6 2010-10-29 19:24:41 rliebscher Exp $"

from fuzzy.complement.Base import Base

class Zadeh(Base): # pylint: disable=R0903
    """Complement after Zadeh"""

    def __init__(self, *args, **keywords):
        """Initialize the complement instance"""
        super(Zadeh, self).__init__(*args, **keywords)

    def __call__(self, value):
        """calculate the complement of the value
        @param value: the value to complement
        @type value: float
        @return: the complemented value
        @rtype: float  
        """
        return 1. - float(value)
