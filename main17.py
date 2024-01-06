# 获取指定卡组中所有卡片的字段内容  例如 正面 背面
# pyinstaller D:\pythonxiangmu\zidonghua\main17.py --onefile --icon=tubiao.ico


import requests

# AnkiConnect服务器地址，默认是http://localhost:8765
ANKI_CONNECT_URL = "http://localhost:8765"

def get_notes_info(deck_name):
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

    notes_info = []

    # 获取每张卡片的字段内容
    for note_id in note_ids:
        payload = {
            "action": "notesInfo",
            "version": 6,
            "params": {
                "notes": [note_id]
            }
        }
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        note_info = response.json()["result"][0]
        notes_info.append(note_info)

    return notes_info

if __name__ == "__main__":
    # 指定要获取信息的卡组名称
    target_deck = "ceshi1"

    # 获取指定卡组中所有卡片的字段内容
    notes_info = get_notes_info(target_deck)

    # 输出每张卡片的 "正面" 和 "背面" 字段内容
    for note_info in notes_info:
        front_content = note_info["fields"]["正面"]
        back_content = note_info["fields"]["背面"]
        print(f"卡片ID: {note_info['noteId']}")
        print(f"正面内容: {front_content}")
        print(f"背面内容: {back_content}")
        print("\n")

