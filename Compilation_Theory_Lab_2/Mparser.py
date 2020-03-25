from lab2 import scanner
import ply.yacc as yacc

tokens = scanner.tokens
reserved = scanner.reserved
literals = ['+', '-', '*', '/', '(', ')']


#
# precedence = (
#     # to fill ...
#     ("left", '+', '-'),
#     ("left", '*', '/')
#     # to fill ...
# )


def p_error(p):
    # scanner.find_tok_column(p)
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, "col",
                                                                                  p.type, p.value))
    else:
        print("Unexpected end of input")

def p_program(p):
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """


def p_instruction_1(p):
    """instruction : if_statement"""


def p_if_statement(p):
    """if_statement : IF '(' condition ')' '{' instructions '}'  """


def p_condition(p):
    """condition : variable logical_operator variable """


def p_logical_operator(p):
    """logical_operator : EQ
                        | '<'
                        | '>'
                        | GE
                        | LE """


def p_variable(p):
    """variable : INTNUM
                | ID"""


def p_instruction_3(p):
    """
  instruction : assign
  """


def p_assign_1(p):
    """assign : ID '=' INTNUM
              | ID '=' ID
              | ID '=' EXPRESSION"""


def p_expression_1(p):
    """EXPRESSION : INTNUM '+' INTNUM"""


    # to finish the grammar
    # ....


parser = yacc.yacc()
