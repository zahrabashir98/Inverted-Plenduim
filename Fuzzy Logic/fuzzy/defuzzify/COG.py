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

"""Defuzzification which uses the center of gravity method."""

__revision__ = "$Id: COG.py,v 1.9 2010-03-28 18:40:33 rliebscher Exp $"

from fuzzy.defuzzify.Base import Base

class COG(Base):
    """Defuzzification which uses
       the center of gravity method."""

    def __init__(self, INF=None, ACC=None, failsafe=None, segment_size=None, *args, **keywords):
        """
            @param failsafe: if is not possible to calculate a center of gravity,
                             return this value if not None or forward the exception
            @param segment_size: maximum length of segment in polygon of accumulated result set
        """ 
        super(COG, self).__init__(INF, ACC, *args, **keywords)
        self.failsafe = failsafe # which value if COG not calculable
        self.segment_size = segment_size # maximum length of segment in polygon of accumulated result set

    def getValue(self, variable):
        """Defuzzification using center of gravity method."""
        temp = self.accumulate(variable, self.segment_size)
        try:
            return temp.getCOG()
        except:
            # was not to calculate
            if self.failsafe is not None:
                # user gave us a value to return
                return self.failsafe
            else:
                # forward exception
                raise

    def _repr_params(self, params):
        """Helper for representation of instance.
        
        Add all own params to given list in params.    
        """
        super(COG, self)._repr_params(params)
        if self.failsafe: params.append("failsafe=%s" % self.failsafe) 
        if self.segment_size: params.append("segment_size=%s" % self.segment_size)
