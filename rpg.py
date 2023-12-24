import random

stats = {"player":[100, 10, 10],
         "bat":[25, 20, 15],
         "spider":[10, 5, 50]}

health = 0
attack = 1 
speed = 2

def Battle(enemy):
    print ("What will you do?")
    print ("Attack")
    print ("Bag")
    choice = input("Run")
    if choice == "attack":
        print(PlayerAttack("bat"))
        
        
def PlayerAttack(enemy):
    damage = random.randint(stats["player"][attack] - 2, stats["player"][attack])
    stats[enemy][health] -= damage 
    return ("You dealt " + str(damage) + " damage against the " + enemy)

print("Welcome to game")
print("Battle against bat")
Battle("bat")