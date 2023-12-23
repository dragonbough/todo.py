subjects = []
topics = []
subTopics = {}
subRanks = {}
topRanks = {}
topHours = []

#Ask for subjects until user inputs empty string (presses enter)
i = 1
subject = input("Enter Subject " + str(i) + " OR press enter to stop: ")
while len(subject) != 0:
    subjects.append(subject)
    subject = input("Enter Subject " + str(i+1) + " OR press enter to stop: ")
    i+=1

#For each subject asks for topics until user inputs empty string (presses enter).
for x in range(len(subjects)):
    i = 1
    topic = input("Enter Topic " + str(i) + " for \"" + subjects[x] + "\" OR press enter to stop: ")
    while len(topic) != 0:
        topics.append(topic)
        topic = input("Enter Topic " + str(i+1) + " for \"" + subjects[x] + "\" OR press enter to stop ")
        i+=1
    #Once the subject has its topics chosen the subject and topics are saved to the subTopics dictionary, the topics are cleared, 
    #and the subject is cycled to the next.
    subject = subjects[x]
    subTopics.update({subject : topics})
    topics.clear()

while True:
    #Asks for ranking of each subject and assigns it to the subRanks dictionary.
    for i in subjects:
        rank = int(input("Rank " + str(i) + " revision time on a scale of 1 - 10"))
        subRanks.update({i : rank})

    #Sorts and rebuild the dictionary based off of rank.
    sortedList=sorted(subRanks.values())
    for sortedKey in sortedList:
        for key, value in subRanks.items():
            if value==sortedKey:
                subRanks[key]=value

    #Displays the rankings of each subject and asks if the user is satisfied.
    for x in subRanks.keys():
        print ("Subject: " + str(x) + ", Rank: " + str(subRanks[x]))
    change = input("Change ranks?")
    if change == "yes":
        continue
    else:
        break

#Calculates and displays the amount of time allocated to each value based off of their rankings.
rTime = int(input ("How many hours in total do you want to spend revising this topic?"))
subHours = list(subRanks.values())
subjectValue = rTime / sum(subHours)
for i in range(len(subHours)):
    subHours[i-1] = round((subHours[i-1] * subjectValue), 2)
    print (str(subjects[i-1]) + ": " + str(subHours[i-1]) + "hours")


while True:
    #Asks for ranking of each topic and assigns it to the subRanks dictionary.
    for i in subTopics.values():
        rank = int(input("Rank " + str(i) + " revision time on a scale of 1 - 10"))
        topRanks.update({i : rank})

    #Sorts and rebuild the dictionary based off of rank.
    sortedList=sorted(topRanks.values())
    for sortedKey in sortedList:
        for key, value in topRanks.items():
            if value==sortedKey:
                topRanks[key]=value

    #Displays the rankings of each subject and topic and asks if the user is satisfied.
    for x in topRanks.keys():
        print ("Subject: ", list(subTopics.keys())[list(subTopics.values()).index(x)], "Topic: ", x, ", Rank: " + str(topRanks[x]))
    change = input("Change ranks?")
    if change == "yes":
        continue
    else:
        break

#Calculates and displays the amount of time allocated to each value based off of their rankings.
for x in subject:
    for y in topRanks[x]:
        topHours.append(y)
    topicValue = subHours[x] / sum(list(topRanks.values()))
for i in topRanks.keys():
    topRanks[i] = round((topRanks[i] * topicValue), 2)
    print (list(subTopics.keys())[list(subTopics.values()).index(i)], ", " + str(topRanks[i]) + ": " + str(topRanks[i]) + "hours")
    


#for i in range(len(hours)):
    #hours[i-1] = round((hours[i-1] * subjectValue), 2)
    #print (str(subjects[i-1]) + ": " + str(hours[i-1]) + "hours")
    