class TodoList:
    """A simple To-Do List class."""

    def __init__(self):
        """Initialize an empty to-do list."""
        self.tasks = []

    def add_task(self, task):
        """Add a task to the to-do list.

        Args:
            task (str): The task to be added.
        """
        try:
            self.tasks.append(task)
        except Exception as e:
            print(f"Exception : {e}")

    def view_tasks(self):
        """View the tasks in the to-do list."""
        try:
            if not self.tasks:
                print("No tasks in the to-do list.")
            else:
                print("To-Do List:")
                for idx, task in enumerate(self.tasks, start=1):
                    print(f"{idx}. {task}")
        except Exception as e:
            print(f"Exception : {e}")


# Example usage
if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Complete coding assignment")
    todo.add_task("Prepare for interview")
    todo.view_tasks()
