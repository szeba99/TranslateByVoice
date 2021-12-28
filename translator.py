import speech_recognition as sr
from googletrans import Translator
import json
import winsound
import keyboard
from time import sleep
import subprocess

datafile = open("settings.json", "r", encoding="utf-8")
settings = json.load(datafile)
datafile.close
hotkey = settings["hotkey"]
print(hotkey)


def TranslateByVoice():
    global hotkey
    translator = Translator(service_urls=[
        'translate.google.com',
        'translate.google.co.kr',
        ])

    datafile = open("settings.json", "r", encoding="utf-8")
    settings = json.load(datafile)
    datafile.close

    source_language = settings["source_language"]
    destination_language = settings["destination_language"]
    duration = settings["duration"]
    service = settings["service"]
    hotkey = settings["hotkey"]

    #data, samplerate = soundfile.read('speech.wav')
    #soundfile.write('speech.wav', data, samplerate, subtype='PCM_16')
    #filename = "speech.wav"

    r = sr.Recognizer()

    # open the file
    print("recording started")
    source = ""
    try:
        with sr.Microphone() as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source, duration=duration)
            print("recording ended")
            # recognize (convert from speech to text)
            temporary_data = r.recognize_google(audio_data, key=None, language=source_language, show_all=True)
            print(temporary_data["alternative"][0]["transcript"])
            text = temporary_data["alternative"][0]["transcript"]
    except TypeError:
        text = "Unable to comprehend"


    
    
    source= ""

    ##############################################################translate
    translator = Translator()
    translation = translator.translate(text, dest=destination_language[:2], src=source_language[:2])
    print(translation.text)

    textfile = open("output_text.txt","w")
    textfile.write(translation.text)
    textfile.close()


    subprocess.run(f"bal4web\\bal4web -s {service} -l {destination_language} -f output_text.txt -w test.wav")

    winsound.PlaySound(r'test.wav', winsound.SND_ASYNC)
    #os.remove("test.wav")

    ##############################################################################

keyboard.add_hotkey(f'{hotkey}', TranslateByVoice)
keyboard.wait()