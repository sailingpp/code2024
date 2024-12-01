import pandas as pd
from SoilLayerFactor import *

list_kc1=[
     {"layerId": 1, "layerName": "粘土", "startHeight": 19,  "endHeight": 18, "qsi": 20, "qua": 20} ,
     {"layerId": 2, "layerName": "粉土", "startHeight": 18,  "endHeight": 15, "qsi": 30, "qua": 20} ,
     {"layerId": 3, "layerName": "砂土", "startHeight": 15,  "endHeight": 13, "qsi": 50, "qua": 20} ,
     {"layerId": 4, "layerName": "岩土", "startHeight": 13,  "endHeight": 12, "qsi": 60, "qua": 200},
     {"layerId": 5, "layerName": "基岩", "startHeight": 12,  "endHeight": 10, "qsi": 70, "qua": 200},
   ]
list_kc2=[
     {"layerId": 1, "layerName": "粘土", "startHeight": 19,  "endHeight": 18, "qsi": 20, "qua": 20} ,
     {"layerId": 2, "layerName": "粉土", "startHeight": 18,  "endHeight": 14, "qsi": 30, "qua": 20} ,
     {"layerId": 3, "layerName": "砂土", "startHeight": 14,  "endHeight": 13, "qsi": 50, "qua": 20} ,
     {"layerId": 4, "layerName": "岩土", "startHeight": 13,  "endHeight": 12, "qsi": 60, "qua": 200},
     {"layerId": 5, "layerName": "基岩", "startHeight": 12,  "endHeight": 10, "qsi": 70, "qua": 200},
   ]
dict_soildata={'kc1':list_kc1,'kc2':list_kc2}

class Soil:
    data={}
    def __init__(self,dict_soildata):
        self.soildata=dict_soildata
        for k in self.soildata:
            self.data[k]=SoilLayerFactory(self.soildata[k])

soil=Soil(dict_soildata)

for k in soil.data:
    print(soil.data[k].Ra)
        