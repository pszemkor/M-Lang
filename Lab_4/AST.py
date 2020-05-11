class Node(object):
    pass


class IntNum(Node):
    def __init__(self, value):
        self.type = 'INTNUM'
        self.value = value


class FloatNum(Node):

    def __init__(self, value):
        self.type = 'FLOATNUM'
        self.value = value


class Tuple(Node):
    def __init__(self):
        self.type = 'TUPLE'
        pass


class Variable(Node):
    def __init__(self, name):
        self.type = 'VARIABLE'
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.type = 'BIN_EXPR'
        self.op = op
        self.left = left
        self.right = right


class Program(Node):
    def __init__(self, instructions_opt):
        self.type = 'PROGRAM'
        self.instructions_opt = instructions_opt


class InstructionsOpt(Node):
    def __init__(self, instructions):
        self.type = 'INSTRUCTIONS_OPT'
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instruction, isntructions):
        self.type = 'INSTRUCTIONS'
        self.instruction = instruction
        self.instructions = isntructions


class Instruction(Node):
    def __init__(self, instruction):
        self.type = 'INSTRUCTION'
        self.instruction = instruction


class InstructionWithArg(Node):
    def __init__(self, op, expr):
        self.type = 'INSTRUCTION_WITH_ARG'
        self.op = op
        self.expr = expr


class Printable(Node):
    def __init__(self, printable, expression):
        self.type = 'PRINTABLE'
        self.printable = printable
        self.expression = expression


class Loop(Node):
    def __init__(self, loop, condition, instruction):
        self.type = 'LOOP'
        self.loop = loop
        self.condition = condition
        self.instruction = instruction


class ArrayRange(Node):
    def __init__(self, counter, beginning, end):
        self.type = 'ARRAY_RANGE'
        self.counter = counter
        self.beginning = beginning
        self.end = end


class IfStatement(Node):
    def __init__(self, condition, instruction, elseStatement):
        self.type = 'IF_STATEMENT'
        self.condition = condition
        self.instruction = instruction
        self.elseStatement = elseStatement


class ElseStatement(Node):
    def __init__(self, instruction):
        self.type = "ELSE"
        self.else_clause = 'else'
        self.instruction = instruction


class LogicalOperator(Node):
    def __init__(self, op):
        self.type = "LOGICAL_OP"
        self.op = op


class Row(Node):
    def __init__(self, row, expression):
        self.type = "ROW"
        self.row = row
        self.expression = expression


class Rows(Node):
    def __init__(self, rows, row):
        self.type = "ROWS"
        self.rows = rows
        self.row = row


class Matrix(Node):
    def __init__(self, rows):
        self.type = "MATRIX"
        self.rows = rows


class Vector(Node):
    def __init__(self, row):
        self.type = "VECTOR"
        self.row = row


class UnaryExpression(Node):
    def __init__(self, op, arg):
        self.type = "UNARY_EXPRESSION"
        self.op = op
        self.arg = arg


class Zeros(Node):
    def __init__(self, arg):
        self.type = "ZEROS"
        self.arg = arg


class Ones(Node):
    def __init__(self, arg):
        self.type = "ONES"
        self.arg = arg


class Eye(Node):
    def __init__(self, arg):
        self.type = "EYE"
        self.arg = arg


class String(Node):
    def __init__(self, value):
        self.type = "STRING"
        self.value = value


class Introw(Node):
    def __init__(self, introw, intnum):
        self.type = "INTROW"
        self.introw = introw
        self.intnum = intnum


class ArrayPart(Node):
    def __init__(self, var, introw):
        self.type = "ARRAY_PART"
        self.var = var
        self.introw = introw


class Break(Node):
    def __init__(self):
        self.type = "BREAK"
        pass


class Continue(Node):
    def __init__(self):
        self.type = "CONTINUE"
        pass


class Error(Node):
    def __init__(self):
        self.type = "ERROR"
        pass