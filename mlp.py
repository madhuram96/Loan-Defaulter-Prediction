import pandas as pd

df = pd.read_csv("F:/Project/application_train.csv")
dum_df = pd.get_dummies(df)
dum_df1 = dum_df.drop('TARGET', axis=1)
df2=dum_df1.dropna(axis=1)
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

X = df2.iloc[:,0:186]
y = df.iloc[:,1]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.3, 
                                                    random_state=2018,
                                                    stratify=y)

mlp = MLPClassifier(hidden_layer_sizes=(3,3,2),activation='tanh',
                    random_state=2018)
mlp.fit( X_train , y_train )
y_pred = mlp.predict(X_test)
print(accuracy_score(y_test, y_pred))

from sklearn.model_selection import GridSearchCV
import numpy as np
parameters = {'n_neighbors': np.array([1,3,5,7,9])}
print(parameters)
knn = KNeighborsClassifier()
cv = GridSearchCV(knn, param_grid=parameters,
                  cv=5,scoring='roc_auc')
cv.fit( X , y )

print(cv.cv_results_  )

print(cv.best_params_)

print(cv.best_score_)

print(cv.best_estimator_)