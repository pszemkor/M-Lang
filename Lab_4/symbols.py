from symtable import Symbol


class VariableSymbol(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type


class SymbolTable(object):

    def __init__(self, parent, name):  # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.symbols = {}
        self.scope = []

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        self.symbols[name] = VariableSymbol(name, symbol)

    def get(self, name):  # get variable symbol or fundef from <name> entry
        return self.symbols.get(name, None)

    def getParentScope(self):
        return self.scope[-1]

    def pushScope(self, name):
        self.scope.append(name)

    def popScope(self):
        self.scope.pop()
