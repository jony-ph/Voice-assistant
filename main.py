import src.Voice_Client as voice_client
import src.engine as engine
import key_words as key_words
import sys

vc = voice_client.Voice_Client('eva')
    
def recognize_command(command):

    function = ''

    print(command)

    for words in key_words.key_words:

        for key in words:

            if key in command:

                function = key_words.key_words.index(words)
                instruction = command.replace(key + ' ', '')


if __name__ == '__main__':

    vc.talk("Bienvenido. Activando el sistema")

    while True:

        command = vc.handler_activator()

        if command != '':
            recognize_command(command)