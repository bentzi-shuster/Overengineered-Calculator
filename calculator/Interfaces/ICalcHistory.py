from calculator.operations import Operations
from decimal import Decimal  

class ICalcHistory(object):
    """
    Interface for the calculator history
    """
    def check_file(self) -> bool|None:
        """
        Checks if the history file exists before trying to read or write to it
        """
        pass

    @staticmethod
    def serialize(self, data: dict) -> str:
        """
        Serializes the data to a string
        """
        pass
    
    @staticmethod
    def deserialize(data: str) -> dict:
        """
        Deserializes the string to a dictionary
        """
        pass

    @staticmethod
    def write(self, data: str) -> bool:
        """
        Writes data to the history file
        """
        pass
        
    @staticmethod
    def read(self) -> str|None:
        """
        Reads data from the history file
        """
        pass

    @staticmethod
    def readJson(self) -> dict|None:
        """
        Reads JSON data from the history file
        """
        pass
        
    @staticmethod
    def append(data: dict) -> bool:
        """
        Appends data to the history file
        """
        pass
    
    @staticmethod
    def clear(self) -> bool:
        """
        Clears the content of the history file
        """
        pass
        
    @staticmethod
    def get_last(self) -> dict:
        """
        Gets the last entry in the history
        """
        pass
        
    @staticmethod
    def get_all(self) -> list:
        """
        Gets all entries in the history
        """
        pass
        
    @staticmethod
    def get_by_index(self, index: int) -> dict:
        """
        Gets an entry in the history by its index
        """
        pass
        
    @staticmethod
    def get_by_operation(self, operation: str) -> list:
        """
        Gets entries in the history by operation type (eg. add, subtract, multiply, divide, power, root)
        """
        pass
    
    @staticmethod
    def new(self, operation: Operations, args: list, start: float, end: float, result: Decimal|None, error: Exception|None) -> bool:
        """
        Adds a new entry to the history
        """
        pass
