import os
import csv
import pandas as pd
from shutil import copyfile
from PIL import Image


labels_dir = '/Users/harvinderpower/images2/Data_Entry_2017.csv'

#determine the length of the dataset
labels_data = pd.read_csv(labels_dir)
#print len(labels_data)

findings = labels_data['Finding Labels']
#print (labels_data.iloc[2, 1].split('|')[0])

#gets a list of all the main classifications (n.b. main not all classifications)
classifications = []
for i in range(len(labels_data)):
    if labels_data.iloc[i,1].split('|')[0] in classifications:
        pass
    else:
        classifications.append(labels_data.iloc[i,1].split('|')[0])
print len(classifications), classifications


#seenSoFar creates a dictionary to determine the number of each classification present
seenSoFar = {}

for i in range(len(labels_data)):
    current_labels = labels_data.iloc[i,1].split('|')
    for j in range(len(current_labels)):
        if current_labels[j] in seenSoFar:
            seenSoFar[current_labels[j]] += 1
        else:
            seenSoFar[current_labels[j]] = 1

print seenSoFar
print classifications

#Check if the directory exists for each classification, if it doesn't, then make one.

for i in range(len(classifications)):
    print "/Users/harvinderpower/images2/" + classifications[i]
    if os.path.exists("/Users/harvinderpower/images2/" + classifications[i]) == False:
        os.mkdir("/Users/harvinderpower/images2/" + classifications[i])
    else:
        pass
############################

#Checks to see if the first mentioned classification is the same as the classifiction being iterated through in list (j), and if it is, moves the image to the corresponding folder
count = 0
for i in range(len(labels_data)):
    for j in range(len(classifications)):
        if labels_data.iloc[i,1].split('|')[0] == classifications[j]:
            print 'Images copied = ', count
            #print labels_data.iloc[i, 0]
            source_loc = ('/Users/harvinderpower/images2/' + labels_data.iloc[i, 0])
            #print source_loc
            sink_loc = ('/Users/harvinderpower/images2/' + classifications[j] + "/" + labels_data.iloc[i, 0])
            if os.path.isfile(source_loc):
                im = Image.open('/Users/harvinderpower/images2/' + labels_data.iloc[i, 0])
                im = im.convert('RGB')
                filename_with_new_extension = (labels_data.iloc[i, 0]).split('.')[0] + '.jpg'
                sink_loc = '/Users/harvinderpower/images2/convert_on_the_fly/' + classifications[j] + "/" + filename_with_new_extension
                copyfile(source_loc, sink_loc)
            else:
                pass

        else:
            pass

print count











'''
#Old moving script
count = 0
for i in range(len(labels_data)):
    current_labels = labels_data.iloc[i,1].split('|')
    for j in range(len(current_labels)):
        if current_labels[j] != 'No Finding':
            print current_labels[j]
            count += 1
            print 'Images copied = ', count
            #print labels_data.iloc[i, 0]
            source_loc = ('/Users/harvinderpower/Desktop/images2/' + labels_data.iloc[i, 0])
            #print source_loc
            sink_loc = ('/Users/harvinderpower/Desktop/images2/Pneumonia' + labels_data.iloc[i, 0])
            if os.path.isfile(source_loc):
                copyfile(source_loc, sink_loc)
            else:
                pass

        elif current_labels[j] == 'No Finding':
            count += 1
            source_loc = ('/Users/harvinderpower/Desktop/images2/' + labels_data.iloc[i, 0])
            sink_loc = ('/Users/harvinderpower/Desktop/images2/No Finding' + labels_data.iloc[i, 0])
            if os.path.isfile(source_loc):
                copyfile(source_loc, sink_loc)
            else:
                pass

print count
'''
