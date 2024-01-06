# 得到了卡片的属性 有卡片id  有标签 有字段 有模板名称 有卡片id
import requests

# AnkiConnect服务器地址，默认是http://localhost:8765
ANKI_CONNECT_URL = "http://localhost:8765"

def get_notes_info(note_ids):
    # 获取指定卡片的详细信息
    payload = {
        "action": "notesInfo",
        "version": 6,
        "params": {
            "notes": note_ids
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    notes_info = response.json()["result"]
    return notes_info

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
    print(note_ids)

    # 获取卡片的详细信息
    notes_info = get_notes_info(note_ids)

    # 输出第一张卡片的所有属性
    if notes_info:
        print("\n第一张卡片的所有属性:")
        print(notes_info[0])
    else:
        print("\n未找到卡片。")
