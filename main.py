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

    switcher(function, instruction)


def switcher(function, instruction):

    if function == 0:
        engine.play()
    elif function == 1:
        engine.searches()
    elif function == 3:
        engine.launcher()
    elif function == 4:
        engine.current_time()
    elif function == 5:
        engine.current_date()
    elif function == 6:
        engine.grettings()
    elif function == 7:
        sys.exit()


if __name__ == '__main__':

    vc.talk("Bienvenido. Activando el sistema")

    while True:

        command = vc.handler_activator()

        if command != '':
            recognize_command(command)