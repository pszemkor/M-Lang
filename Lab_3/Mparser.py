import ply.yacc as yacc

from Lab_3 import scanner
from Lab_3.AST import *

tokens = scanner.tokens
reserved = scanner.reserved
literals = scanner.literals

precedence = (
    ("left", '*', '/'),
    ("left", 'DOTMUL', 'DOTDIV'),
    ("left", '+', '-'),
    ("left", 'DOTADD', 'DOTSUB'),
    ("left", 'TRANSPOSE')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, scanner.find_tok_column(p),
                                                                                  p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""
    p[0] = Program(p[1])


def p_instructions_opt_1(p):
    """instructions_opt : instructions"""
    p[0] = InstructionsOpt(p[1])


def p_instructions_opt_2(p):
    """instructions_opt : """
    p[0] = InstructionsOpt("empty")


def p_instructions_1(p):
    """instructions : instruction instructions"""
    p[0] = Instructions(p[1], p[2])


def p_instructions_2(p):
    """instructions : instruction """
    p[0] = Instructions(p[1], None)


def p_instruction_1(p):
    """instruction : if_statement"""
    p[0] = Instruction(p[1])


def p_instruction_2(p):
    """instruction : assign ';'"""
    p[0] = Instruction(p[1])


def p_instruction_3(p):
    """instruction : loop"""
    p[0] = Instruction(p[1])


def p_instruction_4(p):
    """instruction : BREAK ';'"""
    p[0] = Instruction(Break, )


def p_instruction_5(p):
    """instruction : CONTINUE ';'"""
    p[0] = Instruction(Continue)


def p_instruction_6(p):
    """instruction : instruction_with_argument ';'"""
    p[0] = Instruction(p[1])


def p_instruction_7(p):
    """instruction_with_argument : PRINT printable"""
    p[0] = InstructionWithArg(p[1], p[2])


def p_instruction_8(p):
    """instruction_with_argument : RETURN EXPRESSION"""
    p[0] = InstructionWithArg(p[1], p[2])


def p_instruction_9(p):
    """instruction : '{' instructions '}'"""
    p[0] = Instruction(p[2])


def p_printable_1(p):
    """ printable : printable ',' EXPRESSION"""
    p[0] = Printable(p[1], p[3])


def p_printable_2(p):
    """printable : EXPRESSION"""
    p[0] = Printable(None, p[1])


def p_loop_1(p):
    """loop : WHILE '(' condition ')' instruction"""
    p[0] = Loop('WHILE', p[3], p[5])


def p_loop_2(p):
    """loop : FOR array_range instruction"""
    p[0] = Loop('FOR', p[2], p[3])


def p_array_range_1(p):
    """ array_range : id '=' int ':' id"""
    p[0] = ArrayRange(p[1], p[3], p[5])


def p_array_range_2(p):
    """ array_range : id '=' id ':' id"""
    p[0] = ArrayRange(p[1], p[3], p[5])


def p_array_range_3(p):
    """ array_range : id '=' id ':' int"""
    p[0] = ArrayRange(p[1], p[3], p[5])


def p_array_range_4(p):
    """ array_range : id '=' int ':' int"""
    p[0] = ArrayRange(p[1], p[3], p[5])


def p_if_statement_1(p):
    """if_statement : IF '(' condition ')' instruction"""
    p[0] = IfStatement(p[3], p[5], None)


def p_if_statement_2(p):
    """if_statement : IF '(' condition ')' instruction else_statement"""
    p[0] = IfStatement(p[3], p[5], p[6])


def p_else_statement(p):
    """else_statement : ELSE instruction """
    p[0] = ElseStatement(p[2])


def p_condition_1(p):
    """condition : EXPRESSION logical_operator EXPRESSION"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_condition_2(p):
    """condition : condition OR condition"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_condition_3(p):
    """condition : condition AND condition"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_logical_operator_1(p):
    """logical_operator : EQ"""
    p[0] = p[1]


def p_logical_operator_2(p):
    """logical_operator : '<'"""
    p[0] = p[1]


def p_logical_operator_3(p):
    """logical_operator : '>'"""
    p[0] = p[1]


def p_logical_operator_4(p):
    """logical_operator : GE"""
    p[0] = p[1]


def p_logical_operator_5(p):
    """logical_operator : LE"""
    p[0] = p[1]


def p_logical_operator_6(p):
    """logical_operator : NEQ"""
    p[0] = p[1]


def p_assign_1(p):
    """assign : id '=' EXPRESSION"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_assign_2(p):
    """assign : id ADDASSIGN string_expression"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_assign_3(p):
    """assign : id DIVASSIGN operable_expression"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_assign_4(p):
    """assign : id MULASSIGN operable_expression"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_assign_5(p):
    """assign : id ADDASSIGN operable_expression"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_assign_6(p):
    """assign : id SUBASSIGN operable_expression"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_assign_7(p):
    """assign : array_part '=' EXPRESSION"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_introw_1(p):
    """introw : introw ',' int"""
    p[0] = Introw(p[1], p[3])


def p_introw_2(p):
    """introw : int"""
    p[0] = p[1]


def p_expression_1(p):
    """EXPRESSION : operable_expression"""
    p[0] = p[1]


def p_expression_2(p):
    """EXPRESSION : string_expression"""
    p[0] = p[1]


def p_string_expression(p):
    """string_expression :  str '+' str """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_expression_3(p):
    """operable_expression : operable_expression '*' operable_expression """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_expression_4(p):
    """operable_expression : operable_expression '/' operable_expression """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_expression_5a(p):
    """array_part : id '[' introw ']'"""
    p[0] = ArrayPart(p[1], p[3])


def p_expression_6(p):
    """operable_expression : '(' operable_expression ')'"""
    p[0] = p[2]


def p_expression_7(p):
    """operable_expression : '-' operable_expression"""
    p[0] = UnaryExpression("-", p[1])


def p_expression_8(p):
    """operable_expression : operable_expression '+' operable_expression """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_expression_9(p):
    """operable_expression : operable_expression '-' operable_expression """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_m_expression_1(p):
    """operable_expression : EYE '(' int ')' """
    p[0] = Eye(p[3])


def p_m_expression_2(p):
    """operable_expression : ZEROS '(' int ')' """
    p[0] = Zeros(p[3])


def p_m_expression_3(p):
    """operable_expression : ONES '(' int ')' """
    p[0] = Ones(p[3])


def p_m_expression_4(p):
    """operable_expression : EYE '(' id ')' """
    p[0] = Eye(p[3])


def p_m_expression_5(p):
    """operable_expression : ZEROS '(' id ')' """
    p[0] = Zeros(p[3])


def p_m_expression_6(p):
    """operable_expression : ONES '(' id ')' """
    p[0] = Ones(p[3])


def p_m_expression_7(p):
    """operable_expression : operable_expression DOTADD operable_expression """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_m_expression_8(p):
    """operable_expression : operable_expression DOTSUB operable_expression """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_m_expression_9(p):
    """operable_expression : operable_expression DOTMUL operable_expression """
    p[0] = BinExpr(p[2], p[1], p[3])


def p_m_expression_10(p):
    """operable_expression : operable_expression DOTDIV operable_expression"""
    p[0] = BinExpr(p[2], p[1], p[3])


def p_m_expression_11(p):
    """operable_expression : operable_expression TRANSPOSE """
    p[0] = UnaryExpression('TRANSPOSE', p[1])


def p_create_matrix_1(p):
    """operable_expression : matrix """
    p[0] = p[1]


def p_create_matrix_1a(p):
    """operable_expression : vector """
    p[0] = p[1]


def p_create_vector(p):
    """vector : '[' row ']'"""
    p[0] = Vector(p[2])


def p_create_matrix_2(p):
    """operable_expression : f"""
    p[0] = p[1]


def p_create_matrix_3(p):
    """operable_expression : int"""
    p[0] = p[1]


def p_create_matrix(p):
    """operable_expression : id """
    p[0] = p[1]


def p_matrix(p):
    """matrix : '[' rows ']'"""
    p[0] = Matrix(p[2])


def p_rows_1(p):
    """rows : rows ';' row """
    p[0] = Rows(p[1], p[3])


def p_rows_2(p):
    """rows : row """
    p[0] = Rows(None, p[1])


def p_row_1(p):
    """row : row ',' EXPRESSION"""
    p[0] = Row(p[1], p[3])


def p_row_2(p):
    """row :  EXPRESSION """
    p[0] = Row(None, p[1])


def p_id_prod(p):
    """id : ID """
    p[0] = Variable(p[1])


def p_num_prod(p):
    """int : INTNUM """
    p[0] = IntNum(p[1])


def p_float_prod(p):
    """f : FLOAT """
    p[0] = FloatNum(p[1])


def p_str_prod(p):
    """str : STRING """
    p[0] = String(p[1])


parser = yacc.yacc()
