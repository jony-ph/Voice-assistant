import speech_recognition as sr
import pyttsx3

from playsound import playsound

class Voice_client: 

    def __init__(self):
        
        self.__listener = sr.Recognizer()
        self.__listener.energy_threshold = 4000
        self.__listener.dynamic_energy_threshold = False

        self.__engine = pyttsx3.init()
        self.__engine.setProperty('rate', 150)
        
    def listen(self):

        rec = ''

        with sr.Microphone() as source:

            playsound('./assets/speak-beep.mp3')
            self.__listener.adjust_for_ambient_noise(source)

            try:
                voice = self.__listener.listen(source, timeout=5, phrase_time_limit=10)
                rec = self.__listener.recognize_google(voice, language='es-MX')
                rec = rec.lower()

            except sr.WaitTimeoutError:
                playsound('./assets/finish-beep.mp3')

            except sr.UnknownValueError:
                self.talk("No pude entender lo que dijiste. Intenta de nuevo por favor")
                return self.listen()

            except sr.RequestError as e:
                print("No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google; {0}".format(e))


        return rec

    def talk(self, message):
        
        try: 
            self.__engine.say(message)
            self.__engine.runAndWait()
            self.__engine.stop()

        except:
            print("¡Hubo un error inesperado!")

