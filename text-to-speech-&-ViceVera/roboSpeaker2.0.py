# if we are using mac Os then using os module we can do the text-to-speech
# import os
# if __name__ == '__main__':
#      print("Welcome to Robo Speaker 2.0 Created by Harshali..")
#      x= input("Enter what you want me to speak ")
#      command = f"Say, {x}"
#      os.system(command)

# --------------------------------------------------------------------------------------------------------------------


# ...............................convert text to speech----------------------------------------------
# 1. import the pyttsx3 module
import pyttsx3

print("******Welcome to Robo Speaker 2.0 Created by Harshali*******")
# 2.initialize using init()
engine = pyttsx3.init()

# 3.After initialization, we will make the program speak the text using say(text unicode, name string)
speak = "yes"
while True:
    speak = input("Enter what you want me to speak: ")
    
    if speak == "no" or speak=="":
        engine.say("Good By Friend")
        engine.runAndWait()
        break
    
    # 3.After initialization, we will make the program speak the text using say(text unicode, name string)
    engine.say(speak)
    engine.runAndWait()
    
    
    
