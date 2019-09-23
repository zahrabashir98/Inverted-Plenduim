# -*- coding: utf-8 -*-
#
# Copyright (C) 2013  Rene Liebscher
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
"""Plotting of variables, adjectives, ... using matplotlib"""

__revision__ = "$Id: doc.py,v 1.15 2010-10-29 19:24:41 rliebscher Exp $"

import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# from http://bl.ocks.org/mbostock/5577023 , Set1
colors = ["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00","#ffff33","#a65628","#f781bf","#999999"]

def getMinMax(set):
    """get tuple with minimum and maximum x-values used by the set."""
    x_min = None
    x_max = None
    for x in  set.getValuesX():
        if x_min is None:
            x_min = x
        x_max = x

    return (x_min,x_max)

def getGlobalMinMax(sets):
    """get tuple with minimum and maximum x-values used by the sets of this dicts of sets."""
    x_min = None
    x_max = None
    for s in sets.values():
        (x_min2,x_max2) = getMinMax(s)
        if x_min is None or x_min2 < x_min:
            x_min = x_min2
        if x_max is None or x_max2 > x_max:
            x_max = x_max2
    return (x_min,x_max)


def getPoints(sets):
    """Collect all important points of all adjectives in this dict of sets."""

    from fuzzy.set.Set import merge
    # merge them all
    temp = None
    for s in sets.values():
        if temp is None:
            temp = s
        else:
            temp = merge(max,temp,s)

    # collect points
    # >>> result of merge is always a Polygon object
    points = [p[0] for p in temp.points]
    # avoid to have same value twice (filter points out where successor is equal)
    return points[:1] + [p0 for p0,p1 in zip(points[1:],points) if p0!=p1]


def getSets(variable):
    """Get all sets of adjectives in this variable."""
    sets = {}
    for a_name,adj in variable.adjectives.items():
        sets[a_name] = adj.set
    return sets


class Doc(object):
    """Main object. Get an instance of this to do your work."""

    def __init__(self,directory="doc"):
        self.directory = directory
        self.overscan = 0.1 #: the plotted range is M{[min-o,max+o]} with M{o=(max-min)*overscan}


    def getValues(self,v):
        return self.getValuesSets(getSets(v))


    def getValuesSets(self,sets):
        (x_min,x_max) = getGlobalMinMax(sets)
        width = x_max - x_min
        x_min = x_min - self.overscan * width
        x_max = x_max + self.overscan * width
        width = x_max - x_min

        values = [x_min]+getPoints(sets)+[x_max]

        return (x_min,x_max,values)


    def createDoc(self,system):
        """create plots of all variables defined in the given system."""

        from fuzzy.OutputVariable import OutputVariable
        from fuzzy.InputVariable import InputVariable
        import fuzzy.defuzzify.Dict
        import fuzzy.fuzzify.Dict

        for name,var in system.variables.items():
            if isinstance(var,OutputVariable) and isinstance(var.defuzzify,fuzzy.defuzzify.Dict.Dict):
                sys.stderr.write("ignore variable %s because it is of type OutputVariable => Dict\n" % name)
            elif isinstance(var,InputVariable) and isinstance(var.fuzzify,fuzzy.fuzzify.Dict.Dict):
                sys.stderr.write("ignore variable %s because it is of type InputVariable => Dict\n" % name)
            else:
                self.createDocVariable(var,name)

    def createDocVariable(self,v,name,x_logscale=0,y_logscale=0):
        """Creates a 2D plot of a variable"""

        self.createDocSets(getSets(v),name,x_logscale,y_logscale,description=v.description,units=v.unit)

    def buildDocVariable(self,ax,v,name,x_logscale=0,y_logscale=0):
        """Creates a 2D plot of a variable"""

        self.buildDocSets(ax,getSets(v),name,x_logscale,y_logscale,description=v.description,units=v.unit)

    def buildDocSets(self, ax, sets,name,x_logscale=0,y_logscale=0,description=None,units=None):
        """Creates a 2D plot of dict of sets"""

        import fuzzy.set.Polygon

        # sort sets by lowest x values and higher membership values next
        def sort_key(a):
            s = sets[a]
            x = s.getValuesX().next()
            return (x,-s(x))

        (x_min,x_max,x) = self.getValuesSets(sets)

        ax.set_title(name)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(-0.2, 1.2)
        # calculate values
        plot_items = []
        i = 0
        # needed for older matplotlib
        legend_plots = []
        legend_labels = []
        for s_name in sorted(sets,key=sort_key):
            s = sets[s_name]
            if isinstance(s,fuzzy.set.Polygon.Polygon):
                p = [(x_min,s(x_min))] + s.points + [(x_max,s(x_max))]
                X,Y = zip(*p)
                pl = ax.fill_between(X, Y, alpha=0.5, color=colors[i % len(colors)], label=s_name)
                legend_plots.append(plt.Rectangle((0,0),1,1,alpha=0.5,fc=colors[i % len(colors)]))
                legend_labels.append(s_name)
                #plot_item = Gnuplot.PlotItems.Data(p,title=s_name)
            else:
                pl = ax.fill_between(x,[s(v) for v in x], alpha=0.5, color=colors[i % len(colors)], label=s_name)
                legend_plots.append(plt.Rectangle((0,0),1,1,alpha=0.5,fc=colors[i % len(colors)]))
                legend_labels.append(s_name)
                #plot_item = Gnuplot.funcutils.compute_Data(x,s,title=s_name)
            #plot_items.append(plot_item)
            i += 1

        xlabel = description or ""
        if units is not None:
            xlabel += " [%s]" % units
        ax.set_title(name)
        ax.set_xlabel(unicode(xlabel, "utf-8"))
        ax.set_ylabel("membership")
        ax.legend(legend_plots, legend_labels)

    def createDocSets(self,sets,name,x_logscale=0,y_logscale=0,description=None,units=None):
        """Creates a 2D plot of dict of sets"""

        fig = plt.figure()
        ax = fig.gca()
        self.buildDocSets(ax,sets,name,x_logscale,y_logscale,description,units)
        fig.savefig("%s/%s.png" % (self.directory,name))

    def build2DPlot(self,ax,system,x_name,y_name,input_dict=None,output_dict=None,x_logscale=0,y_logscale=0):
        """Creates a 2D plot of an input variable and an output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict.
        
        @param system: the fuzzy system to use
        @type system: L{fuzzy.System.System}
        @param x_name: name of input variable used for x coordinate values
        @type x_name: string
        @param y_name: name of output variable used for y coordinate values
        @type y_name: string
        @param input_dict: dictionary used for input values, can be used to predefine other input values
        @type input_dict: dict
        @param output_dict: dictionary used for output values
        @type output_dict: dict
        @param x_logscale: use logarithmic scale for x values
        @type x_logscale: bool
        @param y_logscale: use logarithmic scale for y values
        @type y_logscale: bool
        """

        input_dict = input_dict or {}
        output_dict = output_dict or {}

        (x_min,x_max,x) = self.getValues(system.variables[x_name])

        def f(x):
            input_dict[x_name] = x
            output_dict[y_name] = 0.0

            system.calculate(input_dict,output_dict)

            return output_dict[y_name]

        y = [f(v) for v in x]
        y_min = min(y)
        y_max = max(y)
        ax.set_title(y_name+"=f("+x_name+")")
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.fill_between(x, y, alpha=0.5)
        ax.set_title(y_name+"=f("+x_name+")")
        ax.set_xlabel(unicode(x_name, "utf-8"))
        ax.set_ylabel(unicode(y_name, "utf-8"))
        ax.legend()

    def create2DPlot(self,system,x_name,y_name,input_dict=None,output_dict=None,x_logscale=0,y_logscale=0):
        """Creates a 2D plot of an input variable and an output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict.
        
        @param system: the fuzzy system to use
        @type system: L{fuzzy.System.System}
        @param x_name: name of input variable used for x coordinate values
        @type x_name: string
        @param y_name: name of output variable used for y coordinate values
        @type y_name: string
        @param input_dict: dictionary used for input values, can be used to predefine other input values
        @type input_dict: dict
        @param output_dict: dictionary used for output values
        @type output_dict: dict
        @param x_logscale: use logarithmic scale for x values
        @type x_logscale: bool
        @param y_logscale: use logarithmic scale for y values
        @type y_logscale: bool
        """

        fig = plt.figure()
        ax = fig.gca()
        self.build2DPlot(ax,system,x_name,y_name,input_dict,output_dict,x_logscale,y_logscale)
        fig.savefig("%s/%s.png" % (self.directory,x_name+"_"+y_name))

    def build3DPlot(self,ax,system,x_name,y_name,z_name,input_dict=None,output_dict=None,x_logscale=0,y_logscale=0,z_logscale=0):
        """Creates a 3D plot of 2 input variables and an output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict.
        
        @param system: the fuzzy system to use
        @type system: L{fuzzy.System.System}
        @param x_name: name of input variable used for x coordinate values
        @type x_name: string
        @param y_name: name of input variable used for y coordinate values
        @type y_name: string
        @param z_name: name of output variable used for z coordinate values
        @type z_name: string
        @param input_dict: dictionary used for input values, can be used to predefine other input values
        @type input_dict: dict
        @param output_dict: dictionary used for output values
        @type output_dict: dict
        @param x_logscale: use logarithmic scale for x values
        @type x_logscale: bool
        @param y_logscale: use logarithmic scale for y values
        @type y_logscale: bool
        @param z_logscale: use logarithmic scale for z values
        @type z_logscale: bool
        """
        input_dict = input_dict or {}
        output_dict = output_dict or {}

        (x_min,x_max,x) = self.getValues(system.variables[x_name])
        (y_min,y_max,y) = self.getValues(system.variables[y_name])
        (z_min,z_max,z) = self.getValues(system.variables[z_name])

        def f(x,y):
            input_dict[x_name] = x
            input_dict[y_name] = y
            output_dict[z_name] = 0.0

            system.calculate(input_dict,output_dict)

            return output_dict[z_name]

        ax.set_title("%s=f(%s,%s)" % (z_name,x_name,y_name))
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_zlim(z_min, z_max)
        X = [x] * len(y)
        Y = zip(*([y] * len(x)))
        Z = [[f(x_,y_) for x_ in x] for y_ in y]
        #print X, Y, Z
        #X,Y = np.meshgrid(x,y)
        #f_ = np.vectorize(f)
        #Z = f_(X,Y)
        #X_=np.array(X)
        #Y_=np.array(Y)
        #Z_=np.array(Z)
        #print X_.shape,Y_.shape,Z_.shape
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, shade=True, cmap=plt.cm.gnuplot)
        ax.set_title("%s=f(%s,%s)" % (z_name,x_name,y_name))
        ax.set_xlabel(unicode(x_name, "utf-8"))
        ax.set_ylabel(unicode(y_name, "utf-8"))
        ax.set_zlabel(unicode(z_name, "utf-8"))

    def create3DPlot(self,system,x_name,y_name,z_name,input_dict=None,output_dict=None,x_logscale=0,y_logscale=0,z_logscale=0):
        """Creates a 3D plot of 2 input variables and an output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict.
        
        @param system: the fuzzy system to use
        @type system: L{fuzzy.System.System}
        @param x_name: name of input variable used for x coordinate values
        @type x_name: string
        @param y_name: name of input variable used for y coordinate values
        @type y_name: string
        @param z_name: name of output variable used for z coordinate values
        @type z_name: string
        @param input_dict: dictionary used for input values, can be used to predefine other input values
        @type input_dict: dict
        @param output_dict: dictionary used for output values
        @type output_dict: dict
        @param x_logscale: use logarithmic scale for x values
        @type x_logscale: bool
        @param y_logscale: use logarithmic scale for y values
        @type y_logscale: bool
        @param z_logscale: use logarithmic scale for z values
        @type z_logscale: bool
        """
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        self.build3DPlot(ax,system,x_name,y_name,z_name,input_dict,output_dict,x_logscale,y_logscale,z_logscale)
        fig.savefig("%s/%s.png" % (self.directory,x_name+"_"+y_name+"_"+z_name))


    def build3DPlot_adjective(self,ax,system,x_name,y_name,z_name,adjective,input_dict=None,output_dict=None,x_logscale=0,y_logscale=0,z_logscale=0):
        """Creates a 3D plot of 2 input variables and an adjective of the output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict.
        
        @param system: the fuzzy system to use
        @type system: L{fuzzy.System.System}
        @param x_name: name of input variable used for x coordinate values
        @type x_name: string
        @param y_name: name of input variable used for y coordinate values
        @type y_name: string
        @param z_name: name of output variable used for z coordinate values
        @type z_name: string
        @param adjective: name of adjective of output variable used for z coordinate values
        @type adjective: string
        @param input_dict: dictionary used for input values, can be used to predefine other input values
        @type input_dict: dict
        @param output_dict: dictionary used for output values
        @type output_dict: dict
        @param x_logscale: use logarithmic scale for x values
        @type x_logscale: bool
        @param y_logscale: use logarithmic scale for y values
        @type y_logscale: bool
        @param z_logscale: use logarithmic scale for z values
        @type z_logscale: bool
        """
        input_dict = input_dict or {}
        output_dict = output_dict or {}

        (x_min,x_max,x) = self.getValues(system.variables[x_name])
        (y_min,y_max,y) = self.getValues(system.variables[y_name])

        def f(x,y):
            input_dict[x_name] = x
            input_dict[y_name] = y
            output_dict[z_name] = 0.0

            system.calculate(input_dict,output_dict)

            return output_dict[z_name][adjective]

        ax.set_title("%s.%s=f(%s,%s)" % (z_name,adjective,x_name,y_name))
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_zlim(0, 1)
        X = [x] * len(y)
        Y = zip(*([y] * len(x)))
        Z = [[f(x_,y_) for x_ in x] for y_ in y]
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.gnuplot, shade=True)
        ax.set_title("%s.%s=f(%s,%s)" % (z_name,adjective,x_name,y_name))
        ax.set_xlabel(unicode(x_name, "utf-8"))
        ax.set_ylabel(unicode(y_name, "utf-8"))
        ax.set_zlabel(unicode(z_name, "utf-8"))
        ax.legend()

    def create3DPlot_adjective(self,system,x_name,y_name,z_name,adjective,input_dict=None,output_dict=None,x_logscale=0,y_logscale=0,z_logscale=0):
        """Creates a 3D plot of 2 input variables and an adjective of the output variable.
        Other (const) variables have to be set beforehand in the dictionary input_dict.
        
        @param system: the fuzzy system to use
        @type system: L{fuzzy.System.System}
        @param x_name: name of input variable used for x coordinate values
        @type x_name: string
        @param y_name: name of input variable used for y coordinate values
        @type y_name: string
        @param z_name: name of output variable used for z coordinate values
        @type z_name: string
        @param adjective: name of adjective of output variable used for z coordinate values
        @type adjective: string
        @param input_dict: dictionary used for input values, can be used to predefine other input values
        @type input_dict: dict
        @param output_dict: dictionary used for output values
        @type output_dict: dict
        @param x_logscale: use logarithmic scale for x values
        @type x_logscale: bool
        @param y_logscale: use logarithmic scale for y values
        @type y_logscale: bool
        @param z_logscale: use logarithmic scale for z values
        @type z_logscale: bool
        """
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        self.build3DPlot_adjective(ax,system,x_name,y_name,z_name,adjective,input_dict,output_dict,x_logscale,y_logscale,z_logscale)
        fig.savefig("%s/%s.png" % (self.directory,x_name+"_"+y_name+"_"+z_name+"_"+adjective))
