import random

hero = 100
h_att = 0
heal = 20
spa = 0

villain = 120
v_att = 0

def gen_dmg():
    # v_att = random.randint(15,20)
    
    villain -= h_att
    
    # h_att = random.randint(10, 25)
    
    hero -= v_att

    spa = random.randint(30,50) # 50% chance
    print()

def status():
    print(hero)
    # Hp bar (optional)
    print('####################')
    
    print(villain)

def ply_turn():
    print('Menu')
    h_att = random.randint(10, 25)
    

def enm_turn():
    print()
    v_att = random.randint(15,20)

def win_lose():
    if hero == 0:
        print ('Game over, you lose.')
        
    elif villain == 0:
        print('you win!!')
