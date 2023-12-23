# 修改200个py文件 
# pyinstaller D:\pythonxiangmu\zidonghua\main2.py --onefile --icon=tubiao.ico
import os

str0 = "# 请输入这个程序的功能 "
str1 = "# pip命令：      E:\anaconda3\python.exe -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple py2exe"
str2 = "#打包命令1：     pyinstaller E:\pythonxiangmu\zidonghua\main.py --onefile --icon=tubiao.ico"
str3 = "#打包命令2：     pyinstaller --onedir E:\pythonxiangmu\zidonghua\main.py"
str4 = "#                生成的文件夹中会包含一个your_program可执行文件和一个your_program_libs文件夹，其中包含了所有的依赖库和资源文件。您可以将your_program文件复制到任何地方，并在运行时将your_program_libs文件夹放在同一目录下。"
str5 = "# 打包命令3：     pyinstaller --onefile --add-data 'path/to/library;library' E:\pythonxiangmu\zidonghua\main.py"
str6 = "#                这将打包E:\pythonxiangmu\zidonghua\main.py及其依赖库和资源文件到一个可执行文件中，并将path/to/library文件夹打包为一个名为library的文件夹。在运行时，您可以将library文件夹放在任何地方，并在运行可执行文件时使用os.path.join(sys._MEIPASS, 'library')获取它们的绝对路径。"
str7 = ""
str8 = ""
str9 = ""


# 修改200个py文件

#定义一个函数，用来修改.py文件，先清空文件内容，再逐行写入str0~str9
def modify_py_file(file_path):
    with open(file_path, 'w',encoding='utf-8') as f:
        #清空文件内容
        f.truncate()
        #逐行写入str0~str9,
        f.write(str0 + '\r' + str1 + '\r' + str2 + '\r' + str3 + '\r' + str4 + '\r' + str5 + '\r' + str6 + '\r' + str7 + '\r' + str8 + '\r' + str9 + '\r')

#遍历指定目录下的所有文件，如果是.py文件，就调用modify_py_file函数
def modify_py_files(dir_path):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path) and file_path.endswith('.py'):
            modify_py_file(file_path)
        elif os.path.isdir(file_path):
            modify_py_files(file_path)

#调用modify_py_files函数，传入指定目录
dir_path = r'E:/pythonxiangmu/main1-main300'
modify_py_files(os.path.abspath(dir_path))
print('修改完成')


