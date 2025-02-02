import requests
import openai
import re

# Set your OpenAI API key here

def search_magic_card(card_name):
    """Search for a Magic: The Gathering card using the Scryfall API."""
    base_url = "https://api.scryfall.com/cards/named"
    params = {"fuzzy": card_name}  # Allows for approximate matching

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        card_data = response.json()
        return {
            "Name": card_data.get("name", "Unknown"),
            "Image": card_data.get("image_uris", {}).get("normal", "No image available"),
        }
    else:
        return {"Error": f"Card not found. Status code: {response.status_code}"}

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
        user_prompt += " Please list each card name on a separate line, with only the card name and no additional text."

    response = ask_openai(user_prompt)

    print("\nAI Response:")
    print(response)

    if is_commander_deck_request and not response.startswith("Error"):
        # Extract card names from the response
        card_names = []
        for line in response.split('\n'):
            line = line.strip()
            if line:
                # Remove leading numbers or bullets using regex
                cleaned_line = re.sub(r'^(\d+\.\s*|-\s*)', '', line)
                cleaned_line = cleaned_line.strip()
                if cleaned_line:
                    card_names.append(cleaned_line)
        
        print("\nFetching image URLs for the cards...")
        urls = []
        for name in card_names:
            card_info = search_magic_card(name)
            if "Error" not in card_info:
                image_url = card_info.get("Image", "No image available")
                urls.append(f"{name}: {image_url}")
            else:
                urls.append(f"{name}: {card_info['Error']}")
        
        print("\nImage URLs:")
        for url in urls:
            print(url)
    else:
        # Handle general responses or errors
        pass
