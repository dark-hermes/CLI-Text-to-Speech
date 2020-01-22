from gtts import gTTS
import os

print("""
==================
CLI-Text-to-Speech
  @hermawanzss
================== 
""")
while True :
	text = input("\nText\t: ")
	tts = gTTS(text, lang='en')
	tts.save("{text}.mp3".format(text=text))
	os.system("vlc \"{text}.mp3\"".format(text=text)) # replace vlc with your audio player (CLI)
	os.system("del \"{text}.mp3\"".format(text=text))