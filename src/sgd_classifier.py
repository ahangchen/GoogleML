from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score


def load_data():
    train_x = []
    train_y = []
    file_in = open('../data/testSet.txt')
    for line in file_in.readlines():
        line_info = line.strip().split()
        train_x.append([float(line_info[0]), float(line_info[1])])
        train_y.append(float(line_info[2]))
    return train_x, train_y

X, y = load_data()
clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(X[: 90], y[: 90])
SGDClassifier(alpha=0.0001, average=False, class_weight=None, epsilon=0.1,
              eta0=0.0, fit_intercept=True, l1_ratio=0.15,
              learning_rate='optimal', loss='hinge', n_iter=5, n_jobs=1,
              penalty='l2', power_t=0.5, random_state=None, shuffle=True,
              verbose=0, warm_start=False)
predictions = clf.predict(X[90:])

print accuracy_score(y[90:], predictions)

