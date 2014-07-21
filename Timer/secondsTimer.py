#!/usr/bin/python

from time import sleep

def getAlarmTime():
    seconds = input("Enter how many seconds you want to count down from: ")
    while seconds > 0:
        print seconds
        if seconds > 0 and seconds < 1: #counts down by actual seconds until var seconds > 0 and < 1, 
            sleep(seconds)              #in which case it'll count down by remaining value, to insure
        else:                           #that floats and decimals will be accounted for.
            sleep(1)
        seconds -= 1

getAlarmTime()
