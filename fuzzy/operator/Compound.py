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
"""The Compound class takes values of several input operators  and 
processes them through a given norm."""
__revision__ = "$Id: Compound.py,v 1.16 2010-10-29 19:24:41 rliebscher Exp $"

from fuzzy.operator.Operator import Operator

class Compound(Operator): # pylint: disable=R0903
    """Take values of input operators  and process them
       through the given norm.

       @ivar norm: how to combine inputs. (eg. Min,Max,...)
       @type norm: L{fuzzy.norm.Norm.Norm}
       @ivar inputs: list of inputs (subclassed from L{fuzzy.operator.Operator.Operator}).
    """ 

    def __init__(self, norm, *inputs):
        """Constructor.
        
        @param norm: how to combine inputs. (eg. Min,Max,...)
        @type norm: L{fuzzy.norm.Norm.Norm}
        @param inputs: list of inputs (subclassed from L{fuzzy.operator.Operator.Operator}).
        """
        super(Compound, self).__init__()
        self.norm = norm
        self.inputs = inputs

    def __call__(self):
        """Get current value of input and combine them with help of norm."""
        return self.norm(*[x() for x in self.inputs])

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s(norm=%s, inputs=%s)" % (
                self.__class__.__module__,
                self.__class__.__name__,
                repr(self.norm),
                repr(self.inputs),
            )
