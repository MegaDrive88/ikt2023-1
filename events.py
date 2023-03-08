from classes import *
def enemyread(lista):
    file = open('enemy.txt' , 'r', encoding='utf-8')
    for i in file:
        lista.append(Enemy(i))
    file.close()
def itemread(lista):
    file = open('allitems.txt' , 'r', encoding='utf-8')
    for i in file:
        lista.append(Item(i))
    file.close()
def saveread(lista, modszer):
    file = open('save.txt' , modszer, encoding='utf-8')
    if modszer == 'r':
        for i in file:
            lista.append(i.strip())
    else:
        return file
    file.close()
    
#<-multiplier, eddig tart, Kivitte-e, High-score->
#https://www.unrealengine.com/marketplace/en-US/product/1690-rpg-icons