from Lab_4 import AST
from Lab_4.symbols import SymbolTable


class NodeVisitor(object):

    def visit(self, node):
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
    def __init__(self):
        self.symbol_table = SymbolTable(None, None)

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op
        if op == "=":
            if type1 != "VARIABLE":
                print("ERROR, cannot assign to non-variable")
            else:
                self.symbol_table.put(node.left.name, type2)
                print(type2, "*******")
                print(type1, type2, op)
                return type2
        else:
            type_left = self.resolve_if_var(node.left)
            type_right = self.resolve_if_var(node.right)
            print(type_left, type_right, op)

    def visit_IntNum(self, node):
        return node.type

    def visit_Variable(self, node):
        self.symbol_table.put(node.name, node.type)
        return node.type

    def resolve_if_var(self, node):
        if node.type == "VARIABLE":
            res = self.symbol_table.get(node.name)
            if not res:
                print("Variable {} undeclared", node.name)
                return res
            return res.type
        else:
            return node.type
