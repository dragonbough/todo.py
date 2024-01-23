todoListDict = {}

def DisplayList(array):
    for i in array:
        print (str(array.index(i) + 1) + ". " + i)

def CreateList():
    todoList = []
    listName = input ("What would you like to call your todo list? ")
    endAppend = False
    while endAppend == False:
        task = input ("Add a task to your todo list; ENTER to stop:  ")
        if len(task) > 0:
            todoList.append(task)
            DisplayList(todoList)
        else:
            endAppend = True 
    todoListDict.update({listName:todoList})

def ViewList():
    
    
def EditList(listName):
    

print ("Welcome to PyList")
if len(todoListDict) == 0:
    CreateList()
print (*todoListDict.keys())
choice = input ("View, Edit or ")
listName = ""
while listName not in todoListDict.keys():
    listName = input ("Which todo list would you like to view?")
DisplayList(listName)




