import string
import time

list = []
priorityList = []
orderedPList = []
orderedList = []
originalList = []

#For every item in the list (e.g apple, orange banana), it checks every single
#letter of the item, and if that letter is in the alphabet and it is the first
#letter of the word, it stores its priority in a variable which, if it is the 
#latter letters of the word, the priority of the latter is decimalised and added onto the main priority (first letter's priority) and added to the priority list
#The smallest number is then added to the orderedList and then removed from the priorityList. this order of the smallest number being removed from the priority list causes the 
# orderedList to align in a consecutive order.
def SortList(list):
    for item in list:
        for i in item:
            if i in string.ascii_letters:
                if item.index(i) == 0:
                    firstPriority = string.ascii_letters.index(item[0]) + 1
                elif item.index(i) > 0:
                    latterPriority = (string.ascii_letters.index(item[item.index(i)])) / (10 ** (item.index(i)))
                    priority = firstPriority + latterPriority
        priorityList.append(priority)
        originalList.append(priority)
        
    for item in list:
        orderedPList.insert(0, max(priorityList))
        priorityList.remove(max(priorityList))
    for item in list:
        orderedList.insert(orderedPList.index((originalList[(list.index(item))])), item)
    return orderedList, orderedPList
        

listlength = int(input ("How many things are in your list?"))
for i in range(listlength):
    list.append(input ("Add to your list"))
print("Sorting list...")
print(SortList(list))
