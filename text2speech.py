import pyttsx3

data = input("Enter in the text to be converted to speech:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()