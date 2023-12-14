import subprocess
import speech_recognition as sr                     
from openai import OpenAI
from pathlib import Path 
from IPython.display import Audio
import sounddevice as sd
import numpy as np 
import librosa
import pyautogui
 
 
api_key = "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"

pyautogui.press("volumeup",30)
#pyautogui.press("volumedown", 20)

 
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
 
conversation = ""
user_name = "Adi"
bot_name = "Bliss Buddy"


 
while True:
    with mic as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("Please wait...")
 
    try:
        user_input = r.recognize_google(audio)
    except sr.UnknownValueError:
        continue
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        continue
 
    print(f"User said: {user_input}")
 
    # Check if the user wants to exit
    if "bye-bye" in user_input.lower():
        print("Goodbye!")
        break  # Exit the loop and terminate the programe



    prompt = user_name + ":" + user_input + "\n" + bot_name + ":"
    conversation += prompt
 
    client = OpenAI(api_key=api_key)
    response = client.completions.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=1,  # Adjust this value to control the randomness of the response
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
 
    response_str = response.choices[0].text
    response_str = response_str.split(user_name + ":", 1)[0].split(bot_name + ":", 1)[0]
 
    conversation += response_str + "\n"
    print(response_str)                
                               

    speech_file_path = Path(__file__).parent / "speech.wav"
    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input = response_str)
 
    response.stream_to_file(speech_file_path) 
    audio_data, sample_rate = librosa.load(speech_file_path, sr=None)
 
    sd.play(audio_data, sample_rate)
    sd.wait()
