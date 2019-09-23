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

__revision__ = "$Id: DrasticProduct.py,v 1.7 2009-10-27 20:06:27 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class DrasticProduct(Norm):

    def __init__(self):
        super(DrasticProduct, self).__init__(Norm.T_NORM)

    def __call__(self, *args):
        x, y = self.checkArgs2(args)
        if y == 1.0:
            return x
        if x == 1.0:
            return y
        return 0.0
