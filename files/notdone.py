from files.utils import load_tasks

def list_not_done():
    tasks = load_tasks()
    filtered = [task for task in tasks if task["status"] != "done"]
    if not filtered:
        print("All tasks are done. Nothing pending!")
        return
    for task in filtered:
        print(f"[{task['id']}] {task['description']} - {task['status']}")
