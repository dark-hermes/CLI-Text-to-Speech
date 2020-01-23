from gtts import gTTS as speech
import os
from playsound import playsound 
from re import search as relate

print("""
==================
CLI-Text-to-Speech
  @hermawanzss
================== 
""")
while True:
	language = input("\nLanguage (id/en)\t: ")

	if relate(language,"bahasaidindonesia"):
		language = "id"
		break
	elif relate(language,"englishinggris"):
		language = "en"
		break
	else:
		print("\nUnidentified Language\nBahasa and English only")
	
while True :
	text = input("\nText\t\t\t: ")
	tts = speech(text, lang=language)
	tts.save("{text}.mp3".format(text=text))
	playsound("{text}.mp3".format(text=text))
	os.system("del \"{text}.mp3\"".format(text=text))
