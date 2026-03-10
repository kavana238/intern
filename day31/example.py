from sklearn import tree

X = [[0, 0], [1, 1]]
Y = [0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict([[2., 2.]])
print("Prediction:", prediction)

prediction = clf.predict([[3, 3]])
print("Prediction:", prediction)

prediction = clf.predict([[0.5, 0.5]])
print("Prediction:", prediction)

prediction = clf.predict([[0,0], [1,1], [2,2], [3,1]])
print("Prediction:", prediction)