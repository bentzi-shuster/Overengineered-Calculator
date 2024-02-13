import json
from calculator.operations import Operations
from decimal import Decimal  
from calculator.Interfaces.ICalcHistory import ICalcHistory
from pydantic import ValidationError
from calculator.Schemas.HistorySchema import CalculationHistory, OperationResult
historyFile = 'history.json'

class CalcHistory(ICalcHistory):
    def check_file()-> bool|None:
        try:
            with open(historyFile, 'r') as f:
                return True
        except FileNotFoundError:
            with open(historyFile, 'w') as f:
                f.write('[]')
            return False
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def serialize(data: dict)-> str:
            dumps= json.dumps(data, indent=2)
            return dumps
    
    @staticmethod
    def deserialize(data: str)-> dict:
            loads= json.loads(data)
            return loads

        
    @staticmethod
    def write(data: str)-> bool:
        try:
            CalcHistory.check_file()
            with open(historyFile, 'w') as f:
                f.write(data)
            return True
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def read()-> str|None:
        try:
            CalcHistory.check_file()
            with open(historyFile, 'r') as f:
                return f.read()
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def readJson()-> dict|None:
        try:
            read = CalcHistory.read()
            deserialized = CalcHistory.deserialize(read)
            return deserialized
        except Exception as e:
            print(e)
            return None
        
    @staticmethod
    def append(data: dict) -> bool:
        try:    
            current = CalcHistory.readJson()
            current.append(data)
            CalcHistory.write(CalcHistory.serialize(current))
            return True
        except Exception as e:
            print(e)
            return False
    @staticmethod
    def clear()-> bool:
        try:
            CalcHistory.write('[]')
            return True
        except Exception as e:
            print(e)
            return False
        
    @staticmethod
    def get_last()-> dict:
        try:
            current = CalcHistory.readJson()
            return current[-1]
        except Exception as e:
            print(e)
            return None
        
    @staticmethod
    def get_all()-> list:
        try:
            current = CalcHistory.readJson()
            return current
        except Exception as e:
            print(e)
            return None
        
    @staticmethod
    def get_by_index(index: int)-> dict:
        try:
            current = CalcHistory.readJson()
            return current[index]
        except Exception as e:
            print(e)
            return None
        
    @staticmethod
    def get_by_operation(operation: str)-> list:
        try:
            current = CalcHistory.readJson()
            return [i for i in current if i['operation']==operation]
        except Exception as e:
            print(e)
            return None
    @staticmethod
    def new(operation:Operations,args: list, start: float, end: float, result: Decimal|None, error: Exception|None)-> bool:
        try:            
            CalcHistory.append(data={
                'operation': operation.__name__,
                'args': args,
                "start": start,
                "end": end,
                'result': result,
                'error': error.__str__() if error else None
            })
            return True
        except Exception as e:
            print(e)
            return False