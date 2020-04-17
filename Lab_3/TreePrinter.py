from __future__ import print_function

from Lab_3.AST import *


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:

    @addToClass(Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(IntNum)
    def printTree(self, indent=0):
        pass

    @addToClass(FloatNum)
    def printTree(self, indent=0):
        pass

    @addToClass(Tuple)
    def printTree(self, indent=0):
        pass

    @addToClass(Variable)
    def printTree(self, indent=0):
        return self.name

    @addToClass(BinExpr)
    def printTree(self, indent=0):
        pass

    @addToClass(Program)
    def printTree(self, indent=0):
        return self.instructions_opt.printTree()

    @addToClass(InstructionsOpt)
    def printTree(self, indent=0):
        return self.instructions.printTree()

    @addToClass(Instructions)
    def printTree(self, indent=0):
        return self.instruction.printTree()
        self.instructions.printTree()

    @addToClass(Instruction)
    def printTree(self, indent=0):
        return self.instruction.printTree()
        # if (self.printable != ""):
        #     self.printable.printTree()

    @addToClass(Printable)
    def printTree(self, indent=0):
        pass

    @addToClass(Loop)
    def printTree(self, indent=0):
        pass

    @addToClass(ArrayRange)
    def printTree(self, indent=0):
        pass

    @addToClass(IfStatement)
    def printTree(self, indent=0):
        pass

    @addToClass(Assign)
    def printTree(self, indent=0):
        return self.op + "\n" + "| " * (indent + 1) + self.first.printTree() + "\n| " * (
                indent + 1) + self.second.printTree()

    @addToClass(ArrayPart)
    def printTree(self, indent=0):
        pass

    @addToClass(String)
    def printTree(self, indent=0):
        pass

    @addToClass(Eye)
    def printTree(self, indent=0):
        pass

    @addToClass(Ones)
    def printTree(self, indent=0):
        pass

    @addToClass(Zeros)
    def printTree(self, indent=0):
        pass

    @addToClass(UnaryExpression)
    def printTree(self, indent=0):
        pass

    @addToClass(Matrix)
    def printTree(self, indent=0):
        pass

    @addToClass(Rows)
    def printTree(self, indent=0):
        pass

    @addToClass(Row)
    def printTree(self, indent=0):
        pass

    @addToClass(LogicalOperator)
    def printTree(self, indent=0):
        pass

    @addToClass(ElseStatement)
    def printTree(self, indent=0):
        pass
