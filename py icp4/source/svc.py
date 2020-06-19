import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

train_df = pd.read_csv('./train_preprocessed.csv')
test_df = pd.read_csv('./test_preprocessed.csv')
X_train = train_df.drop("Survived",axis=1)
Y_train = train_df["Survived"]
X_test = test_df.drop("PassengerId",axis=1).copy()
score = accuracy_score(Y_test,y_pred)*100
svc = SVC()
svc.fit(X_train,Y_train)
y_pred1 = svc.predict(X_test)
y_pred1

acc_svc = accuracy_score(Y_test, y_pred1) * 100

print("score: " + str(acc_svc))
print(classification_report(Y_test, y_pred1))