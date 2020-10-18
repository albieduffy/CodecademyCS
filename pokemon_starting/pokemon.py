class Pokemon:
  def __init__(self, name, level, poke_type, max_health, knocked_out=False):
    self.name = name
    self.level = level
    self.poke_type = poke_type
    self.max_health = max_health
    self.curr_health = max_health
    self.knocked_out = knocked_out

  def lose_health(self, damage):
    self.curr_health -= damage
    self.curr_health = max(self.curr_health, 0)
    print(f'{self.name} now has {self.curr_health} health')
    self.knock_out()

  def regain_health(self, restore):
    self.curr_health += restore
    self.curr_health = min(self.max_health, self.curr_health)
    print(f'{self.name} now has {self.curr_health} health')

  def knock_out(self):
    if self.curr_health == 0:
      self.knocked_out = True
      print(f'{self.name} is knocked out')

  def revive(self):
    self.curr_health = self.max_health
    self.knocked_out = False
    print(f'{self.name} is now revived')

  def attack(self, opponent):
    opponent.lose_health(self.level)

  def __repr__(self):
    return self.name

class Trainer:
  def __init__(self, name, pokemon, potions):
    self.name = name
    self.pokemon = pokemon
    self.potions = potions
    self.currently_active = 0

  def use_potion(self, potion):
    print(f'{self.name} used a {potion.name} on {self.pokemon[self.currently_active]}')
    self.pokemon[self.currently_active].regain_health(potion.healing)

  def attack(self, opponent):
    print(f'{self.name}\'s {self.pokemon[self.currently_active]} attacked {opponent.name}\'s {opponent.pokemon[opponent.currently_active]}')
    self.pokemon[self.currently_active].attack(opponent.pokemon[opponent.currently_active])

  def switch(self, selection):
    self.currently_active = selection
    print(f'{self.name} switched to {self.pokemon[self.currently_active]}')

class Potion:
  def __init__(self, name, healing):
    self.name = name
    self.healing = healing


charmander = Pokemon('Charmander', 5, 'Fire', 30)

bulbasaur = Pokemon('Bulbasaur', 5, 'Grass', 30)

normal = Potion('Normal Potion', 10)
super_potion = Potion('Super Potion', 25)

ash = Trainer('Ash', [charmander], [normal])
gary = Trainer('Gary', [bulbasaur], [super_potion])

ash.attack(gary)
gary.attack(ash)

ash.attack(gary)
gary.attack(ash)

ash.use_potion(normal)

gary.attack(ash)
gary.attack(ash)
gary.attack(ash)
gary.attack(ash)
gary.attack(ash)
gary.attack(ash)
