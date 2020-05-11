from Lab_4 import AST
from Lab_4.symbols import SymbolTable


class NodeVisitor(object):
    def __init__(self):
        self.symbol_table = SymbolTable(None, None)

    def visit(self, node):
        if self.symbol_table.getParentScope() == "return":
            print("Error, instruction after 'return' is unreachable")
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)


class TypeChecker(NodeVisitor):
    def visit_Loop(self, node):
        self.visit(node.condition)
        self.symbol_table.pushScope("loop")
        self.visit(node.instruction)
        self.symbol_table.popScope()
        return node.type

    def visit_Continue(self, node):
        if self.symbol_table.getParentScope() != "loop":
            print("Error, cannot use 'continue' beyond the loop")
        return node.type

    def visit_InstructionWithArg(self, node):
        if node.op == "return":
            self.symbol_table.pushScope("return")
        return node.type

    def visit_Break(self, node):
        if self.symbol_table.getParentScope() != "loop":
            print("Error, cannot use 'break' beyond the loop")
        return node.type

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op
        if op == "=":
            if type1 != "VARIABLE":
                print("ERROR, cannot assign to non-variable")
            else:
                self.symbol_table.put(node.left.name, type2)
                return type2
        else:
            type_left = self.resolve_if_var(node.left)
            type_right = self.resolve_if_var(node.right)
            # types = {"INTNUM", "FLOATNUM","STRING", "VECTOR"}
            # if type_left == "MATRIX" and type_right in types:
            #     print("Type mismatch, cannot assign {} to {}".format(type_right, type_left))
            if (type_left == "INTNUM" and type_right == "FLOATNUM") or (
                    type_left == "FLOATNUM" and type_right == "INTNUM"):
                return "FLOATNUM"
            elif type_right == "INTNUM" and type_left == "INTNUM":
                return "INTNUM"
            elif type_right == "FLOATNUM" and type_left == "FLOATNUM":
                return "FLOATNUM"
            elif type_left == "STRING" and type_right == "STRING" and op == "+":
                return "STRING"
            # todo check sizes
            elif type_left == "MATRIX" and type_right == "MATRIX":
                return "MATRIX"
            elif type_left == "VECTOR" and type_right == "VECTOR":
                return "VECTOR"
            else:
                print("Error, type mismatch: {}, {}".format(type_left, type_right))
            # todo
            print(type_left, type_right, op)

    def visit_Matrix(self, node):
        # todo
        return node.type

    def visit_IntNum(self, node):
        return node.type

    def visit_Variable(self, node):
        return node.type

    def visit_Vector(self, node):
        return node.type

    def resolve_if_var(self, node):
        if node.type == "VARIABLE":
            res = self.symbol_table.get(node.name)
            if not res:
                print("Variable {} undeclared".format(node.name))
                return res
            return res.type
        else:
            return node.type
