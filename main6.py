# 打印输出mp3文件的时长 
# pyinstaller D:\pythonxiangmu\zidonghua\main6.py --onefile --icon=tubiao.ico
#这将打包E:\pythonxiangmu\zidonghua\main.py及其依赖库和资源文件到一个可执行文件中，并将path/to/library文件夹打包为一个名为library的文件夹。在运行时，您可以将library文件夹放在任何地方，并在运行可执行文件时使用os.path.join(sys._MEIPASS, 'library')获取它们的绝对路径。


import os
from mutagen.mp3 import MP3
import datetime

# Define the folders to traverse
folder_list = ['E:/DOTA2视频/潮汐猎人', 'E:/DOTA2视频/炼金', 'E:/DOTA2视频/狼人', 'E:/DOTA2视频/上古巨神', 'E:/DOTA2视频/玛尔斯', 'E:/DOTA2视频/电炎绝手']

# Traverse each folder, find MP3 files, and print information
for folder in folder_list:
    for filename in os.listdir(folder):
        if filename.endswith('.mp3'):
            filepath = os.path.join(folder, filename)
            audio = MP3(filepath)
            length = datetime.timedelta(seconds=int(audio.info.length))
            # Only print the seconds
            length_seconds = int(audio.info.length)
            
            print(f"{filename}: {length_seconds}")













