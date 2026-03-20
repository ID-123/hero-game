import random

hero = 100
villain = 120
potion = 3

chance = random.randint(0,9)

print(f'Crit: {chance}')

def health_bar(n):
    
    hp_bar = []
    for x in range(1, n):
        if x % 4 == 0:
            hp_bar.append('X')
        
    print(f'Hitpoints: {n} \n', *hp_bar, sep='' ) # '*' unpacks the array, 'sep=' makes the spaces between characters void ('')



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
        crit = random.randint(0,9)
        print(f'Roll: {crit}')

        if crit == chance:
            h_att *= 2
            villain -= h_att
            print (f'Critical hit! Damage made: {h_att}')
        else:
            villain -= h_att
            print (f'You attack. \nDamage made: {h_att}')

        
    
    elif h_op == '2':
    
        spa = random.randint(0,1)
        print(f'Roll_spa: {spa}')
    
        if spa == 1:
    
            spa_d = random.randint(30,50)
            crit = random.randint(0,9)
            print(f'Roll: {crit}')

            if crit == chance:
                spa_d *= 2    
                villain -= spa_d
                print(f'Critical attack suceeded! Damage made: {spa_d}\n')
            
            else: 
                villain -= spa_d
                print(f'Attack suceeded! Damage made: {spa_d}\n')
            
            
    
        else:
            print('You failed.\n')
            

    
    elif h_op == '3':
        
        if potion > 0:
            potion -= 1
            hero += 20
            print(f'Hp restored, now have {hero} points left.\n')
        else:
            print('No potions available.\n')
            
    
    else:
        print('Invalid option, choose again.\n')

    return hero, villain, potion   
        
             

def vill_turn(hero):    
    
    print('-- Villain turn --')

    v_att = random.randint(15,20)
    hero -= v_att
    print(f'Enemy attacks. \nDamage taken: {v_att}. ') # \nCurrent hitpoints: {hero}\n
    return hero
        

        
def game(hero, villain, potion):
    while hero >= 0:
        hero, villain, potion = hero_turn(villain, potion, hero) 
        health_bar(villain) 
        hero = vill_turn(hero)
        health_bar(hero)

        if hero <= 0:
            print ('-- Game over, you lose. --')
            break

        elif villain <= 0:
            print('-- You win!! --')
            break

game(hero, villain, potion)



