import random

hero = 100
villain = 120
potion = 3




def health_status(villain):
    hp_bar = []
    for x in range(1, villain):
        if x % 5 == 0:
            hp_bar.append('#')
        
    print(f'Hitpoints: {villain} ', *hp_bar, sep='' ) # '*' unpacks the array, 'sep=' makes the spaces between characters void ('')


health_status(villain)

def hero_turn(villain, potion, hero):
    

    print('''
        --- Choose an action:
          1. Normal Attack
          2. Special Attack
          3. Heal

          ''')
    
    h_op = input('-- ')

    if h_op == '1':
        
        h_att = random.randint(10,25)
        villain -= h_att
        print (f'Damage made: {h_att}, \nVillain remaining hp : {villain}')

        return villain
    
    elif h_op == '2':
    
        spa = random.randint(1,2)
    
        if spa == 12:
    
            spa_d = random.randint(30,50)
            villain -= spa_d
            print(f'Attack suceeded! Damage made: {spa_d}')
            return villain
    
        else:
            print('You failed.')
    
    elif h_op == '3':
        
        while potion > 0:
            potion -= 1
            hero += 20
            print(f'Hp restored, now have {hero} points left.')
            return hero, potion
        else:
            print('No potions available.')

def vill_turn(hero):    
    print('Villain turn.')

    v_att = random.randint(15,20)
    hero -= v_att
    print(f'Damage taken: {v_att}. Current hitpoints: {hero}')
    return hero
            

villain = hero_turn(villain, potion, hero)
health_status(villain)
hero = vill_turn(hero)       
print('Current hp: ', hero)
