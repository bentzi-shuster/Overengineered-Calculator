import pytest
from calculator.operations import Operations
from decimal import Decimal
from calculator.history import CalcHistory
from calculator.Schemas.HistorySchema import OperationResult


@pytest.fixture
def history_instance():
    return CalcHistory()
@pytest.fixture
def get_operation_add():
    operations = Operations()
    return operations._add

@pytest.fixture
def get_example_data():
     return {
            "operation": "_add",
            "args": [
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "start": 1707770999.7317681,
            "end": 1707770999.7317681,
            "result": "15",
            "error": None
        }
     


def test_check_file():
    assert CalcHistory.check_file() is not None


def test_serialize_deserialize(get_example_data):
    data = [get_example_data]
    serialized_data = CalcHistory.serialize(data)
    deserialized_data = CalcHistory.deserialize(serialized_data)
    assert deserialized_data == data


def test_write_read(history_instance, get_example_data):
    data = [get_example_data]  # Call the function to get example data
    serialized_data = CalcHistory.serialize(data)
    assert history_instance.write(serialized_data)
    assert history_instance.readJson() == data


def test_append(history_instance, get_example_data):
    initial_data = [get_example_data]
    history_instance.write(CalcHistory.serialize(initial_data))

    new_data = [get_example_data]
    history_instance.append(new_data)

    expected_result = initial_data + new_data  # Remove the square brackets around new_data
    assert history_instance.readJson() is not None and len(history_instance.readJson()) is not 0


def test_clear(history_instance,get_example_data):
    history_instance.write(CalcHistory.serialize([get_example_data]))
    assert history_instance.clear()
    assert history_instance.readJson() == []


def test_get_last(history_instance, get_example_data):
    data = [get_example_data,get_example_data]
    history_instance.write(CalcHistory.serialize(data))
    assert history_instance.get_last() == data[-1]

def test_new(history_instance,get_operation_add):
    operation = get_operation_add
    args = [2, 3]
    start = 0
    end = 5
    result = Decimal('5')
    error = None
    old_data = history_instance.readJson()
    assert history_instance.new(operation, args, start, end, result, error)

def test_get_all(history_instance,get_example_data):
    data = [get_example_data,get_example_data]
    history_instance.write(CalcHistory.serialize(data))
    assert history_instance.get_all() == data

def test_get_by_index(history_instance,get_example_data):
    data = [get_example_data,get_example_data]
    history_instance.write(CalcHistory.serialize(data))
    assert history_instance.get_by_index(0) == data[0]

def test_get_by_operation(history_instance,get_example_data):   
    data = [get_example_data,get_example_data]
    history_instance.write(CalcHistory.serialize(data))
    assert history_instance.get_by_operation('_add') == data

    