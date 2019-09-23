# $ANTLR 3.1.2 /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g 2012-10-19 23:25:12

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
                        
#docstring
__doc__ = """Lexer for reading FCL by the pyfuzzy package."""
__revision__ = "$ Id: FCL.g,v 1.7 2009/10/20 19:15:33 rliebscher Exp $"

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





# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
T__27=27
Real_literal=9
OR_=6
T__26=26
T__25=25
T__24=24
T__23=23
LETTER=10
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
T__33=33
WS=12
T__34=34
T__35=35
Integer_literal=8
T__36=36
T__37=37
T__38=38
T__39=39


class FCLLexer(Lexer):

    grammarFileName = "/work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "T__14"
    def mT__14(self, ):

        try:
            _type = T__14
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:30:7: ( 'FUNCTION_BLOCK' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:30:9: 'FUNCTION_BLOCK'
            pass 
            self.match("FUNCTION_BLOCK")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__14"



    # $ANTLR start "T__15"
    def mT__15(self, ):

        try:
            _type = T__15
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:31:7: ( 'END_FUNCTION_BLOCK' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:31:9: 'END_FUNCTION_BLOCK'
            pass 
            self.match("END_FUNCTION_BLOCK")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__15"



    # $ANTLR start "T__16"
    def mT__16(self, ):

        try:
            _type = T__16
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:32:7: ( 'STRUCT' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:32:9: 'STRUCT'
            pass 
            self.match("STRUCT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__16"



    # $ANTLR start "T__17"
    def mT__17(self, ):

        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:33:7: ( 'END_STRUCT' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:33:9: 'END_STRUCT'
            pass 
            self.match("END_STRUCT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__17"



    # $ANTLR start "T__18"
    def mT__18(self, ):

        try:
            _type = T__18
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:34:7: ( ':' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:34:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__18"



    # $ANTLR start "T__19"
    def mT__19(self, ):

        try:
            _type = T__19
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:35:7: ( 'REAL' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:35:9: 'REAL'
            pass 
            self.match("REAL")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__19"



    # $ANTLR start "T__20"
    def mT__20(self, ):

        try:
            _type = T__20
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:36:7: ( ';' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:36:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__20"



    # $ANTLR start "T__21"
    def mT__21(self, ):

        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:37:7: ( 'VAR_INPUT' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:37:9: 'VAR_INPUT'
            pass 
            self.match("VAR_INPUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__21"



    # $ANTLR start "T__22"
    def mT__22(self, ):

        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:38:7: ( 'END_VAR' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:38:9: 'END_VAR'
            pass 
            self.match("END_VAR")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):

        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:39:7: ( 'VAR_OUTPUT' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:39:9: 'VAR_OUTPUT'
            pass 
            self.match("VAR_OUTPUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):

        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:40:7: ( 'FUZZIFY' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:40:9: 'FUZZIFY'
            pass 
            self.match("FUZZIFY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__24"



    # $ANTLR start "T__25"
    def mT__25(self, ):

        try:
            _type = T__25
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:41:7: ( 'END_FUZZIFY' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:41:9: 'END_FUZZIFY'
            pass 
            self.match("END_FUZZIFY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__25"



    # $ANTLR start "T__26"
    def mT__26(self, ):

        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:42:7: ( 'DEFUZZIFY' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:42:9: 'DEFUZZIFY'
            pass 
            self.match("DEFUZZIFY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__26"



    # $ANTLR start "T__27"
    def mT__27(self, ):

        try:
            _type = T__27
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:43:7: ( 'END_DEFUZZIFY' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:43:9: 'END_DEFUZZIFY'
            pass 
            self.match("END_DEFUZZIFY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__27"



    # $ANTLR start "T__28"
    def mT__28(self, ):

        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:44:7: ( 'RULEBLOCK' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:44:9: 'RULEBLOCK'
            pass 
            self.match("RULEBLOCK")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__28"



    # $ANTLR start "T__29"
    def mT__29(self, ):

        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:45:7: ( 'END_RULEBLOCK' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:45:9: 'END_RULEBLOCK'
            pass 
            self.match("END_RULEBLOCK")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:46:7: ( 'OPTION' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:46:9: 'OPTION'
            pass 
            self.match("OPTION")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:47:7: ( 'END_OPTION' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:47:9: 'END_OPTION'
            pass 
            self.match("END_OPTION")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:48:7: ( 'TERM' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:48:9: 'TERM'
            pass 
            self.match("TERM")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):

        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:49:7: ( ':=' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:49:9: ':='
            pass 
            self.match(":=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:50:7: ( '(' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:50:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:51:7: ( ',' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:51:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:52:7: ( ')' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:52:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:53:7: ( 'METHOD' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:53:9: 'METHOD'
            pass 
            self.match("METHOD")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:54:7: ( 'DEFAULT' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:54:9: 'DEFAULT'
            pass 
            self.match("DEFAULT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__38"



    # $ANTLR start "T__39"
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:55:7: ( 'NC' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:55:9: 'NC'
            pass 
            self.match("NC")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__39"



    # $ANTLR start "T__40"
    def mT__40(self, ):

        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:56:7: ( 'RANGE' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:56:9: 'RANGE'
            pass 
            self.match("RANGE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__40"



    # $ANTLR start "T__41"
    def mT__41(self, ):

        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:57:7: ( '..' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:57:9: '..'
            pass 
            self.match("..")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__41"



    # $ANTLR start "T__42"
    def mT__42(self, ):

        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:58:7: ( '[' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:58:9: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__42"



    # $ANTLR start "T__43"
    def mT__43(self, ):

        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:59:7: ( ']' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:59:9: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__43"



    # $ANTLR start "T__44"
    def mT__44(self, ):

        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:60:7: ( 'MIN' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:60:9: 'MIN'
            pass 
            self.match("MIN")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__44"



    # $ANTLR start "T__45"
    def mT__45(self, ):

        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:61:7: ( 'PROD' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:61:9: 'PROD'
            pass 
            self.match("PROD")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__45"



    # $ANTLR start "T__46"
    def mT__46(self, ):

        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:62:7: ( 'BDIF' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:62:9: 'BDIF'
            pass 
            self.match("BDIF")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__46"



    # $ANTLR start "T__47"
    def mT__47(self, ):

        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:63:7: ( 'MAX' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:63:9: 'MAX'
            pass 
            self.match("MAX")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__47"



    # $ANTLR start "T__48"
    def mT__48(self, ):

        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:64:7: ( 'ASUM' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:64:9: 'ASUM'
            pass 
            self.match("ASUM")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__48"



    # $ANTLR start "T__49"
    def mT__49(self, ):

        try:
            _type = T__49
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:65:7: ( 'BSUM' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:65:9: 'BSUM'
            pass 
            self.match("BSUM")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__49"



    # $ANTLR start "T__50"
    def mT__50(self, ):

        try:
            _type = T__50
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:66:7: ( 'ACT' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:66:9: 'ACT'
            pass 
            self.match("ACT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__50"



    # $ANTLR start "T__51"
    def mT__51(self, ):

        try:
            _type = T__51
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:67:7: ( 'ACCU' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:67:9: 'ACCU'
            pass 
            self.match("ACCU")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__51"



    # $ANTLR start "T__52"
    def mT__52(self, ):

        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:68:7: ( 'NSUM' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:68:9: 'NSUM'
            pass 
            self.match("NSUM")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__52"



    # $ANTLR start "T__53"
    def mT__53(self, ):

        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:69:7: ( 'NOT' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:69:9: 'NOT'
            pass 
            self.match("NOT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__53"



    # $ANTLR start "T__54"
    def mT__54(self, ):

        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:70:7: ( 'IS' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:70:9: 'IS'
            pass 
            self.match("IS")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__54"



    # $ANTLR start "T__55"
    def mT__55(self, ):

        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:71:7: ( '.' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:71:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__55"



    # $ANTLR start "T__56"
    def mT__56(self, ):

        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:72:7: ( 'RULE' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:72:9: 'RULE'
            pass 
            self.match("RULE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__56"



    # $ANTLR start "T__57"
    def mT__57(self, ):

        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:73:7: ( 'IF' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:73:9: 'IF'
            pass 
            self.match("IF")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__57"



    # $ANTLR start "T__58"
    def mT__58(self, ):

        try:
            _type = T__58
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:74:7: ( 'THEN' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:74:9: 'THEN'
            pass 
            self.match("THEN")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__58"



    # $ANTLR start "T__59"
    def mT__59(self, ):

        try:
            _type = T__59
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:75:7: ( 'WITH' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:75:9: 'WITH'
            pass 
            self.match("WITH")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__59"



    # $ANTLR start "OR_"
    def mOR_(self, ):

        try:
            _type = OR_
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:373:6: ( 'OR' ( DIGIT )* )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:373:8: 'OR' ( DIGIT )*
            pass 
            self.match("OR")
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:373:13: ( DIGIT )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:373:13: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR_"



    # $ANTLR start "AND_"
    def mAND_(self, ):

        try:
            _type = AND_
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:374:6: ( 'AND' ( DIGIT )* )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:374:8: 'AND' ( DIGIT )*
            pass 
            self.match("AND")
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:374:14: ( DIGIT )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:374:14: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop2





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND_"



    # $ANTLR start "Identifier"
    def mIdentifier(self, ):

        try:
            _type = Identifier
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:510:12: ( LETTER ( LETTER | DIGIT )* )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:510:14: LETTER ( LETTER | DIGIT )*
            pass 
            self.mLETTER()
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:510:21: ( LETTER | DIGIT )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or LA3_0 == 95 or (97 <= LA3_0 <= 122)) :
                    alt3 = 1


                if alt3 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Identifier"



    # $ANTLR start "Integer_literal_wo_sign"
    def mInteger_literal_wo_sign(self, ):

        try:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:513:3: ( ( DIGIT )+ )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:513:5: ( DIGIT )+
            pass 
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:513:5: ( DIGIT )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57)) :
                    alt4 = 1


                if alt4 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:513:5: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1






        finally:

            pass

    # $ANTLR end "Integer_literal_wo_sign"



    # $ANTLR start "Integer_literal"
    def mInteger_literal(self, ):

        try:
            _type = Integer_literal
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:515:3: ( ( '+' | '-' )? Integer_literal_wo_sign )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:516:5: ( '+' | '-' )? Integer_literal_wo_sign
            pass 
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:516:5: ( '+' | '-' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 43 or LA5_0 == 45) :
                alt5 = 1
            if alt5 == 1:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            self.mInteger_literal_wo_sign()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Integer_literal"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:518:18: ( 'A' .. 'Z' | 'a' .. 'z' | '_' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:519:17: ( '0' .. '9' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:519:19: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "Real_literal"
    def mReal_literal(self, ):

        try:
            _type = Real_literal
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:522:3: ( Integer_literal '.' Integer_literal_wo_sign ( ( 'e' | 'E' ) Integer_literal )? )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:522:6: Integer_literal '.' Integer_literal_wo_sign ( ( 'e' | 'E' ) Integer_literal )?
            pass 
            self.mInteger_literal()
            self.match(46)
            self.mInteger_literal_wo_sign()
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:522:50: ( ( 'e' | 'E' ) Integer_literal )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 69 or LA6_0 == 101) :
                alt6 = 1
            if alt6 == 1:
                # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:522:51: ( 'e' | 'E' ) Integer_literal
                pass 
                if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                self.mInteger_literal()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "Real_literal"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:524:5: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:524:8: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel = HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:528:5: ( '(*' ( options {greedy=false; } : . )* '*)' )
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:528:9: '(*' ( options {greedy=false; } : . )* '*)'
            pass 
            self.match("(*")
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:528:14: ( options {greedy=false; } : . )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 42) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == 41) :
                        alt7 = 2
                    elif ((0 <= LA7_1 <= 40) or (42 <= LA7_1 <= 65535)) :
                        alt7 = 1


                elif ((0 <= LA7_0 <= 41) or (43 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:528:42: .
                    pass 
                    self.matchAny()


                else:
                    break #loop7


            self.match("*)")
            #action start
            _channel = HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    def mTokens(self):
        # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:8: ( T__14 | T__15 | T__16 | T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | OR_ | AND_ | Identifier | Integer_literal | Real_literal | WS | COMMENT )
        alt8 = 53
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:10: T__14
            pass 
            self.mT__14()


        elif alt8 == 2:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:16: T__15
            pass 
            self.mT__15()


        elif alt8 == 3:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:22: T__16
            pass 
            self.mT__16()


        elif alt8 == 4:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:28: T__17
            pass 
            self.mT__17()


        elif alt8 == 5:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:34: T__18
            pass 
            self.mT__18()


        elif alt8 == 6:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:40: T__19
            pass 
            self.mT__19()


        elif alt8 == 7:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:46: T__20
            pass 
            self.mT__20()


        elif alt8 == 8:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:52: T__21
            pass 
            self.mT__21()


        elif alt8 == 9:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:58: T__22
            pass 
            self.mT__22()


        elif alt8 == 10:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:64: T__23
            pass 
            self.mT__23()


        elif alt8 == 11:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:70: T__24
            pass 
            self.mT__24()


        elif alt8 == 12:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:76: T__25
            pass 
            self.mT__25()


        elif alt8 == 13:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:82: T__26
            pass 
            self.mT__26()


        elif alt8 == 14:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:88: T__27
            pass 
            self.mT__27()


        elif alt8 == 15:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:94: T__28
            pass 
            self.mT__28()


        elif alt8 == 16:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:100: T__29
            pass 
            self.mT__29()


        elif alt8 == 17:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:106: T__30
            pass 
            self.mT__30()


        elif alt8 == 18:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:112: T__31
            pass 
            self.mT__31()


        elif alt8 == 19:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:118: T__32
            pass 
            self.mT__32()


        elif alt8 == 20:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:124: T__33
            pass 
            self.mT__33()


        elif alt8 == 21:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:130: T__34
            pass 
            self.mT__34()


        elif alt8 == 22:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:136: T__35
            pass 
            self.mT__35()


        elif alt8 == 23:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:142: T__36
            pass 
            self.mT__36()


        elif alt8 == 24:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:148: T__37
            pass 
            self.mT__37()


        elif alt8 == 25:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:154: T__38
            pass 
            self.mT__38()


        elif alt8 == 26:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:160: T__39
            pass 
            self.mT__39()


        elif alt8 == 27:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:166: T__40
            pass 
            self.mT__40()


        elif alt8 == 28:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:172: T__41
            pass 
            self.mT__41()


        elif alt8 == 29:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:178: T__42
            pass 
            self.mT__42()


        elif alt8 == 30:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:184: T__43
            pass 
            self.mT__43()


        elif alt8 == 31:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:190: T__44
            pass 
            self.mT__44()


        elif alt8 == 32:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:196: T__45
            pass 
            self.mT__45()


        elif alt8 == 33:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:202: T__46
            pass 
            self.mT__46()


        elif alt8 == 34:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:208: T__47
            pass 
            self.mT__47()


        elif alt8 == 35:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:214: T__48
            pass 
            self.mT__48()


        elif alt8 == 36:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:220: T__49
            pass 
            self.mT__49()


        elif alt8 == 37:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:226: T__50
            pass 
            self.mT__50()


        elif alt8 == 38:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:232: T__51
            pass 
            self.mT__51()


        elif alt8 == 39:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:238: T__52
            pass 
            self.mT__52()


        elif alt8 == 40:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:244: T__53
            pass 
            self.mT__53()


        elif alt8 == 41:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:250: T__54
            pass 
            self.mT__54()


        elif alt8 == 42:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:256: T__55
            pass 
            self.mT__55()


        elif alt8 == 43:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:262: T__56
            pass 
            self.mT__56()


        elif alt8 == 44:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:268: T__57
            pass 
            self.mT__57()


        elif alt8 == 45:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:274: T__58
            pass 
            self.mT__58()


        elif alt8 == 46:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:280: T__59
            pass 
            self.mT__59()


        elif alt8 == 47:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:286: OR_
            pass 
            self.mOR_()


        elif alt8 == 48:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:290: AND_
            pass 
            self.mAND_()


        elif alt8 == 49:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:295: Identifier
            pass 
            self.mIdentifier()


        elif alt8 == 50:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:306: Integer_literal
            pass 
            self.mInteger_literal()


        elif alt8 == 51:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:322: Real_literal
            pass 
            self.mReal_literal()


        elif alt8 == 52:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:335: WS
            pass 
            self.mWS()


        elif alt8 == 53:
            # /work/projects/pyfuzzy/pyfuzzy/fuzzy/storage/fcl/FCL.g:1:338: COMMENT
            pass 
            self.mCOMMENT()







    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        "\1\uffff\3\30\1\40\1\30\1\uffff\4\30\1\53\2\uffff\2\30\1\63\2\uffff"
        "\5\30\2\uffff\1\75\1\uffff\3\30\2\uffff\6\30\1\111\2\30\2\uffff"
        "\3\30\1\120\2\30\2\uffff\6\30\1\132\1\133\1\30\2\uffff\12\30\1"
        "\uffff\1\111\3\30\1\153\1\154\1\uffff\1\30\1\156\4\30\1\163\1\30"
        "\1\165\2\uffff\5\30\1\u0081\1\u0083\5\30\1\u008a\1\u008b\1\30\2"
        "\uffff\1\u008d\1\uffff\1\u008e\1\u008f\1\u0090\1\u0091\1\uffff"
        "\1\u0092\1\uffff\1\165\1\u0093\11\30\1\uffff\1\30\1\uffff\1\u009e"
        "\5\30\2\uffff\1\30\7\uffff\10\30\1\u00ae\1\30\1\uffff\4\30\1\u00b4"
        "\1\u00b5\1\30\1\u00b7\3\30\1\u00bb\3\30\1\uffff\4\30\1\u00c3\2"
        "\uffff\1\30\1\uffff\3\30\1\uffff\7\30\1\uffff\7\30\1\u00d6\1\u00d7"
        "\1\30\1\u00d9\3\30\1\u00dd\2\30\1\u00e0\2\uffff\1\u00e1\1\uffff"
        "\2\30\1\u00e4\1\uffff\2\30\2\uffff\2\30\1\uffff\4\30\1\u00ed\1"
        "\u00ee\1\u00ef\1\30\3\uffff\3\30\1\u00f4\1\uffff"
        )

    DFA8_eof = DFA.unpack(
        "\u00f5\uffff"
        )

    DFA8_min = DFA.unpack(
        "\1\11\1\125\1\116\1\124\1\75\1\101\1\uffff\1\101\1\105\1\120\1"
        "\105\1\52\2\uffff\1\101\1\103\1\56\2\uffff\1\122\1\104\1\103\1"
        "\106\1\111\1\uffff\1\60\1\56\1\uffff\1\116\1\104\1\122\2\uffff"
        "\1\101\1\114\1\116\1\122\1\106\1\124\1\60\1\122\1\105\2\uffff\1"
        "\124\1\116\1\130\1\60\1\125\1\124\2\uffff\1\117\1\111\2\125\1\103"
        "\1\104\2\60\1\124\2\uffff\1\103\1\132\1\137\1\125\1\114\1\105\1"
        "\107\1\137\1\101\1\111\1\uffff\1\60\1\115\1\116\1\110\2\60\1\uffff"
        "\1\115\1\60\1\104\1\106\2\115\1\60\1\125\1\60\2\uffff\1\110\1\124"
        "\1\111\1\104\1\103\2\60\1\105\1\111\1\132\1\125\1\117\2\60\1\117"
        "\2\uffff\1\60\1\uffff\4\60\1\uffff\1\60\1\uffff\2\60\1\111\1\106"
        "\1\125\1\124\1\101\1\105\1\125\1\120\1\124\1\uffff\1\114\1\uffff"
        "\1\60\1\116\1\125\1\132\1\114\1\116\2\uffff\1\104\7\uffff\1\117"
        "\1\131\1\116\2\122\1\106\1\114\1\124\1\60\1\117\1\uffff\1\120\1"
        "\124\1\111\1\124\2\60\1\116\1\60\1\103\1\132\1\125\1\60\1\125\1"
        "\105\1\111\1\uffff\1\103\1\125\1\120\1\106\1\60\2\uffff\1\137\1"
        "\uffff\1\124\1\111\1\103\1\uffff\1\132\1\102\1\117\1\113\1\124"
        "\1\125\1\131\1\uffff\1\102\1\111\1\106\1\124\1\132\1\114\1\116"
        "\2\60\1\124\1\60\1\114\1\117\1\131\1\60\1\111\1\117\1\60\2\uffff"
        "\1\60\1\uffff\1\117\1\116\1\60\1\uffff\1\106\1\103\2\uffff\1\103"
        "\1\137\1\uffff\1\131\2\113\1\102\3\60\1\114\3\uffff\1\117\1\103"
        "\1\113\1\60\1\uffff"
        )

    DFA8_max = DFA.unpack(
        "\1\172\1\125\1\116\1\124\1\75\1\125\1\uffff\1\101\1\105\1\122\1"
        "\110\1\52\2\uffff\1\111\1\123\1\56\2\uffff\1\122\3\123\1\111\1"
        "\uffff\2\71\1\uffff\1\132\1\104\1\122\2\uffff\1\101\1\114\1\116"
        "\1\122\1\106\1\124\1\172\1\122\1\105\2\uffff\1\124\1\116\1\130"
        "\1\172\1\125\1\124\2\uffff\1\117\1\111\2\125\1\124\1\104\2\172"
        "\1\124\2\uffff\1\103\1\132\1\137\1\125\1\114\1\105\1\107\1\137"
        "\1\125\1\111\1\uffff\1\172\1\115\1\116\1\110\2\172\1\uffff\1\115"
        "\1\172\1\104\1\106\2\115\1\172\1\125\1\172\2\uffff\1\110\1\124"
        "\1\111\1\126\1\103\2\172\1\105\1\117\1\132\1\125\1\117\2\172\1"
        "\117\2\uffff\1\172\1\uffff\4\172\1\uffff\1\172\1\uffff\2\172\1"
        "\111\1\106\1\125\1\124\1\101\1\105\1\125\1\120\1\124\1\uffff\1"
        "\114\1\uffff\1\172\1\116\1\125\1\132\1\114\1\116\2\uffff\1\104"
        "\7\uffff\1\117\1\131\1\132\2\122\1\106\1\114\1\124\1\172\1\117"
        "\1\uffff\1\120\1\124\1\111\1\124\2\172\1\116\1\172\1\103\1\132"
        "\1\125\1\172\1\125\1\105\1\111\1\uffff\1\103\1\125\1\120\1\106"
        "\1\172\2\uffff\1\137\1\uffff\1\124\1\111\1\103\1\uffff\1\132\1"
        "\102\1\117\1\113\1\124\1\125\1\131\1\uffff\1\102\1\111\1\106\1"
        "\124\1\132\1\114\1\116\2\172\1\124\1\172\1\114\1\117\1\131\1\172"
        "\1\111\1\117\1\172\2\uffff\1\172\1\uffff\1\117\1\116\1\172\1\uffff"
        "\1\106\1\103\2\uffff\1\103\1\137\1\uffff\1\131\2\113\1\102\3\172"
        "\1\114\3\uffff\1\117\1\103\1\113\1\172\1\uffff"
        )

    DFA8_accept = DFA.unpack(
        "\6\uffff\1\7\5\uffff\1\26\1\27\3\uffff\1\35\1\36\5\uffff\1\61\2"
        "\uffff\1\64\3\uffff\1\24\1\5\11\uffff\1\65\1\25\6\uffff\1\34\1"
        "\52\11\uffff\1\62\1\63\12\uffff\1\57\6\uffff\1\32\11\uffff\1\51"
        "\1\54\17\uffff\1\37\1\42\1\uffff\1\50\4\uffff\1\45\1\uffff\1\60"
        "\13\uffff\1\6\1\uffff\1\53\6\uffff\1\23\1\55\1\uffff\1\47\1\40"
        "\1\41\1\44\1\43\1\46\1\56\12\uffff\1\33\17\uffff\1\3\5\uffff\1"
        "\21\1\30\1\uffff\1\13\3\uffff\1\11\7\uffff\1\31\22\uffff\1\17\1"
        "\10\1\uffff\1\15\3\uffff\1\4\2\uffff\1\22\1\12\2\uffff\1\14\10"
        "\uffff\1\16\1\20\1\1\4\uffff\1\2"
        )

    DFA8_special = DFA.unpack(
        "\u00f5\uffff"
        )

            
    DFA8_transition = [
        DFA.unpack("\2\33\1\uffff\2\33\22\uffff\1\33\7\uffff\1\13\1\15\1"
        "\uffff\1\31\1\14\1\31\1\20\1\uffff\12\32\1\4\1\6\5\uffff\1\25\1"
        "\24\1\30\1\10\1\2\1\1\2\30\1\26\3\30\1\16\1\17\1\11\1\23\1\30\1"
        "\5\1\3\1\12\1\30\1\7\1\27\3\30\1\21\1\uffff\1\22\1\uffff\1\30\1"
        "\uffff\32\30"),
        DFA.unpack("\1\34"),
        DFA.unpack("\1\35"),
        DFA.unpack("\1\36"),
        DFA.unpack("\1\37"),
        DFA.unpack("\1\43\3\uffff\1\41\17\uffff\1\42"),
        DFA.unpack(""),
        DFA.unpack("\1\44"),
        DFA.unpack("\1\45"),
        DFA.unpack("\1\46\1\uffff\1\47"),
        DFA.unpack("\1\50\2\uffff\1\51"),
        DFA.unpack("\1\52"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\56\3\uffff\1\54\3\uffff\1\55"),
        DFA.unpack("\1\57\13\uffff\1\61\3\uffff\1\60"),
        DFA.unpack("\1\62"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\64"),
        DFA.unpack("\1\65\16\uffff\1\66"),
        DFA.unpack("\1\70\12\uffff\1\71\4\uffff\1\67"),
        DFA.unpack("\1\73\14\uffff\1\72"),
        DFA.unpack("\1\74"),
        DFA.unpack(""),
        DFA.unpack("\12\32"),
        DFA.unpack("\1\76\1\uffff\12\32"),
        DFA.unpack(""),
        DFA.unpack("\1\77\13\uffff\1\100"),
        DFA.unpack("\1\101"),
        DFA.unpack("\1\102"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\103"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack("\1\106"),
        DFA.unpack("\1\107"),
        DFA.unpack("\1\110"),
        DFA.unpack("\12\112\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\121"),
        DFA.unpack("\1\122"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\123"),
        DFA.unpack("\1\124"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\130\20\uffff\1\127"),
        DFA.unpack("\1\131"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\134"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack("\1\146\23\uffff\1\145"),
        DFA.unpack("\1\147"),
        DFA.unpack(""),
        DFA.unpack("\12\112\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\150"),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack("\1\155"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\157"),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\161"),
        DFA.unpack("\1\162"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\164"),
        DFA.unpack("\12\166\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\175\1\uffff\1\172\10\uffff\1\177\2\uffff\1\176\1"
        "\173\2\uffff\1\174"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\1\30\1\u0082\30\30\4\uffff\1\30\1\uffff"
        "\32\30"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\1\u0085\5\uffff\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u008c"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack("\12\166\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u0094"),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\1\u0098"),
        DFA.unpack("\1\u0099"),
        DFA.unpack("\1\u009a"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009c"),
        DFA.unpack(""),
        DFA.unpack("\1\u009d"),
        DFA.unpack(""),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u009f"),
        DFA.unpack("\1\u00a0"),
        DFA.unpack("\1\u00a1"),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\1\u00a3"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00a4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\1\u00a7\13\uffff\1\u00a8"),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\1\u00ad"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00af"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b0"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack("\1\u00b2"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00b8"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack(""),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\1\u00c0"),
        DFA.unpack("\1\u00c1"),
        DFA.unpack("\1\u00c2"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00c4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\1\u00c6"),
        DFA.unpack("\1\u00c7"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\u00cb"),
        DFA.unpack("\1\u00cc"),
        DFA.unpack("\1\u00cd"),
        DFA.unpack("\1\u00ce"),
        DFA.unpack(""),
        DFA.unpack("\1\u00cf"),
        DFA.unpack("\1\u00d0"),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack("\1\u00d3"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack("\1\u00d5"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00d8"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e2"),
        DFA.unpack("\1\u00e3"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e5"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00e7"),
        DFA.unpack("\1\u00e8"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e9"),
        DFA.unpack("\1\u00ea"),
        DFA.unpack("\1\u00eb"),
        DFA.unpack("\1\u00ec"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("\1\u00f0"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f1"),
        DFA.unpack("\1\u00f2"),
        DFA.unpack("\1\u00f3"),
        DFA.unpack("\12\30\7\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack("")
    ]

    # class definition for DFA #8

    DFA8 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(FCLLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
