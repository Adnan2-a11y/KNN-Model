import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_excel('Dataset_1_KNN.xlsx')
df['Draft']=df['Draft'].map({'yes':1,'no':0})

x=df[['Speed','Agility']].values
y=df['Draft'].values
#.\env\Scripts\activate.ps1
k=3
knn=KNeighborsClassifier(n_neighbors=k)
knn.fit(x,y)

speed=float(input("Enter the value of speed of to be predicted: "))
agility=float(input("Enter the value of agility of to be predicted: "))

new_student=np.array([speed,agility])
new_student=new_student.reshape(1,-1)
predicted_class=knn.predict(new_student)
print(f"Predicted class for the student with speed={speed} and agility={agility}:{'Selected' if predicted_class[0]==1 else 'Not selected'}")


