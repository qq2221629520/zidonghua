# 请输入这个程序的功能 
# pip命令：      E:naconda3\python.exe -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple openpyxl
# 打包命令1：     pyinstaller E:\pythonxiangmu\zidonghua\main.py --onefile --icon=tubiao.ico
# 打包命令2：     pyinstaller --onedir E:\pythonxiangmu\zidonghua\main.py
#                生成的文件夹中会包含一个your_program可执行文件和一个your_program_libs文件夹，其中包含了所有的依赖库和资源文件。您可以将your_program文件复制到任何地方，并在运行时将your_program_libs文件夹放在同一目录下。
# 打包命令3：     pyinstaller --onefile --add-data 'path/to/library;library' E:\pythonxiangmu\zidonghua\main.py
#                这将打包E:\pythonxiangmu\zidonghua\main.py及其依赖库和资源文件到一个可执行文件中，并将path/to/library文件夹打包为一个名为library的文件夹。在运行时，您可以将library文件夹放在任何地方，并在运行可执行文件时使用os.path.join(sys._MEIPASS, 'library')获取它们的绝对路径。



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
