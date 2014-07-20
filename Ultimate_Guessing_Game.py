#!/usr/bin/python
#Ultimate Guessing Game

from random import randint
from time import sleep
from sys import exit

user_choice = raw_input('select type of guessing game(letter, number, punctuation): ') 
alphabet = ('abcdefghijklmnopqrstuvwxyz')
characters = ("!@#$%^&*()_+-=[]{}\/.,<>`~\":;'")

class ultimateGuessingGame: 
  global alphabet
  def guessLetter(self): #creating letter guessing game
    player_name = raw_input('Enter your name here:')
    print "Hello " + player_name + " welcome to the letter guessing game."
    print "Instructions: Guess the lucky letter from the latin alphabet (a-z) within 3 tries in order to win the game.\n"
    print 'Try #1 !'
    __lucky_letter = alphabet[randint(1,26)]
    try1 = raw_input('Enter the letter which you think is the lucky letter:')
    if try1.lower() == __lucky_letter:
      print "Wow, you're lucky, you won on your first try."
      sleep(5)
      print('press<enter>')
      sleep(1)
      exit()
    else:
      print "You guessed wrong, 2 tries remaining."
    #Second Attempt
    try2 = raw_input('Enter the letter which you think is the lucky letter:')
    if try2.lower() == __lucky_letter:
      print 'Congratulations, you win!'
      sleep(5)
      print('press<enter>')
      sleep(1)
      exit()
    else:
      print "Your guess was incorrect, 1 try remaining"
    #Third Attempt
    try3 = raw_input('Enter the letter which you think is the lucky letter:')
    if try3.lower() == __lucky_letter:
      print 'Congratulations, you win!'
      sleep(5)
      print('press<enter>')
      sleep(1)
      exit()
    else:
      print "Sorry, your guess was incorrect, you lose :-( \n"
      print "The letter was " + __lucky_letter
      sleep(5)
      print('press<enter>')
      sleep(1)
      exit()
    
  def guessNumber(self): #creating number guessing game
    __lucky_number = randint(1,100)
    print "Welcome to the Guessing Game!"
    player_name = raw_input("Enter Your Name Here: ")
    print "Welcome " + player_name
    print "Instructions: Choose a random number between 1 - 100 within 3 tries in order to win the game."
    try1 = int(raw_input("Enter Number Here: "))
    if __lucky_number == try1:
      print "Congratulations, You Win!"
      sleep(3)
      raw_input('press<enter>')
      exit()
    elif try1 >= 101:
      print "Please select a number between 1-100"
    else:
      print "Sorry wrong number, 2 more tries remaining"
    #2nd Try
    try2 = int(raw_input("Enter Number Here: "))
    if try2 == __lucky_number:
      print "Wow! You Won"
      sleep(3)
      raw_input('press<enter>')
      exit()
    elif try2 >= 101:
      print "Please select a number between 1-100"
    else:
      print "Sorry wrong number, 1 last try remaining"
    #3rd Attempt
    try3 = int(raw_input("Enter Number Here: "))
    if try3 == __lucky_number:
      print "YOU WIN!"
    else:
      print "Sorry you LOSE"
      print "The Number was: " + str(__lucky_number)
      print "Game over!"
      sleep(5)
      raw_input('press <enter>')                        
      exit()

  def guessPunctuation(self): #creating character guessing game
    player_name = raw_input('Enter your name here: ')
    global characters
    print "Welcome to the punctuation mark guessing game " + player_name
    print "Instructions: select the proper character in 3 tries in order to win the game.\n"
    print "Characters availible include: !@#$%^&*()_+-=[]{}\/.,<>`~\":;'"
    __lucky_character = characters[randint(1,29)]
    try1 = raw_input('Enter character here: ')
    if try1 == __lucky_character:
      print "Wow! You Won on the first try."
      sleep(3)
      raw_input('press<enter>')
      exit()
    else:
      print "Sorry wrong character, 2 tries remaining"
    #2nd Attempt
    try2 = raw_input('Enter character here: ')
    if try2 == __lucky_character:
      print "You Win, Congratulations"
      sleep(4)
      raw_input('press<enter>')
      exit()
    else: 
      print "Bad guess, 1 try left"
    #3rd Attempt
    try3 = raw_input('Enter character here: ')
    if try3 == __lucky_character:
      print "Correct! Well Done!"
      sleep(3)
      raw_input('press<enter>')
      exit()
    else:
      print "You Lose"
      print "The character was " + __lucky_character
      sleep(3)
      raw_input('press<enter>')
      print "Game Over"
      exit()

  global user_choice #inializes user query to select type of guessing game and reacts accordingly
  def __init__(self):
    if user_choice == 'letter':
      self.guessLetter()
    elif user_choice == 'number':
      self.guessNumber()
    elif user_choice == 'punctuation':
      self.guessPunctuation()
    else:
      print 'spellingError'
      exit()
      
game = ultimateGuessingGame() #creates object for class
game()

