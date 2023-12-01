import subprocess
import speech_recognition as sr
#import pyttsx3
#   import openai
from openai import OpenAI
from pathlib import Path 
from IPython.display import Audio
import sounddevice as sd
import numpy as np 
import librosa
 
 
api_key = "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"
 
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#zngine.setProperty('voice', voices[1].id)
 
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
 
conversation = ""
user_name = "Adi"
bot_name = "Bliss Buddy"
 
def play_song(song_name):
    # Mapping of songs to local file paths
    song_mapping = {
        '1': r"C:\\Users\\PIYUSH\\Downloads\\Excuses - AP Dhillon, Gurinder Gill & Intense Music (Lyric Video) by RMN NATÎ0N (64 kbps).mp3",
        '3': r"C:\\Users\\PIYUSH\\Downloads\\Sun Saathiya Full Video _ Disney's ABCD 2 _ Varun Dhawan , Shraddha Kapoor _ Sachin Jigar _ Priya S (320 kbps).mp3",
        '4': r"C:\\Users\\PIYUSH\Downloads\\Maroon 5 - Animals (Lyrics) (320 kbps).mp3",
        '6': r"C:\\Users\\PIYUSH\\Desktop\\music\\bollywood_EV - Galliyan.mp3",
        '7': r"C:\\Users\\PIYUSH\\Desktop\\music\\Bijlee Bijlee Harrdy Sandhu 128 Kbps.mp3",
        '8': r"C:\\Users\\PIYUSH\\Desktop\\music\\Lil Nas X - MONTERO (Call Me By Your Name) (Official Video) (320 kbps).mp3",
        '9': r"C:\\Users\\PIYUSH\\Desktop\\music\\Daku.mp3",
        '10': r"C:\\Users\\PIYUSH\\Desktop\\music\\Legends Never Die (ft. Against The Current) [OFFICIAL AUDIO] _ Worlds 2017 - League of Legends (64 kbps).mp3",
        # Mapping of songs to local file paths
 
 
    # Add more songs as needed
}
 
        # Add more songs as needed
 
 
    # Check if the chosen song exists in the mapping
    if song_name.lower() in song_mapping:
        file_path = song_mapping[song_name.lower()]
 
        # Use subprocess to open VLC with the chosen song
        vlc_path = r'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  # Replace with the actual path to vlc.exe
        subprocess.run([vlc_path, file_path])
    else:
        print(f"Song '{song_name}' not found.")
 
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
 
    # Check if the user wants to play a song
    if "play song" in user_input.lower():
        song_number = None
        if "1" in user_input.lower() or "one" in user_input.lower():
            song_number = "1"
        elif "2" in user_input.lower() or "two" in user_input.lower():
            song_number = "2"
        elif "3" in user_input.lower() or "three" in user_input.lower():
            song_number = "3"
        elif "4" in user_input.lower() or "four" in user_input.lower():
            song_number = "4"
        elif "5" in user_input.lower() or "five" in user_input.lower():
            song_number = "5"
        elif "6" in user_input.lower() or "six" in user_input.lower():
            song_number = "6"
        elif "7" in user_input.lower() or "seven" in user_input.lower():
            song_number = "7"
        elif "8" in user_input.lower() or "eight" in user_input.lower():
            song_number = "8"
        elif "9" in user_input.lower() or "nine" in user_input.lower():
            song_number = "9"
        elif "10" in user_input.lower() or "ten" in user_input.lower():
            song_number = "10"
        if song_number:
            play_song(song_number)
            continue  # Skip the rest of the loop to avoid processing the chatbot response
 
    # Process user input as a regular conversation with the chatbot
    prompt = user_name + ":" + user_input + "\n" + bot_name + ":"
    conversation += prompt
 
    client = OpenAI(api_key=api_key)
    response = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=conversation,
        temperature=0.6,  # Adjust this value to control the randomness of the response
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
 
    response_str = response.choices[0].text
    response_str = response_str.split(user_name + ":", 1)[0].split(bot_name + ":", 1)[0]
 
    conversation += response_str + "\n"
    print(response_str)
 