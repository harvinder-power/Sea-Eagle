import os
import csv
import pandas as pd
from shutil import copyfile

labels_dir = './Data_Entry_2017.csv'

#determine the length of the dataset
labels_data = pd.read_csv(labels_dir)
print len(labels_data)

findings = labels_data['Finding Labels']
print (labels_data.iloc[2, 1].split('|')[0])

'''
classifications = []
for i in range(len(labels_data)):
    if labels_data.iloc[i,1].split('|')[0] in classifications:
        pass
    else:
        classifications.append(labels_data.iloc[i,1].split('|')[0])
print len(classifications), classifications
'''

seenSoFar = {}

for i in range(len(labels_data)):
    current_labels = labels_data.iloc[i,1].split('|')
    for j in range(len(current_labels)):
        if current_labels[j] in seenSoFar:
            seenSoFar[current_labels[j]] += 1
        else:
            seenSoFar[current_labels[j]] = 1

print seenSoFar



count = 0
for i in range(len(labels_data)):
    current_labels = labels_data.iloc[i,1].split('|')
    for j in range(len(current_labels)):
        if current_labels[j] == 'Infiltration' or current_labels[j] == 'Pneumonia':
            print current_labels[j]
            count += 1
            print 'Images copied = ', count
            #print labels_data.iloc[i, 0]
            source_loc = ('./images_copy/' + labels_data.iloc[i, 0])
            #print source_loc
            sink_loc = ('./images_copy/positive_result/' + labels_data.iloc[i, 0])
            if os.path.isfile(source_loc):
                copyfile(source_loc, sink_loc)
            else:
                pass

        elif current_labels[j] == 'No Finding':
            count += 1
            source_loc = ('./images_copy/' + labels_data.iloc[i, 0])
            sink_loc = ('./images_copy/negative_result/' + labels_data.iloc[i, 0])
            if os.path.isfile(source_loc):
                copyfile(source_loc, sink_loc)
            else:
                pass

print count
