def BubbleSort(arr):
    for h in range(len(arr)):
        for i in range(len(arr)):
            if i != len(arr) - 1:
                if arr[i] > arr[i+1]:
                    x = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = x
    return arr

def InsertSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                x = arr[i]
                arr.pop(i)
                arr.insert(j, x)
    return arr

# def MergeSort(arr):
#     for i in range(len(arr)):
         #do something
    
def LinearSearch(arr, i):
    count = 0
    for x in arr:
        count += 1
        if x == i:
            return "Found, took " + str(count) + " steps"

def BinarySearch(arr, i):
    item = ""
    count = 0
    while item != i:
        item = arr[int(len(arr) / 2)]
        if item < i:
            del arr[:int(len(arr) / 2)]
            count+=1
        elif item > i:
            del arr[int(len(arr) / 2)]
            count+=1 
        else:
            return "Found, took " + str(count) + " searches"

array = input ("Input a list, with fully alphabetical/numerical items separated by commas and a space: ")
array = array.split(", ")
choice = input ("Would you like to sort [S] or search [W] this list")
if choice.lower() == "s":
    choice = input ("Would you like to perform a bubble [B], insert [I], or merge [M] sort")
    if choice.lower() == "b":
        print("Unsorted list: " + str(array))
        print("Sorted list: " + str(BubbleSort(array)))
    elif choice.lower() == "i":
        print("Unsorted list: " + str(array))
        print("Sorted list: " + str(InsertSort(array))) 
elif choice.lower() == "w":
    it = input ("Enter the item you are looking for")
    choice = input ("Would you like to perform a linear [L] or binary [B] search (for binary search list must be sorted)")
    if choice.lower() == "l":
        print (LinearSearch(array, it))
    elif choice.lower() == "b":
        print(BinarySearch(array, it))