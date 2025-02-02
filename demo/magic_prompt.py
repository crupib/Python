import openai

# Set your OpenAI API key
def ask_openai(prompt):
    """Send a prompt to OpenAI's API and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use gpt-4 or another model
            messages=[{"role": "user", "content": prompt}],
            api_key=OPENAI_API_KEY  # Pass the API key
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Welcome to the Magic: The Gathering Assistant!")
    user_prompt = input("Ask something about Magic: The Gathering: ")
    
    response = ask_openai(user_prompt)
    
    print("\nAI Response:")
    print(response)

