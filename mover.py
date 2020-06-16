import csv
import sys

#input number you want to search
number = input('Search\n')

dataEntryFileLocation = "****"

#read csv, and split on "," the line
csv_file = csv.reader(open('****'), delimiter=",")


def moveFiles(filename, folder):
    #if file exists, then continue
    root = "****"
    filepath = root + filename
    if os.path.isfile(filepath) == True:
        
        # make folder if it doesn't exist
        if not os.path.exists(root+folder):
            os.makedirs(root+folder)
        
        #move to folder with 'number' as the folder name variable
        os.rename(filepath, root+folder+"/"+filename)
        print ("file moved successfully...")
        
    # else pass
    else:
        pass
        
#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[1]:
        print (row[0])
        moveFiles(row[0], number)
            

