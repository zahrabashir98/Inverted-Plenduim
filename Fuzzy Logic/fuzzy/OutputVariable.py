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
"""General instance of an output variable."""
__revision__ = "$Id: OutputVariable.py,v 1.14 2010-03-28 18:38:08 rliebscher Exp $"

from fuzzy.Variable import Variable

class OutputVariable(Variable):
    """General instance of an output variable.
        The defuzzification is provided by special object for this purpose,
        set as defuzzify param.
        Also marker, so you can check if any variable is an (instance of) output variable 

        @ivar defuzzify: Defuzzification method.
        @type defuzzify: L{fuzzy.defuzzify.Base.Base}
       """

    def __init__(self, defuzzify=None, *args, **keywords):
        """Initialize this output variable with a defuzzification method.

        @param defuzzify: Defuzzification method.
        @type defuzzify: L{fuzzy.defuzzify.Base.Base}
        """
        super(OutputVariable, self).__init__(*args, **keywords)
        self.defuzzify = defuzzify

    def getValue(self):
        """defuzzification"""
        return self.defuzzify.getValue(self)

    def _repr_params(self, params):
        """Helper for representation of instance.
        
        Add all own params to given list in params.    
        """
        params.append(repr(self.defuzzify))
        super(OutputVariable, self)._repr_params(params)
