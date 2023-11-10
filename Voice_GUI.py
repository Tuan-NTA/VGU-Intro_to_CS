import speech_recognition as sr
import tkinter
class Voice_GUI:
    def __init__(self, scheduler, chatbot_app):
        self.scheduler = scheduler
        self.chatbot_app = chatbot_app
        self.recognizer=sr.Recognizer()
    def Voice_GUI_run(self):
        # Check if voice chat is enabled
        if self.scheduler.voice_status[0] != 1:
            self.chatbot_app.voice_chatButton.config(text="Voice")
            return  # Do not proceed with speech recognition if voice chat is not enabled

        self.chatbot_app.voice_chatButton.config(text="Text")
        with sr.Microphone() as source:
            print("Say something:")
            audio = self.recognizer.listen(source)
            self.recognizer.adjust_for_ambient_noise(source)
            
        try:
            text = self.recognizer.recognize_google(audio)
            print("You said:", text)
            self.chatbot_app.Insert_response(text)
            # Update shared data or take appropriate actions based on the recognized speech.
            # For example, set the shared user input data.
            self.scheduler.shared_data['user_input'] = text

        except sr.UnknownValueError:
            print("Could not understand audio")
            self.chatbot_app.Insert_response("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            self.chatbot_app.Insert_response("Error with the speech recognition service")
