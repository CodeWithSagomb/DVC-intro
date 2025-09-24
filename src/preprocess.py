import pandas as pd
import json


with open('iris.json', 'r') as f:
    data_json = json.load(f)

df = pd.DataFrame(data_json['data'], columns=data_json['columns'])


df['sepal length (cm)'] = df['sepal length (cm)'] * 2


df.to_csv('iris_clean.csv', index=False)

print("Data preprocessing complete. Saved to iris_clean.csv")