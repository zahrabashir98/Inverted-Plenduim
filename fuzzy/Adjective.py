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
"""Describes a ... of a variable."""
__revision__ = "$Id: Adjective.py,v 1.16 2010-02-17 19:57:13 rliebscher Exp $"


from fuzzy.norm.Max import Max
from fuzzy.set.Set import Set

class Adjective(object):
    """Describes a ... of a variable.
    
    @ivar set: fuzzy set
    @type set: L{fuzzy.set.Set.Set}
    @ivar COM: norm (if None the class default _COM is used.)
    @type COM: L{fuzzy.norm.Norm.Norm}
    @ivar membership: set or calculated membership
    @type membership: float
    @cvar _COM: class default is instance variable is None
    @type _COM: L{fuzzy.norm.Norm.Norm}
    """

    # default if not set in instance
    _COM = Max()
    _set = Set()

    def __init__(self, set=None, COM=None):
        """Initialize adjective.
        
        @param set: fuzzy set
        @type set: L{fuzzy.set.Set.Set}
        @param COM: norm (if None the class default _COM is used.)
        @type COM: L{fuzzy.norm.Norm.Norm}
        """
        self.set = set or Adjective._set
        self.membership = None
        self.COM = COM

    def setMembershipForValue(self, value):
        """Get membership for an input value from the fuzzy set."""
        self.membership = self.set(value)

    def getMembership(self):
        """Return membership set in this adjective."""
        if self.membership is None:
            return 0.0
        else:
            return self.membership

    def setMembership(self, value):
        """Set membership of this adjective as result 
           of a rule calculation, 
           if already set use COM norm to merge
           old and new value."""

        if self.membership is None:
            self.membership = value
        else:
            self.membership = (self.COM or self._COM)(
                                                    self.membership,  # consider already set value
                                                    value
                                                )

    def reset(self):
        """Reset membership to unknown value (None)."""
        self.membership = None

    def getName(self, system):
        """Find own name in given system.
        Returns a tuple (var_name,adj_name) of None."""
        return system.findAdjectiveName(self)

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        params = []
        if self.set is not Adjective._set: params.append("set=%s" % repr(self.set))
        if self.COM: params.append("COM=%s" % repr(self.COM))
        return "%s.%s(%s)" % (self.__class__.__module__, self.__class__.__name__, ", ".join(params))
