#!/usr/bin/python

from time import sleep

def getAlarmTime():
    seconds = input("Enter how many seconds you want to count down from: ")
    while seconds > 0:
        print seconds
        sleep(1)
        seconds -= 1
        
getAlarmTime()
