from sklearn.decomposition import RandomizedPCA
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from PIL import Image
import os
import numpy as np

files = ["./numbers/" + f for f in os.listdir("./numbers")]

STANDARD_SIZE = (50, 50)
def get_image_data(filename):
    img = Image.open(filename)
    img = img.getdata()
    img = img.resize(STANDARD_SIZE)
    img = map(list, img)
    img = np.array(img)
    s = img.shape[0] * img.shape[1]
    img_wide = img.reshape(1, s)
    return img_wide[0]

data = []
labels = []
print "extracting features..."
for f in files:
    data.append(get_image_data(f))
    labels.append(int(f.split(".")[0][-1]))
print "done."

pca = RandomizedPCA(n_components=10)
std_scalar = StandardScaler()

X_train, X_text, y_train, y_test = train_test_split(data, labels, test_size=0.1)

X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

X_train = std_scaler.fit_transform(X_train)
X_test = std_scaler.transform(X_test)

clf = KNeighborsClassifier(n_neighbors=13)
clf.fit(X_train, y_train)
print "done"
print "="*20
print clf

print "Confusion Matrix"
print "="*40
print confusion_matrix(y_test, clf.predict(X_test))


# Predict

