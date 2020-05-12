from Lab_4 import AST
from Lab_4.symbols import SymbolTable


class NodeVisitor(object):
    def __init__(self):
        self.symbol_table = SymbolTable(None, None)

    def visit(self, node):
        # print("visiting:", node.__class__.__name__)
        if self.symbol_table.getParentScope() == "return" and node.type == "INSTRUCTION":
            print("[line: {}]: Error, instruction after 'return' is unreachable".format(node.lineno))
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
    def valid_sizes(self, left, right, op):
        # to check in runtime
        if not left.size or not right.size:
            return True
        if op == "+" or op == "-":
            return left.size == right.size
        else:
            return left.size[0] == right.size[1] and left.size[1] == right.size[0]

    def visit_Loop(self, node):
        self.visit(node.condition)
        self.symbol_table.pushScope("loop")
        self.visit(node.instruction)
        self.symbol_table.popScope()
        return node.type

    def visit_Continue(self, node):
        if self.symbol_table.getParentScope() != "loop":
            print("[line: {}]: Error, cannot use 'continue' beyond the loop".format(node.lineno))
        return node.type

    def visit_InstructionWithArg(self, node):
        if node.op == "return":
            self.symbol_table.pushScope("return")
        return node.type

    def visit_Break(self, node):
        if self.symbol_table.getParentScope() != "loop":
            print("[line: {}]: Error, cannot use 'break' beyond the loop".format(node.lineno))
        return node.type

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op
        if op == "=":
            if type1 != "VARIABLE":
                print("[line: {}]: ERROR, cannot assign to non-variable".format(node.lineno))
            else:
                if (type2 == "MATRIX" or type2 == "VECTOR") and hasattr(node.right, 'size'):
                    self.symbol_table.put(node.left.name, type2, node.right.size)
                else:
                    self.symbol_table.put(node.left.name, type2)
                return type2
        else:
            type_left = self.resolve_if_var(node.left)
            type_right = self.resolve_if_var(node.right)
            # to check in runtime
            if type_right == "BIN_EXPR" or type_left == "BIN_EXPR":
                return "BIN_EXPR"
            if (type_left == "INTNUM" and type_right == "FLOATNUM") or (
                    type_left == "FLOATNUM" and type_right == "INTNUM"):
                return "FLOATNUM"
            elif type_right == "INTNUM" and type_left == "INTNUM":
                return "INTNUM"
            elif type_right == "FLOATNUM" and type_left == "FLOATNUM":
                return "FLOATNUM"
            elif type_left == "STRING" and type_right == "STRING" and op == "+":
                return "STRING"
            elif type_left in ["VECTOR", "MATRIX"] and type_right in ["VECTOR", "MATRIX"]:
                if op == "/":
                    print("[line: {}]: Error, cannot divide two matrix/vectors".format(node.lineno))
                else:
                    left = self.resolve_variable_object(node.left)
                    right = self.resolve_variable_object(node.right)
                    if self.valid_sizes(left, right, op):
                        return "MATRIX"
                    else:
                        print(
                            "[line: {}]: Error, invalid matrix sizes in binary expression: left: {}, right: {}".format(
                                node.lineno, left.size,
                                right.size))
            else:
                print("[line: {}]: Error, type mismatch: {}, {}".format(node.lineno, type_left, type_right))

    def visit_Matrix(self, node):
        matrix_rows = node.rows
        first_row_len = len(matrix_rows.children[0].children)
        for row in matrix_rows.children[1:]:
            if len(row.children) != first_row_len:
                print("[line: {}]: Error, every row of matrix should have the same size".format(node.lineno))
                return node.type
        return node.type

    def visit_Row(self, node):
        for i, child in enumerate(node.children):
            if child.type != self.visit(node.children[i - 1]):
                print("[line: {}]: Error, row contains heterogeneous elements".format(node.lineno))
        return self.visit(node.children[0])

    def visit_Zeros(self, node):
        if node.arg.type == "ROW" and self.is_row_of_ints(node.arg):
            size = []
            for ch in node.arg.children:
                if self.visit(ch) == "VARIABLE":
                    return "MATRIX"
                size.append(ch.value)
            if len(size) == 1:
                size.insert(0, 1)
            node.size = tuple(size)
            return "MATRIX"
        else:
            print("[line: {}]: Error, illegal zeros initialization".format(node.lineno))
        return "MATRIX"

    def visit_Eye(self, node):
        if node.arg.type == "ROW" and self.is_row_of_ints(node.arg):
            size = []
            for ch in node.arg.children:
                size.append(ch.value)
            if len(size) == 1:
                size.insert(0, 1)
            node.size = tuple(size)
            return "MATRIX"
        else:
            print("[line: {}]: Error, illegal eye initialization".format(node.lineno))
        return "MATRIX"

    def visit_Ones(self, node):
        if node.arg.type == "ROW" and self.is_row_of_ints(node.arg):
            size = []
            for ch in node.arg.children:
                size.append(ch.value)
            if len(size) == 1:
                size.insert(0, 1)
            node.size = tuple(size)
            return "MATRIX"
        else:
            print("[line: {}]: Error, illegal ones initialization".format(node.lineno))
        return "MATRIX"

    def visit_IntNum(self, node):
        return node.type

    def visit_FloatNum(self, node):
        return node.type

    def visit_Variable(self, node):
        return node.type

    def visit_Vector(self, node):
        return node.type

    def visit_LogicalOperator(self, node):
        return node.type

    def resolve_variable_object(self, node):
        if node.type == "VARIABLE":
            res = self.symbol_table.get(node.name)
            if not res:
                print("[line: {}]: Variable {} undeclared".format(node.lineno, node.name))
                return res
            return res
        else:
            return node

    def resolve_if_var(self, node):
        if node.type == "VARIABLE":
            res = self.symbol_table.get(node.name)
            if not res:
                print("[line: {}]: Variable {} undeclared".format(node.lineno, node.name))
                return res
            return res.type
        else:
            return node.type

    def is_row_of_ints(self, row):
        for i, child in enumerate(row.children):
            if child.type == "VARIABLE":
                if not self.symbol_table.get(child.name) or self.symbol_table.get(child.name).type != "INTNUM":
                    return False
            elif child.type != "INTNUM":
                return False
        return True
