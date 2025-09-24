import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


df = pd.read_csv('iris_clean.csv')


X = df.iloc[:, :-1] 
y = df.iloc[:, -1]


model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)


joblib.dump(model, 'model.pkl')

print("Model training complete. Saved to model.pkl")