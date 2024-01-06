#  获取到所有卡组的名称，成功
# pyinstaller D:\pythonxiangmu\zidonghua\main15.py --onefile --icon=tubiao.ico

import requests

def get_anki_deck_names():
    # Anki Connect Web 服务器的地址，默认为 http://127.0.0.1:8765
    anki_connect_url = "http://127.0.0.1:8765"

    # 定义 Anki Connect 请求的参数
    action = "deckNames"
    params = {
        "action": action,
        "version": 6  # Anki Connect 版本号
    }

    try:
        # 发送请求并获取响应
        response = requests.post(anki_connect_url, json=params)
        response.raise_for_status()

        # 打印完整的响应内容
        print("Anki Connect Response:")
        print(response.text)

        # 解析响应的 JSON 数据
        deck_names = response.json()

        return deck_names

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# 获取并打印所有 Anki 卡组的名称
# 获取并打印所有 Anki 卡组的名称
anki_deck_names = get_anki_deck_names()
if anki_deck_names:
    print("Anki Deck Names:")
    for deck_name in anki_deck_names["result"]:
        print(deck_name)

