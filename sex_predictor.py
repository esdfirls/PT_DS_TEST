import pandas as pd
import sys
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB

filename = sys.argv[1]
data_test = pd.read_csv(filename)

data = pd.read_csv('test_data_CANDIDATE.csv')
data['sex'] = data['sex'].replace({'m': 'M', 'f': 'F'})
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data.drop(['slope', 'cp', 'index'], axis=1, inplace=True)
data_test.drop(['slope', 'cp', 'index'], axis=1, inplace=True)
data.drop(data[data['chol'] > 500].index, inplace=True)
data['chol'] = data['chol'].fillna(data['chol'].mean())
data.drop(data[data['trestbps'] > 180].index, inplace=True)
data.drop(data[data['oldpeak'] > 4].index, inplace=True)

X = data.drop('sex', axis=1)
y = data['sex']

SS = StandardScaler()
X = SS.fit_transform(X)

model = GaussianNB()
model.fit(X, y)
data_test = SS.fit_transform(data_test)

predict = model.predict(data_test)
newdata = pd.DataFrame(predict)
newdata.columns = ['sex']
newdata.to_csv('newsample_PREDICTIONS_{ALAN_HENGSTMANN_SILVA}.csv', index=False)

print("Script OK, The new data is in your directory")
