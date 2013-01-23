from gconf import path
import csv
def sendPassword(site):

    fileContents = csv.reader(open(path + "pass", 'rb'))
    for row in fileContents:
        if (str(row).find(site) != -1):
            return row

# if __name__ == "__main__":
    # sendPassword("43oh") #Test with sample website