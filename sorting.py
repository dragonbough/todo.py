import string
import time

list = []
orderedList = []
priorityList = []

def SortList(list):
    itemPriority = 0
    for item in list:
        for letter in item:
                nLetter = ord(letter)
                if letter == item[0]:
                    itemPriority += nLetter
                elif letter != item[0]:
                    itemPriority += (nLetter / (10 ** item.index(letter) + len(str(nLetter))))
        print(itemPriority)
        priorityList.append(itemPriority)
        print(priorityList)
    i = 0
    for item in list:
        list[i] = list[priorityList.index(min(priorityList))]
        priorityList.remove(list[i])
        i += 1
    return list
listlength = int(input ("How many things are in your list?"))
for i in range(listlength):
    list.append(input ("Add to your list"))
print("Sorting list...")
print(SortList(list))

