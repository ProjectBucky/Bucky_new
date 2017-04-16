import random
import pyttsx
import pyaudio  
import wave
import time

from jokes_and_quotes import *  
        
def voice (str):
    engine = pyttsx.init()
    engine.say(str)
    engine.runAndWait()

def roll_dice():
	dice_val = random.randint(1,7)
	voice(dice_val) 

def toss_coin():
	toss_val=random.randint(0,2)
	if toss_val==1:
		voice("Heads")
	else:
		voice("Tails")
		
def tell_jokes():
	joke_val=random.randint(0,3)
	voice(jokes[joke_val])

def tell_quote():
	quote_val=random.randint(0,3)
	


def speak(arg):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-5)
    engine.say(arg)
    engine.say("   ")
    engine.runAndWait()

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        secs=mins*60+secs
        if(secs >= 50 and secs %10==0):
            voice(secs)
        elif secs<10:
            speak(secs)
            time.sleep(.4)
                
        elif secs < 50:
            voice(secs)

        
        else:
            time.sleep(1)
        t -= 1
    chunk = 1024 
    f = wave.open(r"alarm.wav","rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)
    data = f.readframes(chunk) 
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)
    stream.stop_stream()  
    stream.close()
    p.terminate()
    speak("Time up")      


countdown(5)