import requests

class RasaBot:

    def __init__(self, url="http://local/webhooks/rest/webhook"):
        self.url = url
        self.headers = {"Content-Type": "application/json"}

    def send_message(self, message):
        payload = {"message": message}

        try:
            response = requests.post(self.url, json=payload, headers=self.headers).json()
            # Check if the response is not empty
            if response:
                return response[0]['text']
            else:
                return "No response from the bot."
        except Exception as e:
            return f"Error: {str(e)}"


if __name__ == "__main__":
    rasa_bot = RasaBot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        bot_response = rasa_bot.send_message(user_input)
        print(f"Bot: {bot_response}")
