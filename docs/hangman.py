import random as r
import time
#variables
lives = 12
wrong = 0
wrongGuess = []

#n stands for number of words in text document
try:
    myFile = open("words.txt", "r")
    wordList = myFile.readlines()
    myFile.close()
except IOError:
    print("bugger, can't locate wordlist")

#determine word & test
word = r.choice(wordList)
print(word)

#determine word length & test
wordLength = len(word)-1
print(wordLength)

#print blank space
blankSpace = "_ " * wordLength
print(blankSpace)

#print lives
displayLives = "O" * lives
print(displayLives)

#experimental

guess = input("Guess a letter  ")
"""
wrongGuess.append(guess)
guess = input("Guess a letter  ")
wrongGuess.append(guess)
print("Previous Guesses ", wrongGuess)
"""

if guess in word:
  print("yesi")
else:
  print("no")
          
