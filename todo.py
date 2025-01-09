# text files with multiple lines separating each tasks
# input validation, error handling
# on run - t=latest task to do a=append task d=delete task

#init defines the todolist and creates the file 
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

# #append appends a new line to todo list
def append(filename, task):
    with open(filename, "a") as todo:
        if type(task) is not str:
            raise TypeError("append() type error: task not a string.")
        if len(task) == 0:
            raise ValueError("append() value error: task is empty")
        todo.write(task + "\n")

#delete takes in task line number to delete and removes it from text file
def delete(filename, task_index):
    with open(filename, "r+") as todo:
        tasks = todo.read()
        print(tasks)
        
##################
    
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
        else:
            while type(latest_file) is not str and not latest_file:
                latest_file = input("Enter todo list name")

choice = ""
while choice.lower() != "e":

    while not choice or choice != "e":
        current_file = init(latest_file)
        print(f"\n{current_file}")
        print("[t] display tasks  [a] append task  [d] delete task  [l] lists  [e] exit")
        choice = input("")
        if choice.lower() == "t":
            try:
                print ("")
                for task in display(current_file):
                    print (task)
            except IndexError:
                print ("\nList is empty!")
            
        elif choice.lower() == "a":
            append(current_file, "~" + input("\n~"))
            
        if choice.lower() == "d":
            with open(current_file) as todo:
                num = 0
                for task in todo:
                    num += 1
                    print (f"~{num}~{task}")
                tasks = list(todo)
            index = None
            while type(index) != int or type(index) != float or index < 1 or index > len(tasks):
                index = input("")
            delete(current_file, index)
