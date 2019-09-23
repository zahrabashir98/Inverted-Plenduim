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

"""Realize a trapezoid-shaped fuzzy set."""

__revision__ = "$Id: Trapez.py,v 1.19 2010-10-29 19:24:41 rliebscher Exp $"


from fuzzy.set.Polygon import Polygon
from fuzzy.utils import prop
from fuzzy.Exception import FuzzyException

class Trapez(Polygon):
    r"""
    Realize a trapezoid-shaped fuzzy set::
               _____ _____  y_max
              /     \
             /|     |\
            / |     | \
           /  |     |  \
         _/   |     |   \_  y_min
          |   m1    m2  |
          |   |     |   |
         alpha|     |beta

    See also U{http://pyfuzzy.sourceforge.net/demo/set/Trapez.png}
    """

    def __init__(self, m1=-0.5, m2=0.5, alpha=0.5, beta=0.5, y_max=1.0, y_min=0.0):
        """
        Initialize a trapezoid-shaped fuzzy set.

        @param y_max:  y-value at top of the trapezoid (1.0)
        @param y_min:  y-value outside the trapezoid (0.0)
        @param m1:     x-value of left top of trapezoid (-0.5)
        @param m2:     x-value of right top of trapezoid (0.5)
        @param alpha:  distance of left corner to m1 (0.5)
        @param beta:   distance of right corner to m2 (0.5)
        """
        super(Trapez, self).__init__()
        self._y_max = float(y_max)
        self._y_min = float(y_min)
        self._m1 = float(m1)
        self._m2 = float(m2)
        self._alpha = float(alpha)
        self._beta = float(beta)
        self._update() # update polygon

    # pylint: disable=E0211,W0212
    @prop
    def y_max(): #@NoSelf
        """y-value at top of the trapezoid
        @type: float"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._y_max
        def fset(self, value): # pylint: disable=W0612,C0111
            self._y_max = float(value)
            self._update()
        return locals()

    # pylint: disable=E0211,W0212
    @prop
    def y_min(): #@NoSelf
        """y-value outside the trapezoid
        @type: float"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._y_min
        def fset(self, value): # pylint: disable=W0612,C0111
            self._y_min = float(value)
            self._update()
        return locals()

    # pylint: disable=E0211,W0212
    @prop
    def m1(): #@NoSelf
        """x-value of left top of trapezoid
        @type: float"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._m1
        def fset(self, value): # pylint: disable=W0612,C0111
            self._m1 = float(value)
            self._update()
        return locals()

    # pylint: disable=E0211,W0212
    @prop
    def m2(): #@NoSelf
        """x-value of right top of trapezoid
        @type: float"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._m2
        def fset(self, value): # pylint: disable=W0612,C0111
            self._m2 = float(value)
            self._update()
        return locals()

    # pylint: disable=E0211,W0212
    @prop
    def alpha(): #@NoSelf
        """distance of left corner to m1
        @type: float"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._alpha
        def fset(self, value): # pylint: disable=W0612,C0111
            self._alpha = float(value)
            self._update()
        return locals()

    # pylint: disable=E0211,W0212
    @prop
    def beta(): #@NoSelf
        """distance of right corner to m2
        @type: float"""
        def fget(self): # pylint: disable=W0612,C0111
            return self._beta
        def fset(self, value): # pylint: disable=W0612,C0111
            self._beta = float(value)
            self._update()
        return locals()

    def _update(self):
        """update polygon"""
        p = super(Trapez, self)
        p.clear()
        p.add(self._m1-self._alpha, self._y_min)
        p.add(self._m1, self._y_max)
        p.add(self._m2, self._y_max)
        p.add(self._m2+self._beta, self._y_min)

    def add(self, x, y, where=Polygon.END):
        """Don't let anyone destroy our trapezoid."""
        raise FuzzyException()

    def remove(self, x, where=Polygon.END):
        """Don't let anyone destroy our trapezoid."""
        raise FuzzyException()

    def clear(self):
        """Don't let anyone destroy our trapezoid."""
        raise FuzzyException()

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        return "%s.%s(m1=%s, m2=%s, alpha=%s, beta=%s, y_max=%s, y_min=%s)" % (
                self.__class__.__module__,
                self.__class__.__name__,
                self._m1,
                self._m2,
                self._alpha,
                self._beta,
                self._y_max,
                self._y_min,
            )
