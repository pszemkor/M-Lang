import sys, os

sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('..'))

import Lab_4.Mparser
import Lab_4.TreePrinter
import Lab_4.scanner
from Lab_4.TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Lab_4.Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=Lab_4.scanner.lexer)
    # res = ast.printTree()
    # print(res)
    # Below code shows how to use visitor

    typeChecker = TypeChecker()
    typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)
