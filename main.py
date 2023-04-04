'''
kmtrebacz/py-blog main.py

Main app of all of project.
'''

import sys 
import time as t
import src.createNew as createNew
import src.const as const

__VERSION__ = "0.2.1"

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
          if inputCommands == "show -help":
               const.clr()

               print("==================")
               print("|      HELP      |")
               print("==================")
               print("show -help  ->  show all avaliable commands")
               print("show -themes  ->  show all avaliable themes, and let you open test page")
               print("create -blog  ->  create new blog")
               print("quit  ->  quit a program")

          #
          # SHOWING THEMES
          #
          elif inputCommands == "show -themes":
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
          # CREATING NEW BLOG
          #
          elif inputCommands == "create -blog":
               const.clr()

               createNew.main()

          #
          # QUIT
          #
          elif inputCommands == "quit":
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

    
