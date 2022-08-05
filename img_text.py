from gtts import gTTS           # used for converting text to speech
from PIL import Image           # used for handling image type file
import PIL                      # Python Imaging Library
import gtts                     # Google's text to Speech API
import pytesseract              # used for image to text conversion using OCR
from tkinter import filedialog  # Used to provide GUI open/save feature
from tkinter import *

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
ch=0
while ch!=4:
    print("")
    print("***MENU***")
    print("1.Image to Text")
    print("2.Image to Speech")
    print("3.Text to Speech")
    print("4.Exit")
    ch= int(input())

    if ch==1 :
        root= Tk()    # Initialize Tkinter module
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select image to open",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
                                                        # provides a dialog box for asking file to open and returns it's path
        img= PIL.Image.open(root.filename)      # opening image type file
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        result= pytesseract.image_to_string(img)   # converting image to text
        
        print(result)
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
        textInp= input("Enter text to be converted:")
        res= gTTS(textInp)
        root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save audio file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        res.save(root.filename+ '.mp3')
        
        print("Saved")
        
    elif ch!=4:
        print("Enter valid choice")