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
        pass

    @addToClass(Error)
    def printTree(self, indent=0):
        pass

