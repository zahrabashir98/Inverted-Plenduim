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
"""
Helper functions for calculation with fuzzy sets.

Examples can be found here U{http://pyfuzzy.sourceforge.net/demo/merge/}

* Intersection of set1 and set2 can be done by
  
  C{set = merge(T_NORM,set1,set2)}
  
  where T_NORM is a t-norm eg. Min.
  (or a function which accepts two parameters as min().)

* Union of set1 and set2 can be done by
  
  C{set = merge(S_NORM,set1,set2)}
  
  where S_NORM is a s-norm eg. Max.
  (or a function which accepts two parameters as max().)

* Complement of set1 can be done by
  
  C{set = norm(lambda a,b:1.0-a ,set1,0.0)}
  
  using a user defined function for it.
  (The second parameter is ignored or better said
  it doesn't influence the value, it only influences
  maybe where the points of the resulting polygon are
  set.)

* Activation function can be done by
  
  C{set = norm(act_norm,set,act_value)}
  
  where act_norm is any L{fuzzy.norm} or two params function (eg. min)
  and act_value is the result of a rule calculation.
"""

__revision__ = "$Id: operations.py,v 1.13 2013-01-09 20:10:19 rliebscher Exp $"

from fuzzy.Exception import FuzzyException

# helper functions
def _find_root(f, x1, x2, f1=None, f2=None, epsilon=None):
    """Find root of function f between x1,x2 by using the regula falsi method
       with the pegasus modification.
       See also U{http://de.wikipedia.org/wiki/Regula_Falsi}. (The english
       version lacks the description of pegasus modification.)
       The algorithm stops if the error estimation is smaller than epsilon
       or there is an ZeroDivisionError, which means both values f1 and f2 are
       identical (should be 0 then).
       
       @param f: function for which to find M{f(x)=0}
       @type f: M{f(x)}
       @param x1: left border of range
       @type x1: float
       @param x2: right border of range
       @type x2: float
       @param f1: value for x1, if available
       @type f1: float
       @param f2: value for x2, if available
       @type f2: float
       @param epsilon: break condition for algorithm (value < epsilon)
       @type epsilon: float/None
       @return: M{x} where M{f(x)=0}
       @rtype: float
    """
    if f1 is None:
        f1 = f(x1)
    if f2 is None:
        f2 = f(x2)
    if f1 * f2 > 0.:
        raise FuzzyException("need interval with root")
    if epsilon is None:
        epsilon = 1.e-10
    epsx = epsz = epsilon
    z = (x1+x2)/2.
    try:
        i = 0
        while i < 1000:
            i += 1
            z = x1 - f1 * (x2 - x1) / (f2 - f1) # approximation for root
            fz = f(z)

            #print x1,z,x2,f1,fz,f2
            # smaller than epsilon: return z as approximation
            if abs(x2 - x1) <= epsx or abs(fz) <= epsz:
                return z

            # root in [f(xz), f(x2)]?:
            if fz * f2 < 0.:
                # check [z, x2], but exchange borders
                x1,x2,f1,f2 = x2,z,f2,fz
            else:
                # check [x1, z], and modify the value f1,
                # so next steps x1 will move
                x1,x2,f1,f2 = x1,z,f1*f2/(f2+fz),fz
        raise FuzzyException("Too much iterations: %d" % i)
    except ZeroDivisionError:
        #print "ZeroDivisionError"
        return z

def _find_root_linear(x1,x2,f1,f2):
    """Find root x1,x2 by using interpolation.
       
       @param x1: left border of range
       @type x1: float
       @param x2: right border of range
       @type x2: float
       @param f1: value for x1
       @type f1: float
       @param f2: value for x2
       @type f2: float
       @return: M{x} where M{f(x)=0}
       @rtype: float
    """
    m = f1 / (f2 - f1)
    return x1 - m * (x2 - x1)

def _find_intersection(x1,x2,fa1,fa2,fb1,fb2):
    """Find intersection of two linear functions fa/fb between x1,x2
       with values there fa1/fb1 and fa2/fb2.
           
       @param x1: left border of range
       @type x1: float
       @param x2: right border of range
       @type x2: float
       @param fa1: value for x1
       @type fa1: float
       @param fa2: value for x2
       @type fa2: float
       @param fb1: value for x1
       @type fb1: float
       @param fb2: value for x2
       @type fb2: float
       @return: M{x} where M{fa(x)-fb(x)=0}
       @rtype: float
    """
    return _find_root_linear(x1,x2,fa1-fb1,fa2-fb2)

def check(x,y1,y2):
    if isinstance(y1,list) and len(y1)==1:
        y1 = y1[0]
    if isinstance(y1,float) and isinstance(y2,float):
        return [(x,y1,y2)]
    elif isinstance(y1,float) and isinstance(y2,list):
        return [(x,y1,y2_) for y2_ in y2]
    elif isinstance(y1,list) and isinstance(y2,float):
        return [(x,y2_,y1_) for x,y1_,y2_ in check(x,y2,y1)]
    else:
        if len(y1) == len(y2):
            # intersection
            # for all x,y1,y2
            return [(x,y1_,y2_) for y1_,y2_ in zip(y1,y2)]
        elif len(y1) < len(y2):
            if len(y2)>3:
                raise FuzzyException()
            # only case 2-3 is left
            return [(x,y1[0],y2[0]),(x,y1[1],y2[1]),(x,y1[1],y2[2])]
        else:
            return [(x,y2,y1) for x,y1,y2 in check(x,y2_,y1_)]


def _merge_generator1(set1, set2):
    """Returns a new fuzzy set which is the merger of set1 and set2,
    where the membership of the result set is equal to C{NORM(set1(x),set2(x))}.
    
    @param set1: fuzzy set
    @type set1: L{fuzzy.set.Set}
    @param set2: fuzzy set
    @type set2: L{fuzzy.set.Set}
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
       """

    g1 = set1.getValuesXY()
    g2 = set2.getValuesXY()

    def next_(g,x,y):
        try:
            x,y = next(g)
            return x,y,False
        except StopIteration:
            return x,y,True

    UPDATE_1 = 1
    UPDATE_2 = 2
    UPDATE_BOTH = 3

    x1,y1,end1 = next_(g1,None,None)
    x2,y2,end2 = next_(g2,None,None)
    while not (end1 and end2):
        if end1:
            update = UPDATE_2
        elif end2:
            update = UPDATE_1
        elif x1 < x2:
            update = UPDATE_1
        elif x1 > x2:
            update = UPDATE_2
        else:
            update = UPDATE_BOTH

        if update == UPDATE_1:
            x = x1
            y1_ = y1
            y2_ = set2(x)
        elif update == UPDATE_2:
            x = x2
            y1_ = set1(x)
            y2_ = y2
        else:
            x = x1 # x1 == x2 !
            y1_ = y1
            y2_ = y2

        #check
        for _,_y1,_y2 in check(x,y1_,y2_):
            # add this point
            yield (x, _y1, _y2)

        if update == UPDATE_1:
            x1,y1,end1 = next_(g1,x1,y1)
        elif update == UPDATE_2:
            x2,y2,end2 = next_(g2,x2,y2)
        else:
            x1,y1,end1 = next_(g1,x1,y1)
            x2,y2,end2 = next_(g2,x2,y2)


def _merge_generator(NORM, set1, set2):
    """Returns a new fuzzy set which is the merger of set1 and set2,
    where the membership of the result set is equal to C{NORM(set1(x),set2(x))}.
    
    @param NORM: fuzzy norm to calculate both sets values. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set1: fuzzy set
    @type set1: L{fuzzy.set.Set}
    @param set2: fuzzy set
    @type set2: L{fuzzy.set.Set}
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
       """

    from fuzzy.set.Polygon import Polygon
    use_find_root = not (isinstance(set1, Polygon) and isinstance(set2, Polygon))

    g = _merge_generator1(set1,set2)
    x,y1,y2 = next(g)
    yield (x, NORM(y1, y2))
    prev_x, prev_y1, prev_y2 = x, y1, y2
    for x,y1,y2 in g:
        # test if intersection => split interval
        if (x != prev_x) and ((y1>y2 and prev_y1<prev_y2) or (y1<y2 and prev_y1>prev_y2)):
            # calculate intersection
            if use_find_root:
                f = lambda x, set1=set1, set2=set2: set1(x)-set2(x)
                x_ = _find_root(f, prev_x, x, prev_y1-prev_y2, y1-y2)
            else:
                x_ = _find_intersection(prev_x,x,prev_y1,y1,prev_y2,y2)
            y1_ = set1(x_)
            y2_ = set2(x_)
            # add this point
            yield (x_, NORM(y1_, y2_))
            # set saved point to intermediate
            prev_x, prev_y1, prev_y2 = x_, y1_, y2_
        # add this point
        yield (x, NORM(y1, y2))
        prev_x, prev_y1, prev_y2 = x, y1, y2

def merge(NORM, set1, set2, segment_size=None):
    """Returns a new fuzzy set which is the merger of set1 and set2,
    where the membership of the result set is equal to C{NORM(set1(x),set2(x))}.
    
    For nonlinear operations you might want set the segment size to a value 
    which controls how large a linear segment of the result can be. 
    See also the following examples:
      - U{http://pyfuzzy.sourceforge.net/demo/merge/AlgebraicProduct_d_d.png} - The algebraic product is M{x*y}, so using it on the same set, it calculates the square of it.
      - U{http://pyfuzzy.sourceforge.net/demo/merge/AlgebraicSum_d_d.png} - The algebraic sum is M{x+y-x*y}.
    
    @param NORM: fuzzy norm to calculate both sets values. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set1: fuzzy set
    @type set1: L{fuzzy.set.Set}
    @param set2: fuzzy set
    @type set2: L{fuzzy.set.Set}
    @param segment_size: maximum size of a segment
    @type segment_size: float/None
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
       """
    from fuzzy.set.Polygon import Polygon
    ret = Polygon()

    prev_x, prev_y = None, None
    for x, y in _merge_generator(NORM, set1, set2):
        if (segment_size is not None) and (prev_x is not None) and (abs(y-prev_y)>0.01):
            diff = x-prev_x
            if  diff > 2.*segment_size:
                n = int(diff/segment_size)
                dx = diff/n
                for i in range(1, n):
                    x_ = prev_x+i*dx
                    ret.add(x_, NORM(set1(x_), set2(x_)))
        ret.add(x, y)
        prev_x, prev_y = x, y

    return ret


def _norm_generator(NORM, set, value):
    """Returns a new fuzzy set which is this set normed with value.
    where the membership of the result set is equal to C{NORM(set(x),value)}.
    
    @param NORM: fuzzy norm to calculate set's values with value. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @param value: value
    @type value: float
    """

    from fuzzy.set.Polygon import Polygon
    use_find_root = not isinstance(set, Polygon)

    prev_x = None
    prev_y = None
    for x,y in set.getValuesXY(flat=True):
        if prev_x is None:
            pass
        else:
            # test if intersection => split interval
            if (x != prev_x) and ((y>value and prev_y<value) or (y<value and prev_y>value)):
                # calculate intersection
                if use_find_root:
                    f = lambda x, set=set: set(x)-value
                    x_ = _find_root(f, prev_x, x, prev_y-value, y-value)
                else:
                    x_ = _find_intersection(prev_x,x,prev_y,y,value,value)
                y_ = set(x_)
                # add this point
                yield (x_, NORM(y_, value))
                # set saved point to intermediate
                prev_x, prev_y = x_, y_
        # add this point
        prev_x,prev_y = x,y
        yield (x, NORM(y, value))

def norm(NORM, set, value, segment_size=None):
    """Returns a new fuzzy set which ist this set normed with value.
    where the membership of the result set is equal to C{NORM(set(x),value)}.

    For meaning of segment_size see also L{fuzzy.set.operations.merge}.
    
    @param NORM: fuzzy norm to calculate set's values with value. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @param value: value
    @type value: float
    @param segment_size: maximum size of a segment
    @type segment_size: float/None
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
    """
    from fuzzy.set.Polygon import Polygon
    ret = Polygon()

    prev_x, prev_y = None, None
    for x, y in _norm_generator(NORM, set, value):
        if (segment_size is not None) and (prev_x is not None) and (abs(y-prev_y)>0.01):
            diff = x-prev_x
            if  diff > 2.*segment_size:
                n = int(diff/segment_size)
                dx = diff/n
                for i in range(1, n):
                    x_ = prev_x+i*dx
                    ret.add(x_, NORM(set(x_), value))
        ret.add(x, y)
        prev_x, prev_y = x, y

    return ret

def _complement_generator(COMPLEMENT, set):
    """Returns a new fuzzy set which is this complement of the given set.
    (Where the membership of the result set is equal to C{COMPLEMENT(set(x))}.
    
    @param COMPLEMENT: fuzzy complement to use. For example Zadeh(), ...
        Also possible as one param function, eg. C{lambda x: 1.-x}.
    @type COMPLEMENT: L{fuzzy.complement.Base.Base}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
    """
    for x,y in set.getValuesXY(flat=True):
        yield (x, COMPLEMENT(y))

def complement(COMPLEMENT, set, segment_size=None):
    """Returns a new fuzzy set which is this complement of the given set.
    (Where the membership of the result set is equal to C{COMPLEMENT(set(x))}.

    For meaning of segment_size see also L{fuzzy.set.operations.merge}.
    
    @param COMPLEMENT: fuzzy complement to use. For example Zadeh(), ...
        Also possible as one param function, eg. C{lambda x: 1.-x}.
    @type COMPLEMENT: L{fuzzy.complement.Base.Base}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @param segment_size: maximum size of a segment
    @type segment_size: float/None
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
    """
    from fuzzy.set.Polygon import Polygon
    ret = Polygon()

    prev_x, prev_y = None, None
    for x, y in _complement_generator(COMPLEMENT, set):
        if (segment_size is not None) and (prev_x is not None) and (abs(y-prev_y)>0.01):
            diff = x-prev_x
            if  diff > 2.*segment_size:
                n = int(diff/segment_size)
                dx = diff/n
                for i in range(1, n):
                    x_ = prev_x+i*dx
                    ret.add(x_, COMPLEMENT(set(x_)))
        ret.add(x, y)
        prev_x, prev_y = x, y

    return ret
