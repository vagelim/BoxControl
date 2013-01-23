#!/usr/bin/python
import time
import datetime
import gconf *

def getTimeFromArg(timeToGet):#Y:M:D:H:M:S
    index = timeToGet.find(":")
    year = timeToGet[:index]
    index = timeToGet.find(":")
    month = timeToGet[:index]
    index = timeToGet.find(":")
    day = timeToGet[:index]
    index = timeToGet.find(":")
    hour = timeToGet[:index]
    index = timeToGet.find(":")
    min = timeToGet[:index]
    index = timeToGet.find(":")
    sec = timeToGet[:index]
    
    return year,month,day,hour,min,sec
def todo(edate, message, priority=3):#Takes time due and has the todo message
#Default priority is lowest
    epochTime = time.mktime(edate.timeuple())
    file.open(path + 'todo', 'a')
    file.write(epochTime + ":" + message + ":", priority)
    file.close()
    

    
    
def checkTodo(priority=None):#check Todo list at each run, optionally for a specific priority
    import datetime
    currentTime = datetime.datetime.now()
    file = file.open(path + 'todo','r')
    todoFile = file.readlines()
    file.close()
    #Message based on priority level
    for each in todoFile
        if priority = None:
            return todoFile
        elif priority = 0:
            datetime.date(
        
    
