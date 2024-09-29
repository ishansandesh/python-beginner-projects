# Create a program that allows users to add, remove, and view tasks. Tasks can be stored in a text file for persistence.
import platform
import os
def paint():
    print(r"""
      ______            ____  ____     __    _      __ 
     /_  __/___        / __ \/ __ \   / /   (_)____/ /_
      / / / __ \______/ / / / / / /  / /   / / ___/ __/
     / / / /_/ /_____/ /_/ / /_/ /  / /___/ (__  ) /_  
    /_/  \____/     /_____/\____/  /_____/_/____/\__/  
                                                (ISS) 
    * Add Task    - add
    * Remove Task - del
    * View Task   - show
    * Exit        - 0
    """)

def clear():
    x = platform.system()
    if x == "Windows":
        os.system('cls')
    elif x == "Linux":
        os.system('clear')

def add():
    new_task = input("Enter Your New Task: ")
    new_task = new_task+"\n"
    f = open("to_do_lst.txt","a")
    f.write(new_task)
    f.close()
    clear()
    print("\033[32mSuccess!\033[0m")
    main()

def show():
    clear()
    with open('to_do_lst.txt', 'r') as file:
        lines = file.readline()
        n=1
        while lines:
            print(n,lines.strip())
            lines = file.readline()
            n += 1
    exit = input("\nGo to Menu (y/n): ")
    if exit == 'y':
        main()
    else:
        exit

def delete():
    task_number = int(input("Enter Task Number: "))
    clear()
    with open("to_do_lst.txt","r") as file:
        lines = file.readlines()
    if 0 < task_number <=len(lines):
        lines.pop(task_number-1)
        print("\033[32mSUCCESS DELETED!\033[0m")
    else:
        print("\033[31mNot TASK Detect!\033[0m")
    with open("to_do_lst.txt", 'w') as file:
        file.writelines(lines)
    main()

def main():
    paint()
    arg = input("Enter Command: ")
    if arg == "add":
        add()
    elif arg == "del":
        delete()
    elif arg == "show":
        show()
    elif arg == "0":
        exit
    else:
        clear()
        print("\033[31mWrong Command!\033[0m")
        main()

main()