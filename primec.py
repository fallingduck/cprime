#!/usr/bin/env python3


import re
import sys


escapednewline = re.compile(r'\\\n')

singleline     = re.compile(r'\n?\s*\/{2}.*?\n')
multiline      = re.compile(r'\/\*.*?\*\/', re.DOTALL) # In C99, comments
                                                       # don't nest!

preprocess     = re.compile(r'^\s*#')
include        = re.compile(r'^(\s*)include(\s)')
cprimeinclude  = re.compile(r'^(\s*)include\s+"(.+?)\.hpr"$')

indentation    = re.compile(r'^(\s*)\S')
blankline      = re.compile(r'^\s*$')

case           = re.compile(r'^\s*(case|default).*?:$')
onelinecase    = re.compile(r'^\s*(case|default).*?:.+$')
startindent    = re.compile(r':$')
reqsemicolon   = re.compile(r'^\s*(struct|enum).*?:$')

strings        = re.compile(r'".*?[^\\]"')


def strip_comments(code):
    code = singleline.sub('\n', code)
    code = multiline.sub('', code)
    return code.rstrip()


def parse_line(line):
    """This mostly focusses on adding in parentheses where required, adding
    semicolons where required, and converting keywords like `and`, `or`, and
    `not` to their respective C operators.
    """

    if onelinecase.search(line):
        line = '{0}; break;'.format(line)

    return line


def transpile(code, includes):
    """First pass through: broader scope"""
    newcode = []
    indent = 0
    indents = []
    blocksarecase = [False]
    blockrequiressemicolon = [False]
    for line in code:
        if blankline.search(line):
            continue

        line = line.rstrip()
        newindent = indentation.search(line)
        newindent = newindent.group(1) if newindent else ''
        oldindent = ''.join(indents)

        if preprocess.search(line):
            newcode.append(line)
            continue

        match = cprimeinclude.search(line)
        if match:
            line = cprimeinclude.sub(r'\g<1>#include "\g<2>.h"', line)
            newcode.append(line)
            includes.append('{0}.hpr'.format(match.group(2)))
            continue

        if include.search(line):
            line = include.sub(r'\g<1>#include\g<2>', line, count=1)
            newcode.append(line)
            continue

        if len(indents) < indent:
            if len(newindent) > len(oldindent):
                indents.append(newindent[len(oldindent):])
                if not blocksarecase[-1]:
                    newcode.append('{0}{{'.format(oldindent))
                oldindent = ''.join(indents)
            else:
                print(line)
                raise RuntimeError('Expected indent!')

        while len(newindent) != len(oldindent):
            if newindent == ''.join(indents[:-1]):
                indent -= 1
                indents.pop()
                if blocksarecase[-1]:
                    newcode.append('{0}break;'.format(oldindent))
                else:
                    newcode.append('{0}}}{1}'.format(newindent,
                        ';' if blockrequiressemicolon[-1] else ''))
                blocksarecase.pop()
                blockrequiressemicolon.pop()
                break
            elif len(newindent) < len(oldindent):
                indent -= 1
                indents.pop()
                if blocksarecase[-1]:
                    newcode.append('{0}break;'.format(oldindent))
                else:
                    newcode.append('{0}}}{1}'.format(''.join(indents),
                        ';' if blockrequiressemicolon[-1] else ''))
                blocksarecase.pop()
                blockrequiressemicolon.pop()
                newindent = indentation.search(line)
                newindent = newindent.group(1) if newindent else ''
                oldindent = ''.join(indents)
            else:
                print(line)
                raise RuntimeError('Indentation mismatch!')

        if startindent.search(line):
            indent += 1
            blocksarecase.append(case.search(line))
            blockrequiressemicolon.append(reqsemicolon.search(line))

        line = parse_line(line)
        newcode.append(line)

    while indent:
        if blocksarecase[-1]:
            newcode.append('{0}break;'.format(''.join(indents)))
        else:
            newcode.append('{0}}}'.format(''.join(indents[:-1])))
        blocksarecase.pop()
        indent -= 1
        indents.pop()

    return '\n'.join(newcode)


def main(filepath):
    with open(filepath, 'r') as fp:
        code = fp.read()
    code = strip_comments(code)
    code = escapednewline.sub(' ', code)
    code = code.split('\n')
    includes = []
    included = []  # List of hashes, so we only include anything once
    newcode = transpile(code, includes)
    print(newcode)


if __name__ == '__main__':
    infile = sys.argv[1]
    main(infile)
