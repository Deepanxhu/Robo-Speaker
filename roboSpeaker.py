import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker version 1.1 by Deepanshu ")
    engine = pyttsx3.init()
    while(True):
        word = input("Enter what you want the system to speak: ")
        if word == 'q':
            engine.say("Bye Bye")
            engine.runAndWait()
            break
        engine.say(word)
        engine.runAndWait()


# print("Welcome to RoboSpeaker version 1.1 by Deepanshu ")
# x = input("Enter what you want the system to speak: ")

# engine = pyttsx3.init()
# engine.say(x)
# engine.runAndWait()


# import os

# if __name__ == '__main__':
#     print("Welcome to Robo Speaker 1.1")
#     x = input("Enter what you want me to speak.")
#     command = f"say {x}"
#     os.system(command)