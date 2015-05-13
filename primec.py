#!/usr/bin/env python3


import re
import sys


singleline  = re.compile(r'\n?\s*\/{2}.*?\n')
multiline   = re.compile(r'\/\*.*?\*\/', re.DOTALL)  # In C99, comments
                                                     # don't nest!

preprocess  = re.compile(r'^\s*#')
include     = re.compile(r'^(\s*)include(\s)')

indentation = re.compile(r'^(\s*)\S')

case        = re.compile(r'^\s*case.*?:$')
onelinecase = re.compile(r'^\s*case.*?:.+$')
startindent = re.compile(r':$')


def strip_comments(code):
    code = singleline.sub('\n', code)
    code = multiline.sub('', code)
    return code


def firstpass(code):
    """First pass through: broader scope"""
    newcode = []
    indent = 0
    indents = []
    blocksarecase = [False]
    for line in code:
        line = line.rstrip()
        newindent = indentation.search(line).group(1)
        oldindent = ''.join(indents)

        if preprocess.search(line):
            newcode.append(line)
            continue

        if include.search(line):
            line = include.sub(r'\g<1>#include\g<2>', count=1)
            newcode.append(line)
            continue

        if len(indents) < indent:
            if len(newindent) > oldindent:
                indents.append(newindent[len(oldindent):])
                if not blocksarecase[-1]:
                    newcode.append('{0}{{'.format(oldindent))
                oldindent = ''.join(indents)
            else:
                raise RuntimeError('Expected indent!')

        if len(newindent) != len(oldindent):
            if newindent == ''.join(indents[:-1]):
                indent -= 1
                indents.pop()
                if blocksarecase[-1]:
                    newcode.append('{0}break;'.format(oldindent))
                else:
                    newcode.append('{0}}}'.format(newindent))
                blocksarecase.pop()
            else:
                raise RuntimeError('Indentation mismatch!')

        if onelinecase.search(line):
            line = '{0}; break;'.format(line)
            newcode.append(line)
            continue

        if case.search(line):
            newcode.append(line)
            indent += 1
            blocksarecase.append(True)
            continue

        if startindent.search(line):
            line = startindent.sub('')
            indent += 1
            blocksarecase.append(False)

    return '\n'.join(newcode)


def main(filepath):
    with open(filepath, 'r') as fp:
        code = fp.read()
    code = strip_comments(code).split('\n')
    newcode = firstpass(code)
    print(newcode)


if __name__ == '__main__':
    infile = sys.argv[1]
    main(infile)
