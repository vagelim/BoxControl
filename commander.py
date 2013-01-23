import ConfigParser
import os

path = os.path.dirname(os.path.abspath(__file__)) + '/'

def Commander(command):
	config = ConfigParser.RawConfigParser()
    config.read(path + "commands.txt")
    section = "commands"
    
    number = config.get(section, "number")
    counter = 0

    passwd = config.get(section, "password")
    email = config.get(section, "email")
    phone = config.get(section, "phone")
    return user,passwd,email,phone