import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
   
arr = np.array([1, 2, 3, 4]) 
print("mean of arr :",np.mean(arr))       
print("std dev of arr :",np.std(arr))     

data = {
    "Name": ["Irfan", "Rahul", "Aman"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print("Avg mark =",df["Marks"].mean())
 
"""data = pd.read_csv("data.csv") 
print(data.head())        
print(data.describe())"""
 
plt.plot([1,2,3], [4,5,6]) 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
plt.show()
 
X = np.array([[1], [2], [3], [4]]) 
y = np.array([2, 4, 6, 8]) 
model = LinearRegression() 
model.fit(X, y) 
print(model.predict([[5]]))   
