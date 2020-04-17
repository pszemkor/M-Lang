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
        return get_indent(indent) + str(self.value)

    @addToClass(FloatNum)
    def printTree(self, indent=0):
        return get_indent(indent) + str(self.value)

    @addToClass(Variable)
    def printTree(self, indent=0):
        return get_indent(indent) + str(self.name)

    @addToClass(BinExpr)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op
        res += "\n"
        res += self.left.printTree(indent + 1)
        res += "\n"
        res += self.right.printTree(indent + 1)
        return res

    @addToClass(Program)
    def printTree(self, indent=0):
        return self.instructions_opt.printTree()

    @addToClass(InstructionsOpt)
    def printTree(self, indent=0):
        return self.instructions.printTree()

    @addToClass(Instructions)
    def printTree(self, indent=0):
        res = self.instruction.printTree(indent)
        if self.instructions is not None:
            res += self.instructions.printTree(indent)
        return res

    @addToClass(Instruction)
    def printTree(self, indent=0):
        return self.instruction.printTree(indent)

    @addToClass(Printable)
    def printTree(self, indent=0):
        result = ""
        if self.printable:
            result += self.printable.printTree(indent)
        result += "\n"
        result += self.expression.printTree(indent)
        return result

    @addToClass(Loop)
    def printTree(self, indent=0):
        result = "\n" + get_indent(indent) + self.loop
        result += "\n"
        result += self.condition.printTree(indent + 1)
        result += "\n"
        result += self.instruction.printTree(indent + 1)
        return result

    @addToClass(ArrayRange)
    def printTree(self, indent=0):
        result = "\n" + self.counter.printTree(indent)
        result += "\n"
        result += get_indent(indent) + "RANGE"
        result += "\n"
        result += self.beginning.printTree(indent + 1)
        result += "\n"
        result += self.end.printTree(indent + 1)
        return result

    @addToClass(IfStatement)
    def printTree(self, indent=0):
        result = "\n" + get_indent(indent) + "IF"
        result += "\n"
        result += self.condition.printTree(indent + 1)
        result += "\n"
        result += get_indent(indent) + "THEN"
        result += "\n"
        result += self.instruction.printTree(indent + 1)
        if self.elseStatement is not None:
            result += self.elseStatement.printTree(indent)

        return result

    @addToClass(ArrayPart)
    def printTree(self, indent=0):
        pass

    @addToClass(String)
    def printTree(self, indent=0):
        return get_indent(indent) + self.value

    @addToClass(Eye)
    def printTree(self, indent=0):
        result = "\n" + get_indent(indent) + "EYE"
        result += self.arg.printTree(indent + 1)
        return result

    @addToClass(Ones)
    def printTree(self, indent=0):
        result = "\n" + get_indent(indent) + "ONES"
        result += self.arg.printTree(indent + 1)
        return result

    @addToClass(Zeros)
    def printTree(self, indent=0):
        result = "\n" + get_indent(indent) + "ZEROS"
        result += self.arg.printTree(indent + 1)
        return result

    @addToClass(UnaryExpression)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op
        res += "\n"
        res += self.arg.printTree(indent + 1)
        res += "\n"
        return res

    @addToClass(Matrix)
    def printTree(self, indent=0):
        pass

    @addToClass(Rows)
    def printTree(self, indent=0):
        pass

    @addToClass(Row)
    def printTree(self, indent=0):
        pass

    @addToClass(ElseStatement)
    def printTree(self, indent=0):
        result = "\n" + get_indent(indent) + "ELSE"
        result += "\n"
        result += self.instruction.printTree(indent + 1)
        result += "\n"
        return result

    @addToClass(InstructionWithArg)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op
        res += "\n"
        res += self.expr.printTree(indent + 1)
        return res


def get_indent(indent):
    return "| " * indent
