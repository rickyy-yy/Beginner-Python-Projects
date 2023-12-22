from datetime import datetime, time
from playsound import playsound
import requests
import os


def get_alarm():
    alarm_url = "http://bit.ly/3v6qbxf"
    alarm = requests.get(alarm_url, allow_redirects=True)

    open('C:\\Users\\yourf\\Music\\Alarm.mp3', 'wb').write(alarm.content)


def welcome_screen():
    print("╭━━━┳╮╱╱╱╱╱╱╱╱╱╭━━━┳╮╱╱╱╱╱╱╭╮")
    print("┃╭━╮┃┃╱╱╱╱╱╱╱╱╱┃╭━╮┃┃╱╱╱╱╱╱┃┃")
    print("┃┃╱┃┃┃╭━━┳━┳╮╭╮┃┃╱╰┫┃╭━━┳━━┫┃╭╮")
    print("┃╰━╯┃┃┃╭╮┃╭┫╰╯┃┃┃╱╭┫┃┃╭╮┃╭━┫╰╯╯")
    print("┃╭━╮┃╰┫╭╮┃┃┃┃┃┃┃╰━╯┃╰┫╰╯┃╰━┫╭╮╮")
    print("╰╯╱╰┻━┻╯╰┻╯╰┻┻╯╰━━━┻━┻━━┻━━┻╯╰╯")

    print("")

    print("Welcome to your Alarm Clock!")

    print("")


def get_time():

    unprocessedTime = str(input("Enter the time you wish to set the alarm for in the following format (24-hour) ("
                                "HH:MM): "))
    split_time = unprocessedTime.split(":")

    return split_time


def set_alarm(split_time):

    hour = int(split_time[0])
    minute = int(split_time[1])

    alarmTime = time(hour, minute)

    return alarmTime


def alarm_ring():
    print("Times up!")
    playsound('C:\\Users\\yourf\\Music\\Alarm.mp3')


def alarm_running(alarmTime):
    print("All set! The alarm is now running!")

    ring = False

    while not ring:
        currentTime = datetime.now().time().replace(microsecond=0)
        if currentTime == alarmTime:
            ring = True

    alarm_ring()


def main():
    welcome_screen()

    if os.path.exists("C:\\Users\\yourf\\Music\\Alarm.mp3"):
        pass
    else:
        get_alarm()

    alarm_running(set_alarm(get_time()))


main()
