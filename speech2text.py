import speech_recognition as sr
from pynput import keyboard
import time
class SpeechRecognizer:
    def __init__(self, language="en-US"):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.language = language
        self.stop = False

    def recognize_speech(self):
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)

        try:
            text = self.r.recognize_google(audio, language=self.language)
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

    def run_continuously(self):
        print("Press ESC then make confirmation sound to stop")
        while not self.stop:
            text = self.recognize_speech()
            if text is not None:
                print(text)
            time.sleep(0.1)

        print("Program stopped")

    def on_press(self, key):
        if key == keyboard.Key.esc:
            self.stop = True

def main():
    speech_recognizer = SpeechRecognizer()
    listener = keyboard.Listener(on_press=speech_recognizer.on_press)
    listener.start()
    speech_recognizer.run_continuously()


