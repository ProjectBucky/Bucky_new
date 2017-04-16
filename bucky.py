import speech_recognition as sr
import pyttsx
import time
import wolframalpha
from questions import * 

'''
engine = pyttsx.init()
engine.say("Your Message")
engine.runAndWait()
'''
def voice (str):
    engine = pyttsx.init()
    engine.say(str)
    engine.runAndWait()

def reply(str):
    if (str in ask_time):
        voice(time.strftime('%X %x %Z'))
    elif (str in who_are_you):
        voice("I am Bucky, the new age personal assistant")
    elif (str in greetings):
        voice("hello, nice to meet you")
    elif (str in about_creators):
        voice("i was created by those 4 people standing next to you")
    elif (str in how_are_you):
        voice("i'm doing fine, thanks how are you ")
    elif (str in where_are_you):
        voice("I am probably inside someone's computer")
    elif (str=="i love you"):
        voice("I love you too handsome")
    elif (str=="go to hell"):
        voice("perhaps i have already been there")
    elif (str in about_skills):
        voice("i can recognize and carry out basic voice commands, and predict your expenses with help of machine learning")
    elif (str=="search *"):
        voice("okay what do you want to search")
    elif (str=="check notelifications"):
        voice("you have no new notelifications")
    elif (str=="music"):
        voice("A husband and wife stepped up to view the body of his mother-in-law. As he began to cry, his wife punched him and said: Why are you crying, you never liked my mother anyway. I know he replied, I thought I saw her move!")
    elif (str=="who am i"):
        voice("i'm sorry, what is your name")
    elif (str=="what is my name"):
        voice("i'm sorry, what is your name")
    elif (str=="how is the weather"):
        voice("32 degree celcius with chances of rain")
    elif (str=="set a reminder"):
        voice("ok, what should i remind you of")
    elif (str=="count to 10"):
        voice("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    elif (str=="toss a coin"):
        import random
        x = random.randint(0,1)
        if (x==0):
            print "Head"
        else:
            print "Tail"
    elif (str=="im confused"):
        voice("lets toss a coin")
    elif (str=="i am sad"):
        voice("hi sad, my name is Bucky ha ha ha")
    elif (str==""):
        voice("I am Bucky, the new age personal assitant")
    else:
        voice("Nothing to say")
        print("Nothing")
        #client = wolframalpha.Client("K9RLXP-GKPWYPR92J")
        #res = client.query(str)
        #voice(next(res.results).text)



r = sr.Recognizer()
m = sr.Microphone()
s=""
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            #print value   #added by abhi

            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))




            s+=value+'.'
            print(s)
            #voice("You said {}".format(value))
            reply(value)

#engine = pyttsx.init()
#           engine.say("You said {}".format(value))
#            engine.runAndWait()


            # we need some special handling here to correctly print unicode characters to standard output
            
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        except KeyError:
            pass    
            
except KeyboardInterrupt:
    pass