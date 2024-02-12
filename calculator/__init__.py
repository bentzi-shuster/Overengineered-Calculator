
from decimal import Decimal  
from operations import Operations
from Interfaces.ICalculator import ICalculator
import time
from history import CalcHistory


class Calculator(ICalculator):
    """
    The entry point for the calculator, this class is responsible for calling the operations and logging the results
    """
    @staticmethod
    def _operation(operation: Operations, *args: Decimal) -> Decimal:
        start = time.time()
        result=None
        error=None
        end=None
        try:
          result= operation(*args)
          end = time.time()
        except Exception as e:
            error = e
        CalcHistory.new(
            operation= operation,
            args= args,
            start= start,
            end= end,
            result= result,
            error= error
        )
        return error or result

operations = Operations()
operations_list = operations.operations
for key in operations_list:
    setattr(Calculator, key, lambda *args, operation=operations_list[key]: Calculator._operation(operation, *args))

CalcHistory.clear()
print(Calculator.add(1,2,3,4,5))
print(Calculator.subtract(1,2,3,4,5))
print(Calculator.divide(0,3,3,0,5))
print(Calculator.multiply(1,2,3,4,5))