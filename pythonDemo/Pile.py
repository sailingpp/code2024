class Pile:
    def __init__(self,diameter):
        self.diameter=diameter
        self.cir=3.14*diameter
        self.area=3.14*diameter*diameter/4
    
    def showmsg(self):
        print(f'桩的直径：{self.diameter:0.3}')
        print(f'桩的周长：{self.cir:0.3}')
        print(f'桩的面积：{self.area:0.3}')

if __name__=='__main__':
    pile=Pile(0.8)
    pile.showmsg()