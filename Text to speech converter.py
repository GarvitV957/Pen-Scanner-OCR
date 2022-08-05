import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id) # for male voice
engine.setProperty("voice", voices[1].id) #for female voice
rate = engine.getProperty("rate")
engine.setProperty("rate",rate-40)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def readlinesfromfile(textfilename):
    filehandle = open(textfilename,"r")
    lines = filehandle.readlines()
    for line in lines:
        speak(line)

readlinesfromfile(r"C://Users//b2027//OneDrive//Desktop//Career//Project//text to speech converter//sample.txt")

# link : https://www.youtube.com/watch?v=buoSzgX9yM4&ab_channel=GeeksforGeeks
