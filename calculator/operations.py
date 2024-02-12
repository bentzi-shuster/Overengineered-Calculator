"""
if i did things right, to add a new operation, you just need to add a new function here
"""

from decimal import Decimal  

class Operations:
    # def __init__(self):
    #     self.operations = {
    #         'add': self._add,
    #         'subtract': self._subtract,
    #         'multiply': self._multiply,
    #         'divide': self._divide,
    #         'power': self._power,
    #         'root': self._root
    #     }

    @staticmethod
    def add(*args: Decimal) -> Decimal:
        return sum(args)

    @staticmethod
    def subtract(*args: Decimal) -> Decimal:
        return args[0] - sum(args[1:])

    @staticmethod
    def multiply(*args: Decimal) -> Decimal:
        result = 1
        for arg in args:
            result *= arg
        return result

    @staticmethod
    def divide(*args: Decimal) -> Decimal:
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result

    @staticmethod
    def power(*args: Decimal) -> Decimal:
        result = args[0]
        for arg in args[1:]:
            result **= arg
        return result

    @staticmethod
    def root(*args: Decimal) -> Decimal:
        return args[0] ** (1 / args[1])

