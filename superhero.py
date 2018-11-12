class Hero:
    def __init__(self, name, starting_health=100):
            self.name = name
            self.starting_health = starting_health
            self.current_health = starting_health
            self.abilities = list()
            self.armors = list()
            self.deaths = 0
            self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)


    def attack(self):
        sum = 0
        for ability in self.abilities
            sum += ability.attack()
        return sum
 
    def take_damage(self, damage):
        self.current_health = self.current_health - damage
        ''' 
        This method should update self.current_health 
        with the damage that is passed in.
        '''

    def is_alive(self):
        if self.current_health > 0:
            return true
        else
            return false
        '''
        This function will 
        return true if the hero is alive 
        or false if they are not. 
        '''

    def fight(self, opponent):  
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        pass

    def defend(self):
        defense = 0
        if self.current_health == 0
            return 0
        else:
            for armor in self.armors
                defense += armor.defend()
            return defense
        '''
        This method should run the defend method on each piece of armor and calculate the total defense. 

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        '''
        pass

    def take_damage(self, damage_amt):
        ''' 
        Refactor this method to use the new defend method and to update the number of deaths if the hero dies in the attack.
        '''
        pass

    def add_kill(self, num_kills):
        self.kills += num_kills
        '''
        This method should add the number of kills to self.kills
        '''
        pass

    def fight(self, opponent):
        '''
        Refactor this method to update the number of kills the hero has when the opponent dies.
        '''
        pass

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_attack = random.randint(0, self.max_damage)
        return random_attack
        ''' 
        Return a random attack value 
        between 0 and max_damage.
        '''

class Weapon(Ability):
    def attack(self):
        random_attack_weapon = random.randint()
        return random.randint(self.max_damage /2, self.max_damage)
        """
        This method should should return a random value
        between one half to the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
class Team:
    def init(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)
        '''Add Hero object to heroes list.'''
        

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                return 0
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''

    def view_all_heroes(self):
        for hero in self.heroes
            print hero
        '''Print out all heroes to the console.'''
        pass

    def attack(self, other_team):
        '''
        This function should randomly select a living hero from each team and have them fight until one or both teams have no surviving heroes.

        Hint: Use the fight method in the Hero class.
        '''
        pass

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
        '''
        This method should reset all heroes health to their
        original starting value.
        '''
        pass

    def stats(self):
        '''
        This method should print the ratio of kills/deaths for each member of the team to the screen. 

        This data must be output to the console.
        '''
        pass

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)
        '''
        Return a random value between 0 and the 
        initialized max_block strength.
        '''
        pass

if __name__ == "__main__":
    # If you run this file from the terminal 
    # this block is executed.
    pass