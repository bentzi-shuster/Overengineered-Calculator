
from decimal import Decimal  
from operations import Operations
import time
from history import CalcHistory
class Calculator:

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
        return result


CalcHistory.clear()
print(Calculator()._operation(Operations.add, 1, 2,3,4,5,6,7,8,9,10)) # 55
print(Calculator()._operation(Operations.power, 2, 3)) # 8