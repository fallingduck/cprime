#!/usr/bin/env python3


import re
import sys


def strip_comments(code):
    singleline = re.compile(r'\n?\s*\/{2}.*?\n')
    multiline  = re.compile(r'\/\*.*?\*\/', re.DOTALL)  # In C99, comments
                                                        # don't nest!
    code = singleline.sub('\n', code)
    code = multiline.sub('', code)
    return code


def main(filepath):
    with open(filepath, 'r') as fp:
        code = fp.read()
    code = strip_comments(code).split('\n')
    newcode = []
    print('\n'.join(newcode))


if __name__ == '__main__':
    infile = sys.argv[1]
    main(infile)
