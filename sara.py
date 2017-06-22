#!usr/bin/python

#	My personal Jarvis, will imrove it slowly
#	Progress- Plays songs only as of now


import os
from utilities import find_file
import speech_recognition as sr 										#speech recognition
from gtts import gTTS as speech											#text to speech


sara = '\n****\tSara: '													#name of my jarvis, still looking for a full name


#speaks out the text
def speak(text):														
	tts = speech(text, lang='en')										
	tts.save('play.mp3')
	print(sara + text + '\n')
	os.system('mpg321 --quiet play.mp3')
	#os.remove('play.mp3')


#task is to play music, plays the relevant music file
def music(res):															
	res = res[res.index(' ')+1:]										#remove word play 
	print(sara + 'Searching for ' + res + '\n')

	path = '/media/shashank/Entertainment/MUSIC'							#folder containig all music files
	file = res.split(' ')													#tokenize
	file, path = find_file(file, path)											#actual name of file looking for
	if(file == None):
		speak('Sorry, ' + res + ' not found')
	else:
		speak('Playing ' + file)
		file = path + '/' + file
		command = 'mpg321 --quiet "' + file + '"' 
		os.system(command)


#function to process the user response
def process(response):													
	if(response.startswith('pla')):										#user wants to play music
		music(response)


#function to listen to user
def listen():															
	recognizer = sr.Recognizer()

	with sr.Microphone() as source:										#use microphone as source
		print(sara + 'Adjusting for ambient noise' + '\n')
		recognizer.adjust_for_ambient_noise(source)
		print(sara + 'Listening' + '\n')

		while True:
			audio = recognizer.listen(source)
			try:
				response = recognizer.recognize_google(audio)
				print(sara + response + '\n')
				#speak(response)
				break
			except sr.UnknownValueError:
				speak("Sorry, I Could not understand you")
			except sr.RequestError as e:
				print("Recog Error; {0}".format(e))
	
	process(response)


#my main function
def main():
	speak('Hello Shashank. Anything I can do for you My Lord')
	listen()


if __name__ == "__main__": main()