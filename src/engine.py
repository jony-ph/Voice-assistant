import os
import subprocess

from datetime import datetime, time

def play():
    pass

def searches():
    pass

def launcher(instruction):
    
    target = instruction + '.exe'
    initial_dir = 'C:\\'

    path = ''
    message = ''

    for root, _, files in os.walk(initial_dir):

        if target in files:
            path = os.path.join(root, target)
            break

    try:
        subprocess.call([path])
        message = 'Ejecutando ' + instruction
    except OSError:
        message = 'No se encontró el programa'

    print(path)

    return message


def current_time():

    time_now = datetime.now().time()

    current_time = datetime.now().time()
    current_time = time.strftime(current_time, '%I:%M')

    FORMAT_TIME = '%H:%M:%S'
    ONE_MORNING = datetime.strptime('01:00:00', FORMAT_TIME).time()
    FINISH_ONE_MORNING = datetime.strptime('01:59:59', FORMAT_TIME).time()
    ONE_AFTERNOON = datetime.strptime('13:00:00', FORMAT_TIME).time()
    FINISH_ONE_AFTERNOON = datetime.strptime('04:59:59', FORMAT_TIME).time()
    MORNING = datetime.strptime('00:00:00', FORMAT_TIME).time()
    AFTERNOON = datetime.strptime('12:00:00', FORMAT_TIME).time()
    NIGHT = datetime.strptime('19:00:00', FORMAT_TIME).time()

    if time_now >= ONE_MORNING and time_now <= FINISH_ONE_MORNING:
        message = "Es la " + current_time + " de la mañana"
    elif time_now >= ONE_AFTERNOON and time_now <= FINISH_ONE_AFTERNOON:
        message = "Es la " + current_time + " de la tarde"
    elif time_now >= MORNING and time_now < AFTERNOON: 
        message = "Son las " + current_time + " de la mañana"
    elif time_now >= AFTERNOON and time_now < NIGHT:
        message = "Son las " + current_time + " de la tarde"
    else:
        message = "Son las " + current_time + " de la noche"

    return message



def current_date():

    date_now = datetime.today()
    date_format = date_now.strftime('%d de %B del %Y')

    if 'January' in date_format:
        date_format = date_format.replace('January', 'enero')
    elif  'February' in date_format:
        date_format = date_format.replace('February', 'febrero')
    elif  'March' in date_format:
        date_format = date_format.replace('March', 'marzo')
    elif  'April' in date_format:
        date_format = date_format.replace('April', 'abril')
    elif  'May' in date_format:
        date_format = date_format.replace('May', 'mayo')
    elif  'June' in date_format:
        date_format = date_format.replace('June', 'junio')
    elif  'July' in date_format:
        date_format = date_format.replace('July', 'julio')
    elif  'August' in date_format:
        date_format = date_format.replace('August', 'agosto')
    elif  'September' in date_format:
        date_format = date_format.replace('September', 'septiembre')
    elif  'October' in date_format:
        date_format = date_format.replace('October', 'octubre')
    elif  'November' in date_format:
        date_format = date_format.replace('November', 'noviembre')
    elif  'December' in date_format:
        date_format = date_format.replace('December', 'diciembre')

    return "Hoy es: " + date_format


def grettings():

    time_now = datetime.now().time()

    FORMAT_TIME = '%H:%M:%S'
    MORNING = datetime.strptime('00:00:00', FORMAT_TIME).time()
    AFTERNOON = datetime.strptime('12:00:00', FORMAT_TIME).time()
    NIGHT = datetime.strptime('19:00:00', FORMAT_TIME).time()

    if time_now >= MORNING and time_now < AFTERNOON: 
        message = "Buen día"
    elif time_now >= AFTERNOON and time_now < NIGHT:
        message = "Buena tarde"
    else:
        message = "Buena noche"

    return message

    



    

    


    
    