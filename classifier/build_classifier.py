import numpy as np
import cv2
from matplotlib import pyplot as plt

def index(req):
    # digits.png is an opencv image that contains 20x20 pixel handwritten digits
    img = cv2.imread('digits.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # split the image to 5000 cells, each 20x20 size
    cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

    # Make it into a Numpy array. Its size will be (50,100,20,20)
    x = np.array(cells)

    # Now we prepare train_data
    train = x.reshape(-1,400).astype(np.float32) # Size = (2500,400)

    # Create labels for train and test data
    k = np.arange(10)
    train_labels = np.repeat(k,500)[:,np.newaxis]

    # Initiate kNN, train the data, then test it with test data for k=1
    knn = cv2.KNearest()
    knn.train(train,train_labels)

    # Load image we are testing
    test_img = cv2.imread('test.png')
    grey = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    # Create numpy array
    nu_cells = [np.hsplit(row,20) for row in np.vsplit(grey, 20)]
    nu_grey = np.array(nu_cells)

    nu_test = nu_grey.reshape(-1, 400).astype(np.float32)

    # Use classifier 
    ret2, result2, neighbours2, dist2 = knn.find_nearest(nu_test,k=1)

    print result2[0][0]

    return 'OK'
