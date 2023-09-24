import gradio as gr
import speech_recognition as sr
import pyttsx3
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Hello I am Jarvis, How may I help you ?')

listener = sr.Recognizer()

def take_command():
    command = ''  # Initialize command
    try:
        with sr.Microphone() as source:
            print(".....listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song) 
        pywhatkit.playonyt(song)



iface = gr.Interface(fn=run_alexa, inputs=gr.inputs.Audio(source="microphone"), outputs="text")
iface.launch()
