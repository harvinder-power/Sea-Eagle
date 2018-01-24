import os
import csv
import pandas as pd
from shutil import copyfile

labels_dir = '/Volumes/SAMSUNG/Kaggle/NIH Test Folder/images1/Data_Entry_2017.csv'

labels_data = pd.read_csv(labels_dir)
print len(labels_data)

findings = labels_data['Finding Labels']
print (labels_data.iloc[2, 1].split('|')[0])

'''
count = 0
for i in range(len(labels_data)):
    if findings[i] == 'Hernia':
        count += 1
        print 'Images copied = ', count
        print labels_data.iloc[i, 0]
        source_loc = ('/Volumes/SAMSUNG/Kaggle/NIH Test Folder/images1/images/' + labels_data.iloc[i, 0])
        print source_loc
        sink_loc = ('/Volumes/SAMSUNG/Kaggle/NIH Test Folder/images1/classified_images/hernia/' + labels_data.iloc[i, 0])
        copyfile(source_loc, sink_loc)
print count
'''

classifications = []
for i in range(len(labels_data)):
    if labels_data.iloc[i,1] in classifications:
        pass
    else:
        classifications.append(labels_data.iloc[i,1])
print classifications
