
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
        try:
          result= operation(*args)
        except Exception as e:
            error = e
        CalcHistory.append({
            'operation': operation.__name__,
            'args': args,
            "start": start,
            "end": time.time(),
            'result': result,
            'error': error
        })
        return result



print(Calculator()._operation(Operations.add, 1, 2,3,4,5,6,7,8,9,10)) # 55