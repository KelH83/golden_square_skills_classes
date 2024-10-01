## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Todo:
    # User-facing properties:
    #   none

    def __init__(self):
        # Parameters:
        #   task_list: list
        # Side effects:
        #   Holds all of the task properties
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self task list
        # Throws an exception if datatype is not string
        pass # No code here yet

    def show(self):
        # Returns:
        #   A list of all the tasks form the self task list
        # Side-effects:
        #   Throws an exception if there are no tasks
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Creates a new instance of Todo
#creates a new instance with an empty list
"""
new_todo = Todo()
new_todo.show() # => []

def test_instance_created():
    new_todo = Todo()
    assert isinstance(new_todo, Todo)
    assert new_todo.task_list == []

"""
Given a task, adds the task to the instance list
#add adds the new task to the task list
"""
new_todo = Todo()
new_todo.add("Walk the dog")
new_todo.show() # => ["Walk the dog"]

def test_add_task():
    new_todo = Todo()
    new_todo.add("Walk the dog")
    assert new_todo.task_list == ["Walk the dog"]

"""

Returns the full list
#show returns task_list
"""
new_todo = Todo()
new_todo.add("Walk the dog")

def test_show():
    new_todo = Todo()
    new_todo.add("Walk the dog")
    assert new_todo.show() == ["Walk the dog"]

"""

Given a task with incorrect datatype
#add raises an exception
"""
new_todo = Todo()
new_todo.add(123) # raises an error with the message "Only strings allowed!"

def test_add_with_incorrect_datatype():
    new_todo = Todo()
    with pytest.raises(Exception) as e:
            new_todo.add(123)
        error_message = str(e.value)
        assert error_message == "Only strings are allowed!"
"""
```



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
