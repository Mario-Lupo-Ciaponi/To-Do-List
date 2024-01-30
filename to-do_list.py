def main_menu():
    print("Task menu:")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. View all tasks")
    print("4. Quit the program")


def add_new_task(todo_list):
    while True:
        task = input("Please type the task: ")
        todo_list.append([task, False])

        print(f"Task '{task}' added successfully!")
        print()

        decision = input("Would you like to add another task to TO-DO list? (Yes/No): ")

        if decision == "Yes":
            continue
        else:
            break

    print()  # This is to add some space to look prettier.


def mark_task_as_completed(todo_list):
    number_of_task = 1

    for task in todo_list:
        print(f"{number_of_task}. {task[0]} - [ ]")
        number_of_task += 1

    mark_as_complete = int(input("Type the number of task that you want to mark as complete: "))

    if 0 < mark_as_complete <= len(todo_list):
        for index in range(0, len(todo_list)):
            if index == mark_as_complete - 1:
                todo_list[index][1] = True

        print("Task successfully marked as complete!")
    else:
        print("Invalid task!")

    print()  # This is to add some space to look prettier.


def view_all_tasks(todo_list):
    print("To-Do list:")
    number_of_task = 1

    state = ""

    for task in todo_list:
        if task[1]:
            state = "[X]"
        else:
            state = "[ ]"

        print(f"{number_of_task}. {task[0]} - {state}")
        number_of_task += 1

    console_holder = input("Type anything to continue when you are ready: ")
    print()  # This is to add some space to look prettier.


def todo_list_program():
    todo_list = []

    while True:
        main_menu()
        print()  # This is to add some space to look prettier.

        choice_of_action = int(input("Please chose the action you want to do: "))
        print()  # This is to add some space to look prettier.

        if choice_of_action == 1:
            add_new_task(todo_list)
        elif choice_of_action == 2:
            mark_task_as_completed(todo_list)
        elif choice_of_action == 3:
            view_all_tasks(todo_list)
        elif choice_of_action == 4:
            print("See you again :)")
            break
        else:
            print("Invalid action!")


todo_list_program()
