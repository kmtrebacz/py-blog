'''
kmtrebacz/py-blog main.py

Main app of all of project.
'''

import sys 
import time as t
import src.createNew as createNew
import src.const as const

__VERSION__ = "0.2"

def startApp():
     print("Version: ", __VERSION__)
     print("""
██████╗ ██╗   ██╗     ██████╗ ██╗      ██████╗  ██████╗ 
██╔══██╗╚██╗ ██╔╝     ██╔══██╗██║     ██╔═══██╗██╔════╝ 
██████╔╝ ╚████╔╝█████╗██████╔╝██║     ██║   ██║██║  ███╗
██╔═══╝   ╚██╔╝ ╚════╝██╔══██╗██║     ██║   ██║██║   ██║
██║        ██║        ██████╔╝███████╗╚██████╔╝╚██████╔╝
╚═╝        ╚═╝        ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ 
""")
     t.sleep(1.5)


def commands():
     while True:
          inputCommands = input(" > ")

          #
          # HELP
          #
          if inputCommands == "-help":
               const.clr()

               print("==================")
               print("|      HELP      |")
               print("==================")
               print("help  ->  show all avaliable commands")
               print("cNew  ->  create new blog")
               print("thms  ->  show all avaliable themes, and let you open test page")
               print("quit  ->  quit a program")

          #
          # CREATING NEW BLOG
          #
          elif inputCommands == "-cNew":
               const.clr()

               createNew.main()

          #
          # SHOWING THEMES
          #
          elif inputCommands == "-thms":
               const.clr()

               print("====================")
               print("|      THEMES      |")
               print("====================")
               print("- the themes times [1]")

               whatOpen = input("Which theme you want to see:")

               if whatOpen == "1":
                    print("ttt")
               else:
                    print("Error")

          #
          # QUIT
          #
          elif inputCommands == "-quit":
               const.clr()

               sys.exit(0)

          #
          # ERROR
          #
          else:
               print("Error [1] -> Wrong command. Please write again")


if __name__ == "__main__":
    startApp()

    commands()

    
