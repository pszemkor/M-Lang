import sys

import Lab_3.Mparser
import Lab_3.TreePrinter
import Lab_3.scanner

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Lab_3.Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=Lab_3.scanner.lexer)
    res = ast.printTree()
    print(res)
