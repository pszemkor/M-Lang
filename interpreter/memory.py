class Memory:

    def __init__(self, name):  # memory name
        self.symbols = {}

    def has_key(self, name):  # variable name
        return name in self.symbols

    def get(self, name):  # gets from memory current value of variable <name>
        return self.symbols[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.symbols[name] = value


class MemoryStack:

    def __init__(self, memory=None):
        self.memory_stack = []
        self.last_pop = None

    def get(self, name):  # gets from memory stack current value of variable <name>
        self.__check_memory()
        for curr_memory in self.memory_stack:
            if curr_memory.has_key(name):
                return curr_memory.get(name)
        raise ValueError("Variable undefined:", name)

    def insert(self, name, value):  # inserts into memory stack variable <name> with value <value>
        self.__check_memory()
        curr_memory: Memory = self.memory_stack[-1]
        if curr_memory.has_key(name):
            raise Exception("Variable already defined in this scope:", name)
        curr_memory.put(name, value)

    def set(self, name, value):  # sets variable <name> to value <value>
        self.__check_memory()
        for curr_memory in self.memory_stack:
            if curr_memory.has_key(name):
                curr_memory.put(name, value)
                return
        raise KeyError("No such variable:", name)

    def push(self, name):  # pushes memory <memory> onto the stack
        self.memory_stack.insert(0, Memory(name))

    def pop(self):  # pops the top memory from the stack
        return self.memory_stack.pop(0)

    def __is_defined(self, curr_memory, name):
        if not curr_memory.has_key(name):
            raise ValueError("Variable undefined:", name)

    def __check_memory(self):
        if len(self.memory_stack) > 0:
            raise Exception("No memory pushed exception")
