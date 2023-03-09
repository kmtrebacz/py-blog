'''
kmtrebacz/BlogCreator commands.py

Python file that let you write commands
'''


import sys
import os
import time as t
from getpass import getpass

_blogTitle = ""
_blogSubtitle = ""
_blogDescription = ""
_blogAuthor = ""
_blogTheme = ""
_adminPass = ""


# CLEARING CMD
def clr():
     os.system('cls')

# REPEAT INPUT WHILE ITS NONE
def inputIsNone(var, inpCont):
     while var == None or var == "":
          clr()
          var = input(inpCont)


# REPEAT GETPASS WHILE ITS NONE
def getPassIsNone(var, inpCont):
     while var == None or var == "":
          clr()
          var = getpass(inpCont)

# WHILE COMMANDS INPUT
def main():

     while True:
          inputCommands = input()

          #
          # HELP
          #
          if inputCommands == "-help":
               print(" HELP ")
               print("======")
               print("-help  ->  show all avaliable commands")
               print("-crtNew  ->  create new blog")
               print("-quit  ->  quit a program")


          #
          # CREATING NEW BLOG
          #
          elif inputCommands == "-crtNew":
               clr()
               print(inputCommands)
               print("! All fields are mandatory to complete !")

               #
               # BASIC INFOTMATIONS ABOUT BLOG
               #
               print("Basic informations")

               _blogTitle = input("Enter a blog title: ")
               inputIsNone(_blogTitle, "Enter a blog title: ")

               _blogSubtitle = input("Enter a blog subtitle: ")
               inputIsNone(_blogSubtitle, "Enter a blog subtitle: ")

               _blogDescription = input("Enter a blog description: ")
               inputIsNone(_blogDescription, "Enter a blog description: ")

               _blogAuthor = input("Enter your name: ")
               inputIsNone(_blogDescription, "Enter your name: ")


               #
               # BLOG'S APPEARANCE
               #
               print("\nAppearance")

               _blogTheme = input("Choose a theme for your blog: \n [1] -> minimalistic-full-white \n [2] -> the-themes-times \n")

               while not (_blogTheme == "1" or _blogTheme == "2" or _blogTheme == 1 or _blogTheme == 2):
                    clr()
                    _blogTheme = input("Choose a theme for your blog: \n [1] -> minimalistic-full-white \n [2] -> the-themes-times \n")


               #
               # BLOG'S MANAGMENT
               #
               print("\nManagement")

               _adminPass = getpass("Enter a password that you will use, when you want to log in to managment side: ")
               getPassIsNone(_adminPass, "Enter a password that you will use, when you want to log in to managment side: ")

               _adminPassRepeat = getpass("Repeat: ")   #Checking password
               while _adminPass != _adminPassRepeat: 
                    _adminPassRepeat = getpass("Repeat: ")
               print("Correct")

               clr()
               print("Everything is done")
               t.sleep(1.2)

               print("\nNow, will be created blog for you ;)")

               # TODO: Create index.html, style.css, main.js, python app that manage exiting blog


          #
          # QUIT
          #
          elif inputCommands == "-quit":
               sys.exit(0)

          #
          # ERROR
          #
          else:
               print("Error [1] -> Wrong command. Please write again")