import speech_recognition as sr  
from textblob import TextBlob

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source) 
    print("Time Over")  

speech = r.recognize_google(audio)

try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

print(type(r.recognize_google(audio)))

#Step 3 - Retrieve Tweets

analysis = TextBlob(speech)
print(analysis.sentiment)