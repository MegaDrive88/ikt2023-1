class Enemy:
    def __init__(self ,sor):
        data = sor.strip().split(';')
        self.hp = int(data[0])
        self.isBoss = bool(data[1])
class Item: # 3 hosszú mindegyik type, kivéve mag nál
    def __init__(self, sor):
        data = sor.strip().split(';')
        self.type = data[0]
        if self.type == 'atk':
            self.damage = int(data[1])
        elif self.type == 'def':
            self.defense = int(data[1])
        elif self.type == 'mag':
            self.damage = int(data[1])
            self.perk = int(data[-2])
            self.perkValue = int(data[-1])
        self.level = int(data[2])