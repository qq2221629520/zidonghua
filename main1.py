# 实现自动抠出人像
# E:\anaconda3\python.exe -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple py2exe
# 打包命令 pyinstaller E:\pythonxiangmu\zidonghua\main1.py --onefile --icon=tubiao.ico
# pyinstaller --onedir E:\pythonxiangmu\zidonghua\main1.py
# 生成的文件夹中会包含一个your_program可执行文件和一个your_program_libs文件夹，其中包含了所有的依赖库和资源文件。您可以将your_program文件复制到任何地方，并在运行时将your_program_libs文件夹放在同一目录下。
# pyinstaller --onefile --add-data 'path/to/library;library' your_program.py
# 这将打包your_program.py及其依赖库和资源文件到一个可执行文件中，并将path/to/library文件夹打包为一个名为library的文件夹。在运行时，您可以将library文件夹放在任何地方，并在运行可执行文件时使用os.path.join(sys._MEIPASS, 'library')获取它们的绝对路径。
import time

import requests
import base64

import tkinter as tk
import tkinter.filedialog

from PIL import Image

def select():
    global filename
    filename = tk.filedialog.askopenfilename()
    if filename:
        print(filename)

root = tk.Tk()
root.title("选择照片")
root.geometry("150x800")
root.resizable(0, 0)
def select():
    global filename
    filename = tk.filedialog.askopenfilename()
    if filename:
        print(filename)


def kouchurenxiang():
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
    # 二进制方式打开图片文件
    global filename
    f = open(filename, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img,
              # "type":"foreground"
              }
    access_token = '24.afd406e092e60de0574169387de9d9dc.2592000.1680172187.282335-30828139'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers, )
    if response:
        # print (response.json())
        # 保存图片，原来的照片名字后面加上“new”，在同一个文件夹下
        with open(filename[:-4] + "new.png", 'wb') as f:
            f.write(base64.b64decode(response.json()['foreground']))
            f.close()
        filename = filename[:-4] + "new.png"
        print("生成新图片！")
        time.sleep(1)
        print("5！")
        time.sleep(1)
        print("4！")
        time.sleep(1)
        print("3！")
        time.sleep(1)
        print("2！")
        time.sleep(1)
        print("1！")
        #退出程序
        root.destroy()


    else:
        print("请求失败！")
        time.sleep(1)
        print("5！")
        time.sleep(1)
        print("4！")
        time.sleep(1)
        print("3！")
        time.sleep(1)
        print("2！")
        time.sleep(1)
        print("1！")

button1 = tk.Button(root, text="选择照片", command=select)
button1.place(x=50, y=50)
button1_1 = tk.Button(root, text="抠出人像", command=kouchurenxiang)
button1_1.place(x=50, y=100)
root.mainloop()





