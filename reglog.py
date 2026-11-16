import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

dt = pd.read_csv("csv/train_clean.csv")

X = dt[["pclass","male", "age"]]
y = dt["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


lr = LogisticRegression(random_state=42)
lr.fit(X_train,y_train)

y_pred = lr.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision du modèle : {accuracy:.2%}")
