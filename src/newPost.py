import codecs
import mammoth
import os
from datetime import datetime
from datetime import date
from getpass import *


_pass = "{_Pass}"
_postTitle = ""
_postContent = ""
_postAuthor = ""

def main():
     checkingPass = getpass("Password:")

     if checkingPass == _pass:
         # password
        _postTitle = input("Enter post title: ")
        
        # content - docx to html
        _postContentFileName = input("Enter content file name: ")
        
        docx_file = open(os.path.join('./docx-files/', _postContentFileName + '.docx'), 'rb')
        html_file = open(os.path.join('./docx-files/', _postContentFileName + ".html"), 'wb')
        
        document = mammoth.convert_to_html(docx_file)
        html_file.write(document.value.encode('utf8'))
        
        docx_file.close()
        html_file.close() 
        
        _postContentFile = codecs.open(os.path.join('./docx-files/', _postContentFileName +  ".html"), 'r', "utf-8")
        _postContent = _postContentFile.read()
        _postContentFile.close()
        

        # author
        _postAuthor = input("Enter post author: ")
        
        # file name
        _postDate = str(date.today())
        _postFileName = _postDate + "-" + _postTitle + ".php"

        # new post file
        print("Creating new post")
        _newPost = open(os.path.join('./', _postFileName), "w")
        _newPost.write(f"""<?php include('./top.php');?><h2 class="blog-post-title mb-1"> {_postTitle} </h2> <p class="blog-post-meta"> {_postDate} </p> {_postContent} <?php include('./bottom.php');?>""")
        _newPost.close()
        print("Created new post")

        # update sideNav
        print("Adding link to sideNav.html")
        _postLink = open(os.path.join('./', "sideNav.html"), "a")
        _postLink.write("<a href='./" + _postFileName + "'>" + _postDate + "-" + _postTitle + "</a><br>")
        _postLink.close()
        print("Added link to sideNav.html")
     else:
        print("Wrong password.  Restart the program for entering again")
    

if __name__ == "__main__":
     main()

