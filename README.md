# Discord Disguised Backup Bot

A simple Discord bot with a few embed creation commands, that secretly allows you only to DM it and be unbanned from your own server and given admin role back, to use in the case of being hacked or having your server hijacked. In the code, you can choose the ID of the only user who will be able to do this, and to most people in a server it will just appear as a bot to create embeds easily.

# Setup

Firstly, make sure Python is installed. For a guide on how to do this, go to [(https://realpython.com/installing-python/)].

Then, install the Discord module for Python, use this: [(https://pypi.org/project/discord.py/)].

Next, download the main.py file from this repository, and note down where it is being stored on your computer.

Finally, open the code in a text editor, I recommend Notepad++, and wherever I have added a note, change that to the value I say there.

## Running

Open a command prompt/terminal and do `python [file path]` where the path is the file path of the main.py file you just downloaded. An example path would be `C:\Users\NAME\Downloads\main.py` for Windows or `/home/NAME/Downloads/main.py` for Linux. 

Well Done! It should now succesfully be running, and you can use !embed help in a server it is in to create embeds, and if you are the owner, you can DM it the word 'backup' and it should unban you from the server if you were and send an invite link. When you rejoin, you can DM it 'admin' and it will create give you an admin role.

NOTE: This will only work if the bot is still in the server and hasn't been removed yet.
