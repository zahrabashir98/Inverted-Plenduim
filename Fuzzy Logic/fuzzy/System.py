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

"""Main coordinator class of a whole fuzzy system"""

__revision__ = "$Id: System.py,v 1.19 2010-02-17 19:57:13 rliebscher Exp $"

class System(object):
    """Holds all stuff together. (variables, rules, ...)
        Provides methods to do calculation with it.
        
        @ivar variables: dictionary to hold all variables.
        @type variables: {string:L{fuzzy.Variable.Variable}}
        @ivar rules: dictionary to hold all rules.
        @type rules: {string:L{fuzzy.Rule.Rule}}
        @ivar description: description
        @type description: string
    """ 

    def __init__(self, description="", variables = None, rules = None):
        """Constructor.

        @param description: description
        @type description: string
        """
        self.variables = variables or {}
        self.rules = variables or {}
        self.description = description

    def reset(self):
        """Reset all memberships for the next run of calculate"""
        for variable in self.variables.values():
            variable.reset()

    def fuzzify(self, input):
        """Fuzzify the inputs.
        The input dictionary contains the input values for the named variables."""

        # feed input values in variables and so in adjectives
        for (name, value) in input.items():
            if name in self.variables:
                self.variables[name].setValue(value)
            #else:
            #   print "ignored input ",name


    def inference(self):
        """Calculate the fuzzy inference given by the rules."""

        # compute fuzzy rules 
        for rule in self.rules.values():
            rule.compute()


    def defuzzify(self, output):
        """Defuzzyfy the variables.
        The output dictionary serves as container and provides the names of the
        variables to read."""

        # get all wanted output variables
        for name in output.keys():
            output[name] = self.variables[name].getValue()

        return output


    def calculate(self, input, output):
        """Do a complete fuzzy calculation step.
        The input dictionary contains the input values for the named variables.
        The output dictionary serves as container and provides the names of the
        variables to read."""

        self.reset()

        self.fuzzify(input)

        self.inference()

        self.defuzzify(output)

        return output


    def findVariableName(self, var):
        """Find name of variable in this system"""
        for name, variable in self.variables.items():
            if var is variable:
                return name
        return None

    def findAdjectiveName(self, adj):
        """Find name of adjective (and variable) in this system"""
        for name, variable in self.variables.items():
            for namea, adjective in variable.adjectives.items():
                if adj is adjective:
                    return [namea, name]
        return None

    def findRuleName(self, _rule):
        """Find name of rule in this system"""
        for name, rule in self.rules.items():
            if _rule is rule:
                return name
        return None

    def __repr__(self):
        """Return representation of instance.
                   
           @return: representation of instance
           @rtype: string
           """
        params = []
        if self.description: params.append("description=%s" % repr(self.description))
        if self.variables: params.append("variables=%s" % repr(self.variables))
        if self.rules: params.append("rules=%s" % repr(self.rules))
        return "%s.%s(%s)" % (self.__class__.__module__, self.__class__.__name__, ", ".join(params))
