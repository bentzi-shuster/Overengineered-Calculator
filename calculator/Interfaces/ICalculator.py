
from decimal import Decimal  

class ICalculator(object):
    """
    Interface for the calculator
    This is needed for the calculator to have intellsense since the methods are added dynamically
    """
    def _operation(operation: str, *args: Decimal) -> Decimal:
        """
        The private method that calls the operations and logs the results
        """
        pass
    
    def add(self, *args: Decimal) -> Decimal:
        """
        Adds the all numbers together
        
        """
        pass
    def subtract(self, *args: Decimal) -> Decimal:
        """
        Subtracts all the numbers together
        """
        pass
    def multiply(self, *args: Decimal) -> Decimal:
        """
        Multiplies all the numbers together
        """
        pass
    def divide(self, *args: Decimal) -> Decimal:
        """
        Divides all the numbers together
        """
        pass
    def power(self, *args: Decimal) -> Decimal:
        """
        Raises the first number to the power of the second number and so on
        """
        pass
    def root(self, *args: Decimal) -> Decimal:
        """
        Takes the root of the first number with the second number as the root and so on
        """
        pass
    def factorial(self, a: Decimal) -> Decimal:
        """
        Takes the factorial of the number
        """
        pass