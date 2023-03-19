import os
from datetime import datetime
from datetime import date
import getpass from getpass

#current_time = datetime.now().strftime("%H:%M:%S")
#print("Current Time =", current_time)


_pass = "b"
_postTitle = ""
_postContent = ""
_postAuthor = ""

def main():
     checkingPass = getpass("Password:")

     if checkingPass == _pass:
        _postTitle = input("Enter post title: ")
        print('- To make a bigger text type <h2> THERE WRITE TEXT </h2>')
        print(' - To add image write <img src="link to image">')
        _postContent = input("Enter post content: ")
        _postAuthor = input("Enter post author: ")
        _postDate = str(date.today())

        _postFileName = _postDate + "-" + _postTitle + ".php"

        print("Creating new post")
        _newPost = open(os.path.join('./', _postFileName), "w")
        _newPost.write("<?php include('./top.php');?>" + '<h2 class="blog-post-title mb-1">' + _postTitle + '</h2> <p class="blog-post-meta">' + _postDate + '</p>' + _postContent + "<?php include('./bottom.php');?>")
        _newPost.close()
        print("Created new post")

        print("Adding link to sideNav.html")
        _postLink = open(os.path.join('./', "sideNav.html"), "a")
        _postLink.write("<a href='./" + _postFileName + "'>" + _postDate + "-" + _postTitle + "</a><br>")
        _postLink.close()
        print("Added link to sideNav.html")
     else:
        print("Wrong password.  Restart the program for entering again")
    

if __name__ == "__main__":
     main()

