from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
from cv2 import FaceDetectorYN
import os
import numpy as np


class face_Recognisation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        title_lbl = Label(
            self.root,
            text="FACE DETECTOR",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="green",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"college image\4.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimage_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"college image\6.webp")
        img_bottom = img_bottom.resize((950, 700), Image.ANTIALIAS)
        self.photoimage_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimage_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # button
        b1_1 = Button(
            f_lbl,
            command=self.face_reco,
            text="Face Recognisation",
            cursor="hand2",
            font=("times new roman", 16, "bold"),
            bg="red",
            fg="white",
        )
        b1_1.place(x=365, y=620, width=200, height=40)

    # ========================ATTENDENCE=========================

    def mark_attendence(self, i, r, n, d):
        with open("Ayush.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_List = []
            for line in myDataList:
                entry = line.split((","))
                name_List.append(entry[0])
                # dont repeat attendence
            if (
                (i not in name_List)
                and (r not in name_List)
                and (n not in name_List)
                and (d not in name_List)
            ):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},present")

    # face recognisation

    def face_reco(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                grey_image, scaleFactor, minNeighbours
            )

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(
                    img[y : y + h, x : x + w], (x, y), (x + w, y + h), (0, 255, 0), 3
                )
                id, predict = clf.predict(grey_image[y : y + h, x : x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Ayush11325@",
                    database="face",
                )
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where StudentID=" + str(id))
                n = my_cursor.fetchone()
                if n is not None:
                    # n = [n]  # Convert to a list
                    n = "+".join(n)

                my_cursor.execute(
                    "select RollNo from student where StudentID=" + str(id)
                )
                r = my_cursor.fetchone()
                if r is not None:
                    # r=[r]
                    r = "+".join(r)

                my_cursor.execute(
                    "select Department from student where StudentID=" + str(id)
                )
                d = my_cursor.fetchone()
                if d is not None:
                    # d=[d]
                    d = "+".join(d)

                my_cursor.execute(
                    "select StudentID from student where StudentID=" + str(id)
                )
                i = my_cursor.fetchone()
                if i is not None:   
                    # i=[i]
                    i = "+".join(i)

                if confidence >50:
                    cv2.putText(
                        img,
                        f"ID:{i}",
                        (x, y - 65),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Roll:{r}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Name:{n}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Department:{d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    self.mark_attendence(i, r, n, d)

                else:
                    cv2.rectangle(
                        img[y : y + h, x : x + w],
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        3,
                    )
                
                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )

                    coord = [x, y, w, h]
                return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(
                img,faceCascade, 1.1, 10, (255, 255, 255), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome TO Face Recognisation", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()

        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_Recognisation(root)
    root.mainloop()
