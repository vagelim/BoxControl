#!/usr/bin/python
from imaplib import *
import time
from readmail import *
from gconf import ReadConfig
from gconf import *
DEBUG = 0
    
#from work import Work
#Work would check the server and see if it was still up
def gmail(delete=None):#if delete != None then gmail deletes all inbox

    #Work()


    server = IMAP4_SSL("imap.gmail.com")
    server.login(ReadConfig("user"),ReadConfig("password"))
    #mboxes = server.list()[1]
    box = server.select("INBOX")
    
    if delete != None:
        typ, data = server.search(None, 'ALL')
        for num in data[0].split():
            server.store(num, '+FLAGS', '\\Deleted')
            server.expunge()
        exit()

    #data = server.search(None, "(FROM \"default@gmail.com\")")
    data = server.search(None, "(FROM \""+ ReadConfig('phone') + "\")")


    #Find most recent message
    #Turn the data to a string, find the last element, and strip the ['] characters
    #msgNum must be converted from string to int
    msgNum = str(data[1]).rsplit(None)[-1].strip('[\']')
    if msgNum == '':#This is only true if there is no mail!!
        print "No mail in box"
        file = open(path + "latest", 'w')
        file.write('0')
        exit()
        
    msgNum = int(msgNum)
    #Check if msgNum is the most recent message
    file = open(path + "latest", 'r')
    latest = file.read()
    file.close()

    latest = int(latest)

    if latest == msgNum:
        print "No new mail"
        exit()

    file = open(path + "latest", 'w')
    file.write(str(msgNum))#File output must be char buffer
    file.close()
    print latest
    print msgNum
    #The following makes sure to get ALL mails, not just the most recent one
    counter = 1
    while (latest + counter) != (msgNum + 1):
        data = server.fetch(latest + counter, '(UID BODY[TEXT])')
        contents = str(data[1][0][1]).rstrip('\r\n')
        print contents[:10]
        readmail(str(data[1][0][1]))
        counter = counter + 1

if __name__ == "__main__":
    gmail()
