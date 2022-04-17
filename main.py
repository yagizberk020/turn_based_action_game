import random

min_chance, max_chance = 1, 100
min_damage, max_damage = 10, 25
upgrade_amount = 5
health = 100
enemy_health = 100
enemy_killed = 0
money = 10
gain_of_kill = 10
cost_of_upgrade = 3
cost_of_health = 2
damage = random.randint(min_damage, max_damage)
round_ = 1

while round_ < 20:
    action = input("heal/attack/upgrade ")
    print("round", round_)
    damage = random.randint(min_damage, max_damage)
    round_ += 1

    attack_success_threshold = 0.3 # %30

    if action == "attack":

        if random.random() > attack_success_threshold:
            # Decrease enemy health by a random number between min_damage and max damage
            enemy_health -= damage
        else:
            # Enemy hurt you
            health -= damage
        # check if you are dead
        if health <= 0:
            print("GAME OVER")
            break
        # Check if your enemy is dead
        if enemy_health <= 0:
            enemy_health = 100
            money += gain_of_kill
            enemy_killed += 1
            print(f"You have {money} money and have killed {enemy_killed} enemies so far")

    elif action == "heal":
        # if you have enough money your health will improve by a random number between min_damage and max damage
        if money >= cost_of_health:
            money -= cost_of_health
            health += damage
            print(f"you have {health} health and {money} money")
        else:
            print("sorry you dont have enough money you couldn't heal yourself")
    elif action == "upgrade":
        # if you have enough money min and max damage parameters will be increased by upgrade amount
        if money >= cost_of_upgrade:
            money -= cost_of_upgrade
            min_damage += upgrade_amount
            max_damage += upgrade_amount
            print(f"You have {money} money and new damage values are ({min_damage}, {max_damage})")
        else:
            print("Sorry, you don't have enough money to upgrade!")

    print(f"Money: {money}, Health: {health}, Num of enemies killed: {enemy_killed}, enemy healt: {enemy_health} ")


print(f"Money: {money}, Health: {health}, Num of enemies killed: {enemy_killed}")
