'''
kmtrebacz/py-blog createNew.py

Python file that get imformation about blog and create it.
'''


import os
import time as t
from getpass import getpass
# import themes
import the_themes_times


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

def main():
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

     if _blogTheme == "1":
          print("1")
     elif _blogTheme == "2":
         the_themes_times.main(_blogTitle, _blogSubtitle, _blogDescription, _blogAuthor, _adminPass)
