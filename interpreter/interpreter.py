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
        r2 = node.right.accept(self)
        if node.op == "=":
            try:
                val = self.memory_stack.get(node.left.name)
                self.memory_stack.set(node.left.name, r2)
            except ValueError:
                self.memory_stack.insert(node.left.name, r2)
            return None

        r1 = node.left.accept(self)
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

    @when(AST.FloatNum)
    def visit(self, node: AST.FloatNum):
        return node.value

    @when(AST.IntNum)
    def visit(self, node: AST.IntNum):
        return node.value

    @when(AST.String)
    def visit(self, node: AST.String):
        return node.value

    @when(AST.Variable)
    def visit(self, node: AST.Variable):
        return self.memory_stack.get(node.name)

    @when(AST.Loop)
    def visit(self, node: AST.Loop):
        self.memory_stack.push(node.type)
        result = None
        while node.condition.accept(self):
            node.instruction.accept(self)

        self.memory_stack.pop()
        return result

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
