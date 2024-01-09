#获取电梯具体位置
import os
from docx import Document
import re

folder_path = r'D:\个人资料\电梯\28台\2020领仕郡28台自检报告及报检申请表\2020领仕郡28台自检报告及报检申请表\临时'

# 定义一个正则表达式模式，匹配目标内容
pattern = r'同圆领仕郡(.+?)'

# 初始化数据字典
data = {}

# 遍历指定文件夹中的每个文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.docx'):
            file_path = os.path.join(root, file)
            document = Document(file_path)
            
            # 遍历文档中的所有表格
            for table in document.tables:
                # 遍历表格的所有行和列
                for row in table.rows:
                    for cell in row.cells:
                        # 在单元格文本中搜索匹配项
                        match = re.search(pattern, cell.text)
                        if match:
                            # 如果找到匹配项，将整个单元格的内容存储在字典中，以文件名为键
                            data[file] = cell.text
                            # 跳出当前表格的遍历，继续处理下一个文件
                            break
                    # 如果已经找到匹配项，跳出当前表格的遍历，继续处理下一个文件
                    if match:
                        break

print(data)
