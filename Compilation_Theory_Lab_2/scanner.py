import ply.lex as lex

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

tokens = ['DIVASSIGN', 'ADDASSIGN', 'MULASSIGN', 'SUBASSIGN', 'STRING', 'FLOAT', 'INTNUM',
          'GE', 'LE', 'EQ', 'NEQ', 'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 'ID'] \
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
t_ignore = '  \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_FLOAT(t):
    r'[0-9]*(\.[0-9]|[0-9]\.)[0-9]*([eE][-+]?[0-9]+)?'
    t.value = float(t.value)
    return t


def t_comment(t):
    r"\#.*"
    # t.lexer.lineno += 1


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print('Illegal character: ', t.value[0], 'at', t.lexer.lineno, 'line')
    t.lexer.skip(1)


def t_STRING(t):
    r'"[^"]*"'
    return t


lexer = lex.lex()
# fh = open('code.txt', "r")
# lexer.input(fh.read())
# for token in lexer:
#     print("line %d: %s(%s)" % (token.lineno, token.type, token.value))