# $ANTLR 3.1.2 /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g 2012-10-19 23:25:10

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
#docstring
__doc__ = """Parser for reading FCL by the pyfuzzy package."""
__revision__ = "$Id: FCLParser.py,v 1.9 2013-01-09 20:10:19 rliebscher Exp $"

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




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
Real_literal=9
OR_=6
T__27=27
T__26=26
T__25=25
T__24=24
LETTER=10
T__23=23
T__22=22
T__21=21
T__20=20
AND_=7
EOF=-1
Identifier=4
T__55=55
T__56=56
T__19=19
T__57=57
T__58=58
T__16=16
T__51=51
T__15=15
T__52=52
T__18=18
T__53=53
T__54=54
T__17=17
Integer_literal_wo_sign=11
T__14=14
T__59=59
DIGIT=5
COMMENT=13
T__50=50
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
T__48=48
T__49=49
T__30=30
T__31=31
T__32=32
WS=12
T__33=33
T__34=34
Integer_literal=8
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "Identifier", "DIGIT", "OR_", "AND_", "Integer_literal", "Real_literal", 
    "LETTER", "Integer_literal_wo_sign", "WS", "COMMENT", "'FUNCTION_BLOCK'", 
    "'END_FUNCTION_BLOCK'", "'STRUCT'", "'END_STRUCT'", "':'", "'REAL'", 
    "';'", "'VAR_INPUT'", "'END_VAR'", "'VAR_OUTPUT'", "'FUZZIFY'", "'END_FUZZIFY'", 
    "'DEFUZZIFY'", "'END_DEFUZZIFY'", "'RULEBLOCK'", "'END_RULEBLOCK'", 
    "'OPTION'", "'END_OPTION'", "'TERM'", "':='", "'('", "','", "')'", "'METHOD'", 
    "'DEFAULT'", "'NC'", "'RANGE'", "'..'", "'['", "']'", "'MIN'", "'PROD'", 
    "'BDIF'", "'MAX'", "'ASUM'", "'BSUM'", "'ACT'", "'ACCU'", "'NSUM'", 
    "'NOT'", "'IS'", "'.'", "'RULE'", "'IF'", "'THEN'", "'WITH'"
]




class FCLParser(Parser):
    grammarFileName = "/work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)




               
        self.System = None




                


        

              
    # test



    # $ANTLR start "main"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:154:1: main returns [system] : function_block_declaration ;
    def main(self, ):

        system = None

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:154:23: ( function_block_declaration )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:154:25: function_block_declaration
                pass 
                #action start
                self.System = None;
                #action end
                self._state.following.append(self.FOLLOW_function_block_declaration_in_main55)
                self.function_block_declaration()

                self._state.following.pop()
                #action start
                system =  self.System
                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return system

    # $ANTLR end "main"


    # $ANTLR start "function_block_declaration"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:156:1: function_block_declaration : 'FUNCTION_BLOCK' function_block_name ( type_definition )* ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF ;
    def function_block_declaration(self, ):

        function_block_name1 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:157:3: ( 'FUNCTION_BLOCK' function_block_name ( type_definition )* ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:158:5: 'FUNCTION_BLOCK' function_block_name ( type_definition )* ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF
                pass 
                self.match(self.input, 14, self.FOLLOW_14_in_function_block_declaration71)
                self._state.following.append(self.FOLLOW_function_block_name_in_function_block_declaration77)
                function_block_name1 = self.function_block_name()

                self._state.following.pop()
                #action start
                self.System = fuzzy.System.System(description=((function_block_name1 is not None) and [self.input.toString(function_block_name1.start,function_block_name1.stop)] or [None])[0]); 
                #action end
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:160:5: ( type_definition )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 16) :
                        alt1 = 1


                    if alt1 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:160:5: type_definition
                        pass 
                        self._state.following.append(self.FOLLOW_type_definition_in_function_block_declaration85)
                        self.type_definition()

                        self._state.following.pop()


                    else:
                        break #loop1


                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:161:5: ( fb_io_var_declarations )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 21 or LA2_0 == 23) :
                        alt2 = 1


                    if alt2 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:161:5: fb_io_var_declarations
                        pass 
                        self._state.following.append(self.FOLLOW_fb_io_var_declarations_in_function_block_declaration92)
                        self.fb_io_var_declarations()

                        self._state.following.pop()


                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_function_block_body_in_function_block_declaration100)
                self.function_block_body()

                self._state.following.pop()
                self.match(self.input, 15, self.FOLLOW_15_in_function_block_declaration106)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_function_block_declaration112)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "function_block_declaration"


    # $ANTLR start "type_definition"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:168:1: type_definition : 'STRUCT' Identifier ( struct_element[$Identifier.text] )+ 'END_STRUCT' ;
    def type_definition(self, ):

        Identifier2 = None

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:169:3: ( 'STRUCT' Identifier ( struct_element[$Identifier.text] )+ 'END_STRUCT' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:169:6: 'STRUCT' Identifier ( struct_element[$Identifier.text] )+ 'END_STRUCT'
                pass 
                self.match(self.input, 16, self.FOLLOW_16_in_type_definition126)
                Identifier2=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_type_definition128)
                #action start
                defineStructType(Identifier2.text); 
                #action end
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:169:66: ( struct_element[$Identifier.text] )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == Identifier) :
                        alt3 = 1


                    if alt3 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:169:66: struct_element[$Identifier.text]
                        pass 
                        self._state.following.append(self.FOLLOW_struct_element_in_type_definition132)
                        self.struct_element(Identifier2.text)

                        self._state.following.pop()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                self.match(self.input, 17, self.FOLLOW_17_in_type_definition136)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "type_definition"


    # $ANTLR start "struct_element"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:172:1: struct_element[struct_name] : Identifier ':' 'REAL' ';' ;
    def struct_element(self, struct_name):

        Identifier3 = None

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:173:3: ( Identifier ':' 'REAL' ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:173:6: Identifier ':' 'REAL' ';'
                pass 
                Identifier3=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_struct_element151)
                self.match(self.input, 18, self.FOLLOW_18_in_struct_element153)
                self.match(self.input, 19, self.FOLLOW_19_in_struct_element155)
                self.match(self.input, 20, self.FOLLOW_20_in_struct_element157)
                #action start
                defineStructTypeElement(struct_name, Identifier3.text);
                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "struct_element"


    # $ANTLR start "fb_io_var_declarations"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:176:1: fb_io_var_declarations : ( input_declarations | output_declarations );
    def fb_io_var_declarations(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:177:3: ( input_declarations | output_declarations )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 21) :
                    alt4 = 1
                elif (LA4_0 == 23) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:177:5: input_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_input_declarations_in_fb_io_var_declarations172)
                    self.input_declarations()

                    self._state.following.pop()


                elif alt4 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:178:5: output_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_output_declarations_in_fb_io_var_declarations178)
                    self.output_declarations()

                    self._state.following.pop()



            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "fb_io_var_declarations"


    # $ANTLR start "input_declarations"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:181:1: input_declarations : 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR' ;
    def input_declarations(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:181:20: ( 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:181:22: 'VAR_INPUT' ( var_decl[0] )+ 'END_VAR'
                pass 
                self.match(self.input, 21, self.FOLLOW_21_in_input_declarations189)
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:181:34: ( var_decl[0] )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == Identifier) :
                        alt5 = 1


                    if alt5 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:181:34: var_decl[0]
                        pass 
                        self._state.following.append(self.FOLLOW_var_decl_in_input_declarations191)
                        self.var_decl(0)

                        self._state.following.pop()


                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1


                self.match(self.input, 22, self.FOLLOW_22_in_input_declarations195)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "input_declarations"


    # $ANTLR start "output_declarations"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:182:1: output_declarations : 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR' ;
    def output_declarations(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:182:21: ( 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:182:23: 'VAR_OUTPUT' ( var_decl[1] )+ 'END_VAR'
                pass 
                self.match(self.input, 23, self.FOLLOW_23_in_output_declarations203)
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:182:36: ( var_decl[1] )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == Identifier) :
                        alt6 = 1


                    if alt6 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:182:36: var_decl[1]
                        pass 
                        self._state.following.append(self.FOLLOW_var_decl_in_output_declarations205)
                        self.var_decl(1)

                        self._state.following.pop()


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                self.match(self.input, 22, self.FOLLOW_22_in_output_declarations209)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "output_declarations"


    # $ANTLR start "var_decl"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:185:1: var_decl[output_var] : Identifier ':' type ';' ;
    def var_decl(self, output_var):

        Identifier5 = None
        type4 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:186:3: ( Identifier ':' type ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:187:3: Identifier ':' type ';'
                pass 
                Identifier5=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_var_decl223)
                self.match(self.input, 18, self.FOLLOW_18_in_var_decl227)
                self._state.following.append(self.FOLLOW_type_in_var_decl231)
                type4 = self.type()

                self._state.following.pop()
                self.match(self.input, 20, self.FOLLOW_20_in_var_decl235)
                #action start
                 
                if output_var == 0:
                    var=fuzzy.InputVariable.InputVariable()
                    if type4 is not None:
                        # set fuzzification method to dictionary input
                        var.fuzzify = fuzzy.fuzzify.Dict.Dict();
                        # create adjectives for all struct members
                        for i in type4:
                            var.adjectives[i] = fuzzy.Adjective.Adjective(fuzzy.set.Set.Set())
                    else:
                        # default is the plain fuzzification
                        var.fuzzify = fuzzy.fuzzify.Plain.Plain();
                else:
                    var = fuzzy.OutputVariable.OutputVariable()
                    if type4 is not None:
                        # set defuzzification method to dictionary output
                        var.defuzzify = fuzzy.defuzzify.Dict.Dict();
                        # create adjectives for all struct members
                        for i in type4:
                            var.adjectives[i] = fuzzy.Adjective.Adjective(fuzzy.set.Set.Set())
                self.System.variables[Identifier5.text]=var;

                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "var_decl"


    # $ANTLR start "type"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:215:1: type returns [struct_type] : ( 'REAL' | Identifier );
    def type(self, ):

        struct_type = None

        Identifier6 = None

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:216:3: ( 'REAL' | Identifier )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 19) :
                    alt7 = 1
                elif (LA7_0 == Identifier) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:217:3: 'REAL'
                    pass 
                    self.match(self.input, 19, self.FOLLOW_19_in_type254)
                    #action start
                    struct_type =  None 
                    #action end


                elif alt7 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:219:3: Identifier
                    pass 
                    Identifier6=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_type264)
                    #action start
                    struct_type =  getStructType(Identifier6.text) 
                    #action end



            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return struct_type

    # $ANTLR end "type"


    # $ANTLR start "function_block_body"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:225:1: function_block_body : ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )* ;
    def function_block_body(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:226:3: ( ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )* )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:227:5: ( fuzzify_block )* ( defuzzify_block )* ( rule_block )* ( option_block )*
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:227:5: ( fuzzify_block )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 24) :
                        alt8 = 1


                    if alt8 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:227:5: fuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_fuzzify_block_in_function_block_body286)
                        self.fuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop8


                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:228:5: ( defuzzify_block )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 26) :
                        alt9 = 1


                    if alt9 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:228:5: defuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_defuzzify_block_in_function_block_body293)
                        self.defuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop9


                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:229:5: ( rule_block )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 28) :
                        alt10 = 1


                    if alt10 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:229:5: rule_block
                        pass 
                        self._state.following.append(self.FOLLOW_rule_block_in_function_block_body300)
                        self.rule_block()

                        self._state.following.pop()


                    else:
                        break #loop10


                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:230:5: ( option_block )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 30) :
                        alt11 = 1


                    if alt11 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:230:5: option_block
                        pass 
                        self._state.following.append(self.FOLLOW_option_block_in_function_block_body307)
                        self.option_block()

                        self._state.following.pop()


                    else:
                        break #loop11






            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "function_block_body"


    # $ANTLR start "fuzzify_block"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:233:1: fuzzify_block : 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY' ;
    def fuzzify_block(self, ):

        variable_name7 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:234:3: ( 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:235:5: 'FUZZIFY' variable_name ( linguistic_term[$variable_name.text] )* 'END_FUZZIFY'
                pass 
                self.match(self.input, 24, self.FOLLOW_24_in_fuzzify_block325)
                self._state.following.append(self.FOLLOW_variable_name_in_fuzzify_block331)
                variable_name7 = self.variable_name()

                self._state.following.pop()
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:237:5: ( linguistic_term[$variable_name.text] )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 32) :
                        alt12 = 1


                    if alt12 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:237:5: linguistic_term[$variable_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_fuzzify_block337)
                        self.linguistic_term(((variable_name7 is not None) and [self.input.toString(variable_name7.start,variable_name7.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop12


                self.match(self.input, 25, self.FOLLOW_25_in_fuzzify_block345)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "fuzzify_block"


    # $ANTLR start "defuzzify_block"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:241:1: defuzzify_block : 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY' ;
    def defuzzify_block(self, ):

        f_variable_name8 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:242:3: ( 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:243:5: 'DEFUZZIFY' f_variable_name ( linguistic_term[$f_variable_name.text] )* accumulation_method defuzzification_method[$f_variable_name.text] ( default_value[$f_variable_name.text] )? ( range )? 'END_DEFUZZIFY'
                pass 
                self.match(self.input, 26, self.FOLLOW_26_in_defuzzify_block362)
                self._state.following.append(self.FOLLOW_f_variable_name_in_defuzzify_block368)
                f_variable_name8 = self.f_variable_name()

                self._state.following.pop()
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:245:5: ( linguistic_term[$f_variable_name.text] )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 32) :
                        alt13 = 1


                    if alt13 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:245:5: linguistic_term[$f_variable_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_defuzzify_block374)
                        self.linguistic_term(((f_variable_name8 is not None) and [self.input.toString(f_variable_name8.start,f_variable_name8.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop13


                self._state.following.append(self.FOLLOW_accumulation_method_in_defuzzify_block382)
                self.accumulation_method()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_defuzzification_method_in_defuzzify_block388)
                self.defuzzification_method(((f_variable_name8 is not None) and [self.input.toString(f_variable_name8.start,f_variable_name8.stop)] or [None])[0])

                self._state.following.pop()
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:248:5: ( default_value[$f_variable_name.text] )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 38) :
                    alt14 = 1
                if alt14 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:248:5: default_value[$f_variable_name.text]
                    pass 
                    self._state.following.append(self.FOLLOW_default_value_in_defuzzify_block395)
                    self.default_value(((f_variable_name8 is not None) and [self.input.toString(f_variable_name8.start,f_variable_name8.stop)] or [None])[0])

                    self._state.following.pop()



                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:249:5: ( range )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 40) :
                    alt15 = 1
                if alt15 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:249:5: range
                    pass 
                    self._state.following.append(self.FOLLOW_range_in_defuzzify_block403)
                    self.range()

                    self._state.following.pop()



                self.match(self.input, 27, self.FOLLOW_27_in_defuzzify_block410)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "defuzzify_block"


    # $ANTLR start "rule_block"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:253:1: rule_block : 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK' ;
    def rule_block(self, ):

        rule_block_name9 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:254:3: ( 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:255:5: 'RULEBLOCK' rule_block_name ( operator_definition )* ( activation_method )? ( rule[$rule_block_name.text] )* 'END_RULEBLOCK'
                pass 
                self.match(self.input, 28, self.FOLLOW_28_in_rule_block427)
                self._state.following.append(self.FOLLOW_rule_block_name_in_rule_block435)
                rule_block_name9 = self.rule_block_name()

                self._state.following.pop()
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:257:7: ( operator_definition )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((OR_ <= LA16_0 <= AND_)) :
                        alt16 = 1


                    if alt16 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:257:7: operator_definition
                        pass 
                        self._state.following.append(self.FOLLOW_operator_definition_in_rule_block443)
                        self.operator_definition()

                        self._state.following.pop()


                    else:
                        break #loop16


                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:258:7: ( activation_method )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == 50) :
                    alt17 = 1
                if alt17 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:258:7: activation_method
                    pass 
                    self._state.following.append(self.FOLLOW_activation_method_in_rule_block452)
                    self.activation_method()

                    self._state.following.pop()



                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:259:7: ( rule[$rule_block_name.text] )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 56) :
                        alt18 = 1


                    if alt18 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:259:7: rule[$rule_block_name.text]
                        pass 
                        self._state.following.append(self.FOLLOW_rule_in_rule_block461)
                        self.rule(((rule_block_name9 is not None) and [self.input.toString(rule_block_name9.start,rule_block_name9.stop)] or [None])[0])

                        self._state.following.pop()


                    else:
                        break #loop18


                self.match(self.input, 29, self.FOLLOW_29_in_rule_block469)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "rule_block"


    # $ANTLR start "option_block"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:262:1: option_block : 'OPTION' 'END_OPTION' ;
    def option_block(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:262:14: ( 'OPTION' 'END_OPTION' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:262:16: 'OPTION' 'END_OPTION'
                pass 
                self.match(self.input, 30, self.FOLLOW_30_in_option_block477)
                self.match(self.input, 31, self.FOLLOW_31_in_option_block481)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "option_block"


    # $ANTLR start "linguistic_term"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:267:1: linguistic_term[var_name] : 'TERM' term_name ':=' membership_function ';' ;
    def linguistic_term(self, var_name):

        term_name10 = None

        membership_function11 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:268:3: ( 'TERM' term_name ':=' membership_function ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:269:3: 'TERM' term_name ':=' membership_function ';'
                pass 
                self.match(self.input, 32, self.FOLLOW_32_in_linguistic_term496)
                self._state.following.append(self.FOLLOW_term_name_in_linguistic_term498)
                term_name10 = self.term_name()

                self._state.following.pop()
                self.match(self.input, 33, self.FOLLOW_33_in_linguistic_term500)
                self._state.following.append(self.FOLLOW_membership_function_in_linguistic_term502)
                membership_function11 = self.membership_function()

                self._state.following.pop()
                self.match(self.input, 20, self.FOLLOW_20_in_linguistic_term504)
                #action start
                 
                self.System.variables[var_name].adjectives[((term_name10 is not None) and [self.input.toString(term_name10.start,term_name10.stop)] or [None])[0]] = fuzzy.Adjective.Adjective(membership_function11);

                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "linguistic_term"


    # $ANTLR start "membership_function"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:276:1: membership_function returns [set] : ( singleton | points | pyfuzzy_set );
    def membership_function(self, ):

        set = None

        singleton12 = None

        points13 = None

        pyfuzzy_set14 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:277:3: ( singleton | points | pyfuzzy_set )
                alt19 = 3
                LA19 = self.input.LA(1)
                if LA19 == Integer_literal or LA19 == Real_literal:
                    alt19 = 1
                elif LA19 == Identifier:
                    LA19_2 = self.input.LA(2)

                    if (LA19_2 == 34) :
                        alt19 = 3
                    elif (LA19_2 == 20) :
                        alt19 = 1
                    else:
                        nvae = NoViableAltException("", 19, 2, self.input)

                        raise nvae

                elif LA19 == 20 or LA19 == 34:
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:278:5: singleton
                    pass 
                    self._state.following.append(self.FOLLOW_singleton_in_membership_function526)
                    singleton12 = self.singleton()

                    self._state.following.pop()
                    #action start
                    set =  singleton12
                    #action end


                elif alt19 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:280:5: points
                    pass 
                    self._state.following.append(self.FOLLOW_points_in_membership_function538)
                    points13 = self.points()

                    self._state.following.pop()
                    #action start
                    set =  points13
                    #action end


                elif alt19 == 3:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:282:5: pyfuzzy_set
                    pass 
                    self._state.following.append(self.FOLLOW_pyfuzzy_set_in_membership_function550)
                    pyfuzzy_set14 = self.pyfuzzy_set()

                    self._state.following.pop()
                    #action start
                    set =  pyfuzzy_set14
                    #action end



            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "membership_function"


    # $ANTLR start "singleton"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:285:1: singleton returns [set] : ( numeric_literal | variable_name );
    def singleton(self, ):

        set = None

        numeric_literal15 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:286:3: ( numeric_literal | variable_name )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((Integer_literal <= LA20_0 <= Real_literal)) :
                    alt20 = 1
                elif (LA20_0 == Identifier) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:287:5: numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_singleton573)
                    numeric_literal15 = self.numeric_literal()

                    self._state.following.pop()
                    #action start
                    set =  fuzzy.set.Singleton.Singleton(float(((numeric_literal15 is not None) and [self.input.toString(numeric_literal15.start,numeric_literal15.stop)] or [None])[0]))
                    #action end


                elif alt20 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:289:5: variable_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_singleton585)
                    self.variable_name()

                    self._state.following.pop()



            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "singleton"


    # $ANTLR start "points"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:292:1: points returns [set] : ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* ;
    def points(self, ):

        set = None

        x = None

        y = None


               
        p = []

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:296:3: ( ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:297:4: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:297:4: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == 34) :
                        alt22 = 1


                    if alt22 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:298:6: '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')'
                        pass 
                        self.match(self.input, 34, self.FOLLOW_34_in_points617)
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:299:6: (x= numeric_literal | variable_name )
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((Integer_literal <= LA21_0 <= Real_literal)) :
                            alt21 = 1
                        elif (LA21_0 == Identifier) :
                            alt21 = 2
                        else:
                            nvae = NoViableAltException("", 21, 0, self.input)

                            raise nvae

                        if alt21 == 1:
                            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:299:7: x= numeric_literal
                            pass 
                            self._state.following.append(self.FOLLOW_numeric_literal_in_points627)
                            x = self.numeric_literal()

                            self._state.following.pop()


                        elif alt21 == 2:
                            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:299:27: variable_name
                            pass 
                            self._state.following.append(self.FOLLOW_variable_name_in_points631)
                            self.variable_name()

                            self._state.following.pop()



                        self.match(self.input, 35, self.FOLLOW_35_in_points639)
                        self._state.following.append(self.FOLLOW_numeric_literal_in_points648)
                        y = self.numeric_literal()

                        self._state.following.pop()
                        self.match(self.input, 36, self.FOLLOW_36_in_points655)
                        #action start
                        p.append((float(((x is not None) and [self.input.toString(x.start,x.stop)] or [None])[0]), float(((y is not None) and [self.input.toString(y.start,y.stop)] or [None])[0])));
                        #action end


                    else:
                        break #loop22


                #action start
                set =  fuzzy.set.Polygon.Polygon(p)
                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "points"


    # $ANTLR start "pyfuzzy_set"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:308:1: pyfuzzy_set returns [set] : Identifier '(' (p1= numeric_literal ( ',' pn= numeric_literal )* )? ')' ;
    def pyfuzzy_set(self, ):

        set = None

        Identifier16 = None
        p1 = None

        pn = None


               
        p = []

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:312:3: ( Identifier '(' (p1= numeric_literal ( ',' pn= numeric_literal )* )? ')' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:313:4: Identifier '(' (p1= numeric_literal ( ',' pn= numeric_literal )* )? ')'
                pass 
                Identifier16=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_pyfuzzy_set699)
                self.match(self.input, 34, self.FOLLOW_34_in_pyfuzzy_set704)
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:315:4: (p1= numeric_literal ( ',' pn= numeric_literal )* )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if ((Integer_literal <= LA24_0 <= Real_literal)) :
                    alt24 = 1
                if alt24 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:316:4: p1= numeric_literal ( ',' pn= numeric_literal )*
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_pyfuzzy_set716)
                    p1 = self.numeric_literal()

                    self._state.following.pop()
                    #action start
                    p.append(float(((p1 is not None) and [self.input.toString(p1.start,p1.stop)] or [None])[0]));
                    #action end
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:317:5: ( ',' pn= numeric_literal )*
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == 35) :
                            alt23 = 1


                        if alt23 == 1:
                            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:318:7: ',' pn= numeric_literal
                            pass 
                            self.match(self.input, 35, self.FOLLOW_35_in_pyfuzzy_set732)
                            self._state.following.append(self.FOLLOW_numeric_literal_in_pyfuzzy_set742)
                            pn = self.numeric_literal()

                            self._state.following.pop()
                            #action start
                            p.append(float(((pn is not None) and [self.input.toString(pn.start,pn.stop)] or [None])[0]));
                            #action end


                        else:
                            break #loop23





                self.match(self.input, 36, self.FOLLOW_36_in_pyfuzzy_set762)
                #action start
                set =  getSet(Identifier16.text,p)
                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return set

    # $ANTLR end "pyfuzzy_set"


    # $ANTLR start "defuzzification_method"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:328:1: defuzzification_method[var_name] : 'METHOD' ':' Identifier ';' ;
    def defuzzification_method(self, var_name):

        Identifier17 = None

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:328:35: ( 'METHOD' ':' Identifier ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:329:3: 'METHOD' ':' Identifier ';'
                pass 
                self.match(self.input, 37, self.FOLLOW_37_in_defuzzification_method785)
                self.match(self.input, 18, self.FOLLOW_18_in_defuzzification_method787)
                Identifier17=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_defuzzification_method791)
                #action start
                self.System.variables[var_name].defuzzify = getDefuzzificationMethod(Identifier17.text);
                #action end
                self.match(self.input, 20, self.FOLLOW_20_in_defuzzification_method797)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "defuzzification_method"


    # $ANTLR start "default_value"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:334:1: default_value[var_name] : 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';' ;
    def default_value(self, var_name):

        numeric_literal18 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:334:26: ( 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:335:3: 'DEFAULT' ':=' ( numeric_literal | 'NC' ) ';'
                pass 
                self.match(self.input, 38, self.FOLLOW_38_in_default_value812)
                self.match(self.input, 33, self.FOLLOW_33_in_default_value814)
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:336:3: ( numeric_literal | 'NC' )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if ((Integer_literal <= LA25_0 <= Real_literal)) :
                    alt25 = 1
                elif (LA25_0 == 39) :
                    alt25 = 2
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:337:5: numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_default_value824)
                    numeric_literal18 = self.numeric_literal()

                    self._state.following.pop()
                    #action start
                    self.System.variables[var_name].defuzzify.failsafe = float(((numeric_literal18 is not None) and [self.input.toString(numeric_literal18.start,numeric_literal18.stop)] or [None])[0]);
                    #action end


                elif alt25 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:339:5: 'NC'
                    pass 
                    self.match(self.input, 39, self.FOLLOW_39_in_default_value836)
                    #action start
                    self.System.variables[var_name].defuzzify.failsafe = None;
                    #action end



                self.match(self.input, 20, self.FOLLOW_20_in_default_value846)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "default_value"


    # $ANTLR start "range"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:344:1: range : 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';' ;
    def range(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:344:7: ( 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:344:9: 'RANGE' ':=' '(' numeric_literal '..' numeric_literal ')' ';'
                pass 
                self.match(self.input, 40, self.FOLLOW_40_in_range857)
                self.match(self.input, 33, self.FOLLOW_33_in_range859)
                self.match(self.input, 34, self.FOLLOW_34_in_range861)
                self._state.following.append(self.FOLLOW_numeric_literal_in_range863)
                self.numeric_literal()

                self._state.following.pop()
                self.match(self.input, 41, self.FOLLOW_41_in_range865)
                self._state.following.append(self.FOLLOW_numeric_literal_in_range867)
                self.numeric_literal()

                self._state.following.pop()
                self.match(self.input, 36, self.FOLLOW_36_in_range869)
                self.match(self.input, 20, self.FOLLOW_20_in_range871)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "range"


    # $ANTLR start "operator_name_any"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:347:1: operator_name_any returns [op] : i1= Identifier ( '[' param= numeric_literal ']' )? ;
    def operator_name_any(self, ):

        op = None

        i1 = None
        param = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:348:3: (i1= Identifier ( '[' param= numeric_literal ']' )? )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:349:3: i1= Identifier ( '[' param= numeric_literal ']' )?
                pass 
                i1=self.match(self.input, Identifier, self.FOLLOW_Identifier_in_operator_name_any890)
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:349:17: ( '[' param= numeric_literal ']' )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == 42) :
                    alt26 = 1
                if alt26 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:349:18: '[' param= numeric_literal ']'
                    pass 
                    self.match(self.input, 42, self.FOLLOW_42_in_operator_name_any893)
                    self._state.following.append(self.FOLLOW_numeric_literal_in_operator_name_any897)
                    param = self.numeric_literal()

                    self._state.following.pop()
                    self.match(self.input, 43, self.FOLLOW_43_in_operator_name_any899)



                #action start
                                                                  
                if ((param is not None) and [self.input.toString(param.start,param.stop)] or [None])[0] is not None:
                    p = float(((param is not None) and [self.input.toString(param.start,param.stop)] or [None])[0])
                else:
                    p = None
                op =  getNorm(i1.text, p)
                  
                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "operator_name_any"


    # $ANTLR start "operator_name_AND"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:359:1: operator_name_AND returns [op] : ( ( 'MIN' ) | ( 'PROD' ) | ( 'BDIF' ) | (norm= operator_name_any ) );
    def operator_name_AND(self, ):

        op = None

        norm = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:360:3: ( ( 'MIN' ) | ( 'PROD' ) | ( 'BDIF' ) | (norm= operator_name_any ) )
                alt27 = 4
                LA27 = self.input.LA(1)
                if LA27 == 44:
                    alt27 = 1
                elif LA27 == 45:
                    alt27 = 2
                elif LA27 == 46:
                    alt27 = 3
                elif LA27 == Identifier:
                    alt27 = 4
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:360:5: ( 'MIN' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:360:5: ( 'MIN' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:360:6: 'MIN'
                    pass 
                    self.match(self.input, 44, self.FOLLOW_44_in_operator_name_AND922)
                    #action start
                    op =  getNorm("Min")
                    #action end





                elif alt27 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:361:5: ( 'PROD' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:361:5: ( 'PROD' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:361:6: 'PROD'
                    pass 
                    self.match(self.input, 45, self.FOLLOW_45_in_operator_name_AND932)
                    #action start
                    op =  getNorm("AlgebraicProduct")
                    #action end





                elif alt27 == 3:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:362:5: ( 'BDIF' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:362:5: ( 'BDIF' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:362:6: 'BDIF'
                    pass 
                    self.match(self.input, 46, self.FOLLOW_46_in_operator_name_AND942)
                    #action start
                    op =  getNorm("BoundedDifference")
                    #action end





                elif alt27 == 4:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:363:5: (norm= operator_name_any )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:363:5: (norm= operator_name_any )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:363:6: norm= operator_name_any
                    pass 
                    self._state.following.append(self.FOLLOW_operator_name_any_in_operator_name_AND955)
                    norm = self.operator_name_any()

                    self._state.following.pop()
                    #action start
                    op =  norm
                    #action end






            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "operator_name_AND"


    # $ANTLR start "operator_name_OR"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:366:1: operator_name_OR returns [op] : ( ( 'MAX' ) | ( 'ASUM' ) | ( 'BSUM' ) | (norm= operator_name_any ) );
    def operator_name_OR(self, ):

        op = None

        norm = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:367:3: ( ( 'MAX' ) | ( 'ASUM' ) | ( 'BSUM' ) | (norm= operator_name_any ) )
                alt28 = 4
                LA28 = self.input.LA(1)
                if LA28 == 47:
                    alt28 = 1
                elif LA28 == 48:
                    alt28 = 2
                elif LA28 == 49:
                    alt28 = 3
                elif LA28 == Identifier:
                    alt28 = 4
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:367:5: ( 'MAX' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:367:5: ( 'MAX' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:367:6: 'MAX'
                    pass 
                    self.match(self.input, 47, self.FOLLOW_47_in_operator_name_OR976)
                    #action start
                    op =  getNorm("Max")
                    #action end





                elif alt28 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:368:5: ( 'ASUM' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:368:5: ( 'ASUM' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:368:6: 'ASUM'
                    pass 
                    self.match(self.input, 48, self.FOLLOW_48_in_operator_name_OR986)
                    #action start
                    op =  getNorm("AlgebraicSum")
                    #action end





                elif alt28 == 3:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:369:5: ( 'BSUM' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:369:5: ( 'BSUM' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:369:6: 'BSUM'
                    pass 
                    self.match(self.input, 49, self.FOLLOW_49_in_operator_name_OR996)
                    #action start
                    op =  getNorm("BoundedSum")
                    #action end





                elif alt28 == 4:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:370:5: (norm= operator_name_any )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:370:5: (norm= operator_name_any )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:370:6: norm= operator_name_any
                    pass 
                    self._state.following.append(self.FOLLOW_operator_name_any_in_operator_name_OR1009)
                    norm = self.operator_name_any()

                    self._state.following.pop()
                    #action start
                    op =  norm
                    #action end






            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "operator_name_OR"


    # $ANTLR start "operator_definition"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:376:1: operator_definition : ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) ) ';' ;
    def operator_definition(self, ):

        or_name = None
        and_name = None
        or_op = None

        and_op = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:376:21: ( ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) ) ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:377:1: ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) ) ';'
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:377:1: ( (or_name= OR_ ':' or_op= operator_name_OR ) | (and_name= AND_ ':' and_op= operator_name_AND ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == OR_) :
                    alt29 = 1
                elif (LA29_0 == AND_) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:378:1: (or_name= OR_ ':' or_op= operator_name_OR )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:378:1: (or_name= OR_ ':' or_op= operator_name_OR )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:378:2: or_name= OR_ ':' or_op= operator_name_OR
                    pass 
                    or_name=self.match(self.input, OR_, self.FOLLOW_OR__in_operator_definition1053)
                    self.match(self.input, 18, self.FOLLOW_18_in_operator_definition1055)
                    self._state.following.append(self.FOLLOW_operator_name_OR_in_operator_definition1059)
                    or_op = self.operator_name_OR()

                    self._state.following.pop()
                    #action start
                    defineOperator(or_name.text, or_op);
                    #action end





                elif alt29 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:380:1: (and_name= AND_ ':' and_op= operator_name_AND )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:380:1: (and_name= AND_ ':' and_op= operator_name_AND )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:380:2: and_name= AND_ ':' and_op= operator_name_AND
                    pass 
                    and_name=self.match(self.input, AND_, self.FOLLOW_AND__in_operator_definition1070)
                    self.match(self.input, 18, self.FOLLOW_18_in_operator_definition1072)
                    self._state.following.append(self.FOLLOW_operator_name_AND_in_operator_definition1076)
                    and_op = self.operator_name_AND()

                    self._state.following.pop()
                    #action start
                    defineOperator(and_name.text, and_op);
                    #action end






                self.match(self.input, 20, self.FOLLOW_20_in_operator_definition1085)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "operator_definition"


    # $ANTLR start "activation_method"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:385:1: activation_method : 'ACT' ':' ( 'PROD' | 'MIN' ) ';' ;
    def activation_method(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:385:19: ( 'ACT' ':' ( 'PROD' | 'MIN' ) ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:385:21: 'ACT' ':' ( 'PROD' | 'MIN' ) ';'
                pass 
                self.match(self.input, 50, self.FOLLOW_50_in_activation_method1094)
                self.match(self.input, 18, self.FOLLOW_18_in_activation_method1096)
                if (44 <= self.input.LA(1) <= 45):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self.match(self.input, 20, self.FOLLOW_20_in_activation_method1106)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "activation_method"


    # $ANTLR start "accumulation_method"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:387:1: accumulation_method : 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';' ;
    def accumulation_method(self, ):

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:387:21: ( 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:387:23: 'ACCU' ':' ( 'MAX' | 'BSUM' | 'NSUM' ) ';'
                pass 
                self.match(self.input, 51, self.FOLLOW_51_in_accumulation_method1114)
                self.match(self.input, 18, self.FOLLOW_18_in_accumulation_method1116)
                if self.input.LA(1) == 47 or self.input.LA(1) == 49 or self.input.LA(1) == 52:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self.match(self.input, 20, self.FOLLOW_20_in_accumulation_method1130)




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "accumulation_method"


    # $ANTLR start "condition"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:392:1: condition returns [input] : (s1= subcondition ) ( (op= ( AND_ | OR_ ) s2= subcondition ) )* ;
    def condition(self, ):

        input = None

        op = None
        s1 = None

        s2 = None


              
        op_name = None;

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:396:3: ( (s1= subcondition ) ( (op= ( AND_ | OR_ ) s2= subcondition ) )* )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:397:3: (s1= subcondition ) ( (op= ( AND_ | OR_ ) s2= subcondition ) )*
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:397:3: (s1= subcondition )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:398:5: s1= subcondition
                pass 
                self._state.following.append(self.FOLLOW_subcondition_in_condition1161)
                s1 = self.subcondition()

                self._state.following.pop()
                #action start
                input = s1
                #action end



                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:402:3: ( (op= ( AND_ | OR_ ) s2= subcondition ) )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if ((OR_ <= LA30_0 <= AND_)) :
                        alt30 = 1


                    if alt30 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:403:5: (op= ( AND_ | OR_ ) s2= subcondition )
                        pass 
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:403:5: (op= ( AND_ | OR_ ) s2= subcondition )
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:404:7: op= ( AND_ | OR_ ) s2= subcondition
                        pass 
                        op = self.input.LT(1)
                        if (OR_ <= self.input.LA(1) <= AND_):
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        #action start
                               
                        if op_name is not None and op_name != op.text:
                            raise Exception("Don't mix different operations in an expression.")
                        else:
                            op_name = op.text
                              
                        #action end
                        self._state.following.append(self.FOLLOW_subcondition_in_condition1211)
                        s2 = self.subcondition()

                        self._state.following.pop()
                        #action start
                               
                        input =  fuzzy.operator.Compound.Compound(getOperator(op.text), input, s2)
                              
                        #action end





                    else:
                        break #loop30






            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "condition"


    # $ANTLR start "subcondition"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:422:1: subcondition returns [input] : ( ( 'NOT' '(' condition ')' ) | ( subcondition2 ) );
    def subcondition(self, ):

        input = None

        condition19 = None

        subcondition220 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:423:3: ( ( 'NOT' '(' condition ')' ) | ( subcondition2 ) )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == 53) :
                    alt31 = 1
                elif (LA31_0 == Identifier or LA31_0 == 34) :
                    alt31 = 2
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:423:5: ( 'NOT' '(' condition ')' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:423:5: ( 'NOT' '(' condition ')' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:423:6: 'NOT' '(' condition ')'
                    pass 
                    self.match(self.input, 53, self.FOLLOW_53_in_subcondition1251)
                    self.match(self.input, 34, self.FOLLOW_34_in_subcondition1253)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition1255)
                    condition19 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_subcondition1257)
                    #action start
                    input =  fuzzy.operator.Not.Not(condition19)
                    #action end





                elif alt31 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:424:5: ( subcondition2 )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:424:5: ( subcondition2 )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:424:7: subcondition2
                    pass 
                    self._state.following.append(self.FOLLOW_subcondition2_in_subcondition1269)
                    subcondition220 = self.subcondition2()

                    self._state.following.pop()
                    #action start
                    input =  subcondition220
                    #action end






            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "subcondition"


    # $ANTLR start "subcondition2"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:431:1: subcondition2 returns [input] : ( ( '(' c1= condition ')' ) | ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name ) | (norm= operator_name_any '(' c4= condition ',' c5= condition ')' ) );
    def subcondition2(self, ):

        input = None

        x = None
        c1 = None

        norm = None

        c4 = None

        c5 = None

        variable_name21 = None

        term_name22 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:432:3: ( ( '(' c1= condition ')' ) | ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name ) | (norm= operator_name_any '(' c4= condition ',' c5= condition ')' ) )
                alt34 = 3
                LA34_0 = self.input.LA(1)

                if (LA34_0 == 34) :
                    alt34 = 1
                elif (LA34_0 == Identifier) :
                    LA34_2 = self.input.LA(2)

                    if (LA34_2 == 34 or LA34_2 == 42) :
                        alt34 = 3
                    elif ((54 <= LA34_2 <= 55)) :
                        alt34 = 2
                    else:
                        nvae = NoViableAltException("", 34, 2, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:433:3: ( '(' c1= condition ')' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:433:3: ( '(' c1= condition ')' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:433:4: '(' c1= condition ')'
                    pass 
                    self.match(self.input, 34, self.FOLLOW_34_in_subcondition21296)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition21300)
                    c1 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_subcondition21302)
                    #action start
                         
                    input =  c1
                        
                    #action end





                elif alt34 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:3: ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:3: ( variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:5: variable_name ( 'IS' (x= 'NOT' )? | '.' ) term_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_subcondition21322)
                    variable_name21 = self.variable_name()

                    self._state.following.pop()
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:19: ( 'IS' (x= 'NOT' )? | '.' )
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == 54) :
                        alt33 = 1
                    elif (LA33_0 == 55) :
                        alt33 = 2
                    else:
                        nvae = NoViableAltException("", 33, 0, self.input)

                        raise nvae

                    if alt33 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:20: 'IS' (x= 'NOT' )?
                        pass 
                        self.match(self.input, 54, self.FOLLOW_54_in_subcondition21325)
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:26: (x= 'NOT' )?
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == 53) :
                            alt32 = 1
                        if alt32 == 1:
                            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:26: x= 'NOT'
                            pass 
                            x=self.match(self.input, 53, self.FOLLOW_53_in_subcondition21329)





                    elif alt33 == 2:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:439:36: '.'
                        pass 
                        self.match(self.input, 55, self.FOLLOW_55_in_subcondition21334)



                    self._state.following.append(self.FOLLOW_term_name_in_subcondition21338)
                    term_name22 = self.term_name()

                    self._state.following.pop()
                    #action start
                         
                    input = fuzzy.operator.Input.Input(self.System.variables[((variable_name21 is not None) and [self.input.toString(variable_name21.start,variable_name21.stop)] or [None])[0]].adjectives[((term_name22 is not None) and [self.input.toString(term_name22.start,term_name22.stop)] or [None])[0]])
                    if x is not None:
                        input = fuzzy.operator.Not.Not(input)
                        
                    #action end





                elif alt34 == 3:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:447:3: (norm= operator_name_any '(' c4= condition ',' c5= condition ')' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:447:3: (norm= operator_name_any '(' c4= condition ',' c5= condition ')' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:447:4: norm= operator_name_any '(' c4= condition ',' c5= condition ')'
                    pass 
                    self._state.following.append(self.FOLLOW_operator_name_any_in_subcondition21360)
                    norm = self.operator_name_any()

                    self._state.following.pop()
                    self.match(self.input, 34, self.FOLLOW_34_in_subcondition21362)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition21366)
                    c4 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 35, self.FOLLOW_35_in_subcondition21368)
                    self._state.following.append(self.FOLLOW_condition_in_subcondition21372)
                    c5 = self.condition()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_subcondition21374)
                    #action start
                         
                    input =  fuzzy.operator.Compound.Compound(norm, c4, c5)
                        
                    #action end






            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return input

    # $ANTLR end "subcondition2"


    # $ANTLR start "conclusion"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:456:1: conclusion returns [adjs] : ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* ) ;
    def conclusion(self, ):

        adjs = None

        c1 = None

        c2 = None


              
        _adjs = []

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:460:3: ( ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* ) )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:460:5: ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* )
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:460:5: ( (c1= conclusion2 ) ( ',' c2= conclusion2 )* )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:461:5: (c1= conclusion2 ) ( ',' c2= conclusion2 )*
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:461:5: (c1= conclusion2 )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:461:11: c1= conclusion2
                pass 
                self._state.following.append(self.FOLLOW_conclusion2_in_conclusion1422)
                c1 = self.conclusion2()

                self._state.following.pop()
                #action start
                _adjs.append(c1);
                #action end



                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:462:5: ( ',' c2= conclusion2 )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == 35) :
                        alt35 = 1


                    if alt35 == 1:
                        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:462:8: ',' c2= conclusion2
                        pass 
                        self.match(self.input, 35, self.FOLLOW_35_in_conclusion1436)
                        self._state.following.append(self.FOLLOW_conclusion2_in_conclusion1440)
                        c2 = self.conclusion2()

                        self._state.following.pop()
                        #action start
                        _adjs.append(c2);
                        #action end


                    else:
                        break #loop35





                #action start
                adjs =  _adjs 
                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adjs

    # $ANTLR end "conclusion"


    # $ANTLR start "conclusion2"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:466:1: conclusion2 returns [adj] : ( ( '(' c2= conclusion3 ')' ) | (c1= conclusion3 ) );
    def conclusion2(self, ):

        adj = None

        c2 = None

        c1 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:467:3: ( ( '(' c2= conclusion3 ')' ) | (c1= conclusion3 ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == 34) :
                    alt36 = 1
                elif (LA36_0 == Identifier) :
                    alt36 = 2
                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:468:3: ( '(' c2= conclusion3 ')' )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:468:3: ( '(' c2= conclusion3 ')' )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:468:5: '(' c2= conclusion3 ')'
                    pass 
                    self.match(self.input, 34, self.FOLLOW_34_in_conclusion21474)
                    self._state.following.append(self.FOLLOW_conclusion3_in_conclusion21478)
                    c2 = self.conclusion3()

                    self._state.following.pop()
                    self.match(self.input, 36, self.FOLLOW_36_in_conclusion21481)
                    #action start
                    adj = c2
                    #action end





                elif alt36 == 2:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:470:3: (c1= conclusion3 )
                    pass 
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:470:3: (c1= conclusion3 )
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:470:9: c1= conclusion3
                    pass 
                    self._state.following.append(self.FOLLOW_conclusion3_in_conclusion21501)
                    c1 = self.conclusion3()

                    self._state.following.pop()
                    #action start
                    adj = c1
                    #action end






            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adj

    # $ANTLR end "conclusion2"


    # $ANTLR start "conclusion3"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:473:1: conclusion3 returns [adj] : ( (v2= variable_name 'IS' t2= term_name ) ) ;
    def conclusion3(self, ):

        adj = None

        v2 = None

        t2 = None


        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:474:3: ( ( (v2= variable_name 'IS' t2= term_name ) ) )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:475:3: ( (v2= variable_name 'IS' t2= term_name ) )
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:475:3: ( (v2= variable_name 'IS' t2= term_name ) )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:478:3: (v2= variable_name 'IS' t2= term_name )
                pass 
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:478:3: (v2= variable_name 'IS' t2= term_name )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:478:4: v2= variable_name 'IS' t2= term_name
                pass 
                self._state.following.append(self.FOLLOW_variable_name_in_conclusion31538)
                v2 = self.variable_name()

                self._state.following.pop()
                self.match(self.input, 54, self.FOLLOW_54_in_conclusion31540)
                self._state.following.append(self.FOLLOW_term_name_in_conclusion31544)
                t2 = self.term_name()

                self._state.following.pop()
                #action start
                adj =  self.System.variables[((v2 is not None) and [self.input.toString(v2.start,v2.stop)] or [None])[0]].adjectives[((t2 is not None) and [self.input.toString(t2.start,t2.stop)] or [None])[0]]
                #action end










            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return adj

    # $ANTLR end "conclusion3"


    # $ANTLR start "rule"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:482:1: rule[block_name] : 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';' ;
    def rule(self, block_name):

        Integer_literal26 = None
        weighting_factor23 = None

        condition24 = None

        conclusion25 = None


              
        certainty = 1.0

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:485:3: ( 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';' )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:485:5: 'RULE' Integer_literal ':' 'IF' condition 'THEN' conclusion ( 'WITH' weighting_factor )? ';'
                pass 
                self.match(self.input, 56, self.FOLLOW_56_in_rule1568)
                Integer_literal26=self.match(self.input, Integer_literal, self.FOLLOW_Integer_literal_in_rule1570)
                self.match(self.input, 18, self.FOLLOW_18_in_rule1572)
                self.match(self.input, 57, self.FOLLOW_57_in_rule1574)
                self._state.following.append(self.FOLLOW_condition_in_rule1576)
                condition24 = self.condition()

                self._state.following.pop()
                self.match(self.input, 58, self.FOLLOW_58_in_rule1578)
                self._state.following.append(self.FOLLOW_conclusion_in_rule1580)
                conclusion25 = self.conclusion()

                self._state.following.pop()
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:485:65: ( 'WITH' weighting_factor )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == 59) :
                    alt37 = 1
                if alt37 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:485:66: 'WITH' weighting_factor
                    pass 
                    self.match(self.input, 59, self.FOLLOW_59_in_rule1583)
                    self._state.following.append(self.FOLLOW_weighting_factor_in_rule1585)
                    weighting_factor23 = self.weighting_factor()

                    self._state.following.pop()
                    #action start
                    certainty = float(((weighting_factor23 is not None) and [self.input.toString(weighting_factor23.start,weighting_factor23.stop)] or [None])[0]);
                    #action end



                self.match(self.input, 20, self.FOLLOW_20_in_rule1591)
                #action start
                 
                input = condition24
                adjective = conclusion25
                self.System.rules[block_name+'.'+Integer_literal26.text] = fuzzy.Rule.Rule(adjective, input, certainty=certainty)

                #action end




            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "rule"

    class weighting_factor_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "weighting_factor"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:493:1: weighting_factor : numeric_literal ;
    def weighting_factor(self, ):

        retval = self.weighting_factor_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:493:18: ( numeric_literal )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:496:3: numeric_literal
                pass 
                self._state.following.append(self.FOLLOW_numeric_literal_in_weighting_factor1606)
                self.numeric_literal()

                self._state.following.pop()



                retval.stop = self.input.LT(-1)


            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "weighting_factor"

    class function_block_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "function_block_name"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:499:1: function_block_name : Identifier ;
    def function_block_name(self, ):

        retval = self.function_block_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:499:21: ( Identifier )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:499:23: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_function_block_name1617)



                retval.stop = self.input.LT(-1)


            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "function_block_name"

    class rule_block_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "rule_block_name"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:501:1: rule_block_name : Identifier ;
    def rule_block_name(self, ):

        retval = self.rule_block_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:501:17: ( Identifier )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:501:19: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_rule_block_name1625)



                retval.stop = self.input.LT(-1)


            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "rule_block_name"

    class term_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "term_name"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:502:1: term_name : Identifier ;
    def term_name(self, ):

        retval = self.term_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:502:11: ( Identifier )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:502:13: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_term_name1633)



                retval.stop = self.input.LT(-1)


            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "term_name"

    class f_variable_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "f_variable_name"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:503:1: f_variable_name : Identifier ;
    def f_variable_name(self, ):

        retval = self.f_variable_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:503:17: ( Identifier )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:503:19: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_f_variable_name1641)



                retval.stop = self.input.LT(-1)


            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "f_variable_name"

    class variable_name_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "variable_name"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:504:1: variable_name : Identifier ;
    def variable_name(self, ):

        retval = self.variable_name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:504:15: ( Identifier )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:504:17: Identifier
                pass 
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_variable_name1649)



                retval.stop = self.input.LT(-1)


            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "variable_name"

    class numeric_literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)





    # $ANTLR start "numeric_literal"
    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:505:1: numeric_literal : ( Integer_literal | Real_literal );
    def numeric_literal(self, ):

        retval = self.numeric_literal_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:505:17: ( Integer_literal | Real_literal )
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:
                pass 
                if (Integer_literal <= self.input.LA(1) <= Real_literal):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


            except RecognitionException:
                re = sys.exc_info()[1]
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "numeric_literal"


    # Delegated rules


 

    FOLLOW_function_block_declaration_in_main55 = frozenset([1])
    FOLLOW_14_in_function_block_declaration71 = frozenset([4])
    FOLLOW_function_block_name_in_function_block_declaration77 = frozenset([15, 16, 21, 23, 24, 26, 28, 30])
    FOLLOW_type_definition_in_function_block_declaration85 = frozenset([15, 16, 21, 23, 24, 26, 28, 30])
    FOLLOW_fb_io_var_declarations_in_function_block_declaration92 = frozenset([15, 21, 23, 24, 26, 28, 30])
    FOLLOW_function_block_body_in_function_block_declaration100 = frozenset([15])
    FOLLOW_15_in_function_block_declaration106 = frozenset([])
    FOLLOW_EOF_in_function_block_declaration112 = frozenset([1])
    FOLLOW_16_in_type_definition126 = frozenset([4])
    FOLLOW_Identifier_in_type_definition128 = frozenset([4])
    FOLLOW_struct_element_in_type_definition132 = frozenset([4, 17])
    FOLLOW_17_in_type_definition136 = frozenset([1])
    FOLLOW_Identifier_in_struct_element151 = frozenset([18])
    FOLLOW_18_in_struct_element153 = frozenset([19])
    FOLLOW_19_in_struct_element155 = frozenset([20])
    FOLLOW_20_in_struct_element157 = frozenset([1])
    FOLLOW_input_declarations_in_fb_io_var_declarations172 = frozenset([1])
    FOLLOW_output_declarations_in_fb_io_var_declarations178 = frozenset([1])
    FOLLOW_21_in_input_declarations189 = frozenset([4])
    FOLLOW_var_decl_in_input_declarations191 = frozenset([4, 22])
    FOLLOW_22_in_input_declarations195 = frozenset([1])
    FOLLOW_23_in_output_declarations203 = frozenset([4])
    FOLLOW_var_decl_in_output_declarations205 = frozenset([4, 22])
    FOLLOW_22_in_output_declarations209 = frozenset([1])
    FOLLOW_Identifier_in_var_decl223 = frozenset([18])
    FOLLOW_18_in_var_decl227 = frozenset([4, 19])
    FOLLOW_type_in_var_decl231 = frozenset([20])
    FOLLOW_20_in_var_decl235 = frozenset([1])
    FOLLOW_19_in_type254 = frozenset([1])
    FOLLOW_Identifier_in_type264 = frozenset([1])
    FOLLOW_fuzzify_block_in_function_block_body286 = frozenset([1, 24, 26, 28, 30])
    FOLLOW_defuzzify_block_in_function_block_body293 = frozenset([1, 26, 28, 30])
    FOLLOW_rule_block_in_function_block_body300 = frozenset([1, 28, 30])
    FOLLOW_option_block_in_function_block_body307 = frozenset([1, 30])
    FOLLOW_24_in_fuzzify_block325 = frozenset([4])
    FOLLOW_variable_name_in_fuzzify_block331 = frozenset([25, 32])
    FOLLOW_linguistic_term_in_fuzzify_block337 = frozenset([25, 32])
    FOLLOW_25_in_fuzzify_block345 = frozenset([1])
    FOLLOW_26_in_defuzzify_block362 = frozenset([4])
    FOLLOW_f_variable_name_in_defuzzify_block368 = frozenset([32, 51])
    FOLLOW_linguistic_term_in_defuzzify_block374 = frozenset([32, 51])
    FOLLOW_accumulation_method_in_defuzzify_block382 = frozenset([37])
    FOLLOW_defuzzification_method_in_defuzzify_block388 = frozenset([27, 38, 40])
    FOLLOW_default_value_in_defuzzify_block395 = frozenset([27, 40])
    FOLLOW_range_in_defuzzify_block403 = frozenset([27])
    FOLLOW_27_in_defuzzify_block410 = frozenset([1])
    FOLLOW_28_in_rule_block427 = frozenset([4])
    FOLLOW_rule_block_name_in_rule_block435 = frozenset([6, 7, 29, 50, 56])
    FOLLOW_operator_definition_in_rule_block443 = frozenset([6, 7, 29, 50, 56])
    FOLLOW_activation_method_in_rule_block452 = frozenset([29, 56])
    FOLLOW_rule_in_rule_block461 = frozenset([29, 56])
    FOLLOW_29_in_rule_block469 = frozenset([1])
    FOLLOW_30_in_option_block477 = frozenset([31])
    FOLLOW_31_in_option_block481 = frozenset([1])
    FOLLOW_32_in_linguistic_term496 = frozenset([4])
    FOLLOW_term_name_in_linguistic_term498 = frozenset([33])
    FOLLOW_33_in_linguistic_term500 = frozenset([4, 8, 9, 34])
    FOLLOW_membership_function_in_linguistic_term502 = frozenset([20])
    FOLLOW_20_in_linguistic_term504 = frozenset([1])
    FOLLOW_singleton_in_membership_function526 = frozenset([1])
    FOLLOW_points_in_membership_function538 = frozenset([1])
    FOLLOW_pyfuzzy_set_in_membership_function550 = frozenset([1])
    FOLLOW_numeric_literal_in_singleton573 = frozenset([1])
    FOLLOW_variable_name_in_singleton585 = frozenset([1])
    FOLLOW_34_in_points617 = frozenset([4, 8, 9])
    FOLLOW_numeric_literal_in_points627 = frozenset([35])
    FOLLOW_variable_name_in_points631 = frozenset([35])
    FOLLOW_35_in_points639 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_points648 = frozenset([36])
    FOLLOW_36_in_points655 = frozenset([1, 34])
    FOLLOW_Identifier_in_pyfuzzy_set699 = frozenset([34])
    FOLLOW_34_in_pyfuzzy_set704 = frozenset([8, 9, 36])
    FOLLOW_numeric_literal_in_pyfuzzy_set716 = frozenset([35, 36])
    FOLLOW_35_in_pyfuzzy_set732 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_pyfuzzy_set742 = frozenset([35, 36])
    FOLLOW_36_in_pyfuzzy_set762 = frozenset([1])
    FOLLOW_37_in_defuzzification_method785 = frozenset([18])
    FOLLOW_18_in_defuzzification_method787 = frozenset([4])
    FOLLOW_Identifier_in_defuzzification_method791 = frozenset([20])
    FOLLOW_20_in_defuzzification_method797 = frozenset([1])
    FOLLOW_38_in_default_value812 = frozenset([33])
    FOLLOW_33_in_default_value814 = frozenset([8, 9, 39])
    FOLLOW_numeric_literal_in_default_value824 = frozenset([20])
    FOLLOW_39_in_default_value836 = frozenset([20])
    FOLLOW_20_in_default_value846 = frozenset([1])
    FOLLOW_40_in_range857 = frozenset([33])
    FOLLOW_33_in_range859 = frozenset([34])
    FOLLOW_34_in_range861 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_range863 = frozenset([41])
    FOLLOW_41_in_range865 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_range867 = frozenset([36])
    FOLLOW_36_in_range869 = frozenset([20])
    FOLLOW_20_in_range871 = frozenset([1])
    FOLLOW_Identifier_in_operator_name_any890 = frozenset([1, 42])
    FOLLOW_42_in_operator_name_any893 = frozenset([8, 9])
    FOLLOW_numeric_literal_in_operator_name_any897 = frozenset([43])
    FOLLOW_43_in_operator_name_any899 = frozenset([1])
    FOLLOW_44_in_operator_name_AND922 = frozenset([1])
    FOLLOW_45_in_operator_name_AND932 = frozenset([1])
    FOLLOW_46_in_operator_name_AND942 = frozenset([1])
    FOLLOW_operator_name_any_in_operator_name_AND955 = frozenset([1])
    FOLLOW_47_in_operator_name_OR976 = frozenset([1])
    FOLLOW_48_in_operator_name_OR986 = frozenset([1])
    FOLLOW_49_in_operator_name_OR996 = frozenset([1])
    FOLLOW_operator_name_any_in_operator_name_OR1009 = frozenset([1])
    FOLLOW_OR__in_operator_definition1053 = frozenset([18])
    FOLLOW_18_in_operator_definition1055 = frozenset([4, 47, 48, 49])
    FOLLOW_operator_name_OR_in_operator_definition1059 = frozenset([20])
    FOLLOW_AND__in_operator_definition1070 = frozenset([18])
    FOLLOW_18_in_operator_definition1072 = frozenset([4, 44, 45, 46, 47, 48, 49])
    FOLLOW_operator_name_AND_in_operator_definition1076 = frozenset([20])
    FOLLOW_20_in_operator_definition1085 = frozenset([1])
    FOLLOW_50_in_activation_method1094 = frozenset([18])
    FOLLOW_18_in_activation_method1096 = frozenset([44, 45])
    FOLLOW_set_in_activation_method1098 = frozenset([20])
    FOLLOW_20_in_activation_method1106 = frozenset([1])
    FOLLOW_51_in_accumulation_method1114 = frozenset([18])
    FOLLOW_18_in_accumulation_method1116 = frozenset([47, 49, 52])
    FOLLOW_set_in_accumulation_method1118 = frozenset([20])
    FOLLOW_20_in_accumulation_method1130 = frozenset([1])
    FOLLOW_subcondition_in_condition1161 = frozenset([1, 6, 7])
    FOLLOW_set_in_condition1189 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_subcondition_in_condition1211 = frozenset([1, 6, 7])
    FOLLOW_53_in_subcondition1251 = frozenset([34])
    FOLLOW_34_in_subcondition1253 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition1255 = frozenset([36])
    FOLLOW_36_in_subcondition1257 = frozenset([1])
    FOLLOW_subcondition2_in_subcondition1269 = frozenset([1])
    FOLLOW_34_in_subcondition21296 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition21300 = frozenset([36])
    FOLLOW_36_in_subcondition21302 = frozenset([1])
    FOLLOW_variable_name_in_subcondition21322 = frozenset([54, 55])
    FOLLOW_54_in_subcondition21325 = frozenset([4, 53])
    FOLLOW_53_in_subcondition21329 = frozenset([4])
    FOLLOW_55_in_subcondition21334 = frozenset([4])
    FOLLOW_term_name_in_subcondition21338 = frozenset([1])
    FOLLOW_operator_name_any_in_subcondition21360 = frozenset([34])
    FOLLOW_34_in_subcondition21362 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition21366 = frozenset([35])
    FOLLOW_35_in_subcondition21368 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_subcondition21372 = frozenset([36])
    FOLLOW_36_in_subcondition21374 = frozenset([1])
    FOLLOW_conclusion2_in_conclusion1422 = frozenset([1, 35])
    FOLLOW_35_in_conclusion1436 = frozenset([4, 34])
    FOLLOW_conclusion2_in_conclusion1440 = frozenset([1, 35])
    FOLLOW_34_in_conclusion21474 = frozenset([4, 34])
    FOLLOW_conclusion3_in_conclusion21478 = frozenset([36])
    FOLLOW_36_in_conclusion21481 = frozenset([1])
    FOLLOW_conclusion3_in_conclusion21501 = frozenset([1])
    FOLLOW_variable_name_in_conclusion31538 = frozenset([54])
    FOLLOW_54_in_conclusion31540 = frozenset([4])
    FOLLOW_term_name_in_conclusion31544 = frozenset([1])
    FOLLOW_56_in_rule1568 = frozenset([8])
    FOLLOW_Integer_literal_in_rule1570 = frozenset([18])
    FOLLOW_18_in_rule1572 = frozenset([57])
    FOLLOW_57_in_rule1574 = frozenset([4, 34, 47, 48, 49, 53])
    FOLLOW_condition_in_rule1576 = frozenset([58])
    FOLLOW_58_in_rule1578 = frozenset([4, 34])
    FOLLOW_conclusion_in_rule1580 = frozenset([20, 59])
    FOLLOW_59_in_rule1583 = frozenset([8, 9])
    FOLLOW_weighting_factor_in_rule1585 = frozenset([20])
    FOLLOW_20_in_rule1591 = frozenset([1])
    FOLLOW_numeric_literal_in_weighting_factor1606 = frozenset([1])
    FOLLOW_Identifier_in_function_block_name1617 = frozenset([1])
    FOLLOW_Identifier_in_rule_block_name1625 = frozenset([1])
    FOLLOW_Identifier_in_term_name1633 = frozenset([1])
    FOLLOW_Identifier_in_f_variable_name1641 = frozenset([1])
    FOLLOW_Identifier_in_variable_name1649 = frozenset([1])
    FOLLOW_set_in_numeric_literal0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FCLLexer", FCLParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
