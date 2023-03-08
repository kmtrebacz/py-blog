import sys, os

_blogTitle = ""
_blogSubtitle = ""
_blogDescription = ""
_blogAuthor = ""
_blogTheme = ""
_adminPass = ""

def clr():
     os.system('cls')

def writeCommands():

     while True:
          inputCommands = input()

          if inputCommands == "-help":
               print("      HELP      ")
               print("================")
               print("-help  ->  show all avaliable commands")
               print("-crtNew  ->  create new blog")
               print("-crntVer  ->  print current version of program")
               print("-quit  ->  quit a program")

          elif inputCommands == "-crtNew":
               clr()
               print(inputCommands)

               print("Basic informations")
               _blogTitle = input("Enter a blog title: ")
               _blogSubtitle = input("Enter a blog subtitle: ")
               _blogDescription = input("Enter a blog description: ")
               _blogAuthor = input("Enter your name: ")

               print("\nAppearance")
               _blogTheme = input("Choose a theme for your blog: \n [1] -> minimalistic-full-white \n [2] -> the-themes-times \n")
               while not (_blogTheme == "1" or _blogTheme == "2" or _blogTheme == 1 or _blogTheme == 2):
                    clr()
                    _blogTheme = input("Choose a theme for your blog: \n [1] -> minimalistic-full-white \n [2] -> the-themes-times \n")

               print("\nManagement")
               _adminPass = input("Enter a password that you will use, when you want to log in to managment side: ")
               _adminPassRepeat = input("Repeat: ")

               while _adminPass != _adminPassRepeat: 
                    _adminPassRepeat = input("Repeat: ")
               print("Correct")

               clr()
               print("\n Now, will be created blog for you ;)")


          elif inputCommands == "-crntVer":
               print("Version: 0.0.2")

          elif inputCommands == "-quit":
               sys.exit(0)

          else:
               print("Error [1] -> Wrong command. Please write again")


if __name__ == "__main__":
     writeCommands()
