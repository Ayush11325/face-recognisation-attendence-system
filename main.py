from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import train
import os
from face_recognisation import face_Recognisation
from attendence import Attendence

class facerecognisation_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

# first image
        img=Image.open(r"college image\si.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=500,height=130)

#second image
        img1=Image.open(r"college image\sin.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=500,y=0,width=500,height=130)

#third image
        img2=Image.open(r"college image\si.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

#background image
        img3=Image.open(r"college image\bg.jpg")
        img3=img3.resize((1550,720),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

#attendence heading
        title_lbl=Label(bg_img,text="FACE RECOGNISATION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#student button

        img4=Image.open(r"college image\ii.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


# detect face button
        
        img5=Image.open(r"college image\ansh.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)      

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

#attendence button
        img6=Image.open(r"college image\attendence.webp")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimage6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimage6,cursor="hand2",command=self.attendence_btn)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_btn,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

#Help button
        img7=Image.open(r"college image\help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimage7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimage7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

#Train button
        img8=Image.open(r"college image\1.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimage8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Training Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

#Photos button
        img9=Image.open(r"college image\photo.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimage9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_image)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

 #Developer button  
        img10=Image.open(r"college image\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimage10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimage10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


#Exit button

        img11=Image.open(r"college image\exit.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimage11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimage11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

#open image

    def open_image(self):
        os.startfile("Data")
#student buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
#train button

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

#face_recognisation
  
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_Recognisation(self.new_window)

#attendence
     
    def attendence_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)



 

if __name__== "__main__":
    root=Tk()
    obj=facerecognisation_system(root)
    root.mainloop()
