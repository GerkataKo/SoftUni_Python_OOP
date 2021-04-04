class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name):
        task_to_complete = [t for t in self.tasks if task_name == t.name]
        if not task_to_complete:
            return f"Could not find task with the name {task_name}"
        task_to_complete[0].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        tasks_cleaned=[t for t in self.tasks if t.completed]
        return f"Cleared {len(tasks_cleaned)} tasks."

    def view_section(self):
        info = f"Section {self.name}:\n"
        for task in self.tasks:
            info += f"{task.details()}\n"
        return info
