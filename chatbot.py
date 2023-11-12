import requests
from speech2text import main
from get_path import model_path0

from rasa.cli.run import run

def deploy_rasa_chatbot(model_path, endpoints_path, user_input):
    # Run Rasa server with specified model and endpoints
    run(model=model_path, endpoints=endpoints_path)

if __name__ == '__main__':
    # Replace these paths with the actual paths to your trained model and endpoints configuration
    model_path = model_path0
    endpoints_path = ""http://localhost:5005/webhooks""

    # Simulate the speech-to-text output (replace this with your actual implementation)
    user_input = "main()"

    # Pass the user's input to the Rasa chatbot
    if user_input:
        deploy_rasa_chatbot(model_path, endpoints_path, user_input)

# Pass the text to Rasa
rasa_response = send_message_to_rasa(main())

# Handle Rasa's response as needed
print(rasa_response)
