import pandas as pd
from openpyxl import Workbook


# 读取 Excel 文件中的所有 Sheet 共计105个表格
df_dict = pd.read_excel(r'C:\Users\17653\Desktop\反洗钱1558户\历史数据查询266911\历史数据查询-2（20241230）.xlsx', sheet_name=None)
i=1
# 遍历每个 Sheet
for sheet_name, df in df_dict.items():
    print(f"Sheet 名称: {sheet_name}")
    print(i)
    i=i+1
    #print(df.head()) # 打印前五行数据


print(df_dict['Sheet1'])

