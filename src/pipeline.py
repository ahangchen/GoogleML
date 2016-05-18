from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
# half data for testing (cross_validation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

# different classifiers for same task
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)
print predictions

# compare the predicted labels to the true labels
from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)

# use another classifier
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)
print predictions

# compare the predicted labels to the true labels
from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)
