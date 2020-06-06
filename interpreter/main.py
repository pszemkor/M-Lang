import sys, os

from interpreter.interpreter import Interpreter

sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('..'))

import interpreter.Mparser
import interpreter.scanner
from interpreter.TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = interpreter.Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=interpreter.scanner.lexer)
    # res = ast.printTree()
    # print(res)
    # Below code shows how to use visitor

    typeChecker = TypeChecker()
    typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)

    ast.accept(Interpreter())
    # in future
    # ast.accept(OptimizationPass1())
    # ast.accept(OptimizationPass2())
    # ast.accept(CodeGenerator())
    # or alternatively ast.accept(typeChecker)
