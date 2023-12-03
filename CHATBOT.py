import subprocess
import speech_recognition as sr
from openai import OpenAI
from pathlib import Path 
from IPython.display import Audio
import sounddevice as sd
import numpy as np 
import librosa
 
 
api_key = "YOUR_API_KEY"
 
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
 
conversation = ""
user_name = "User_1234"
bot_name = "Zaddy_HogRider"

 
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
    if "bye-bye bot" in user_input.lower():
        print("Goodbye!")
        break  # Exit the loop and terminate the program
 
    # Process user input as a regular conversation with the chatbot
    prompt = user_name + ":" + user_input + "\n" + bot_name + ":"
    conversation += prompt
 
    client = OpenAI(api_key=api_key)
    response = client.completions.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.3,  # Adjust this value to control the randomness of the response
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
 
    response_str = response.choices[0].text
    response_str = response_str.split(user_name + ":", 1)[0].split(bot_name + ":", 1)[0]
 
    conversation += response_str + "\n"
    print(response_str)
 
    speech_file_path = Path(__file__).parent / "speech.wav"
 
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input = response_str)
 
    response.stream_to_file(speech_file_path) 
    audio_data, sample_rate = librosa.load(speech_file_path, sr=None)
 
    sd.play(audio_data, sample_rate)
    sd.wait()
