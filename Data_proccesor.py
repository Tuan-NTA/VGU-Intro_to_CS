import openai

class ChatGPTAssistant:
    def __init__(self, api_key, model_id='gpt-3.5-turbo'):
        openai.api_key = api_key
        self.model_id = model_id
        self.message_history = []

    def generate_response(self, user_input, role="user"):
        array_exit = ["", "Bye ChatGPT", " Bye ChatGPT", "bye", "bye chat", " bye", " see you"]
        if user_input in array_exit:
            return None

        self.message_history.append({'role': 'system', 'content': 'You are a helpful assistant.'})
        self.message_history.append({"role": role, "content": f"{user_input}"})
        completion = openai.ChatCompletion.create(
            model=self.model_id,
            messages=self.message_history
        )
        response = completion.choices[0].message.content.strip()
        print(response)
        return response 
        self.message_history.append({"role": "assistant", "content": f"{response}"})
        return response

# Usage
#assistant = ChatGPTAssistant(api_key="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")
#response = assistant.generate_response("Hello, how can you help me?")





