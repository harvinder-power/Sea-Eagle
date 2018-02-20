from PIL import Image
import glob, os, sys

directory = "/Users/harvinderpower/images2/Folders/Images/TRAIN/Pneumothorax/"
new_directory = "/Users/harvinderpower/images2/Folders/Images/Data PNG/Pneumothorax/"
new_size = 128,128
extension = ".png"
new_extension = ".jpg"

if os.path.exists(new_directory) == False:
    os.mkdir(new_directory)
else:
    pass

count = 0
for i in os.listdir(directory):
    if i.endswith(extension):
        im = Image.open(directory + i)
        im = im.resize((new_size), Image.ANTIALIAS)
        im = im.convert('RGB')
        count += 1
        filename_with_new_extension = i.split('.')[0] + '.jpg'
        print new_directory + filename_with_new_extension
        im.save(new_directory + filename_with_new_extension)
        print count
