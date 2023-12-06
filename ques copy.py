import kivy
import speech_recognition as sr
import openai
from kivy.uix.button import Button
kivy.require('2.2.1')
import pyttsx3
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRaisedButton
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color, Line
import requests
from kivy.uix.textinput import TextInput



class TalkAI(Screen):
    def __init__(self, **kwa):
        super(TalkAI, self).__init__(**kwa)
        bgimg = Image(source="background.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(bgimg)

        age = MDLabel(text = "Enter your age:", pos_hint ={"x":0.15, "y":0.05}, font_style="H5")
        self.add_widget(age)
        age_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.35, 'y':0.53})
        age_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(age_textinput)

        Aneamia = MDLabel(text = "Does the patient have Aneamia:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(Aneamia)
        Aneamia_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        Aneamia_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(Aneamia_textinput)

        creatinine_phosphokinase = MDLabel(text = "Enter the creatinine phosphokinase of the patient:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(creatinine_phosphokinase)
        creatinine_phosphokinase_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        creatinine_phosphokinase_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(creatinine_phosphokinase_textinput)

        diabetes = MDLabel(text = "Does the patient have diabetes?:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(diabetes)
        diabetes_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        diabetes_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(diabetes_textinput)

        ejection_fraction = MDLabel(text = "Enter the ejection fraction of the patient:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(ejection_fraction)
        ejection_fraction_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        ejection_fraction_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(ejection_fraction_textinput)

        blood_pressure = MDLabel(text = "Does the patient have high blood pressure?:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(blood_pressure)
        blood_pressure_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        blood_pressure_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(blood_pressure_textinput)

        platelets = MDLabel(text = "Enter the platelets of the patient:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(platelets)
        platelets_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        platelets_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(platelets_textinput) 
        
        serum_creatinine = MDLabel(text = "Enter the serum creatinine of the patient::", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(serum_creatinine)
        serum_creatinine_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        serum_creatinine_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(serum_creatinine_textinput)

        serum_sodium = MDLabel(text = "Enter the serum sodium of the patient::", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(serum_sodium)
        serum_sodium_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        serum_sodium_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(serum_sodium_textinput)

        gender = MDLabel(text = "Enter the gender of the patient::", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(gender)
        gender_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        gender_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(gender_textinput)

        smoking = MDLabel(text = "Does the patient smoke?:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(smoking)
        smoking_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        smoking_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(smoking_textinput)

        Time = MDLabel(text = "Enter the time at which the patient has been admitted:", pos_hint ={'x' :0.15, 'y':0.001 },font_style = "H5", color = "brown")
        self.add_widget(Time)
        Time_textinput = TextInput(text='Hello world', multiline=False, size_hint={0.2,0.05}, pos_hint={'x': 0.575, 'y':0.48})
        Time_textinput.bind(on_text_validate=self.on_enter)
        self.add_widget(Time_textinput)

    def on_enter(self):
      print('User pressed enter in')
class MindMagic(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self._app_name = "RakshaKavach"
        self.icon = "logo.png"
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(TalkAI(name="talkai"))
        return sm

if __name__ == "__main__":
    MindMagic().run()