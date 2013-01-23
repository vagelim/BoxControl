#!/usr/bin/python
import commands #To call system functions
import os
from pymail import mail #To send imap mail (over GMAIL in this case)
from gconf import ReadConfig #To read the configuration file
from gconf import path, codefile #The path variable (aka the current directory) and random file
#from gmail import gmail
import time
from code import Code, deleteCode#For SMS 2-Factor Authentication capabilities
from sendPassword import sendPassword
#from todo import todo, checkTodo
update_url = "http://freedns.afraid.org/dynamic/update.php?YOURHASHHERE"#Change this if you have a url to update a dynamic dns service. Try freedns.afraid.org
update = "lynx -dump " + update_url
admin = ReadConfig("admin") #Administrator email is the third element of the config array
number = ReadConfig("phone") #The phone number to txt is the fourth element of the config array


def getFileName(mailContents, command):#Basically finds words. But used mostly to find the second argument, the filename
    index = mailContents.find(command) + len(command) +1 # the +1 is for the whitespace after the command
    mailContents = mailContents[index:] #remove the change+whitespace out of mailContents
    if mailContents.find(' ') == -1: #this is necessary, otherwise it would remove the last letter of the filename
        return mailContents
    else:#The filename might not be the last argument
        word = mailContents.find(' ') #need to handle whitespace because there may be other arguments after the filename
        
    filename = mailContents[:word] #set the filename (also includes anything after second argument)
    return filename
    
def convertToSMS(subject, txtContents, chars=160):
    #import textwrap
    #Zero is a special case, meaning the message is less than 160 chars
    if (len(txtContents)/chars) >= 1:
        modulus = (len(txtContents)/chars) + 1 #+1 Because the index starts at zero
        counter = 0
        index   = 160 #The ending index of the message
        previous_index = 0
        while counter < modulus:
            mail(number, subject, txtContents[previous_index:index])
            previous_index = index
            index = (index*counter)
            counter += 1
        
    #mail(number, subject, textwrap.fill(txtContents, width=chars))
    
def readmail(mailContents=''):
    
    deleteCode()#Check the radfile and delete the SMS code if applicable
    
    mailContents = mailContents.rstrip('\r\n')
    #mailSearch = mailContents[:10] #This imposes a limit to 10 characters for commands
    mailSearch = mailContents.lower() #temporary replacement for above line
    
    if mailSearch.find('help') != -1:#Lists all commands (AUTOMATE THIS)
        newline = "\n"
        helpMsg = "!:Write To Journal" + "\n" \
            +"change" + newline \
            +"code" + newline \
            +"delete" + newline \
            +"help" + newline \
            +"journal" + newline \
            +"mail" + newline \
            +"pass" + newline \
            +"ping" + newline \
            +"update" + newline \
            +"send" + newline \
            +"ssh" + newline \
            +"syslog" + newline \
            +"webmin" + newline \
            +"run" + newline
        convertToSMS("Help",helpMsg)
        
    
    if mailSearch.find('pass') != -1:
        site = getFileName(mailContents, "pass")#Find website to look for
        mail(number, site, str(sendPassword(site)))
        
    if mailSearch.find('mail') != -1:
        filename = getFileName(mailContents, "mail")
        mail(admin, filename, "", filename)
        
    if mailSearch.find('send') != -1:
        filename = getFileName(mailContents, "send")
        mail(number, filename, str(commands.getoutput("cat " + filename)))
        
    #if mailSearch.find('!') != -1:#Save a journal (sort of like a personal twitter)
        #file = open(path + "journal", 'a')
        #file.write(time.asctime())
        #journalEntry = mailContents[76:mailContents.find("\n")
        #file.write(journalEntry)#76 is the "magic number" as of 01/26/2012
        #file.write("\n")
        #file.close()
    
    #if mailSearch.find('journal') != -1:
        #entries = getFileName(mailContents, 'journal') #Use this to find out how many entries to show
        #file = open(path + "journal", 'r')
        #if entries != '':
        #    journal = file.readlines()[(int(entries) * -1)]
        #else:
        #    entries = 1
        #file.close()
       # mail(number, "journal", journal)
    
    #update IP address in DNS
    if mailSearch.find('update') != -1:
        mail(number, "UPDATE", commands.getoutput(update))
    #PONG to show server is alive
    if mailSearch.find('ping') != -1:
        mail(number, "PING", "pong")
        print "PING"
    #Turn on SSH    
    if mailSearch.find('ssh on') != -1:
        commands.getoutput("/etc/init.d/ssh start")
        mail(number, "SSH", "ON")
    #Turn off SSH
    if mailSearch.find('ssh off') != -1:
        commands.getoutput("/etc/init.d/ssh stop")
        mail(number, "SSH", "OFF")
    
    #Run an arbitrary command EXTREMELY DANGEROUS
    if mailSearch.find('run') != -1:
        index = mailContents.find('run') + 3 #moves the index over 'u','n',' ' to beginning of command
        output = commands.getoutput(mailContents[index:])
        mail(number, "RUN", output)
     
    #Mail Syslog to the ADMIN EMAIL 
    if mailSearch.find('syslog') != -1:
        mail(admin, "SYSLOG", "", "/var/log/syslog")
     
    #Turn on Webmin
    if mailSearch.find('webmin on') != -1:
        output = commands.getoutput("/etc/init.d/webmin start")
        mail(number, "WEBMIN", "ON")
    #Turn off Webmin
    if mailSearch.find('webmin off') != -1:
        output = commands.getoutput("/etc/init.d/webmin stop")
        mail(number, "WEBMIN", str(output))
     
    #Change the contents of a given filename
    if mailSearch.find('change') != -1:
        filename = getFileName(mailContents, "change")
        file = open(filename, 'w')
        index = mailContents.find(filename) + len(filename) + 1 #strip filename and space from contents
        file.write(mailContents[index:])
    #Append a file with the given contents    
    if mailSearch.find('append') != -1:
        filename = getFileName(mailContents, "append")
        file = open(filename, 'a')
        index = mailContents.find(filename) + len(filename) + 1 #strip filename and space from contents
        file.write(mailContents[index:])
     
    if mailSearch.find('code') != -1:
        code = Code()
        mail(number, 'CODE', code)
        #insert code here to start a daemon
           
    if mailSearch.find('delete') != -1:
        deleteCode("delete")
        gmail("delete")
        
        
    #print mailContents
    #print commands.getoutput(mailContents)
