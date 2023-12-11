import requests
from match_ids_module import match_ids

specific_player_items = []
def main():
    api_key = "your_api_key_here"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Array to store item IDs for the specific player


    for match_id in match_ids:
        try:
            url = f"https://api.opendota.com/api/matches/{match_id}"
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            match_details = response.json()

            # Check if 'players' key exists in the response
            if 'players' in match_details:
                for player in match_details['players']:
                    # Check if the player has the specified ID (86853590)
                    if player.get('account_id') == 86853590:
                        items = []
                        for i in range(6):  # Assuming item_0 to item_5
                            item_key = f"item_{i}"
                            if item_key in player:
                                item_id = player[item_key]
                                items.append(item_id)
                                specific_player_items.append(item_id)

                        print(f"Items for Player with ID 86853590 in Match ID {match_id}: {items}")

            print(f"Successful response for Match ID {match_id}")
        except requests.exceptions.HTTPError as errh:
            if response.status_code == 500:
                print(f"Error 500: Internal Server Error for Match ID {match_id}")
            else:
                print(f"HTTP Error {response.status_code}: {errh}")

    # Print item IDs for the specific player
    print("Specific player (ID 86853590) item IDs:", specific_player_items)
    import itemsname
    itemsname.main()
if __name__ == "__main__":
    main()
