import requests

def search_magic_card(card_name):
    """Search for a Magic: The Gathering card using the Scryfall API."""
    base_url = "https://api.scryfall.com/cards/named"
    params = {"fuzzy": card_name}  # Allows for approximate matching

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        card_data = response.json()
        card_info = {
            "Name": card_data.get("name", "Unknown"),
            "Mana Cost": card_data.get("mana_cost", "N/A"),
            "Type": card_data.get("type_line", "N/A"),
            "Rarity": card_data.get("rarity", "N/A").capitalize(),
            "Text": card_data.get("oracle_text", "No description available"),
            "Set": card_data.get("set_name", "Unknown"),
            "Image": card_data.get("image_uris", {}).get("normal", "No image available"),
        }
        return card_info
    else:
        return {"Error": f"Card not found. Status code: {response.status_code}"}

if __name__ == "__main__":
    card_name = input("Enter the name of a Magic: The Gathering card: ")
    card_details = search_magic_card(card_name)

    if "Error" in card_details:
        print(card_details["Error"])
    else:
        print("\nMagic: The Gathering Card Information")
        print("=" * 40)
        for key, value in card_details.items():
            print(f"{key}: {value}")

