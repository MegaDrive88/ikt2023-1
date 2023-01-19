class Enemy:
    def __init__(self ,sor):
        data = sor.strip().split(',')
        self.name = data[0]
        self.hp = int(data[1])
        self.isBoss = bool(data[2])
class Item: # 4 hosszú mindegyik type, kivéve mag nál
    def __init__(self, sor):
        data = sor.strip().split(',')
        self.name = data[0]
        self.type = data[1]
        self.energy = int(data[2])
        if self.type == ' atk':
            self.damage = int(data[3])
        elif self.type == ' def':
            self.defense = int(data[3])
        elif self.type == ' mag':
            self.damage = int(data[3])
            self.perk = data[5]
            self.perkValue = int(data[6])
        self.rese = int(data[4]) #ritkasagerossegszintegyutthato