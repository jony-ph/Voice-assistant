import speech_recognition as sr

from time import sleep
from gtts import gTTS
from os import chdir, getcwd, path, remove
from playsound import playsound

class Voice_client: 

    def __init__(self):
        
        self.__listener = sr.Recognizer()
        
    def listen(self):

        rec = ''

        with sr.Microphone() as source:

            self.__listener.adjust_for_ambient_noise(source)
            self.__listener.energy_threshold = 4000
            self.__listener.dynamic_energy_threshold = False

            print("Escuchando...")

            try:
                voice = self.__listener.listen(source, timeout=10, phrase_time_limit=15)
                rec = self.__listener.recognize_google(voice, language='es-MX')
                rec = rec.lower()

            except sr.WaitTimeoutError:
                self.talk("Tiempo excedido")

            except sr.UnknownValueError:
                self.talk("No pude entender lo que dijiste. Intenta de nuevo, por favor")
                return self.listen()

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


        return rec

    def talk(self, message):

        CURRENT_PATH = getcwd()
        VOICE_MESSAGE_FILE = 'message.mp3'

        tts = gTTS(message, lang='es', tld='com.mx')

        try: 
            chdir('./assets')
            tts.save(VOICE_MESSAGE_FILE)

            while not path.exists(VOICE_MESSAGE_FILE):
                sleep(0.3)

            playsound(VOICE_MESSAGE_FILE)

        except:
            print("Hubo un error inesperado")

        finally:

            if( path.exists(VOICE_MESSAGE_FILE) ):
                remove(VOICE_MESSAGE_FILE)

            chdir(CURRENT_PATH)

