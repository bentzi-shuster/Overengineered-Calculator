"""
if i did things right, to add a new operation, you just need to add a new function here
"""
from Interfaces.IOperations import IOperations
from decimal import Decimal  

class Operations(IOperations):
    def __init__(self):
        self.operations = {
            'add': self._add,
            'subtract': self._subtract,
            'multiply': self._multiply,
            'divide': self._divide,
            'power': self._power,
            'root': self._root
        }

    @staticmethod
    def _add(*args: Decimal) -> Decimal:
        return sum(args)

    @staticmethod
    def _subtract(*args: Decimal) -> Decimal:
        return args[0] - sum(args[1:])

    @staticmethod
    def _multiply(*args: Decimal) -> Decimal:
        result = 1
        for arg in args:
            result *= arg
        return result

    @staticmethod
    def _divide(*args: Decimal) -> Decimal:
        result = args[0]
        for arg in args[1:]:
            if arg == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result /= arg
        return result

    @staticmethod
    def _power(*args: Decimal) -> Decimal:
        result = args[0]
        for arg in args[1:]:
            result **= arg
        return result

    @staticmethod
    def _root(*args: Decimal) -> Decimal:
        #check for anything that might make the root invalid or complex
        if args[0] < 0 or args[1] == 0:
            raise ValueError
        return args[0] ** (1 / args[1])
    