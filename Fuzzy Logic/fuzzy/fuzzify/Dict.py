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

"""Fuzzification which sets adjectives values according the values in given dictionary."""

__revision__ = "$Id: Dict.py,v 1.8 2010-10-29 19:24:41 rliebscher Exp $"

from fuzzy.fuzzify.Base import Base


class Dict(Base): # pylint: disable=R0903
    """Fuzzification method which gets adjective memberships
       in a dictionary instead of values to fuzzify.
       You should use in the adjectives instances of Set itself.

       Q : What can be done with this?

       A : Break complexity, by divide big and heavy fuzzy
       systems into small ones ::

        input1 ----> *******
        input2 ----> * FIS *
        input3 ----> *     * ------> output
        input4 ----> *******

       should be::

        input1 ----> *******
        input2 ----> *FIS 1* ----+
                     *******     |
                                 +--> *******
        input3 ----> ******* -------> *FIS 3* ----> output
        input4 ----> *FIS 2*          *******
                     *******
 
       Q : Why don't defuzzify outputs of FIS1 and FIS2 ?

       A : Defuzzification mean data loss.

      """

    def __init__(self, *args, **keywords):
        super(Dict, self).__init__(*args, **keywords)

    def setValue(self, variable, value):
        """Do not let adjectives calculate their membership values.
           Instead use the provided values from dictionary.
           
           @param variable: variable which adjective to set
           @type variable: L{fuzzy.Variable.Variable}
           @param variable: values to set the adjectives
           @type: dict
           """
        for adjective_key in value:
            variable.adjectives[adjective_key].membership = value[adjective_key]
        return None
