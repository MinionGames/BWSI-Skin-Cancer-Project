from tkinter import *

# Create Window
root = Tk(className = "Skin Cancer Model")

# Title
title = Label(root, text="Skin Cancer Model")
title.grid(row=0, column=1)

# Patient Age
Label(root, text="Patient Age:").grid(row=1, column=0, sticky="w")
age = Entry(root).grid(row=1, column=1, sticky="w")

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

# ----Insert Run Function Here----
def run():
    print("Button Press")

# Submit Button
Button(root, text="Submit", command=run).grid(row=9, column=0)

root.mainloop()

