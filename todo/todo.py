import os
import sys

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
            raise TypeError("Task not a string.")
            return
        if len(task) == 0:
            raise ValueError("Task is empty")
            return
        todo.write("~" + task + "\n")

#delete takes in task line number to delete and removes it from text file
def delete(filename, task_index):
    with open(filename, "r+") as todo:
        tasks = list(todo)
        if task_index > len(display(filename)) or task_index < 0:
            raise IndexError("Task index outside of range")
        tasks.pop(task_index)
        #clears file
        todo.seek(0)
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
new_file = False
completed_shown = False

while not choice or choice != "e":
    
    #####checking for file stuff###############
    with open("files.txt", "a+") as files:
        files.seek(0)
        file_names = list(files)
        #falsy - if filenames not empty...
        if file_names:
            latest_file = file_names[len(file_names)-1].strip()
        if reset == True:
            break
        if new_file == True or not file_names:
            new_file = False 
            latest_file = input("\nEnter todo list name:\n")
            if type(latest_file) is str and latest_file and latest_file + "\n" not in file_names:
                files.write(latest_file + "\n")
            elif reset == False:
                while type(latest_file) is not str or not latest_file or latest_file + "\n" in file_names:
                    latest_file = input("Enter todo list name:\n")
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
    completed_tasks = completed_tasks[::-1]
    if not completed_tasks:
        print ("No completed tasks")
    elif completed_shown == False:
        for completed_num in range(len(completed_tasks)):
                if completed_num <= 4:
                    print ("✓" + completed_tasks[completed_num])
        if len(completed_tasks) >= 5:
            print ("...[f] show full completed tasks")
    elif completed_shown == True:
        for completed in completed_tasks:
            print("✓" + completed)
        print ("[f] hide completed tasks")
    
    print("\n" + set_error)
    set_error = ""
    choice = input("[c] mark task completed  [a] append task  [d] delete task  [s] switch lists  [e] exit\n")
    
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
        except Exception as error:
            set_error = str(error)
        else:
            complete(current_file, index)
        
    elif choice.lower() == "a":
        try:
            append(current_file, str(input("\n~")))
        except Exception as error:
            set_error = str(error)
                                
    if choice.lower() == "d":
        print (" ")
        try:
            tasks = display(current_file)
            for task_index in range(len(tasks)):
                print (tasks[task_index].replace("~", f"~{task_index+1}~ "))
        except Exception as error:
            set_error = str(error)
            continue
        try:
            index = int(input("index:\n")) - 1
        except Exception as error:
            set_error = str(error)
        else:
            try:
                delete(current_file, index)
            except Exception as error:
                set_error = str(error)
            
    if choice.lower() == "s":
        choice = "."
        print(" ")
        try:
            files = display("files.txt")
            for file_index in range(len(files)):
                print (f"~{file_index+1}~{files[file_index]}")
        except Exception as error:
            set_error = str(error)
            continue
        print(f"~{len(files)+1}~ *add new list*")
        try:
            index = int(input("index:\n")) - 1
        except Exception as error:
            set_error = str(error)
        else: 
            if index == len(files):
                new_file = True
            else:
                try:
                    with open("files.txt", "w") as files_txt:
                        new_latest = files.pop(index)
                        files.append(new_latest)
                        files_txt.seek(0)
                        files_txt.truncate(0)
                        for file in files:
                            if file:
                                files_txt.write(file)
                except Exception as error:
                    set_error = str(error)
    
    if choice.lower() == "f":
        completed_shown = not completed_shown
        
    if choice.lower() == "e":
        sys.exit()
    
    #DEBUG
    if choice.lower() == "reset":
        with open("files.txt", "r") as files_txt:
            files = list(files_txt)
            for file in files:
                os.remove(file.strip()+".txt")
        with open("completed.txt", "w+") as completed:
            completed.seek(0)
            completed.truncate(0)
        with open("files.txt", "w+") as file_names:
            completed.seek(0)
            file_names.truncate(0)
        reset = True
    
    
    # add functionality to delete lists 
    # try:choice.split
    # if choice.split(" ")[0] == "reset":
    #     
    