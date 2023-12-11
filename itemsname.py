import requests
from matchdecode import specific_player_items
import json

def get_item_names(ids):
    # Fetch the item data from the Dota 2 constants repository
    url = "https://raw.githubusercontent.com/odota/dotaconstants/master/build/item_ids.json"
    response = requests.get(url)

    if response.status_code == 200:
        item_data = response.json()
        item_names = []

        # Append names to items using the provided IDs
        for item_id in ids:
            item_name = item_data.get(str(item_id), "Item not found")
            item_names.append(item_name)

        return item_names
    else:
        print("Failed to fetch item data")
        return None

def main():
    # Use specific_player_items as the array of item IDs
    item_ids_array = specific_player_items

    # Get item names for the given array of item IDs
    result = get_item_names(item_ids_array)

    # Display the result
    if result:
        print("Item Names Array:", result)

if __name__ == "__main__":
    main()
