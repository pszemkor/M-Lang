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

# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
