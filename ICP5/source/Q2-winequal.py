import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

wine_df = pd.read_csv('./winequality-red.csv')
numeric_features  = wine_df.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print(corr['quality'].sort_values(ascending=False)[:3],'\n')

#delete null values
nulls = pd.DataFrame(wine_df.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)
print("\n")

##handling missing value
data = wine_df.select_dtypes(include=[np.number]).interpolate().dropna()
print("missing values: " + str(sum(data.isnull().sum() != 0))+ "\n")

##building model
y = np.log(wine_df.quality)
X = data.drop(['quality'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=0.4)
l_model = linear_model.LinearRegression()
model = l_model.fit(X_train, y_train)
print ("R2 score: ", model.score(X_test, y_test))


prdc = model.predict(X_test)
print ('RMSE score: ', mean_squared_error(y_test, prdc))