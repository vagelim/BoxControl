BoxControl
==========

SMS control of computer
Module currently only supports *NIX systems (this is due to cron use, easily ported)

Creating a cron-job calling gmail.py will run the application



Code.py          - Sends One Time Password for use in SSH authentication (similar to google's OTP-auth)
Commander.py     - Features not yet implemented
gconf.py         - Handles configuration of program
gmail.py         - Interface for retrieving mail from gmail account
pymail.py        - SMTP interface for python (configured for gmail)
readmail.py      - Executes certain actions depending on content of SMS-message (this does the message parsing after download)
sendPassword.py  - Parses plaintext CSV-formatted file (i.e. from Lastpass or other password manager) and sends specified password
todo.py          - Functions to implement a todo-list feature for the program
