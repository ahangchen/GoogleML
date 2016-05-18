import numpy as np
import pydot

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO

iris = load_iris()
# metadata tells you the names of the features and labels
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]
for i in range(len(iris.target)):
    print('Example %d: label %s, features %s' % (i, iris.target[i], iris.data[i]))
test_idx = [0, 50, 100]

# training data
# delete a records for each flower from 150 records
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
#
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# train
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# test
print test_target
print clf.predict(test_data)

# visual code


dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris_decision_tree.pdf")
