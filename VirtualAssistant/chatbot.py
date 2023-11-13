import requests


def send_message_to_rasa(message):
    url = "http://_______:5005/webhooks/rest/webhook"
    payload = {"message": message}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers).json()
        # Check if the response is not empty
        if response:
            return response[0]['text']
        else:
            return "No response from the bot."
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        bot_response = send_message_to_rasa(user_input)
        print(f"Bot: {bot_response}")
