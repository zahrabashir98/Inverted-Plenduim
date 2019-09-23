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
"""Base class for all complement methods"""
__revision__ = "$Id: Base.py,v 1.7 2010-10-29 19:24:41 rliebscher Exp $"

import fuzzy.Exception

class ComplementException(fuzzy.Exception.FuzzyException):
    """An own exception type for complements."""
    pass


class Base(object): # pylint: disable=R0903
    """Base class for all complement methods"""

    def __init__(self, *args, **keywords):
        """Initialize the complement instance"""
        super(Base, self).__init__(*args, **keywords)

    def __call__(self, value):
        """Calculate the complement of the value.
        @param value: the value to complement
        @type value: float
        @return: the complemented value
        @rtype: float
        """
        raise NotImplementedError("don't use the abstract base class") # pragma: no coverage

    def __repr__(self):
        """Return representation of instance.
           
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s()" % (self.__class__.__module__, self.__class__.__name__)
