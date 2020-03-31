import scanner
import ply.yacc as yacc

tokens = scanner.tokens
reserved = scanner.reserved
literals = scanner.literals

precedence = (
    ("left", '*', '/'),
    ("left", '+', '-')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, scanner.find_tok_column(p),
                                                                                  p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""
    p[0] = tuple(p)


def p_instructions_opt_1(p):
    """instructions_opt : instructions"""
    p[0] = tuple(p)


def p_instructions_opt_2(p):
    """instructions_opt : """
    p[0] = tuple(p)


def p_instructions_1(p):
    """instructions : instruction instructions"""
    p[0] = tuple(p[1:])
    print("**************", p[1], p[2])


def p_instructions_2(p):
    """instructions : instruction """
    p[0] = tuple(p[1:])


def p_instruction_1(p):
    """instruction : if_statement
                   | assign ';'
                   | loop
                   | PRINT printable ';'
                   | BREAK ';'
                   | CONTINUE ';'
                   | RETURN EXPRESSION ';'
                   | '{' instructions '}'"""
    p[0] = tuple(p[1:])


def p_printable(p):
    """ printable : EXPRESSION
                 | printable ',' EXPRESSION
                 | STRING"""
    p[0] = tuple(p[1:])


def p_loop_1(p):
    """loop : WHILE '(' condition ')' instruction
            | WHILE '(' condition ')' '{' instructions '}'
            | FOR array_range instruction
            | FOR array_range '{' instructions '}' """
    p[0] = tuple(p[1:])


def p_array_range(p):
    """ array_range : ID '=' INTNUM ':' ID
                    | ID '=' ID ':' ID
                    | ID '=' INTNUM ':' INTNUM"""
    p[0] = tuple(p[1:])


def p_if_statement_1(p):
    """if_statement : IF '(' condition ')' '{' instructions '}' else_statement """
    p[0] = tuple(p[1:])


def p_if_statement_2(p):
    """if_statement : IF '(' condition ')' instruction else_statement"""
    p[0] = tuple(p[1:])


def p_else_statement(p):
    """else_statement : ELSE '{' instructions '}'
                      | ELSE instruction
                      | """
    p[0] = tuple(p[1:])


def p_condition(p):
    """condition : EXPRESSION logical_operator EXPRESSION
                 | condition OR condition
                 | condition AND condition"""
    p[0] = ('cond', p[1], p[2], p[3])


def p_logical_operator(p):
    """logical_operator : EQ
                        | '<'
                        | '>'
                        | GE
                        | LE
                        | NEQ"""
    p[0] = tuple(p[1:])


def p_assign_1(p):
    """assign : ID '=' EXPRESSION
              | ID ADDASSIGN EXPRESSION
              | ID ADDASSIGN STRING
              | ID '=' STRING '+' STRING
              | ID SUBASSIGN EXPRESSION
              | ID DIVASSIGN EXPRESSION
              | ID MULASSIGN EXPRESSION
              | ID '=' '-' ID
              | ID '=' '-' INTNUM
              | ID '=' '-' FLOAT
              | ID '=' '-' '[' rows ']'
              | ID '=' '-' ID '[' introw ']'
              | ID '='  ID "'"
              | ID '=' '[' rows ']'
              | ID '[' introw ']' '=' EXPRESSION
              """
    p[0] = tuple(p[1:])



def p_introw_1(p):
    """introw : introw ',' INTNUM
              | INTNUM"""
    p[0] = tuple(p[1:])


def p_rows_1(p):
    """rows : rows ';' row
            | row"""
    p[0] = tuple(p[1:])


def p_row_1(p):
    """row : row ',' EXPRESSION
           | EXPRESSION"""
    p[0] = tuple(p[1:])


def p_expression_1(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION
                  | EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION
                  | ID DOTADD EXPRESSION
                  | ID DOTSUB EXPRESSION
                  | ID DOTMUL EXPRESSION
                  | ID DOTDIV EXPRESSION """
    p[0] = ('binop', p[1], p[2], p[3])


def p_expression_2(p):
    """EXPRESSION : '-' EXPRESSION
                  | ID
                  | FLOAT
                  | ID '[' introw ']'
                  | '[' rows ']'
                  | INTNUM
                  | EYE '(' INTNUM ')'
                  | ZEROS '(' INTNUM ')'
                  | ONES '(' INTNUM ')'
                  | EYE '(' ID ')'
                  | ZEROS '(' ID ')'
                  | ONES '(' ID ')'
                  | EXPRESSION "'"
                  | '(' EXPRESSION ')'"""
    p[0] = tuple(p[1:])


parser = yacc.yacc()
