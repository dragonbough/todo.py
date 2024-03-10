subjects = []
subRanks = {}
subHours = {}

#Ask for subjects until user inputs empty string (presses enter)
i = 1
subject = input("Enter Subject " + str(i) + " OR press enter to stop: ")
while len(subject) != 0:
    subjects.append(subject)
    subject = input("Enter Subject " + str(i+1) + " OR press enter to stop: ")
    i+=1
    
#Asks for ranking of each subject and assigns it to the subRanks dictionary.
for i in subjects:
    rank = int(input("Rank " + str(i) + " revision time on a scale of 1 - 9"))
    if len(str(rank)) == 2:
        rank = (int(str(rank)[0]) + int(str(rank)[1])) / 2
    subRanks.update({i : rank})

#Sorts and rebuild the dictionary based off of rank.
sortedList=sorted(subRanks.values())
for sortedKey in sortedList:
    for key, value in subRanks.items():
        if value==sortedKey:
            subRanks[key]=value

#Displays the rankings of each subject 
for x in subRanks.keys():
    print (str(x) + ", Rank: " + str(subRanks[x]))

#Calculates and displays the amount of time allocated to each value based off of their rankings.
avgHours = int(input("How many hours on average do you want to spend revising a day?"))
for i in subRanks.keys():
    till = int(input("How many days do you have until your " + i + " exam?")) * 12
    hours = int(round((till / sum(subRanks.values())) * subRanks[i]))
    subHours.update({i : hours})

for x in subHours.keys():
    print (str(x) + ", Hours: " + str(subHours[x]))

        
