#!/usr/bin/env python3


import re
import sys


escapednewline  = re.compile(r'\\\n')

singlecomment   = re.compile(r'\n?\s*\/{2}.*?\n')
multicomment    = re.compile(r'\/\*.*?\*\/', re.DOTALL)

preprocess      = re.compile(r'^\s*#')
include         = re.compile(r'^(\s*)include(\s)')
cprimeinclude   = re.compile(r'^(\s*)include\s+"(.+?)\.(h|c)pr"$')

indentation     = re.compile(r'^(\s*)\S')
blankline       = re.compile(r'^\s*$')

case            = re.compile(r'^\s*(case|default).*?:$')
onelinecase     = re.compile(r'^\s*(case|default).*?:.+$')
startindent     = re.compile(r':$')
reqsemicolon    = re.compile(r'^\s*(struct|enum|union).*?:$')

andkeyword      = re.compile(r'"[^"]+"|(\sand\s)')
andsub          = lambda m: ' && ' if m.group(1) else m.group(0)
orkeyword       = re.compile(r'"[^"]+"|(\sor\s)')
orsub           = lambda m: ' || ' if m.group(1) else m.group(0)

parenkeyword    = re.compile(r'"[^"]+"|(\s*while\s+|\s*if\s+|\s*switch\s+)([^\(].*?)(:|$)')
parensub        = lambda m: '{0}({1}){2}'.format(m.group(1), m.group(2), m.group(3)) if m.group(1) else m.group(0)

singlelineblock = re.compile(r'"[^"]+"|:(.+)$')
slbsub          = lambda m: ' {{{0} }}'.format(m.group(1)) if m.group(1) else m.group(0)

voidfunction    = re.compile(r'"[^"]+"|(\(\):)')
voidsub         = lambda m: '(void):' if m.group(1) else m.group(0)

def strip_comments(code):
    code = singlecomment.sub('\n', code)
    code = multicomment.sub('', code)
    return code.rstrip()


def parse_line(line):
    """This mostly focuses on adding in parentheses where required, adding
    semicolons where required, and converting keywords like `and`, `or`, and
    `not` to their respective C operators.
    """

    line = voidfunction.sub(voidsub, line)

    if onelinecase.search(line):
        line = '{0}; break'.format(line)

    line = parenkeyword.sub(parensub, line)

    if case.search(line):
        pass
    elif startindent.search(line):
        line = startindent.sub('', line)
    else:
        line = '{0};'.format(line)

    if not onelinecase.search(line):
        line = singlelineblock.sub(slbsub, line)

    line = andkeyword.sub(andsub, line)
    line = orkeyword.sub(orsub, line)

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


def main(infile, outfile=None):
    with open(infile, 'r') as fp:
        code = fp.read()
    code = strip_comments(code)
    code = escapednewline.sub(' ', code)
    code = code.split('\n')
    includes = []
    included = []  # List of hashes, so we only include anything once
    output = transpile(code, includes)
    if outfile is None:
        outfile = re.sub(r'^(.+?)(\.\w+)?$', '\g<1>.c', infile)
    with open(outfile, 'w') as fp:
        fp.write(output)


if __name__ == '__main__':
    infile = sys.argv[1]
    main(infile)
