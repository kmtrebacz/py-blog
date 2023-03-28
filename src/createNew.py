'''
kmtrebacz/py-blog createNew.py

Python file that get imformation about blog and create it.
'''


import time as t
from getpass import getpass
import src.the_themes_times as the_themes_times
import src.const as const


_blogTitle = ""
_blogSubtitle = ""
_blogDescription = ""
_blogAuthor = ""
_blogTheme = ""
_adminPass = ""


# REPEAT INPUT WHILE ITS NONE
def inputIsNone(var, inpCont):
     while var == None or var == "":
          const.clr()
          var = input(inpCont)


# REPEAT GETPASS WHILE ITS NONE
def getPassIsNone(var, inpCont):
     while var == None or var == "":
          const.clr()
          var = getpass(inpCont)

def main():
     print("! All fields are mandatory to complete !")


     #
     # BASIC INFOTMATIONS ABOUT BLOG
     #
     print("Basic informations")

     _blogTitle = input("Blog title: ")
     inputIsNone(_blogTitle, "Blog title: ")

     _blogSubtitle = input("Blog subtitle: ")
     inputIsNone(_blogSubtitle, "Blog subtitle: ")

     _blogDescription = input("Blog description: ")
     inputIsNone(_blogDescription, "Blog description: ")

     _blogAuthor = input("Your name: ")
     inputIsNone(_blogDescription, "Your name: ")


     #
     # BLOG'S APPEARANCE
     #
     print("\n========================")
     print("|      Appearance      |")
     print("========================")

     _blogTheme = input("Blog theme: \n [1] -> minimalistic-full-white \n [2] -> the-themes-times \n")

     while not (_blogTheme == "1" or _blogTheme == "2" or _blogTheme == 1 or _blogTheme == 2):
          const.clr()
          _blogTheme = input("Blog theme: \n [1] -> minimalistic-full-white \n [2] -> the-themes-times \n")


     #
     # BLOG'S MANAGMENT
     #
     print("\n========================")
     print("|      Management      |")
     print("========================")

     _adminPass = getpass("Password:")
     getPassIsNone(_adminPass, "Password:")

     _adminPassRepeat = getpass("Repeat password: ")   #Checking password
     while _adminPass != _adminPassRepeat: 
          _adminPassRepeat = getpass("Repeat password: ")
     print("Correct")

     const.clr()

     t.sleep(1)
     print("\nNow, will be created blog for you ;)")

     if _blogTheme == "1":
          print("This blog theme don't work.")
     elif _blogTheme == "2":
         the_themes_times.main(_blogTitle, _blogSubtitle, _blogDescription, _blogAuthor, _adminPass)
