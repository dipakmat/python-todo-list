import unittest
import sys

sys.path.append(".")
from src.todolist import TodoList


class TestTodoList(unittest.TestCase):
    """Test cases for the TodoLis class."""

    def test_add_task(self):
        """Test adding a task to the to-do list."""
        todo = TodoList()
        todo.add_task("Test Task")
        self.assertEqual(todo.tasks, ["Test Task"])

    def test_view_tasks_empty(self):
        """Test viewing a tasks in an empty to-do list."""
        todo = TodoList()
        self.assertEqual(todo.tasks, [])

    def test_view_tasks(self):
        """Test viewing a tasks in a non-empty to-do list."""
        todo = TodoList()
        todo.add_task("Task 1")
        todo.add_task("Task 2")
        self.assertEqual(todo.tasks, ['Task 1', 'Task 2'])


if __name__ == "__main__":
    unittest.main()
