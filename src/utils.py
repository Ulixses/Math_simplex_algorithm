#!/usr/bin/env python3

import sys

HELP_MESSAGE = """USAGE
\t./307multigrains n1 n2 n3 n4 po pw pc pb ps

DESCRIPTION
\t n1 \t number of tons of fertilizer F1
\t n2 \t number of tons of fertilizer F2
\t n3 \t number of tons of fertilizer F3
\t n4 \t number of tons of fertilizer F4
\t po \t price of one unit of oat
\t pw \t price of one unit of wheat
\t pc \t price of one unit of corn
\t pb \t price of one unit of barley
\t ps \t price of one unit of soy
"""

def help():
    return HELP_MESSAGE


def error(message):
    sys.stderr.write(message+'\n')
    sys.exit(84)