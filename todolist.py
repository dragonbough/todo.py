# A dictionary of every created list and its values
todoListDict = {}

# Goes through every item in the to-do list and prints them on new lines with a number in front. e.g 1.xxx 2.yyy
def DisplayList(array):
    for i in range(len(array)):
        print (str(i + 1) + ". " + array[i])

# List name is defined and it asks for items to be added to list continuously until string passed is empty. List name and values added to dict.
def CreateList():
    todoList = []
    listName = input ("What would you like to call your todo list? ")
    endAppend = False
    i = 1
    while endAppend == False:
        task = input ("\nInput Task (" + str(i) + "); Stop [ENTER]:  ")
        if len(task) > 0:
            todoList.append(task)
            DisplayList(todoList)
            i += 1
        else:
            endAppend = True 
    todoListDict.update({listName:todoList})


def EditList(array):
    DisplayList(array)
    choice = input ("Sort [S] Add tasks [A] Delete tasks[D] ")
    if choice.lower() == "s":
        newOrder = []
        for i in array:
            newOrder.append(" ")
        for i in array:
            DisplayList(newOrder)
            print (i)
            while True:
                index = int(input("Where would you like to put this task?")) - 1
                if newOrder[index] == " ":
                    newOrder[index] = i
                    break
                else:
                    print ("Invalid slot")
                    newOrder[newOrder.index(" ")] = i
        todoListDict.update({list(todoListDict.keys())[list(todoListDict.values()).index(array)]:newOrder})
    if choice.lower() == "a":
        endAppend = False
        i = len(array)
        while endAppend == False:
            task = input ("\nInput Task (" + str(i) + "); Stop [ENTER]:  ")
            if len(task) > 0:
                array.append(task)
                DisplayList(array)
                i += 1
            else:
                endAppend = True
    if choice.lower() == "d":
        delTasks = list(input ("Enter the task numbers you want to delete separated by commas.").split(","))
        for i in range(len(delTasks)):
            
            

print ("-----------------")
print ("Welcome to PyList")
print ("-----------------\n")

if len(todoListDict) == 0:
    CreateList()

while True:   
    print ("\nYour Todo Lists:\n")
    for i in todoListDict.keys():
        print(str(list(todoListDict.keys()).index(i) + 1) + ". " + i)
    choice = input ("\nCreate New [C] Select [S]")
    if choice.lower() == "c":
        CreateList()
    if choice.lower() == "s":
        if len(list(todoListDict.keys())) > 1:
            listSelected = int(input ("Select list: "))
        else:
            listSelected = 1
        print (">" + list(todoListDict.keys())[listSelected - 1])
        choice = input ("View [V] Edit [E] Archive [A] Deselect [D]\n")
        if choice.lower() == "v":
            print (list(todoListDict.keys())[listSelected - 1] + ": ")
            DisplayList(todoListDict[list(todoListDict.keys())[listSelected - 1]])
        if choice.lower() == "e":
            EditList(todoListDict[list(todoListDict.keys())[listSelected - 1]])
        if choice.lower() == "a":
            finalchoice = input ("Are you SURE you want to delete your list? It will be gone forever. [Y]/[N]")
            if finalchoice.lower() == "y":
                del todoListDict[list(todoListDict)[listSelected-1]]







