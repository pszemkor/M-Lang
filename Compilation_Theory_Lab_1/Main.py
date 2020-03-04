import ply.lex as lex
import sys

literals = "+-*/()=<>:;',[]{}"

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}

print(list(reserved.values()))
tokens = ['DIVASSIGN', 'ADDASSIGN', 'MULASSIGN', 'SUBASSIGN',
          'GE', 'LE', 'EQ', 'NEQ', 'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 'INTNUM', 'ID'] \
         + list(reserved.values())

t_DIVASSIGN = r'/='
t_ADDASSIGN = r'\+='
t_MULASSIGN = r'\*='
t_SUBASSIGN = r'-='
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NEQ = r'!='
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_INTNUM = r'\d+'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


t_ignore = '  \t'


def t_comment(t):
    r"\#.*"
    # t.lexer.lineno += 1


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
fh = open('code.txt', "r")
lexer.input(fh.read())
for token in lexer:
    print("line %d: %s(%s)" % (token.lineno, token.type, token.value))
