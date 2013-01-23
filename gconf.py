import ConfigParser
import os

path = os.path.dirname(os.path.abspath(__file__)) + '/'

conf = path + 'gmail.conf'
codefile = path + "code"
def ReadConfig(key):
    if os.path.isfile(conf) != True:
        WriteConfig()
    config = ConfigParser.RawConfigParser()
    config.read(conf)
    section = "gmail"
    value = config.get(section, key)
    return value

 
def WriteConfig():
    user = raw_input("Username: ")
    print "YOUR PASSWORD WILL BE STORED AS PLAINTEXT\n"
    passwd = raw_input("Password: ")
    admin = raw_input("Admin Email: ")
    phone = raw_input("Phone Email: ")
    config = ConfigParser.RawConfigParser()
    config.add_section('gmail')
    config.set(section, "phone", phone)
    config.set(section, "admin", admin)
    config.set(section, "password", passwd)
    config.set(section, "user", user)
    config.write(open(conf, 'wb'))