from gtts import gTTS
import os
from playsound import playsound
import re

print("""
==================
CLI-Text-to-Speech
  @hermawanzss
================== 
""")
while True:
	language = input("\nLanguage (id/en)\t: ")

	if re.search(language,"bahasaidindonesia"):
		language = "id"
		break
	elif re.search(language,"englishinggris"):
		language = "en"
		break
	else:
		print("\nUnidentified Language\nBahasa and English only")
	
while True :
	text = input("\nText\t\t\t: ")
	tts = gTTS(text, lang=language)
	tts.save("{text}.mp3".format(text=text))
	playsound("{text}.mp3".format(text=text))
	os.system("del \"{text}.mp3\"".format(text=text))
