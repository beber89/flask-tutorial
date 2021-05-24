import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle


df = pd.read_csv('model/homeprices.csv')
print(df.head())

model = linear_model.LinearRegression()
model.fit(df[['area']],df.price)

# now to save the model as serialized object pickle

with open('mysaved_md_pickle', 'wb') as file:
    pickle.dump(model,file)