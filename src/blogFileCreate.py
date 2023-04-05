'''
kmtrebacz/py-blog commands.py

Python file that create blog in style of The Themes Times
'''

import os
import time
import src.const

def createFiles(_Title, _Subtitle, _Description ,_Author, _Pass, _themeName):


     os.mkdir(os.path.join("./", "blog"))
     os.mkdir(os.path.join("./blog/", "docx-files"))


     print("Creating file nav.php")

     with open (os.path.join(f'./themes/{_themeName}/nav.php')) as navThms:
          navThms = navThms.read()
          navThms = navThms.replace("_Title", _Title)
          navThms = navThms.replace("_Description", _Description)
          navThms = navThms.replace("_Author", _Author)
          navThms = navThms.replace("<_Pass>", _Pass)
          with open(os.path.join('./blog/',"nav.php"), "w") as nav:
               nav.write(navThms)

     print("Created file nav.php")



     print("Creating file top.php")

     with open (os.path.join(f'./themes/{_themeName}/top.php')) as topThms:
          topContent = topThms.read()
          topContent = topContent.replace("_Title", _Title)
          topContent = topContent.replace("_Description", _Description)
          topContent = topContent.replace("_Author", _Author)
          topContent = topContent.replace("<_Pass>", _Pass)
          with open(os.path.join('./blog/',"top.php"), "w") as top:
               top.write(topContent)

     print("Created file top.php")



     print("Creating file bottom.php")

     with open (os.path.join(f'./themes/{_themeName}/bottom.php')) as bottomThms:
          bottomContent = bottomThms.read()
          bottomContent = bottomContent.replace("_Title", _Title)
          bottomContent = bottomContent.replace("_Description", _Description)
          bottomContent = bottomContent.replace("_Author", _Author)
          bottomContent = bottomContent.replace("<_Pass>", _Pass)
          with open(os.path.join('./blog/',"bottom.php"), "w") as bottom:
               bottom.write(bottomContent)

     print("Created file bottom.php")




     print("Creating file index.php")

     with open (os.path.join(f'./themes/{_themeName}/index.php')) as indexThms:
          indexContent = indexThms.read()
          indexContent = indexContent.replace("_Title", _Title)
          indexContent = indexContent.replace("_Description", _Description)
          indexContent = indexContent.replace("_Author", _Author)
          indexContent = indexContent.replace("<_Pass>", _Pass)
          with open(os.path.join('./blog/',"index.php"), "w") as index:
               index.write(indexContent)

     print("Created file index.php")



     print("Creating sidenav.html")

     sidenav = open(os.path.join('./blog/', "sidenav.html"), "w")
     sidenav.write("""""")
     sidenav.close()

     print("Created file sidenav.html")



     print("Creating newPost.py")

     with open(os.path.join('./src/', "newPost.py")) as newPostSrc:
          indexContent = newPostSrc.read()
          with open(os.path.join('./blog/',"newPost.py"), "w") as newPost:
               newPost.write(indexContent)

     print("Created newPost.py")


     print("Done")


def ttt(_Title, _Subtitle, _Description ,_Author, _Pass):
     _themeName = "ttt"
     createFiles(_Title, _Subtitle, _Description ,_Author, _Pass, _themeName)