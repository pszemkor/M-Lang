from interpreter import AST
from interpreter.memory import *
from interpreter.exceptions import *
from interpreter.visit import *
import sys

sys.setrecursionlimit(10000)


class Interpreter(object):
    def __init__(self):
        self.memory_stack: MemoryStack = MemoryStack()

    @on('node')
    def visit(self, node):
        pass

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        if node.op == "=":
            self.memory_stack.set(r1, r2)

        # todo: add rest of operators -> for matrices
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y,
               '&&': lambda x, y: x and y,
               '||': lambda x, y: x or y,
               "!=": lambda x, y: x != y,
               ">": lambda x, y: x > y,
               "<": lambda x, y: x < y,
               ">=": lambda x, y: x >= y,
               "<=": lambda x, y: x <= y}
        return ops[node.op](r1, r2)

    @when(AST.Assignment)
    def visit(self, node):
        pass

    # simplistic while loop interpretation
    @when(AST.WhileInstr)
    def visit(self, node):
        r = None
        while node.cond.accept(self):
            r = node.body.accept(self)
        return r
