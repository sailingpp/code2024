from SoilLayer import *

#输入kc1 产生 list soillayer对象
class SoilLayerFactory:
    list_soillayer=[]
    Fq=0
    def __init__(self,list_data) :
        self.list_soildata=list_data
        for item in  self.list_soildata:
            temp=SoilLayer(item['layerId'],item['layerName'],item['startHeight'],item['endHeight'],item['qsi'],item['qua'])
            self.list_soillayer.append(temp)
            self.Fq+=temp.layer_fi
            self.Ra=self.Fq+temp.layer_fa
    
