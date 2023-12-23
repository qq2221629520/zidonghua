#
# pyinstaller D:\pythonxiangmu\zidonghua\main12.py --onefile --icon=tubiao.ico






import os

folder_path = r'D:\pythonxiangmu\zidonghua'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.startswith('main') and filename.endswith('.py'):
        # 提取文件编号
        file_number = int(filename[4:-3])  # 假设文件名的格式为"mainXX.py"
        
        # 检查文件编号是否大于等于11
        if file_number >= 11:
            file_path = os.path.join(folder_path, filename)
            
            # 打开文件并在开头添加独立的一行 "#"
            with open(file_path, 'r+', encoding='utf-8') as file:
                content = file.read()
                file.seek(0, 0)
                file.write("#\n" + content)
