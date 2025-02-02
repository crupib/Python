import requests
import openai
import re
import json

# Set your OpenAI API key here
def search_magic_card(card_name):
    """Search for a Magic: The Gathering card using the Scryfall API."""
    base_url = "https://api.scryfall.com/cards/named"
    params = {"fuzzy": card_name}  # Allows for approximate matching

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        card_data = response.json()
        return {
            "name": card_data.get("name", "Unknown"),
            "image": card_data.get("image_uris", {}).get("normal", "No image available"),
        }
    else:
        return {"name": card_name, "image": "No image available"}

def ask_openai(prompt):
    """Send a prompt to OpenAI's API and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            api_key=OPENAI_API_KEY
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Welcome to the Magic: The Gathering Assistant!")
    user_prompt = input("Ask something about Magic: The Gathering: ")

    # Check if the user is asking for a commander deck list
    is_commander_deck_request = "commander" in user_prompt.lower() and "deck" in user_prompt.lower()
    
    if is_commander_deck_request:
        # Append formatting instructions to the prompt
        user_prompt += " Please list each card name on a separate line, with each card preceded by its quantity (e.g., '1x Sol Ring')."

    response = ask_openai(user_prompt)

    print("\nAI Response:")
    print(response)

    if is_commander_deck_request and not response.startswith("Error"):
        # Extract card names and quantities from the response
        deck_list = []
        card_count = 1  # Start numbering from 1

        for line in response.split('\n'):
            line = line.strip()
            if line:
                # Extract quantity and card name using regex
                match = re.match(r'^(\d+)[xX]?\s*(.+)$', line)
                if match:
                    quantity = int(match.group(1))
                    card_name = match.group(2).strip()
                else:
                    quantity = 1  # Default to 1 if no quantity is specified
                    card_name = line.strip()

                # Fetch card details
                card_info = search_magic_card(card_name)
                card_info["number"] = card_count  # Assign sequential number
                card_info["quantity"] = quantity  # Store quantity
                deck_list.append(card_info)
                
                card_count += 1  # Increment card number

        # Save the deck as a JSON file
        with open("deck.json", "w") as json_file:
            json.dump(deck_list, json_file, indent=4)

        print("\nDeck list saved as deck.json!")
    else:
        # Handle general responses or errors
        print("No deck list was requested.")

