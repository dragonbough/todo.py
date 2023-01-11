list = []
orderedList = []

def SortList(list):
    k = len(list)
    for i in range(k):
        for j in range (k - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


listLength = input ("How many things are in your list?")
for i in range(int(listLength)):
    list.append(input ("Add to your list"))
print(SortList(list))