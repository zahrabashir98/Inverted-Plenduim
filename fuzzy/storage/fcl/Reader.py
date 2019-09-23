#!/usr/bin/env python
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
"""Load a fuzzy system from FCL file, stream or string."""

__revision__ = "$Id: Reader.py,v 1.6 2013-01-09 20:10:19 rliebscher Exp $"

# antlr3 uses sys.maxint which is removed in python3
import sys
try:
    sys.maxint
except:
    sys.maxint = sys.maxsize

import antlr3

try:
    from fuzzy.storage.fcl.FCLLexer import FCLLexer
except:
    from fuzzy.storage.fcl.FCLLexer3 import FCLLexer
from fuzzy.storage.fcl.FCLParser import FCLParser

class Reader(object):
    """Parses a FCL file to a fuzzy.System.System instance"""

    def __load(self, char_stream):
        """Common part of load methods."""
        lexer = FCLLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = FCLParser(tokens)
        return parser.main()

    def load_from_file(self, filename):
        """Load a fuzzy system from FCL file."""
        encoding = None
        f = None
        try:
            # read first line
            f = open(filename)
            line = f.readline()
            import re
            # check for coding
            result = re.search(r'coding[=:]\s*([-\w.]+)', line)
            if result:
                # found one and use it
                encoding = result.group(1)
        except:
            # ok, then try without encoding
            pass
        if f:
            f.close()
        return self.__load(antlr3.ANTLRFileStream(filename, encoding))

    def load_from_stream(self, stream):
        """Load a fuzzy system from FCL stream."""
        return self.__load(antlr3.ANTLRInputStream(stream))

    def load_from_string(self, str):
        """Load a fuzzy system from FCL string."""
        return self.__load(antlr3.ANTLRStringStream(str))

