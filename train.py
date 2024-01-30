from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")    

        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"C:\college image\2.webp")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimage_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # 2nd image

        img_bottom = Image.open(r"C:\college image\3.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimage_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimage_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

        # button
        b1_1 = Button(
            self.root,
            text="TRAIN DATA",
            command=self.train_classifier,
            cursor="hand2",
            font=("times new roman", 30, "bold"),
            bg="red",
            fg="white",
        )
        b1_1.place(x=0, y=380, width=1530, height=60)

    def train_classifier(self):
        data_dir=("Data")
        path = [
            os.path.join(data_dir, file) for file in os.listdir(data_dir)
        ]  # list comprehension 

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # gray scale image
            imageNp= np.array(img, "uint8")  # numpy use
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13  # enter dabate hi window close ho jai ga
        ids = np.array(ids)

        # Train the classifier and save

        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        # Create a Tkinter root window
        # root = Tk.tk()
        # root.withdraw()

        # Show the message box
        messagebox.showinfo("Result", "Training Dataset completed")


if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()
