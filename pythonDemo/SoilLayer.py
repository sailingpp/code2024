import pandas as pd
from Pile import *

class SoilLayer:
    
    layer_length=None
    layer_fi=None
    diameter=0.8
    pile=Pile(diameter)

    list_soillayer=[]

    def __init__(self,layerid,layername,startheight,endheight,layerqsi,layerqua):
        self.layer_Id=layerid
        self.layer_name=layername
        self.layer_startheight=startheight
        self.layer_endthegith=endheight
        self.layer_length=self.layer_startheight-self.layer_endthegith
        self.layer_qsi=layerqsi
        self.layer_qua=layerqua
        self.layer_fi=(self.layer_length*self.layer_qsi)*self.pile.cir
        self.layer_fa=self.layer_qua*self.pile.area

    def show_msg(self):
        print(f'本层土的fi:{self.layer_fi:0.3f}KN')
        print(f'本层土的fa:{self.layer_fa:0.3f}KN')


    









    

