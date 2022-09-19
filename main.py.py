from gettext import translation
from gtts import gTTS           # used for converting text to speech
from PIL import Image           # used for handling image type file
import PIL                      # Python Imaging Library
import gtts                     # Google's text to Speech API
import pytesseract              # used for image to text conversion using OCR
from tkinter import filedialog  # Used to provide GUI open/save feature
from tkinter import *
import cv2
import os
import pyttsx3
#from englishtohindi.englishtohindi import EngtoHindi
from translate import Translator

engine=pyttsx3.init()

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
ch=0
while ch!=4:
    print("")
    print("***MENU***")
    print("1.Image to Text (English)")
    print("2.Image to Speech")
    print("3.Text to Speech")
    print("4.Exit")
    ch= int(input())

    if ch==1 :
       # root= Tk()    # Initialize Tkinter module
       # root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select image to open",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        
        filename="D:\img_dp\sight.jpg"
        img= PIL.Image.open(filename)      # opening image type file
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        result= pytesseract.image_to_string(img)   # converting image to text
        
        # print("Press 0 for english")
        # print("Press 1 for Hindi")
        # ch1=int(input())
        #if(ch1==0):
        f=open("output.txt","a")
        f.write(result)
        f.write("\n")
        f.close()

        # if(ch1==1):
        #     op="Yes"
            #res=EngtoHindi(op)
            # f=open("output_hindi.txt","a")
            # f.write(translation)
            # f.write("\n")
            # f.close()
            #print(res.convert)

        # deleting img1 file
        os.remove(filename)

        #print(result)
        if(result==""):
            print("Sorry!! Nothing recogonized")

    
        
    elif ch==2:
        root= Tk()    # Initialize Tkinter module
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select image to open",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
                                                        # provides a dialog box for asking file to open and returns it's path
        img= PIL.Image.open(root.filename)      # opening image type file
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        result= pytesseract.image_to_string(img)   # converting image to text
        
        if(result==""):
            print("Sorry!! Nothing recogonized")
            continue
            
        res= gTTS(result)                # converting text to speech
        root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save audio file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
                                         # provides a dialog box for asking file to save and returns it's path
        res.save(root.filename+ '.mp3')     # inbuit audio saving function
        print("Saved")
        
    elif ch==3:
        # textInp= input("Enter text to be converted:")
        # textInp=open("output.txt","r")
        # res= gTTS(textInp)
        # root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save audio file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        # res.save(root.filename+ '.mp3')
        
        # print("Saved")

        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        # engine.setProperty("voice", voices[0].id) # for male voice
        engine.setProperty("voice", voices[1].id) #for female voice
        rate = engine.getProperty("rate")
        engine.setProperty("rate",rate-40)
        
        # age = engine.getProperty("age")
         # engine.setProperty("rate",age-40)

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def readlinesfromfile(textfilename):
            filehandle = open(textfilename,"r")
            lines = filehandle.readlines()
            for line in lines:
                speak(line)

        readlinesfromfile(r"output.txt")
        
    elif ch!=4:
        print("Enter valid choice")