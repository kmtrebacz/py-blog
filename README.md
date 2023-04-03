py-blog
===========

An easy-to-use app that allows you to create your own blog and write new entries with just a few simple commands!

# Requirements
Before getting started, make sure you have the following requirements installed on your computer:
- `Python`
- `pip`
- `venv`
- `mammoth`
- `xampp`

# Getting Started
Here's how to get started with py-blog:
## Your first blog.
- Navigate to the py-blog directory on your computer.
- Open the directory using the command prompt.
- Type `py main.py` or `python main.py` to launch the app.
- Once you see the `>` prompt, you can start typing commands.
- After creating your blog, move the `blog` folder to `/xampp/htdocs`.
- Start the XAMPP app and start Apache.
- In your web browser, type `localhost/blog` to view your new blog.

## Adding Your First Post
- Navigate to `/xampp/htdocs/blog/docx-files`.
- Put your post's content file (must be .docx) in the `docx-files` folder.
- Navigate to `/xampp/htdocs/blog/` in the command prompt.
- Type `py newPost.py` or `python newPost.py`.
- When prompted, enter the name of your post's content file (without the .docx extension).
- Fill out any additional information as prompted.
- Refresh your website in your browser to see your new post.

# Themes
Currently, py-blog offers two themes:
- The Themes Times
- Minimalistic full white theme (which is currently not functional in version 0.2).

However, there will be more themes added in the future!

# Command List
Here are all the commands you can use in py-blog:
- `-help`: Displays all available commands
- `-cNew`: Allows you to create a new blog
- `-thms`: Displays all available themes and allows you to open a test page
- `-quit`: Lets you quit the program