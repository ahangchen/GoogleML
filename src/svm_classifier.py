import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import seaborn

from sgd_classifier import load_data

rng = np.random.RandomState(0)

X, y = load_data()
X = np.r_[X]
xx = np.linspace(-5, 5)

wclf = svm.SVC(kernel='linear', class_weight={1: 10})
wclf.fit(X, y)

ww = wclf.coef_[0]
wa = -ww[0] / ww[1]
wyy = wa * xx - wclf.intercept_[0] / ww[1]

h1 = plt.plot(xx, wyy, 'k--', label='with weights')
plt.scatter(X[:, 0], X[:, 1], c=[[yi, 0, 1-yi] for yi in y], cmap=plt.cm.Paired)
plt.legend()
plt.axis('tight')
plt.show()