"""-----AI TRAINING-----"""
import tensorflow as tf         # Models
import sklearn as sk       # Other Models and Data Manipulation
import numpy as np              # Math and Calculations
import pandas as pd             # Data Science and Storage
import matplotlib.pyplot as plt # Data Visualization and Graphs
import kagglehub                # Also Data Imports
from xgboost import XGBClassifier   # XGBoost Model

"""DATA PROCESSING"""
dataset_path = kagglehub.dataset_download("farjanakabirsamanta/skin-cancer-dataset") # Get Data from Kaggle Database
print("Data set path: ", dataset_path)

df = pd.read_csv(dataset_path + "/HAM10000_metadata.csv")

# Remove Unnecessary Data
df = df.drop(df[df.sex == "unknown"].index)

# Label Data
label_encoder = sk.preprocessing.LabelEncoder()
df["localization"] = label_encoder.fit_transform(df["localization"])
df["sex"] = label_encoder.fit_transform(df["sex"])
df["dx"] = label_encoder.fit_transform(df["dx"])

# Split data
X = df[["age", "sex", "localization"]]
y = df["dx"]

X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(X, y)

"""MODEL TRAINING"""
# Training
xgb = XGBClassifier()
xgb.fit(X_train, y_train)

# Predicting
predictions = xgb.predict(X_test)

# Determine Model Accuracy
print("Model Accuracy: ", sk.metrics.accuracy_score(y_test, predictions))

"""-----USER INTERFACE-----"""
from tkinter import *
from tkinter import messagebox

# Create Window
root = Tk(className = "Skin Cancer Model")

# Title
title = Label(root, text="Skin Cancer Model")
title.grid(row=0, column=1)

# Patient Age
Label(root, text="Patient Age:").grid(row=1, column=0, sticky="w")
age = IntVar(value=1)
Spinbox(root, from_=1, to=100, textvariable=age).grid(row=1, column=1, sticky="w")

# Patient Sex
Label(root, text="Patient Sex:").grid(row=2, column=0, sticky="w")
sex = IntVar()
Radiobutton(root, text="Female", variable=sex, value=0).grid(row=2, column=1, sticky="w")
Radiobutton(root, text="Male", variable=sex, value=1).grid(row=2, column=2, sticky="w")

# Localization of Skin Lesion
Label(root, text="Localization:").grid(row=3, column=0, sticky="w")
localization = IntVar()
Radiobutton(root, text="Abdomen", variable=localization, value=0).grid(row=4, column=0, sticky="w")
Radiobutton(root, text="Acral", variable=localization, value=1).grid(row=4, column=1, sticky="w")
Radiobutton(root, text="Back", variable=localization, value=2).grid(row=4, column=2, sticky="w")
Radiobutton(root, text="Chest", variable=localization, value=3).grid(row=5, column=0, sticky="w")
Radiobutton(root, text="Ear", variable=localization, value=4).grid(row=5, column=1, sticky="w")
Radiobutton(root, text="Face", variable=localization, value=5).grid(row=5, column=2, sticky="w")
Radiobutton(root, text="Foot", variable=localization, value=6).grid(row=6, column=0, sticky="w")
Radiobutton(root, text="Genital", variable=localization, value=7).grid(row=6, column=1, sticky="w")
Radiobutton(root, text="Hand", variable=localization, value=8).grid(row=6, column=2, sticky="w")
Radiobutton(root, text="Lower Extremity", variable=localization, value=9).grid(row=7, column=0, sticky="w")
Radiobutton(root, text="Neck", variable=localization, value=10).grid(row=7, column=2, sticky="w")
Radiobutton(root, text="Scalp", variable=localization, value=11).grid(row=8, column=0, sticky="w")
Radiobutton(root, text="Trunk", variable=localization, value=12).grid(row=8, column=1, sticky="w")
Radiobutton(root, text="Unknown", variable=localization, value=13).grid(row=8, column=2, sticky="w")
Radiobutton(root, text="Upper Extremity", variable=localization, value=14).grid(row=7, column=1, sticky="w")

# Output Message
output = Message(root).grid(row=9, column=1, columnspan=2)

# ----RUN FUNCTION----
def run():
    test = pd.DataFrame({
        "age":  [age.get()],
        "sex":  [sex.get()],
        "localization": [localization.get()]
    })

    result = xgb.predict(test)

    output = "An error occurred"

    if (result[0] == 0):
        output = "Actinic keratoses and intraepithelial carcinoma / Bowen's disease"
    elif (result[0] == 1):
        output = "Basal cell carcinoma"
    elif (result[0] == 2):
        output = "Benign keratosis-like lesions"
    elif (result[0] == 3):
        output = "Dermatofibroma"
    elif (result[0] == 4):
        output = "Melanoma"
    elif (result[0] == 5):
        output = "Melanocytic nevi"
    elif (result[0] == 6):
        output = "Vascular lesions"

    messagebox.showinfo("Results", f"The model predicts that you most likely have: {output}")

# Submit Button
Button(root, text="Submit", command=run).grid(row=9, column=0)

root.mainloop()