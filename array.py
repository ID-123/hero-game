n = int(input('Tamaño inicial lista: '))

list = []

target = 0

for i in range (n) :
    x = input('Añade algo: ')
    list.append(x)
    if x == '0':
        continue
    else: 
        print('Desea añadir algo mas?: (s/n)')
        y = input()
        if y == 's':
            continue
        else:
            break

print(list)

def bin_search (list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        center = (left + right) // 2
        
        if list[center] == target:
            return center
        elif list [center] < target:
            left = center + 1
        else:
            right = center - 1
