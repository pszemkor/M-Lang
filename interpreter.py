import sys, os

sys.path.append(os.path.abspath('/'))
sys.path.append(os.path.abspath(''))

import AST
from memory import *
from visit import *

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
               "<=": lambda x, y: x <= y,
               "==": lambda x, y: x == y}
        op = node.op
        if isinstance(node.op, AST.LogicalOperator):
            op = node.op.accept(self)
        return ops[op](r1, r2)

    @when(AST.FloatNum)
    def visit(self, node: AST.FloatNum):
        return float(node.value)

    @when(AST.IntNum)
    def visit(self, node: AST.IntNum):
        return int(node.value)

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
            result = node.instruction.accept(self)

        self.memory_stack.pop()
        return result

    @when(AST.IfStatement)
    def visit(self, node: AST.IfStatement):
        self.memory_stack.push(node.type)
        result = None
        if node.condition.accept(self):
            result = node.instruction.accept(self)
            self.memory_stack.pop()
        else:
            self.memory_stack.pop()
            if node.elseStatement:
                result = node.elseStatement.accept(self)
        return result

    @when(AST.ElseStatement)
    def visit(self, node: AST.ElseStatement):
        self.memory_stack.push(node.type)
        result = node.instruction.accept(self)
        self.memory_stack.pop()
        return result

    @when(AST.Instruction)
    def visit(self, node: AST.Instruction):
        return node.instruction.accept(self)

    @when(AST.Program)
    def visit(self, node: AST.Program):
        self.memory_stack.push("main")
        res = None
        for ch in node.children:
            res = ch.accept(self)
        self.memory_stack.pop()
        return res

    @when(AST.Instructions)
    def visit(self, node: AST.Instructions):
        res = None
        for ch in node.children:
            res = ch.accept(self)
        return res

    @when(AST.InstructionsOpt)
    def visit(self, node: AST.InstructionsOpt):
        res = None
        for ch in node.children:
            res = ch.accept(self)
        return res

    @when(AST.Printable)
    def visit(self, node: AST.Printable):
        res = None
        for ch in node.children:
            res = ch.accept(self)
            print(res)
        return res

    @when(AST.InstructionWithArg)
    def visit(self, node: AST.InstructionWithArg):
        # todo: handle 'return'
        return node.expr.accept(self)

    @when(AST.LogicalOperator)
    def visit(self, node: AST.LogicalOperator):
        return node.op
