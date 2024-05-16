import random
class Enemy :
    type_of_enemy : str
    health_point : int = 15
    attack_damage : int = 1 

    def __init__(self,type_of_enemy, health_points = 10, attack_damage = 1) :
        self.__type_of_enemy = type_of_enemy
        self.health_point = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk (self): 
        print(f'Iam an {self.type_of_enemy} Enemys')

    def walk_fowrward(self):
        print(f'I am a {self.type_of_enemy} Be prepared to fight')
    
    def attack(self):
        print(f'{self.get_type_of_enemy()} attacks for {self.attack_damage} damage')
    
    def special_attack(self):
        print('Enemy has no special attack')

class Zombie(Enemy):
    def __init__(self,health_points,attack_damage):
        super().__init__(type_of_enemy='ZOMBIE',health_points=health_points,attack_damage=attack_damage)

    def talk(self):
        print('GRUMBLING')
    
    def spread_disease(self):
        print('The zombie is trying to spread infection')
    
    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_point += 2
            print('zombie regerenated 2 HP !')

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print('Ogre is slamming hand all around')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print('ogre ANGRY and Attack has increased by 4')

class Weapon :
    def __init__(self,weapon_type,Attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = Attack_increase

class Hero : 
    def __init__(self,health_point,attack_damage):
        self.health_point = health_point
        self.attack_damage = attack_damage
        self.is_weapon_equiped = False
        self.weapon : Weapon = None

    def equip_weapon (self):
        if self.weapon is not None and not self.is_weapon_equiped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equiped = True

    def attack(self):
        print(f'hero attacks for {self.attack_damage} damage ')
