/**

 Grammar definition for FCL used fuzzy.fcl.Reader of pyfuzzy 

 Copyright (C) 2009  Rene Liebscher

 This program is free software; you can redistribute it and/or modify it under
 the terms of the GNU Lesser General Public License as published by the Free
 Software Foundation; either version 3 of the License, or (at your option) any
 later version.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License along with
 this program; if not, see <http://www.gnu.org/licenses/>. 

 $Id: FCL.g,v 1.8 2012-11-17 20:29:24 rliebscher Exp $
*/
grammar FCL;

options {
    language=Python;
}
@lexer::header{
#docstring
__doc__ = """Lexer for reading FCL by the pyfuzzy package."""
__revision__ = "\$ Id: FCL.g,v 1.7 2009/10/20 19:15:33 rliebscher Exp $"

# pylint: disable-msg=W0107,W0301,W0401,W0614,W0621,C0103,C0111,C0301,C0302,C0322,R0904,R0912,R0915
#ID:W0107 : Unnecessary pass statement
#ID:W0301 : Unnecessary semicolon
#ID:W0401 : Wildcard import antlr3
#ID:W0614 : Unused import ... from wildcard import
#ID:W0621 : Redefining name 'main' from outer scope
#ID:C0103 : Invalid name
#ID:C0111 : Missing docstring
#ID:C0301 : Line too long
#ID:C0302 : Too many lines in module
#ID:C0322 : Operator not preceded by a space
#ID:R0904 : Too many public methods
#ID:R0912 : Too many branches
#ID:R0915 : Too many statements


}
@header {
#docstring
__doc__ = """Parser for reading FCL by the pyfuzzy package."""
__revision__ = "\$Id: FCL.g,v 1.8 2012-11-17 20:29:24 rliebscher Exp $"

import fuzzy.System
import fuzzy.InputVariable
import fuzzy.OutputVariable
import fuzzy.Adjective
import fuzzy.set.Polygon
import fuzzy.set.Singleton
import fuzzy.defuzzify
import fuzzy.defuzzify.Dict
import fuzzy.fuzzify
import fuzzy.fuzzify.Plain
import fuzzy.fuzzify.Dict
import fuzzy.operator.Not
import fuzzy.operator.Input
import fuzzy.operator.Compound
import fuzzy.Rule
import fuzzy.norm.Min
import fuzzy.norm.Max

def getNorm(name, p=None):
    """Get an instance of a fuzzy norm with given name.
    Normally looks into the fuzzy.norm package for a suitable class.
    """
    m = __import__("fuzzy.norm."+name, fromlist=[name])
    c = m.__dict__[name]
    if p is None:
        return c()
    else:
        return c(p)

def getSet(name, params=[]):
    """Get an instance of a fuzzy set with given name.
    Normally looks into the fuzzy.set package for a suitable class.
    """
    m = __import__("fuzzy.set."+name, fromlist=[name])
    c = m.__dict__[name]
    return c(*params)

def getDefuzzificationMethod(name):
    """Get an instance of a defuzzification method with given name.
    Normally looks into the fuzzy.defuzzify package for a suitable class.
    """
    m = __import__("fuzzy.defuzzify."+name, fromlist=[name])
    c = m.__dict__[name]
    return c()

# container for definitions of operator/norm pairs
_operators = {
    "AND":fuzzy.norm.Min.Min(),
    "OR":fuzzy.norm.Max.Max()
    }

def defineOperator(name, norm):
    """Defines a operator (AND,OR,...) to use a given norm."""
    _operators[name] = norm
    #print "defineOperator ",name,norm

def getOperator(name):
    """Get the norm for previous defined operator name."""
    #print "getOperator ",name
    import copy
    return copy.deepcopy(_operators[name])

_structs = {}

def defineStructType(name):
    """Remember name of a struct definition"""
    _structs[name] = []

def defineStructTypeElement(name, elem):
    """Add a struct element"""
    _structs[name].append(elem)

def getStructType(name):
    """Get list of elements of a struct definition"""
    return _structs[name]

# pylint: disable-msg=W0107,W0301,W0401,W0614,W0621,C0103,C0111,C0301,C0302,C0322,C0324,R0904,R0912,R0915
#ID:W0107 : Unnecessary pass statement
#ID:W0301 : Unnecessary semicolon
#ID:W0401 : Wildcard import antlr3
#ID:W0614 : Unused import ... from wildcard import
#ID:W0621 : Redefining name 'main' from outer scope
#ID:C0103 : Invalid name
#ID:C0111 : Missing docstring
#ID:C0301 : Line too long
#ID:C0302 : Too many lines in module
#ID:C0322 : Operator not preceded by a space
#ID:C0324 : Comma not followed by a space
#ID:R0912 : Too many branches
#ID:R0915 : Too many statements
#ID:R0904 : Too many public methods

}
@init {
self.System = None
}
@members {
# test
}

// main rule of parser
main returns [system] : {self.System = None;} function_block_declaration {$system = self.System;};

function_block_declaration
  :
    'FUNCTION_BLOCK'
    function_block_name { self.System = fuzzy.System.System(description=$function_block_name.text); }
    type_definition*
    fb_io_var_declarations*
//    other_var_declarations*
    function_block_body
    'END_FUNCTION_BLOCK'
    EOF
  ;

type_definition
  :  'STRUCT' Identifier { defineStructType($Identifier.text); } struct_element[$Identifier.text]+ 'END_STRUCT'
  ;

struct_element[struct_name]
  :  Identifier ':' 'REAL' ';' { defineStructTypeElement($struct_name, $Identifier.text);}
  ;

fb_io_var_declarations
  : input_declarations
  | output_declarations
  ;

input_declarations : 'VAR_INPUT' var_decl[0]+ 'END_VAR'; //see IEC 1131-3 Annex B
output_declarations : 'VAR_OUTPUT' var_decl[1]+ 'END_VAR';//see IEC 1131-3 Annex B

// define a fuzzy variable (param output_var is a flag if an input or output variable)
var_decl[output_var]
  :
  Identifier
  ':'
  type
  ';'
{
if $output_var == 0:
    var=fuzzy.InputVariable.InputVariable()
    if $type.struct_type is not None:
        # set fuzzification method to dictionary input
        var.fuzzify = fuzzy.fuzzify.Dict.Dict();
        # create adjectives for all struct members
        for i in $type.struct_type:
            var.adjectives[i] = fuzzy.Adjective.Adjective(fuzzy.set.Set.Set())
    else:
        # default is the plain fuzzification
        var.fuzzify = fuzzy.fuzzify.Plain.Plain();
else:
    var = fuzzy.OutputVariable.OutputVariable()
    if $type.struct_type is not None:
        # set defuzzification method to dictionary output
        var.defuzzify = fuzzy.defuzzify.Dict.Dict();
        # create adjectives for all struct members
        for i in $type.struct_type:
            var.adjectives[i] = fuzzy.Adjective.Adjective(fuzzy.set.Set.Set())
self.System.variables[$Identifier.text]=var;
};

// variable definition type (returns None for REAL typed variables or a list of element name for struct typed ones.)
type returns [struct_type]
  :
  'REAL' {$struct_type = None; }
  |
  Identifier { $struct_type = getStructType($Identifier.text); }
  ;

//other_var_declarations : var_declarations;
//var_declarations : ;//see IEC 1131-3 Annex B

function_block_body
  :
    fuzzify_block*
    defuzzify_block*
    rule_block*
    option_block*
  ;

fuzzify_block
  :
    'FUZZIFY'
    variable_name
    linguistic_term[$variable_name.text]*
    'END_FUZZIFY'
  ;

defuzzify_block
  :
    'DEFUZZIFY'
    f_variable_name
    linguistic_term[$f_variable_name.text]*
    accumulation_method
    defuzzification_method[$f_variable_name.text]
    default_value[$f_variable_name.text]?
    range?
    'END_DEFUZZIFY'
  ;

rule_block
  :
    'RULEBLOCK'
      rule_block_name
      operator_definition*
      activation_method?
      rule[$rule_block_name.text]*
    'END_RULEBLOCK';

option_block : 'OPTION'
 //any manufacturere specific parameter
'END_OPTION';

// define an adjective of a variable
linguistic_term [var_name]
  :
  'TERM' term_name ':=' membership_function ';'
{
self.System.variables[$var_name].adjectives[$term_name.text] = fuzzy.Adjective.Adjective($membership_function.set);
}
;

// parse the membership of adjective definition (currently only singletons or polygons)
membership_function returns [set]
  :
    singleton {$set = $singleton.set;}
  |
    points {$set = $points.set;}
  |
    pyfuzzy_set {$set = $pyfuzzy_set.set;}
  ;

singleton returns [set]
  :
    numeric_literal {$set = fuzzy.set.Singleton.Singleton(float($numeric_literal.text));}
  |
    variable_name
  ;

points returns [set]
@init {
p = []
}
  :
   (
     '('
     (x=numeric_literal | variable_name)
     ','
     y=numeric_literal
     ')'
     {p.append((float($x.text), float($y.text)));}
   )*
   {$set = fuzzy.set.Polygon.Polygon(p);}
   ;

pyfuzzy_set returns [set]
@init {
p = []
}
  :
   Identifier
   '('
   (
   p1=numeric_literal {p.append(float($p1.text));}
    (
      ','
      pn=numeric_literal {p.append(float($pn.text));}
    )*
   )?
   ')'
   {$set = getSet($Identifier.text,p);}
   ;

// parse the defuzzification method, any existent class in fuzzy.defuzzify is accepted.
// COA from the standard is currently not available in fuzzy.defuzzify
defuzzification_method [var_name] :
  'METHOD' ':'
  Identifier {self.System.variables[$var_name].defuzzify = getDefuzzificationMethod($Identifier.text);}
  ';'
  ;

default_value [var_name] :
  'DEFAULT' ':='
  (
    numeric_literal {self.System.variables[$var_name].defuzzify.failsafe = float($numeric_literal.text);}
  |
    'NC' {self.System.variables[$var_name].defuzzify.failsafe = None;}
  )
  ';'
  ;

range : 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';';

// take any norm name with optional parameters eg. Min, MinMax, Gamma[0.4], ...
operator_name_any returns [op]
  :
  i1=Identifier ('[' param=numeric_literal ']')? {
    if $param.text is not None:
        p = float($param.text)
    else:
        p = None
    $op = getNorm($i1.text, p);
  }
  ;

// take any predefined name for AND or any other norm
operator_name_AND returns [op]
  : ('MIN' {$op = getNorm("Min");})
  | ('PROD' {$op = getNorm("AlgebraicProduct");})
  | ('BDIF' {$op = getNorm("BoundedDifference");})
  | (norm= operator_name_any {$op = $norm.op;})
  ;
// take any predefined name for OR or any other norm
operator_name_OR returns [op]
  : ('MAX' {$op = getNorm("Max");})
  | ('ASUM' {$op = getNorm("AlgebraicSum");})
  | ('BSUM' {$op = getNorm("BoundedSum");})
  | (norm= operator_name_any {$op = $norm.op;})
  ;

OR_  : 'OR' DIGIT* ;
AND_ : 'AND' DIGIT* ;
// define an operator like AND, OR, AND1,AND2, OR1,OR123, ... to use a specific norm
operator_definition : 
(
(or_name=OR_ ':' or_op=operator_name_OR  {defineOperator($or_name.text, $or_op.op);})
|
(and_name=AND_ ':' and_op=operator_name_AND  {defineOperator($and_name.text, $and_op.op);})
)
 ';'
;

activation_method : 'ACT' ':' ('PROD' | 'MIN') ';';

accumulation_method : 'ACCU' ':' ('MAX' | 'BSUM' | 'NSUM') ';';

// condition part of a rule
// concatination of several subconditions with same operator allowed
// otherwise one has to use parentheses
condition returns [input]
@init{
op_name = None;
}
  :
  (
    s1=subcondition {$input = $s1.input}
//    |
//    variable_name
  )
  (
    (
      op=(AND_|OR_)
      {
        if op_name is not None and op_name != op.text:
            raise Exception("Don't mix different operations in an expression.")
        else:
            op_name = op.text
      }
      s2=subcondition
      {
        $input = fuzzy.operator.Compound.Compound(getOperator($op.text), $input, $s2.input);
      }
    )
//    |
//    variable_name
  )*
  ;

// subcondition which manages the NOT operator
subcondition returns [input]
  : ('NOT' '(' condition ')' {$input = fuzzy.operator.Not.Not($condition.input);}) 
  | ( subcondition2 {$input = $subcondition2.input;})
  ;

// other variants
// - any paranthesed expression
// - any 'var IS xy' or 'var.xy' expression
// - any function call like usage of norms as 'BoundedSum(...,...)'
subcondition2 returns [input]
  :
  ('(' c1=condition ')'
    {
        $input = $c1.input;
    }
  )
  |
  ( variable_name ('IS' x='NOT'? | '.' ) term_name 
    {
        $input = fuzzy.operator.Input.Input(self.System.variables[$variable_name.text].adjectives[$term_name.text])
        if x is not None:
            $input = fuzzy.operator.Not.Not($input)
    }
  )
  |
  (norm=operator_name_any '(' c4=condition ',' c5=condition ')'
    {
        $input = fuzzy.operator.Compound.Compound($norm.op, $c4.input, $c5.input);
    }// function call
  )
  ;

// in case we have more than one conclusion in a rule, this is handled here 

conclusion returns  [adjs]
@init{
_adjs = []
}
  : (
    (     c1=conclusion2  {_adjs.append($c1.adj);} )
    (  ',' c2=conclusion2  {_adjs.append($c2.adj);} )*
  ) { $adjs = _adjs; }
  ;

conclusion2 returns  [adj]
  :
  ( '(' c2=conclusion3  ')' {$adj=$c2.adj;} )
  |
  (     c1=conclusion3     {$adj=$c1.adj;} )
  ;

conclusion3 returns  [adj]
  :
  (
//  variable_name
//  |
  (v2=variable_name 'IS' t2=term_name {$adj = self.System.variables[$v2.text].adjectives[$t2.text];})
  )
  ;

rule [block_name]
@init{
certainty = 1.0
} : 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ('WITH' weighting_factor {certainty = float($weighting_factor.text);})? ';'
{
    input = $condition.input
    adjective = $conclusion.adjs
    self.System.rules[$block_name+'.'+$Integer_literal.text] = fuzzy.Rule.Rule(adjective, input, certainty=certainty)
}
;

weighting_factor :
//  variable
//  |
  numeric_literal
  ;

function_block_name : Identifier;

rule_block_name : Identifier ;
term_name : Identifier ;
f_variable_name : Identifier ;
variable_name : Identifier;
numeric_literal : Integer_literal | Real_literal ;

//variable 
//  :   variable_name; //????

Identifier : LETTER (LETTER|DIGIT)*;//see IEC 1131-3 Annex B

fragment Integer_literal_wo_sign
  : DIGIT+;
Integer_literal
  :
    ('+'|'-')? Integer_literal_wo_sign ;// ???? see IEC 1131-3 Annex B

fragment LETTER  : 'A'..'Z'|'a'..'z'|'_';
fragment DIGIT  : '0'..'9';

Real_literal
  :  Integer_literal '.' Integer_literal_wo_sign (('e'|'E') Integer_literal)?;//see IEC 1131-3 Annex B

WS  :  (' '|'\r'|'\t'|'\u000C'|'\n') {$channel = HIDDEN;}
    ;

COMMENT
    :   '(*' ( options {greedy=false;} : . )* '*)' {$channel = HIDDEN;}
    ;
