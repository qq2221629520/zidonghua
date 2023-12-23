# 请输入这个程序的功能 
# pyinstaller D:\pythonxiangmu\zidonghua\main4.py --onefile --icon=tubiao.ico



""" import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:/Users/86152/Desktop/故事大纲.xlsx', sheet_name='故事大纲')

# 将数据转换成一列
df = pd.DataFrame(df.stack())

# 将数据写入Sheet2
with pd.ExcelWriter(r'C:/Users/86152/Desktop/故事大纲副本.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet2', index=False, header=False) """



import pandas as pd
from openpyxl import Workbook

# 读取源Excel文件
df = pd.read_excel('C:/Users/86152/Desktop/故事大纲.xlsx', header=None)

# 创建一个新的Excel文件，并获取工作表
wb = Workbook()
ws = wb.active

# 将非空单元格的内容写入新Excel文件的一列中
row_num = 1
for row in df.iterrows():
    for cell in row[1]:
        if pd.notnull(cell):
            ws.cell(row=row_num, column=1, value=cell)
            row_num += 1

# 保存新Excel文件
wb.save('C:/Users/86152/Desktop/故事大纲副本.xlsx')
