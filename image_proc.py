from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread
from timeit import default_timer as timer

start = timer()
example_file = glob.glob("/Users/harvinderpower/interpret/cxr1.jpg")[0]
im = imread(example_file, as_grey=True)
plt.imshow(im, cmap='gray')

blobs_log = blob_log(im, min_sigma = 5, max_sigma=100, num_sigma=10, threshold=0.1)
#can also define a min_sigma to get a lower end for size determinate
blobs_log[:,2] = blobs_log[:,2]*sqrt(2)
numrows = len(blobs_log)
print "Number of blobs counted:", numrows

fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap='gray')
for blob in blobs_log:
    y, x, r= blob
    c = plt.Circle((x,y), r+5, color='lime', linewidth=0.5, fill=False)
    ax.add_patch(c)
end = timer()
print (end-start), "seconds elapsed"
plt.show()

##consider changing the system to use shades of white rather than blob based system
## also need to remove the edges - consider using ignore feature for high gradient bones and lung fields
