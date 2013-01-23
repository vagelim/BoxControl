import random
from gconf import * #For all of the globals and stuff
radfile = path + 'rads'
def Code():

    file = open(codefile, 'w')
    code = random.random()
    code = code * 100000000
    code = str(code)
    code = code[:6]
    file.write(code)
    file.close()
    
    return code

def deleteCode(delete=None):
    file = open(radfile, 'r')
    rads = file.read()
    rads = int(rads)
    if delete != None:
        if os.path.exists(codefile):
            os.remove(codefile)
            file = open(radfile,'w')
            rads = 0
            file.write(str(rads))
            file.close()
    elif rads == 0:
        file = open(radfile,'w')
        file.write(str(rads + 1))
        file.close()
    elif rads == 1:
        file = open(radfile,'w')
        file.write(str(rads + 1))
        file.close()
       
    elif rads == 2:
        if os.path.exists(codefile):
            os.remove(codefile)
            file = open(radfile,'w')
            rads = 0
            file.write(str(rads))
            file.close()
    