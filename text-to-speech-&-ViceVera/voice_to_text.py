# 1. import these two modules
import speech_recognition as sr
import pyttsx3


# 2.Initialize the recognizer
r = sr.Recognizer()

# 3.convert text to speech
def speakText(command):
    # initializing the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
# loop
while(1):
      try:
       # use the microphone as source for input.
       with sr.Microphone() as source2:
            #   wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source2,duration=0.2)
            
            # listen to the input from the user
            print("Listening.........")
            audio2 = r.listen(source2)
            
            # using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            print("Did you say ", MyText)
            speakText(MyText)
            
      except sr.RequestError as e:
           print("Could not request results; {0}".format(e))
      except sr.UnknownValueError:
             print("Sorry I could not understand")
             
             
             
             
             
        
