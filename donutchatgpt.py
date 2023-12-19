import random

class Pokemon:
    def __init__(self, name, level, ptype, moves):
        self.name = name
        self.level = level
        self.ptype = ptype
        self.moves = moves
        self.max_hp = level * 5
        self.current_hp = self.max_hp
        self.attack = level * 2
        self.defense = level * 2
        self.special_attack = level * 2
        self.special_defense = level * 2
        self.speed = level * 2
        self.is_fainted = False
        self.status = None
        self.stat_changes = {"attack": 0, "defense": 0, "special_attack": 0, "special_defense": 0, "speed": 0}

    def __str__(self):
        return f"{self.name} (Level {self.level} {self.ptype}) HP: {self.current_hp}/{self.max_hp}"

    def show_moves(self):
        for i, move in enumerate(self.moves):
            print(f"{i+1}. {move.name} ({move.type}, {move.power} power, {move.accuracy}% accuracy)")

    def choose_move(self):
        while True:
            print(f"What will {self.name} do?")
            self.show_moves()
            choice = input("> ")
            try:
                index = int(choice) - 1
                move = self.moves[index]
                return move
            except:
                print("Invalid choice. Try again.")
                continue

    def attack(self, other_pokemon, move):
        damage = self.calculate_damage(other_pokemon, move)
        other_pokemon.current_hp -= damage
        print(f"{self.name} used {move.name} and did {damage} damage to {other_pokemon.name}!")
        if other_pokemon.current_hp <= 0:
            other_pokemon.current_hp = 0
            other_pokemon.is_fainted = True
            print(f"{other_pokemon.name} fainted!")
            self.gain_exp(other_pokemon)

    def calculate_damage(self, other_pokemon, move):
        if move.power is None:
            return 0

        type_effectiveness = self.get_type_effectiveness(move.type, other_pokemon.ptype)

        critical_hit = False
        if random.random() < (self.speed / 512):
            critical_hit = True

        modifier = random.uniform(0.85, 1.00)
        if critical_hit:
            modifier *= 2
        modifier *= type_effectiveness
        modifier *= random.uniform(0.85, 1.00)

        attack_stat = self.attack
        if move.category == "Special":
            attack_stat = self.special_attack

        defense_stat = other_pokemon.defense
        if move.category == "Special":
            defense_stat = other_pokemon.special_defense

        damage = (((2 * self.level + 10) / 250) * (attack_stat / defense_stat) * move.power + 2) * modifier

        return int(damage)

    def get_type_effectiveness(self, move_type, target_type):
        effectiveness = 1
        for t in move_type:
            for tt in target_type:
                effectiveness *= TypeChart[t][tt]
        return effectiveness

    def gain_exp(self, other_pokemon):
        exp_gain = other_pokemon.level * 20
        print(f"{self.name} gained {exp_gain} exp!")
        self.check_level_up(exp_gain)

    def check_level_up(self, exp_gain):
        if self.level == 100:
           