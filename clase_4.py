class Player:
    def __init__(self,x,y,health):
        self.health=100
        self.x=x
        self.y=y
    
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
    
    def damage(self,pts):
        self.health -=pts

p1 = Player(2,3)
p2 = Player(10,30)

print(p1.x)
print(p2.y)
