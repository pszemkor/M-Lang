from __future__ import print_function

from Lab_4.AST import *


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
        return get_indent(indent) + str(self.value) + "\n"

    @addToClass(FloatNum)
    def printTree(self, indent=0):
        return get_indent(indent) + str(self.value) + "\n"

    @addToClass(Variable)
    def printTree(self, indent=0):
        return get_indent(indent) + str(self.name) + "\n"

    @addToClass(BinExpr)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op
        res += "\n"
        res += self.left.printTree(indent + 1)
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
        result += self.expression.printTree(indent)
        return result

    @addToClass(Loop)
    def printTree(self, indent=0):
        result = get_indent(indent) + self.loop
        result += "\n"
        result += self.condition.printTree(indent + 1)
        result += self.instruction.printTree(indent + 1)
        return result

    @addToClass(ArrayRange)
    def printTree(self, indent=0):
        result = self.counter.printTree(indent)
        result += get_indent(indent) + "RANGE"
        result += "\n"
        result += self.beginning.printTree(indent + 1)
        result += self.end.printTree(indent + 1)
        return result

    @addToClass(IfStatement)
    def printTree(self, indent=0):
        result = get_indent(indent) + "IF"
        result += "\n"
        result += self.condition.printTree(indent + 1)
        result += get_indent(indent) + "THEN"
        result += "\n"
        result += self.instruction.printTree(indent + 1)
        if self.elseStatement is not None:
            result += self.elseStatement.printTree(indent)

        return result

    @addToClass(String)
    def printTree(self, indent=0):
        return get_indent(indent) + self.value + "\n"

    @addToClass(Eye)
    def printTree(self, indent=0):
        result = get_indent(indent) + "EYE"
        result += "\n"
        result += self.arg.printTree(indent + 1)
        return result

    @addToClass(Ones)
    def printTree(self, indent=0):
        result = get_indent(indent) + "ONES"
        result += "\n"
        result += self.arg.printTree(indent + 1)
        return result

    @addToClass(Zeros)
    def printTree(self, indent=0):
        result = get_indent(indent) + "ZEROS"
        result += "\n"
        result += self.arg.printTree(indent + 1)
        return result

    @addToClass(UnaryExpression)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op
        res += "\n"
        res += self.arg.printTree(indent + 1)
        return res

    @addToClass(Matrix)
    def printTree(self, indent=0):
        res = get_indent(indent) + "MATRIX"
        res += "\n"
        res += self.rows.printTree(indent + 1)
        return res

    @addToClass(Rows)
    def printTree(self, indent=0):
        res = ""
        if self.rows:
            res += self.rows.printTree(indent)
        res += get_indent(indent) + "MATRIX ROW:"
        res += "\n"
        res += self.row.printTree(indent + 1)
        return res

    @addToClass(Row)
    def printTree(self, indent=0):
        res = ""
        if self.row:
            res += self.row.printTree(indent)
        res += self.expression.printTree(indent)
        return res

    @addToClass(ElseStatement)
    def printTree(self, indent=0):
        result = get_indent(indent) + "ELSE"
        result += "\n"
        result += self.instruction.printTree(indent + 1)
        return result

    @addToClass(InstructionWithArg)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op
        res += "\n"
        res += self.expr.printTree(indent + 1)
        return res

    @addToClass(Vector)
    def printTree(self, indent=0):
        res = get_indent(indent) + "VECTOR"
        res += "\n"
        res += self.row.printTree(indent + 1)
        return res

    @addToClass(ArrayPart)
    def printTree(self, indent=0):
        result = get_indent(indent) + "REF"
        result += "\n"
        result += self.var.printTree(indent + 1)
        result += self.introw.printTree(indent + 1)
        return result

    @addToClass(Introw)
    def printTree(self, indent=0):
        res = self.intnum.printTree(indent)
        res += self.introw.printTree(indent)
        return res


def get_indent(indent):
    return "| " * indent
