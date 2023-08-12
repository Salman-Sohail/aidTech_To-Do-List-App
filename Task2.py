import pickle

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f"Deleted task: {deleted_task.title}")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("Current tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. Title: {task.title}, Description: {task.description}")
        else:
            print("No tasks in the list.")

    def save_tasks(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)
        print("Tasks saved successfully.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)

        elif choice == '3':
            todo_list.view_tasks()

        elif choice == '4':
            filename = input("Enter filename to save tasks (most preferably in ending in .txt): ")
            todo_list.save_tasks(filename)

        elif choice == '5':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks(filename)

        elif choice == '6':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()