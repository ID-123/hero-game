colores = ['rojo', 'verde', 'amarillo', 'azul']

indice = colores.index('amarillo')

print(colores)
print (indice)

existe = 'amarillo' in colores

colores.append('rosado')
colores.insert(0, 'gris')

print(colores)



color = ''

def agg_unico(color, lista):
    agg = False

    if color in colores:
        agg = False
    else:
        agg = True
        list.append(color)
    return (agg)