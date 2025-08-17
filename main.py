from files import add , update
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
            pass

        # view all tasks
        elif play == 4:
            pass

        # list all tasks that are not done
        elif play == 5:
            pass
        
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
