'''Module for the parsing on input data from .tia file.'''

# Provides:
#   readIn
#   dicOf

import numpy as np
from ..helpers import settings
from ..helpers.units import *
from ..helpers.tools import InputError

# these defs are for evaluation from input file
cos = np.cos
sin = np.sin
tan = np.tan
arcsin = np.arcsin
arccos = np.arccos
arctan = np.arctan
sqrt = np.sqrt
exp = np.exp

def readIn(name):
    '''Finds the input data in a file.

    Returns a list of tuples where tuple[0] identifies the object of which data
    has been found and tuple[1] the data itself. tuple[1] may be a simple value
    or a dictionary for constructors, etc.

    Example return value: [ ('bd', {'X': 0., 'Y': 0., 'Z': 1.}),    #constructor
                            ('LName', 'foo')]   #string data.

    name: file to read. [string]

    May raise an InputError.

    Returns a list of tuples.

    '''

    #error messages
    malformed = "Malformed input in %s, line %s. Could not %s '%s'"
    ans = []
    j = 0   #counts lines
    with open(name, 'r') as inF:
        for line in inF.readlines():
            j = j+1
            line = line.translate(None, ' ')  #no spaces nor tabs
            line = line.translate(None, '\t')
            if line.find('#') > -1:
                line = line[0:line.find('#')]   #no comments
            if len(line) < 2:
                continue
            elif line[0:5] == 'order':
                word = line[6:line.find('\n')]
                try:
                    ans.append(('order', int(eval(word))))
                except (SyntaxError, NameError):
                    raise InputError(malformed \
                                    %(fileName, str(j), 'parse', word) + ".")
                except TypeError:
                    raise InputError((malformed \
                                    %(fileName, str(j), 'cast', word)) \
                                    + "to int.")

            elif line[0:9] == 'threshold':
                word = line[10:line.find('\n')]
                try:
                    ans.append(('threshold', float(eval(word))))
                except (SyntaxError, NameError):
                    raise InputError(malformed \
                                    %(fileName, str(j), 'parse', word) + ".")
                except TypeError:
                    raise InputError((malformed \
                                    %(fileName, str(j), 'cast', word)) \
                                    + "to float.")

            elif line[0:2] == 'bm':
                ans.append(('bm',dicOf('bm',line[2:line.find('\n')],name,j)))
            elif line[0:2] == 'mr':
                ans.append(('mr',dicOf('mr',line[2:line.find('\n')],name,j)))
            elif line[0:2] == 'bs':
                ans.append(('bs',dicOf('bs',line[2:line.find('\n')],name,j)))
            elif line[0:2] == 'th':
                ans.append(('th',dicOf('th',line[2:line.find('\n')],name,j)))
            elif line[0:2] == 'tk':
                ans.append(('tk',dicOf('tk',line[2:line.find('\n')],name,j)))
            elif line[0:2] == 'bd':
                ans.append(('bd',dicOf('bd',line[2:line.find('\n')],name,j)))
            elif line[0:2] == 'gh':
                ans.append(('gh',dicOf('gh',line[2:line.find('\n')],name,j)))
            elif line[0:2] == 'bo':
                ans.append(('bo',dicOf('bo',line[2:line.find('\n')],name,j)))
            else:
                ans.append(('LName', line[0:line.find('\n')]))

    return ans

def dicOf(st, line, fileName, lineNumber):
    '''Extract the initializer dictionary from a line.

    st: object tag, 'bm', 'th', ... [string]
    line: line of data in .tia format (supposed no spaces nor tabs nor comments)
    and without the obect tag. [string]
    fileName: name of file (used to write errors). [string]
    lineNumber: number fo this line in the file (used to write errors). [int]

	May raise an InputError
	Returns a dictionary ready for construction.

    '''
    #error message
    malformed = "Malformed input in %s, line %s, entry %s"
    ans = {}

    #allow empty constructor
    if line == '':
        return ans

    words = line.split(',')
    i = 0
    while i < len(words):    #inputs without '='
        if '=' in words[i]:
            break
        try:
            ans[settings.inOrder[st][i]] = eval(words[i])
        except SyntaxError:
            raise InputError((malformed %(fileName, lineNumber, str(i+1)))\
                    + ". Could not parse '%s'." %words[i])
        except NameError:
            raise InputError((malformed %(fileName, lineNumber, str(i+1)))\
                    + ". Did not recognize reference in '%s'." %words[i])
        except IndexError:
            raise InputError((malformed %(fileName, lineNumber, str(i+1)))\
                    + ". To many arguments given.")
        i = i + 1

    while i < len(words):   #inputs with '='
        word = words[i]
        if word.find('=') == -1:
            raise InputError((malformed %(fileName, lineNumber, str(i+1)))\
                    + ". Found non explicit entry '%s' among explicit entries."\
                     %word)
        var = word[0:word.find('=')]
        if var not in settings.inOrder[st]:
            raise InputError((malformed %(fileName, lineNumber, str(i+1)))\
                    + ". Unknown constructor parameter '%s'." %var)
        val = word[word.find('=')+1:]
        try:
            ans[var] = eval(val)
        except SyntaxError:
            raise InputError((malformed %(fileName, lineNumber, str(i+1)))\
                    + ". Could not parse '%s'." %val)
        except NameError:
            raise InputError((malformed %(fileName, lineNumber, str(i+1)))\
                    + ". Did not recognize reference in '%s'." %val)
        i = i+1

    return ans
