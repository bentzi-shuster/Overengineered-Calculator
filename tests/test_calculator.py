from decimal import Decimal
import pytest
from calculator.operations import Operations
from calculator import Calculator


oppertions = Operations().operations
@pytest.mark.parametrize("test_input,expected,operations", [([1,2,3,4],10,oppertions["add"]),([1,2,3,4],-8,oppertions["subtract"]),([1,2],Decimal('0.5'),oppertions["divide"]),([1,2,3,4],24,oppertions["multiply"])])
def test_calculator_operations(test_input:list, expected:Decimal,operations:callable):
   assert Calculator.__getattribute__(Calculator,operations.__name__.split("_")[1])(*test_input)==expected