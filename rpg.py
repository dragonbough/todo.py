import random

#Stats for the player and mobs in the world, in order of health, attack, defense and then speed.
stats = {"player":[100, 10, 10, 10],
         "Bat":[70, 15, 3, 20],
         "Spider":[90, 12, 8, 15],
         "Slime":[80, 8, 5, 5],
         "DeathTest":[1000, 100, 100, 100],
         "WinTest":[1, 1, 1, 1] }

#Stats for the items in the world with tags and then integers after
items = {"potion":["health", +1],
         "boost potion":["health", -1, "attack", +1]}

health = 0
attack = 1 
defense = 2
speed = 3

playerHealth = 0
enemyHealth = 0
playerAtt = 0 
enemyAtt = 0
playerDefense = 0
enemyDefense = 0
playerSpeed = 0
enemySpeed = 0

bag = ["Potion", "Boost Potion"]

runCount = 0

winCount = 0
lossCount = 0 

def PlayerAttack(enemy):
    global playerAtt, enemyHealth, enemyDefense
    if playerAtt >= enemyDefense:
        damage = random.randint(playerAtt - 2, playerAtt) * 2 - enemyDefense
    else:
        damage = random.randint(playerAtt - 2, playerAtt) * playerAtt / enemyDefense
    enemyHealth -= damage 
    return ("\nYou dealt " + str(damage) + " damage against the " + enemy + "\n")

def Select(item):
    global playerHealth, playerAttack, playerDefense
    message = []
    if item not in items:
        return False
    elif "health" in items[item]:
        healthGain = items[item][items[item].index("health") + 1]
        playerHealth += healthGain
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
        playerAttack += attackGain
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
    if "defense" in items[item]:
        defenseGain = items[item][items[item].index("defense") + 1]
        playerDefense += defenseGain
        if defenseGain > 0:
            if len(message) >= 1:
                message.append("and you gained " + str(defenseGain) + " defense")
            else:
                message.append("You gained " + str(defenseGain) + " defense")
        if defenseGain < 0:
            if len(message) >= 1:
                message.append("and you lost " + str(defenseGain) + " defense")
            else:
                message.append("You lost " + str(defenseGain) + " defense")
    print ("You used the " + item)
    return " ".join(message) + "!"

def enemyAttack(enemy):
    global enemyAtt, playerHealth, playerDefense
    if enemyAtt >= playerDefense:
        damage = random.randint(enemyAtt - 2, enemyAtt) * 2 - playerDefense
    else: 
        damage = random.randint(enemyAtt - 2, enemyAtt) * enemyAtt / playerDefense
    playerHealth -= damage 
    return ("\nThe " + enemy + " dealt " + str(damage) + " damage against you!\n")

def Battle(enemy):
    global turn, runCount, playerHealth, enemyHealth, playerAtt, enemyAtt, playerSpeed, enemySpeed, winCount, lossCount
    playerHealth = stats["player"][health]
    enemyHealth = stats[enemy][health]
    playerAtt = stats["player"][attack] 
    enemyAtt = stats[enemy][attack]
    playerDefense = stats["player"][defense]
    enemyDefense = stats[enemy][defense]
    playerSpeed = stats["player"][speed]
    enemySpeed = stats[enemy][speed]
    enemyBarHealth = 100 / enemyHealth
    run = False 

    print ("\nYou have been approached by a " + enemy + "!")
    if playerSpeed > enemySpeed:
        turn = "player"
    else:
        turn = enemy
    while enemyHealth > 0 and playerHealth > 0:
        while turn == enemy:
            print(enemyAttack(enemy))
            turn = "player"
        while turn == "player":
            if playerHealth <= 0:
                break
            healthBar = []
            for i in range(round(playerHealth / 8.3)):
                healthBar.append("_")
            print ("".join(healthBar))
            healthBar.clear()
            print ("Your HP: " + str(playerHealth))
            for i in range(round((enemyBarHealth * enemyHealth) / 8.3)):
                healthBar.append("_")
            print ("".join(healthBar))
            healthBar.clear()
            print (enemy + " HP: " + str(enemyHealth) + "\n")
            print ("What will you do?:")
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
                probability = (((playerSpeed * 128) / enemySpeed) + 30 * runCount) // 265
                if random.randint(0, 255) < probability:
                    runCount += 1
                    run = True 
                    break
                else:
                    runCount += 1
                    print("You failed to escape!")
                    turn = enemy
        if enemyHealth <= 0:
            print ("You successfully slayed the " + enemy + "!")
            print ("You win!")
            winCount += 1
            return "win"
        elif playerHealth <= 0:
            print ("You pass out at the feet of the " + enemy)
            print ("You lost!")
            lossCount += 1 
            return "loss"
        elif run == True:
            print ("You successfully escaped from the " + enemy + "!")
            print ("Yipee!")
            return "escape"


        
    

Battle("Slime")