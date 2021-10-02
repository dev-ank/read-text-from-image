from extract_text import text_extraction_from_image
from auto_img_download import get_attachment
from credentials import user,password,imap_url
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import os
from PIL import Image
engine = pyttsx3.init('sapi5')

'''main module where all helping functions are called for the application '''






#reads the text in english after it is extracted from the image
def read_eng_text(img):


    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    text=text_extraction_from_image(img)
    engine.say('The image says.....\n'+text)
    engine.runAndWait()



#reads the text in hindi after it is extracted from the image
def read_hin_text(img):

    text = text_extraction_from_image(img)
    speech = gTTS(text = text, lang = 'hi', slow = False)
    speech.save("text.mp3")
    os.system("text.mp3")


#takes the command download the image from mail and reads the text present in the image
def take_command():


    r = sr.Recognizer()
    sample_rate = 48000
    chunk_size = 2048
    with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:

        try:
            r.adjust_for_ambient_noise(source)
            engine.say("The program has started...Please speak\n")
            engine.runAndWait()
            print('speak')
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(str(text))
            if 'English' in text:
                said = "Ok downloading the image from your mail and reading it in english\n"
                engine.say(said)
                img = get_attachment(user, password, imap_url)
                engine.runAndWait()
                img1=Image.open(img)
                img1.show()
                read_eng_text(img)



            elif 'Hindi' in text:
                said = "Ok downloading the image from your mail and reading it in hindi\n"
                engine.say(said)
                img = get_attachment(user, password, imap_url)
                engine.runAndWait()
                img1 = Image.open(img)
                img1.show()
                read_hin_text(img)



        except sr.UnknownValueError:
            said = "Sorry I could not hear that"
            engine.say(said)
            engine.runAndWait()


take_command()