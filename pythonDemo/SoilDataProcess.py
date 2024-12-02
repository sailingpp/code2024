import pandas as pd
import json
from glom import glom
from Soil import *

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)
pd.set_option('display.expand_frame_repr',False)

dic={}
df=pd.read_json('./pythonDemo/SoilData.json')
for i in df.keys():
     dic[i]=df[i].values

print(dic)

soil=Soil(dic)

for k in soil.data:
    print(soil.data[k].Ra)



