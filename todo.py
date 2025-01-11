import os

completed = open("completed.txt", "a")
completed.close()

def init(name):
    if type(name) is not str:
        return None
    filename = name + ".txt"
    todo = open(filename, "a+") 
    todo.close()
    return filename

#latest reads last line of todo list 
def display(filename):
    with open(filename, "r") as todo:
        tasks = list(todo)
        if tasks:
            return tasks
        else:
            raise IndexError("List is empty!")

def display_completed(filename):
    with open("completed.txt", "r") as completed:
        completed_tasks = list(completed)
        if completed_tasks:
            tasks = []
            for task in completed_tasks:
                if task.strip().split(",", 1)[0] == filename:
                    tasks.append(task.strip().split(",", 1)[1])
        else:
            return ""
        return tasks 
                

# #append appends a new line to todo list
def append(filename, task):
    with open(filename, "a") as todo:
        if type(task) is not str:
            raise TypeError("append() type error: task not a string.")
            return
        if len(task) == 0:
            raise ValueError("append() value error: task is empty")
            return
        todo.write("~" + task + "\n")

#delete takes in task line number to delete and removes it from text file
def delete(filename, task_index):
    with open(filename, "r+") as todo:
        tasks = list(todo)
        tasks.pop(task_index)
        #clears file
        todo.truncate(0)
        if tasks:
            for task in tasks:
                todo.write(task)
        else:
            return
        
#takes in index of task, task replaced with strikethrough version, encoding changed for strikethrough
def complete(filename, task_index):
    with open(filename, "r") as todo:
        tasks = list(todo)
        delete(filename, task_index)

    with open("completed.txt", "a+") as completed:
        completed.write(str(filename) + "," + str(tasks[task_index]) + "\n")
        
##################

choice = "."
set_error = ""
reset = False

while not choice or choice != "e":
    
    #####checking for file stuff###############
    with open("files.txt", "a+") as files:
        files.seek(0)
        file_names = list(files)
        #falsy - if filenames not empty...
        if file_names:
            latest_file = file_names[len(file_names)-1].strip()
        else:
            latest_file = input("Enter todo list name")
            if type(latest_file) is str and latest_file:
                files.write(latest_file + "\n")
            elif reset == False:
                while type(latest_file) is not str or not latest_file:
                    latest_file = input("Enter todo list name")
            elif reset == True:
                break
    ##################################################
    
    current_file = init(latest_file)
    
    print(f"\n{current_file}")
    print("-" * len(current_file))

    try:
        for task in display(current_file):
            print (task)
    except IndexError:
            print ("\nList is empty!")
            
    print("\ncompleted:")
    completed_tasks = display_completed(current_file)
    if not completed_tasks:
        print ("No completed tasks")
    else:
        for completed in completed_tasks:
            print (completed)
    
    print("\n" + set_error)
    set_error = ""
    print("[c] mark task completed  [a] append task  [d] delete task  [l] lists  [e] exit")
    choice = input("")
    
    if choice.lower() == "c":
        print (" ")
        try:
            tasks = display(current_file)
            for task_index in range(len(tasks)):
                print (tasks[task_index].replace("~", f"~{task_index+1}~ "))
        except IndexError:
            continue
        try:
            index = int(input("index:\n")) - 1
        except:
            set_error = "Invalid input"
        else:
            complete(current_file, index)
        
    elif choice.lower() == "a":
        try:
            append(current_file, input("\n~"))
        except:
            set_error = "Invalid input"
                                
    if choice.lower() == "d":
        print (" ")
        try:
            tasks = display(current_file)
            for task_index in range(len(tasks)):
                print (tasks[task_index].replace("~", f"~{task_index+1}~ "))
        except IndexError:
            set_error = "List is empty"
            continue
        try:
            index = int(input("index:\n")) - 1
        except:
            set_error = "Invalid input"
        else:
            delete(current_file, index)
    #DEBUG
    if choice.lower() == "reset":
        os.remove(current_file)
        with open("completed.txt", "w+") as completed:
            completed.truncate(0)
        with open("files.txt", "w+") as file_names:
            file_names.truncate(0)
        reset = True