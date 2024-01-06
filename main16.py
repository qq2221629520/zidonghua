# 获取制定卡组中的所有卡片ID
# pyinstaller D:\pythonxiangmu\zidonghua\main16.py --onefile --icon=tubiao.ico


import requests

# AnkiConnect服务器地址，默认是http://localhost:8765
ANKI_CONNECT_URL = "http://localhost:8765"

def get_notes_in_deck(deck_name):
    # 获取卡组ID
    payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": f"deck:{deck_name}"
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    note_ids = response.json()["result"]
    return note_ids

if __name__ == "__main__":
    # 指定要遍历的卡组名称
    target_deck = "ceshi1"

    # 获取指定卡组中的所有卡片ID
    note_ids = get_notes_in_deck(target_deck)

    # 输出卡组中的所有卡片ID
    print(f"卡组 {target_deck} 中的所有卡片ID:")
    # 输出id的数据类型
    print(type(note_ids))

    print(note_ids)


