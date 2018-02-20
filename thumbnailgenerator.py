from PIL import Image
import glob, os

new_size = 128, 128
directory = '/Users/harvinderpower/images2/Resized/Keras Ready/TRAIN'
extension = '.png'
end_directory = '/Users/harvinderpower/images2/Resized/Keras Ready/Data PNG Versions'

'''
for i in os.listdir(directory):
    if i.endswith(extension):
        img = Image.open(directory + i)
        img = img.resize((new_size), Image.ANTIALIAS)
        img.save(directory + i)
'''

count = 0
for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(extension):
            count += 1
            img = Image.open(filepath)
            img = img.resize((new_size), Image.ANTIALIAS)
            bg = Image.new("RGB", img.size, (255,255,255))
            bg.paste(img, (0,0), img)
            bg.save(filepath + ".jpg", quality=95)
            print count
