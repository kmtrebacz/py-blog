'''
kmtrebacz/py-blog commands.py

Python file that create blog in style of The Themes Times
'''


import os
import time
import src.const

def main(_Title, _Subtitle, _Description ,_Author, _Pass):

     os.mkdir(os.path.join("./", "blog"))
     os.mkdir(os.path.join("./blog/", "docx-files"))



     print("Creating file nav.php")

     nav = open(os.path.join('./blog/',"nav.php"), 'w')
     nav.write('<nav class="nav d-flex justify-content-center"> <a class="p-2 link-secondary" href="index.php#all-posts">All posts</a> </nav> <a class="p-2 link-secondary" href="#">Newest Post</a>')
     nav.close()

     print("Created file nav.php")



     print("Creating file top.php")

     top = open(os.path.join('./blog/',"top.php"), "w")
     top.write("""<!doctype html><html lang="en"><head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <meta name="description" content=""> <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors"> <meta name="generator" content="Hugo 0.108.0"><title>""" + _Title + """</title><link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/blog/"> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">  <link rel="apple-touch-icon" href="/docs/5.3/assets/img/favicons/apple-touch-icon.png" sizes="180x180"> <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png"> <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png"> <link rel="manifest" href="/docs/5.3/assets/img/favicons/manifest.json"> <link rel="mask-icon" href="/docs/5.3/assets/img/favicons/safari-pinned-tab.svg" color="#712cf9"> <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon.ico"> <meta name="theme-color" content="#712cf9"> <style> .bd-placeholder-img { font-size: 1.125rem; text-anchor: middle; -webkit-user-select: none; -moz-user-select: none; user-select: none;} @media (min-width: 768px) { .bd-placeholder-img-lg { font-size: 3.5rem; }} .b-example-divider { height: 3rem; background-color: rgba(0, 0, 0, .1); border: solid rgba(0, 0, 0, .15); border-width: 1px 0; box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);} .b-example-vr { flex-shrink: 0; width: 1.5rem; height: 100vh;} .bi { vertical-align: -.125em; fill: currentColor;} .nav-scroller { position: relative; z-index: 2; height: 2.75rem; overflow-y: hidden;} .nav-scroller .nav { display: flex; flex-wrap: nowrap; padding-bottom: 1rem; margin-top: -1px; overflow-x: auto; text-align: center; white-space: nowrap; -webkit-overflow-scrolling: touch;} </style>  <link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900&display=swap" rel="stylesheet">  <style> /* stylelint-disable selector-list-comma-newline-after */ .blog-header { border-bottom: 1px solid #e5e5e5;} .blog-header-logo { font-family: "Playfair Display", Georgia, "Times New Roman", serif /*rtl:Amiri, Georgia, "Times New Roman", serif*/ ; font-size: 2.25rem;} .blog-header-logo:hover { text-decoration: none;} h1, h2, h3, h4, h5, h6 { font-family: "Playfair Display", Georgia, "Times New Roman", serif /*rtl:Amiri, Georgia, "Times New Roman", serif*/ ;} .display-4 { font-size: 2.5rem;} @media (min-width: 768px) { .display-4 { font-size: 3rem; }} .flex-auto { flex: 0 0 auto;} .h-250 { height: 250px;} @media (min-width: 768px) { .h-md-250 { height: 250px; }} /* Pagination */ .blog-pagination { margin-bottom: 4rem;} /* * Blog posts */ .blog-post { margin-bottom: 4rem;} .blog-post-title { font-size: 2.5rem;} .blog-post-meta { margin-bottom: 1.25rem; color: #727272;} /* * Footer */ .blog-footer { padding: 2.5rem 0; color: #727272; text-align: center; background-color: #f9f9f9; border-top: .05rem solid #e5e5e5;} .blog-footer p:last-child { margin-bottom: 0;} </style></head><body> <div class="container"> <header class="blog-header lh-1 py-3"> <div class="row flex-nowrap justify-content-between align-items-center"> <div class="col-12 text-center"> <a class="blog-header-logo text-dark" href="index.php">""" + _Title + """</a> </div> </div> </header> <div class="nav-scroller py-1 mb-2"> <?php include('./nav.php');?> </div> </div> <main class="container">  <div class="row g-5" id="newest"> <div class="col-md-8"> <article class="blog-post">""")
     top.close()

     print("Created file top.php")



     print("Creating file bottom.php")

     bottom = open(os.path.join('./blog/',"bottom.php"), "w")
     bottom.write("""</article></div><div class="col-md-4"><div class="position-sticky" style="top:2rem"><div class="p-4"><h4 class="fst-italic">Archives</h4><ol class="list-unstyled mb-0"><?php include('./sidenav.html');?></ol></div></div></div></div></main><footer class="blog-footer"><p>All <a href="https://github.com/kmtrebacz/BlogCreator" target="_blank">BlogCreator</a> was made by <a href="https://github.com/kmtrebacz" target="_blank">@kmtrebacz</a></p><p>Blog template built for <a href="https://getbootstrap.com/" target="_blank">Bootstrap</a> by <a href="https://twitter.com/mdo" target="_blank">@mdo</a>.</p><p><a href="#">Back to top</a></p></footer></body></html><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>""")
     bottom.close()

     print("Created file bottom.php")



     print("Creating file index.php")

     index = open(os.path.join('./blog/',"index.php"), "w")
     index.write( """ <!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content=""><meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors"><meta name="generator" content="Hugo 0.108.0"><title>""" + _Title + """</title><link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/blog/"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous"><link rel="apple-touch-icon" href="/docs/5.3/assets/img/favicons/apple-touch-icon.png" sizes="180x180"><link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png"><link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png"><link rel="manifest" href="/docs/5.3/assets/img/favicons/manifest.json"><link rel="mask-icon" href="/docs/5.3/assets/img/favicons/safari-pinned-tab.svg" color="#712cf9"><link rel="icon" href="/docs/5.3/assets/img/favicons/favicon.ico"><meta name="theme-color" content="#712cf9"><style>.bd-placeholder-img{font-size:1.125rem;text-anchor:middle;-webkit-user-select:none;-moz-user-select:none;user-select:none}@media (min-width: 768px){.bd-placeholder-img-lg{font-size:3.5rem}}.b-example-divider{height:3rem;background-color:rgba(0, 0, 0, .1);border:solid rgba(0, 0, 0, .15);border-width:1px 0;box-shadow:inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15)}.b-example-vr{flex-shrink:0;width:1.5rem;height:100vh}.bi{vertical-align:-.125em;fill:currentColor}.nav-scroller{position:relative;z-index:2;height:2.75rem;overflow-y:hidden}.nav-scroller .nav{display:flex;flex-wrap:nowrap;padding-bottom:1rem;margin-top:-1px;overflow-x:auto;text-align:center;white-space:nowrap;-webkit-overflow-scrolling:touch}</style><link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900&display=swap" rel="stylesheet"><style>.blog-header{border-bottom:1px solid #e5e5e5}.blog-header-logo{font-family:"Playfair Display", Georgia, "Times New Roman", serif;font-size:2.25rem}.blog-header-logo:hover{text-decoration:none}h1,h2,h3,h4,h5,h6{font-family:"Playfair Display", Georgia, "Times New Roman", serif}.display-4{font-size:2.5rem}@media (min-width: 768px){.display-4{font-size:3rem}}.flex-auto{flex:0 0 auto}.h-250{height:250px}@media (min-width: 768px){.h-md-250{height:250px}}.blog-pagination{margin-bottom:4rem}.blog-post{margin-bottom:4rem}.blog-post-title{font-size:2.5rem}.blog-post-meta{margin-bottom:1.25rem;color:#727272}.blog-footer{padding:2.5rem 0;color:#727272;text-align:center;background-color:#f9f9f9;border-top:.05rem solid #e5e5e5}.blog-footer p:last-child{margin-bottom:0}</style></head><body><div class="container"><header class="blog-header lh-1 py-3"><div class="row flex-nowrap justify-content-between align-items-center"><div class="col-12 text-center"><a class="blog-header-logo text-dark" href="index.php">""" + _Title + """</a></div></div></header><div class="nav-scroller py-1 mb-2"><nav class="nav d-flex justify-content-center"><a class="p-2 link-secondary" href="#">Newest Post</a><a class="p-2 link-secondary" href="index.php#all-posts">All posts</a></nav></div></div><main class="container"><div class="p-4 p-md-5 mb-4 rounded text-bg-dark"><div class="col-md-6 px-0"><h1 class="display-4 fst-italic">""" + _Title + """</h1><p class="lead my-3">""" + _Description + """ </p></div></div><div class="row g-5" id="all-posts"><div class="col-md-4"><div class="position-sticky" style="top:2rem"><div class="p-4"><h4 class="fst-italic">Archives</h4><ol class="list-unstyled mb-0"><?php include('./sidenav.html');?></ol></div></div></div></div></main><footer class="blog-footer"><p>All <a href="https://github.com/kmtrebacz/BlogCreator" target="_blank">BlogCreator</a> was made by <a href="https://github.com/kmtrebacz" target="_blank">@kmtrebacz</a></p><p>Blog template built for <a href="https://getbootstrap.com/" target="_blank">Bootstrap</a> by <a href="https://twitter.com/mdo" target="_blank">@mdo</a>.</p><p><a href="#">Back to top</a></p></footer></body></html><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>""")
     index.close()

     print("Created file index.php")



     print("Creating sidenav.html")

     sidenav = open(os.path.join('./blog/', "sidenav.html"), "w")
     sidenav.write("""""")
     sidenav.close()

     print("Created file sidenav.html")



     print("Creating newPost.py")

     newPost = open(os.path.join('./blog/', "newPost.py"), "w")
     newPost.write(f'''import codecs
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
        _postContentFileName = input("Enter content file name:")
        
        docx_file = open(os.path.join('./docx-files/', _postContentFileName + '.docx'), 'rb')
        html_file = open(os.path.join('./docx-files/', _postContentFileName + ".html"), 'wb')
        
        document = mammoth.convert_to_html(docx_file)
        html_file.write(document.value.encode('utf8'))
        
        docx_file.close()
        html_file.close() 
        
        _postContentFile = codecs.open(os.path.join('./docx-files/', _postContentFileName +  ".html"), "r", "utf-8")
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
        _newPost.write(f"""<?php include('./top.php');?><h2 class="blog-post-title mb-1">''' + "{_postTitle" + "}" + '''</h2> <p class="blog-post-meta">''' + "{" + "_postDate}" + '</p>' + "{" + "_postContent}" + f''' <?php include('./bottom.php');?>""")
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
     ''')
     newPost.close()

     print("Created newPost.py")


     print("Done")
