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
    p[0] = ('program', p[1])


def p_instructions_opt_1(p):
    """instructions_opt : instructions"""
    p[0] = ('instructions_opt', p[1])


def p_instructions_opt_2(p):
    """instructions_opt : """
    p[0] = "empty"


def p_instructions_1(p):
    """instructions : instruction instructions"""
    p[0] = (p[1], p[2])


def p_instructions_2(p):
    """instructions : instruction """
    p[0] = (p[1])


def p_instruction_1(p):
    """instruction : if_statement
                   | assign ';'
                   | loop
                   | BREAK ';'
                   | CONTINUE ';'"""
    p[0] = (p[1])


def p_instruction_2(p):
    """instruction : PRINT printable ';'
                   | RETURN EXPRESSION ';'"""
    p[0] = (p[1], p[2])


def p_instruction_3(p):
    """instruction : '{' instructions '}'"""
    p[0] = (p[2])


def p_printable_1(p):
    """ printable : EXPRESSION
                 | STRING"""
    p[0] = (p[1])


def p_printable_2(p):
    """ printable : printable ',' EXPRESSION"""
    p[0] = ('printable', p[1], p[3])


def p_loop_1(p):
    """loop : WHILE '(' condition ')' instruction"""
    p[0] = ('while_loop', p[3], p[5])


def p_loop_2(p):
    """loop : FOR array_range instruction"""
    p[0] = ('for_loop', p[2], p[3])


def p_array_range(p):
    """ array_range : ID '=' INTNUM ':' ID
                    | ID '=' ID ':' ID
                    | ID '=' INTNUM ':' INTNUM"""
    p[0] = ('array_range', p[1], 'from', p[3], 'to', p[5])


def p_if_statement_1(p):
    """if_statement : IF '(' condition ')' instruction"""
    p[0] = ('if', p[3], p[5])


def p_if_statement_2(p):
    """if_statement : IF '(' condition ')' instruction else_statement"""
    p[0] = ('if', p[3], p[5], p[6])


def p_else_statement(p):
    """else_statement : ELSE instruction """
    p[0] = ('else', p[2])


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
    p[0] = ('logical_op', p[1])


def p_assign_1(p):
    """assign : ID '=' EXPRESSION
              | ID ADDASSIGN STRING
              | ID DIVASSIGN EXPRESSION
              | ID SUBASSIGN EXPRESSION
              | ID MULASSIGN EXPRESSION
              | ID ADDASSIGN EXPRESSION
              """
    p[0] = ('assign', p[1], p[2], p[3])


def p_assign_2(p):
    """assign : ID '=' STRING '+' STRING
              | ID '[' introw ']' '=' EXPRESSION"""
    p[0] = ('assign', p[1:])


def p_introw_1(p):
    """introw : introw ',' INTNUM
              | INTNUM"""
    if len(p) == 4:
        p[0] = ('introw', p[1], p[3])
    else:
        p[0] = p[1]


def p_expression_1(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION
                  | EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION """
    p[0] = ('binop', p[1], p[2], p[3])


def p_expression_4(p):
    """EXPRESSION : ID '[' introw ']'
                  | '(' EXPRESSION ')'"""
    if len(p) == 5:
        p[0] = ('array_part', p[1], p[3])
    else:
        p[0] = p[2]


def p_expression_5(p):
    """EXPRESSION : '-' EXPRESSION"""
    p[0] = ('negative', p[2])


def p_expression_6(p):
    """EXPRESSION : matrix_expression
                  | numeric_expression"""
    p[0] = p[1]


def p_n_expression_1(p):
    """numeric_expression : ID
                          | FLOAT
                          | INTNUM """
    p[0] = ('var', p[1])


def p_m_expression_1(p):
    """matrix_expression : EYE '(' INTNUM ')'
                  | ZEROS '(' INTNUM ')'
                  | ONES '(' INTNUM ')'
                  | EYE '(' ID ')'
                  | ZEROS '(' ID ')'
                  | ONES '(' ID ')'"""
    p[0] = ('matrix_creation', p[1], p[3])


def p_m_expression_2(p):
    """matrix_expression : matrix_expression DOTADD matrix_expression
                         | matrix_expression DOTSUB matrix_expression
                         | matrix_expression DOTMUL matrix_expression
                         | matrix_expression DOTDIV matrix_expression """
    p[0] = ('matrix_op', p[1], p[2], p[3])


def p_m_expression_3(p):
    """matrix_expression : matrix_expression "'" """
    p[0] = ('transpose', p[1])


def p_create_matrix(p):
    """matrix_expression : matrix
                         | ID"""
    p[0] = p[1]


def p_matrix(p):
    """matrix : '[' rows ']'"""
    p[0] = ('matrix', p[1], p[2], p[3])


def p_rows_1(p):
    """rows : rows ';' row
            | row"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])


def p_row_1(p):
    """row : row ',' EXPRESSION
           | EXPRESSION"""
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]


parser = yacc.yacc()
