# 请输入这个程序的功能  下饭 
# pyinstaller D:\pythonxiangmu\zidonghua\main9.py --onefile --icon=tubiao.ico







import webbrowser
import random
import re

def save_last_file_path(file_path):
    with open('last_file_path.txt', 'w') as file:
        file.write(file_path)

def load_last_file_path():
    try:
        with open('last_file_path.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def extract_urls(line):
    # 使用正则表达式提取网址部分
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    matches = url_pattern.findall(line)
    return matches

def open_random_urls(file_path, num_urls):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取文件中的网址并存储在列表中
        urls = [url for line in file for url in extract_urls(line)]

        # 随机选择指定数量的网址
        selected_urls = random.sample(urls, min(num_urls, len(urls)))

        # 在默认浏览器中打开选定的网址
        for url in selected_urls:
            webbrowser.open(url)

# 尝试加载上一次保存的文件路径
last_file_path = load_last_file_path()

# 获取用户输入的文件路径
new_file_path = input(f"请输入包含网址的txt文件的绝对路径{' (' + last_file_path + ')' if last_file_path else ''}: ") or last_file_path

# 询问用户是否要修改文件路径
change_path = input(f"当前文件路径为: {new_file_path}，是否要修改？ (按 Enter 确认修改，直接回车默认不修改): ").strip()

# 如果用户选择修改文件路径
if change_path:
    new_file_path = input("请输入新的包含网址的txt文件的绝对路径: ")

# 获取用户输入的要打开的网址数量
try:
    num_urls = int(input("请输入要打开的网址数量: "))
except ValueError:
    print("请输入有效的数字。")
else:
    open_random_urls(new_file_path, num_urls)
    # 保存用户输入的文件路径
    save_last_file_path(new_file_path)
