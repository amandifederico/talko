import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 10)

voices = engine.getProperty('voices')
#print "Using voice:", repr(voices[20])
#engine.setProperty('voice', voices[11].id)
engine.setProperty('voice', voices[20].id)
#engine.say("A B C D E F G H I J K L M")
#engine.say("N O P Q R S T U V W X Y Z")
#engine.say("0 1 2 3 4 5 6 7 8 9")
#engine.say("We're charging our battery, and now we're full of energy, we are the robots") #letra de kraftwerk
engine.say("Hola, puedo hacer hablar a mi computadora")

engine.runAndWait()
