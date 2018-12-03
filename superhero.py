import random
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0
   
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
           total += ability.attack()
        return total
            
    def take_damage(self, damage):
        self.current_health -= damage

    def add_kill(self, num_kills):
        self.kills += num_kills
        
    def is_alive(self):
        return self.current_health > 0
            
    def fight(self, opponent):
        '''Runs a loop to attack opponent until someoe dies'''
        fighting = True
        while fighting:
            hero_damage = self.attack()
            opponent_damage = self.attack()
            opponent.take_damage(hero_damage)
            self.take_damage(opponent_damage)
            if self.is_alive():
                self.add_kill(1)
                opponent.deaths += 1
                fighting = False
            else:
                opponent.add_kill(1)
                self.deaths += 1
                fighting = False
       
    def add_weapon(self, weapon):
        '''
        This method will append the weapon object passed in as an argument to the list of abilities that already exists -- self.abilities.
        This means that self.abilities will be a list of abilities and weapons.
        '''
        weaponry = self.abilities.append(weapon)
        return weaponry
  
    def add_armor(self, armor):
        '''
        This method will add the armor object that is passed in to the list of armor objects definied in the initializer as self.armors.
        '''
        armory = self.armors.append(armor)
        return armory
    def defend(self):
        '''
        This method should run the block method on each piece of armor 
        and calculate total defense
        If the hero's health is zero return zero
        '''
        total_def = 0
        if self.current_health == 0:
            return 0
        else:
            for armor in self.armors:
                total_def += armor.block()
            return total_def
    
class Ability:
    def __init__ (self, name, max_attack):
        '''Initialize starting values'''
        self.name = name
        self.max_attack = max_attack
        
    def attack(self):
        '''Returns attack value between 0 and full attack'''
        return random.randint(0, self.max_attack)

class Weapon(Ability):
    def attack(self):
        '''returns a random value between one half to full attack power'''
        return random.randint(self.max_attack//2, self.max_attack)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block
        
    def block(self):
        '''returns a random value between 0 and max_block'''
        return random.randint(0, self.max_block)

class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.team_name = team_name
        self.heroes = []

    def add_hero(self, Hero):
        '''Add hero object to heroes list.'''
        self.heroes.append(Hero)

    def remove_hero(self, name):
        '''Removes hero from hero list.'''
        self.heroes.remove(name)
  
    def view_heroes(self):
        '''Prints out all heroes to console.'''
        for hero in self.heroes:
            print("{}".format(hero.name))
            
    def alive_heroes(self):
        '''adds heroes that are still alive to a list'''
        alive_list = []
        for hero in self.heroes:
            if hero.is_alive():
                alive_list.append(hero)

        return alive_list

    def attack(self, opponents):
        while len(self.alive_heroes()) > 0 and len(opponents.alive_heroes()) > 0:
            hero = random.choice(self.alive_heroes())
            opponent = random.choice(opponents.alive_heroes())
            hero.fight(opponent)
            opponent.fight(hero)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
    
    def stats(self):
        '''
        This method should print the ratio of 
        kills/deaths for each member of the 
        team to the screen. 
        This data must be output to the console.
        '''
        for hero in self.heroes:
            print("{} had {} kills and {} deaths.".format(hero.name, hero.kills, hero.deaths))

class Arena:
    def __init__(self):
      self.team_one = None
      self.team_two = None

    def create_ability(self):
        '''
        This method will let user create an ability,
        prompt them for necessary info,
        return the new ability object.
        '''
        print("Abilities!")
        ability_input= input("Name your ability: ")
        max_input = int(input("What is the max damage of your ability: "))
        ability = Ability(ability_input, max_input)
        return ability

    def create_weapon(self):
        '''
        This method will let user create a weapon.
        prompt them for necessary info,
        return new weapon
        '''
        print("Weapon!")
        weapon_input = input("What is the name of your weapon?: ")
        max_input = int(input("What is the max damage of your weapon?: "))
        weapon = Weapon(weapon_input, max_input)
        return weapon

    def create_armor(self):
        ''' 
        This method lets user create armor,
        prompt them for necessary info,
        return new armor object
        '''
        print("Armor!")
        armor_input = input("Name your armor: ")
        max_input = int(input("What is the max defense of your armor?: "))
        armor = Armor(armor_input, max_input)
        return armor

    def create_hero(self):
        '''
        This method lets user create a hero,
        user should specify if they want armor, weapons, and abilities,
        return new hero object
        '''
        hero_input = input("Name your Hero!: ")
        user_hero = Hero(hero_input)
        user_hero.add_ability(self.create_ability())
        user_hero.add_armor(self.create_armor())
        user_hero.add_weapon(self.create_weapon())
        return user_hero

    def build_team(self):
        team_name = input("Team Name?: ")
        team = Team(team_name)
        hero_num_input = int(input("How may heroes are on your team?: "))
        while hero_num_input > 0:
            hero = self.create_hero()
            hero_num_input -= 1
            team.add_hero(hero)
        return team
        
    def build_team_one(self):
        '''
        This method will let user create team one,
        prompt them for number of heroes,
        call self.hero() for every hero the user wants to add,
        add created hero to team one
        '''
        self.team_one = self.build_team()
        
    def build_team_two(self):
        '''
        This method will let user create team two,
        prompt them for number of heroes,
        call self.hero() for every hero the user wants to add,
        add created hero to team two
        '''
        self.team_two = self.build_team()

    def team_battle(self):
        '''
        This method battles with both teams,
        call the attack method in team objects for functionality
        '''
        self.team_one.attack(self.team_two)
        
    def show_stats(self):
        '''
        This method prints out battle stats, kill/death ratio,
        winning team, surviving heros
        '''
        self.team_one.stats()
        self.team_two.stats()

        if (len(self.team_one.alive_heroes()) > 0):
            print("Team one is the winner!")
        else:
            print("Team two is the winner!")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()