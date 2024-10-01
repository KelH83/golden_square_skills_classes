from lib.recipe1and2 import *
import pytest

def test_instance_created():
    new_todo = Todo()
    assert isinstance(new_todo, Todo)
    assert new_todo.task_list == []

def test_add_task():
    new_todo = Todo()
    new_todo.add("Walk the dog")
    assert new_todo.task_list == ["Walk the dog"]

def test_add_with_incorrect_datatype():
    new_todo = Todo()
    with pytest.raises(Exception) as e:
            new_todo.add(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"

def test_show():
    new_todo = Todo()
    new_todo.add("Walk the dog")
    assert new_todo.show() == ["Walk the dog"]

def test_mark_complete():
    new_todo = Todo()
    new_todo.add("Walk the dog")
    new_todo.add("Feed the cat")
    new_todo.mark_complete("Walk the dog")
    assert new_todo.task_list == ["Feed the cat"]

def test_mark_complete_with_non_existent_data():
    new_todo = Todo()
    new_todo.add("Walk the dog")
    new_todo.add("Feed the cat")
    with pytest.raises(Exception) as e:
            new_todo.mark_complete("Water the plants")
    error_message = str(e.value)
    assert error_message == "No such task!"

def test_mark_complete_with_incorrect_datatype():
    new_todo = Todo()
    with pytest.raises(Exception) as e:
            new_todo.mark_complete(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"