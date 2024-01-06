import requests

anki_connect_url = "http://localhost:8765"

def get_reviews_of_cards(card_ids):
    payload = {
        "action": "getReviewsOfCards",
        "version": 6,
        "params": {
            "cards": card_ids
        }
    }

    try:
        response = requests.post(anki_connect_url, json=payload)
        data = response.json()

        return data['result']
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    card_ids_to_check = [1703497934105, 1703497957188, 1703497969563, 1703497979071, 1703497987162]

    reviews = get_reviews_of_cards(card_ids_to_check)

    if reviews is not None:
        print("Reviews for the given card IDs:")
        for card_id, review_info_list in reviews.items():
            print(f"Card ID {card_id}: {review_info_list}")
    else:
        print("Error retrieving reviews for the given card IDs.")
