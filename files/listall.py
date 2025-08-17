from files.utils import load_tasks

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def list_by_status(status):
    tasks = load_tasks()
    filtered = [task for task in tasks if task["status"] == status]
    if not filtered:
        print(f"No tasks with status '{status}'.")
        return
    for task in filtered:
        print(f"[{task['id']}] {task['description']} - {task['status']}")
