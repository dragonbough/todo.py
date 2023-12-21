subjects = []
topics = []
subdict = {}
rankdict = {}

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
    #Once the subject has its topics chosen the subject and topics are saved to the subdict dictionary, the topics are cleared, 
    #and the subject is cycled to the next.
    subject = subjects[x]
    subdict.update({subject : topics})
    topics.clear()

while True:
    #Asks for ranking of each subject and assigns it to the rankdict dictionary.
    for i in subjects:
        rank = int(input("Rank " + str(i) + " revision time on a scale of 1 - 10"))
        rankdict.update({i : rank})

    #Sorts and rebuild the dictionary based off of rank.
    sortedList=sorted(rankdict.values())
    for sortedKey in sortedList:
        for key, value in rankdict.items():
            if value==sortedKey:
                rankdict[key]=value

    #Displays the rankings of each subject and asks if the user is satisfied.
    for x in rankdict.keys():
        print ("Subject: " + str(x) + ", Rank: " + str(rankdict[x]))
    change = input("Change ranks?")
    if change == "yes":
        continue
    else:
        break

#Calculates and displays the amount of time allocated to each value based off of their rankings.
rTime = int(input ("How many hours in total do you want to spend revising this topic?"))
hours = list(rankdict.values())
subjectValue = rTime / sum(hours)
for i in range(len(hours)):
    hours[i-1] = round((hours[i-1] * subjectValue), 2)
    print (str(subjects[i-1]) + ": " + str(hours[i-1]) + "hours")
    hours[i-1] = round((hours[i-1] / 12), 2)
    print (str(subjects[i-1]) + ": " + str(hours[i-1]) + "hours (Daily)")
    