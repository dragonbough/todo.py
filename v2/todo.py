#todo object -- self.items [dict] of strings and completed (true or false), self.name, self.directory, self.file
#todo object will be saved to a list
#pickle will put dump all the todo objects into a binary file  

#validates the items passed in by making sure its an Item object even if inputted as a string or integer, and ensuring that the Item is a Item or 
#Todo object and not the same as the object validating it
def validated_items(object: object, items: list):
    new_items = []
    
    for item in items:
            if type(item) == str or type(item) == int:
                new_items.append(Item(str(item)))
            else:
                new_items.append(item)
        
    for item in new_items:
        if type(item) != Item and type(item) != Todo or item == object:
            return ValueError(f"Invalid item: {item}")
    
    return new_items

#item class that is passed into todo class -- represents individual item in todolist
class Item():
    def __init__(self, value: str):
        self.value = value
        self.completed = False
    
    def get_value(self):
        return self.value

    def set_completed(self, completed: bool):
        if type(completed) != bool:
            raise TypeError(f"{completed} invalid complete status")
        else:
            self.completed = completed

#todo class -- object that stores its name, items, and directory
class Todo():
    def __init__(self, name: str = "untitled", items: list = [], directory: str = "todos/"):
        
        self.name = name
        self.items = validated_items(self, items)
        self.directory = directory 
        self.completed = False

    
    def set_name(self, new_name: str):
        if type(new_name) is str:
            self.name = new_name
        else:
            raise ValueError("Todo name is not a string")
        
    def add_items(self, *args):
        
        self.items.extend(validated_items(self, args))
    
    #displays todo list
    def display(self, indent=0):
        
        #prints out the name of the todo list
        if indent == 0:
            print("-" * len(self.name))
            print(self.name)
            print(f"{"-" * len(self.name)}")
        
        #bullets for each indentation level
        bullets = ["--", "-", "~", ">" ]
        
        for item in self.items:
            
            #check for if item is completed or not
            if item.completed == True:
                check = " ✓"
            else:
                check = ""
            
            #if the item is a Todo list: it displays the items within the todo list under its name in bold
            if type(item) == Todo:
                #prints name of the sub-todo in bold with appropriate bullet based on the indent level
                open_bold = "\033[1m"
                close_bold = "\033[0m"
                print(f"{"    " * indent}{open_bold}{bullets[indent]} {item.name}{check}:{close_bold}")
                #calls display on that todo list -- displays all of todos items
                item.display(indent+1)
            else:
                #displays item with appropriate indent level
                print(f"{"    " * indent}{bullets[indent]} {item.get_value()}{check}")
    
    #sets all the items and itself as the completed status
    def set_completed(self, completed: bool):
        if type(completed) != bool:
            raise TypeError (f"{completed} invalid complete status")
        for item in self.items:
            item.set_completed(completed)
        self.completed = completed


########################################################################################


todo1 = Todo("this is a test", ["this", "is", "a", "test"])
todo1.add_items(Todo("sub list", ["this", "is", "a", "sub sub sub sub sub sub", "test"]))

todo1.display()