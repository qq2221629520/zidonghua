# 生成电梯的随机数，九个数据
# pyinstaller D:\pythonxiangmu\zidonghua\main21.py --onefile --icon=tubiao.ico



import random

# 生成nub1到nub3在[2.02, 2.32]之间的随机数
nub1 = round(random.uniform(2.02, 2.20), 2)
nub2 = round(random.uniform(2.02, 2.20), 2)
nub3 = round(random.uniform(2.02, 2.20), 2)

# 生成nub4到nub6在[2.02, 2.32]之间的随机数，但大于nub1, nub2, nub3
nub4 = round(random.uniform(max(nub1, nub2, nub3), 2.31), 2)
nub5 = round(random.uniform(max(nub1, nub2, nub3), 2.31), 2)
nub6 = round(random.uniform(max(nub1, nub2, nub3), 2.31), 2)

# 生成nub7到nub9在[2.02, 2.32]之间的随机数，但小于nub4, nub5, nub6
nub7 = round(random.uniform(2.02, min(nub4, nub5, nub6)), 2)
nub8 = round(random.uniform(2.02, min(nub4, nub5, nub6)), 2)
nub9 = round(random.uniform(2.02, min(nub4, nub5, nub6)), 2)

# 打印生成的随机数

#将这九个数字打印成三行三列的矩阵
print(nub1, nub2, nub3)
print(nub4, nub5, nub6)
print(nub7, nub8, nub9)

