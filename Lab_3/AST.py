class Node(object):
    pass


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):

    def __init__(self, value):
        self.value = value


class Tuple(Node):
    def __init__(self):
        pass


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Program(Node):
    def __init__(self, instructions_opt):
        self.instructions_opt = instructions_opt


class InstructionsOpt(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instruction, isntructions):
        self.instruction = instruction
        self.instructions = isntructions


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class InstructionWithArg(Node):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr


class Printable(Node):
    def __init__(self, printable, expression):
        self.printable = printable
        self.expression = expression


class Loop(Node):
    def __init__(self, loop, condition, instruction):
        self.loop = loop
        self.condition = condition
        self.instruction = instruction


class ArrayRange(Node):
    def __init__(self, counter, beginning, end):
        self.counter = counter
        self.beginning = beginning
        self.end = end


class IfStatement(Node):
    def __init__(self, condition, instruction, elseStatement):
        self.condition = condition
        self.instruction = instruction
        self.elseStatement = elseStatement


class ElseStatement(Node):
    def __init__(self, instruction):
        self.else_clause = 'else'
        self.instruction = instruction


class LogicalOperator(Node):
    def __init__(self, op):
        self.op = op


class Row(Node):
    def __init__(self, row, expression):
        self.row = row
        self.expression = expression


class Rows(Node):
    def __init__(self, rows, row):
        self.rows = rows
        self.row = row


class Matrix(Node):
    def __init__(self, rows):
        self.rows = rows


class UnaryExpression(Node):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg


class Zeros(Node):
    def __init__(self, arg):
        self.arg = arg


class Ones(Node):
    def __init__(self, arg):
        self.arg = arg


class Eye(Node):
    def __init__(self, arg):
        self.arg = arg


class String(Node):
    def __init__(self, value):
        self.value = value


class Introw(Node):
    def __init__(self, introw, intnum):
        self.introw = introw
        self.intnum = intnum


class ArrayPart(Node):
    def __init__(self, var, introw):
        self.var = var
        self.introw = introw


class Break(Node):
    def __init__(self):
        pass


class Continue(Node):
    def __init__(self):
        pass


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
