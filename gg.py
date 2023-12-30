class Pokemon:
    def eng(self,id,type,species,hp,speed,attack,defense,experience):
        self.id=1
        self.type = 'trans'
        self.species='rg'
        self.hp=100
        self.speed=25
        self.attack=15
        self.defense=45
        self.experience=0
        def fight(self,others):
            first, second =None,None
            if self.speed>other.speed:
                first,second=self,others
            else:
                first,second=others,self
            while self.hp>0 and others.hp >0:
                damage=max(first.attack-second.defense, 0)
                second.hp-=damage
                first,second=second,first

rg=Pokemon
print(rg.hp)
scorbunny
another=Pokemon()
anothaer.speed=30
esult