import random

#Stats for the player and mobs in the world, in order of health, attack and then speed.
stats = {"player":[100, 10, 10],
         "Bat":[25, 20, 15],
         "Spider":[10, 5, 50],
         "Slime":[25, 10, 5]}
#Stats for the items in the world with tags and then integers after
items = {"potion":["health", +1],
         "boost potion":["health", -1, "attack", +1]}

health = 0
attack = 1 
speed = 2

bag = ["Potion", "Boost Potion"]

runCount = 0

def PlayerAttack(enemy):
    damage = random.randint(stats["player"][attack] - 2, stats["player"][attack])
    stats[enemy][health] -= damage 
    return ("You dealt " + str(damage) + " damage against the " + enemy)

def Select(item):
    message = []
    if item not in items:
        return False
    elif "health" in items[item]:
        healthGain = items[item][items[item].index("health") + 1]
        stats["player"][health] += healthGain
        if healthGain > 0:
            if len(message) >= 1:
                message.append("and you gained " + str(healthGain) + " health")
            else:
                message.append("You gained " + str(healthGain) + " health")
        if healthGain < 0:
            if len(message) >= 1:
                message.append("and you lost " + str(healthGain) + " health")
            else:
                message.append("You lost " + str(healthGain) + " health")
    if "attack" in items[item]:
        attackGain = items[item][items[item].index("attack") + 1]
        stats["player"][attack] += attackGain
        if attackGain > 0:
            if len(message) >= 1:
                message.append("and you gained " + str(attackGain) + " attack")
            else:
                message.append("You gained " + str(attackGain) + " attack")
        if attackGain < 0:
            if len(message) >= 1:
                message.append("and you lost " + str(attackGain) + " attack")
            else:
                message.append("You lost " + str(attackGain) + " attack")
    print ("You used the " + item)
    return " ".join(message) + "!"

def enemyAttack(enemy):
    damage = random.randint(stats[enemy][attack] - 2, stats[enemy][attack])
    stats["player"][health] -= damage 
    return ("\nThe " + enemy + " dealt " + str(damage) + " damage against you!\n")

def Battle(enemy):
    global turn 
    global runCount
    print ("You have been approached by a " + enemy + "!")
    if stats["player"][speed] > stats[enemy][speed]:
        turn = "player"
    else:
        turn = enemy
    while stats[enemy][health] > 0:
        while turn == enemy:
            print(enemyAttack(enemy))
            turn = "player"
        while turn == "player":
            print ("HP: " + str(stats["player"][health]))
            print (enemy + " HP: " + str(stats[enemy][health]))
            print ("What will you do?")
            print ("Attack")
            print ("Bag")
            choice = input("Run\n")
            if choice == "attack":
                print(PlayerAttack(enemy))
                turn = enemy 
            if choice == "bag":
                for i in bag:
                    print (i)
                while True:
                    itemChoice = input ("What item will you use?\n")
                    result = Select(itemChoice)
                    if result == False:
                        print("Invalid item selection")
                        continue
                    else:
                        print(result) 
                        break
                turn = enemy 
            if choice == "run":
                probability = (((stats["player"][speed] * 128)/stats[enemy][speed]) + 30 * runCount) // 265
                if random.randint(0, 255) < probability:
                    runCount += 1
                    return "end"
                else:
                    runCount += 1
                    print("You failed to escape!")
                    turn = enemy
    if stats["player"][health] == 0:
       print ("You died!")
    else:
        print ("You have successfully defeated the " + enemy)

Battle("Slime")
print ("H")
Battle("Bat")