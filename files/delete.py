from files.utils import load_tasks, save_tasks

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(updated_tasks)
        print("Task deleted successfully.")
