import datetime
from files.utils import load_tasks, save_tasks

def mark_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f" Task marked as '{status}'.")
            return
    print("Task not found.")
