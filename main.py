from files import add , update , delete , listall , notdone
# main.py
class Task:

    def __init__(self):
        while True:
            if not self.menu():
                break

    def menu(self):
        try:
            play = int(input("""
a. Select 1 to add a task
b. Select 2 to update a task
c. Select 3 to delete a task
d. Select 4 to view all tasks
e. Select 5 to list all tasks that are not done
f. Select 6 to list all tasks that are in progress
g. Select 7 to mark a task as done
h. Select 8 to mark a task as in progress
i. Select any other key to exit
                        """))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return True
        
        # add a task 
        if play == 1:
            desc = input("Enter task description: ")
            add.add_task(desc)

        
        # update a task
        elif play == 2:
            try:
                task_id = int(input("Enter task ID to update: "))
                new_desc = input("Enter new description: ")
                update.update_task(task_id, new_desc)
            except ValueError:
                print("Invalid task ID.")

        # delete a task
        elif play == 3:
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete.delete_task(task_id)
            except ValueError:
                print("Invalid task ID.")


        # view all tasks
        elif play == 4:
            listall.list_tasks()

        # list all tasks that are not done
        elif play == 5:
            notdone.list_not_done()
        
        # list all tasks that are in progress
        elif play == 6:
            pass

        # mark a task as done or in progress
        elif play == 7:
            pass


        # mark a task as in progress
        elif play == 8:
            pass


        # exit the task manager
        else:
            print("Exiting the task manager.")




if __name__ == "__main__":
    Task()
