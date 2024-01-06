#
# pyinstaller D:\pythonxiangmu\zidonghua\main13.py --onefile --icon=tubiao.ico




import os

# 指定文件夹路径
base_directory = r'C:\Users\22216\AppData\Roaming\Anki2\addons21'

# 创建多个文件夹
for i in range(4, 101):
    folder_name = f'ceshichajian{i}'
    folder_path = os.path.join(base_directory, folder_name)
    os.makedirs(folder_path)
    
    # 在每个文件夹中创建 __init__.py 文件
    init_file_path = os.path.join(folder_path, '__init__.py')
    with open(init_file_path, 'w') as init_file:
        pass  # 空文件

print("已成功创建文件夹和 __init__.py 文件。")

