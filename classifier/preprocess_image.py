import numpy as np
import Image

# Standard size to normalize everything to the same shape
STANDARD_SIZE = (300, 167)
def img_to_matrix(filename, verbose=False):
    """ 
    Turns filename into numpy array of RGB pixels
    """
    img = Image.open(filename)
    if verbose==True:
        print "Changing size from %s to %s" % (str(img.size), str(STANDARD_SIZE))
    img = img.resize(STANDARD_SIZE)
    img = list(img.getdata())
    img = map(list, img)
    img = np.array(img)
    return img

def flatten_image(img):
    """ 
    Takes in (m,n) numpy array and flattens it into an array of shape (1, m*n)
    """
    s = img.shape[0] * img.shape[1]
    img_wide = img.reshape(1, s)
    return img_wide[0]

