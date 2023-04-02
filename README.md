py-blog
===========

App that will allow you to build your own blog, write new entries and many more with several easy to remember commands.

## Requirements
- `Python`
- `pip`
- `venv`
- `mammoth`
- `xampp`

## How to use it?
#### Creating first blog and opening it
- At first go to py-blog directory
- Open that directory using cmd
- In cmd ype `py main.py` or `python main.py`
- After seeing ` > `, you can type commands
- After creating blog move `blog` folder to `/xampp/htdocs`
- Start xampp app and start apache
- Then in your internet browser type `localhost/blog`
#### Adding first post
- Go to `/xampp/htdocs/blog/docx-files`
- In `docx-files` folder put your post's content file (must be .docx)
- Now go to `/xampp/htdocs/blog/`
- Open it using cmd
- Type w cmd  `py newPost.py` or `python newPost.py`
- If you see `Enter content file name: ` type post's content file name (without .docx)
- After filled out everythink you can refresh website  in your browser
- Now you should see that new post was added


## Themes
At the moment app has 2 themes:
- The Themes Times
- Minimalistic full white (in version 0.2 don't work)
- In future there will be way more themes.

## List of all commands
- `-help` -> show all avaliable commands
- `-cNew` -> it lets you create new blog
- `-thms` -> show all avaliable themes, and let you open test page
- `-quit` -> it let you quit a program
