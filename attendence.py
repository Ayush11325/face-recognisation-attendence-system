from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        #======================variables==========================

        self.var_attendid=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendence=StringVar()

# first image
        img = Image.open(r"college image\6.webp")
        img = img.resize((800,200), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # second image
        img1 = Image.open(r"college image\7.png")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=800, y=0, width=800, height=200)

                # background image
        img3 = Image.open(r"college image\8.webp")
        img3 = img3.resize((1550, 720), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimage3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        # attendence heading
        title_lbl = Label(
            bg_img,
            text="ATTENDENCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)
        #frame
        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=10, y=55, width=1500, height=660)

        # left label frame
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Attendence Details",
            font=("times new roman", 13, "bold"),
        )
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"college image\9.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimage_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

#inside frame 
        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)


        #labels and entry
        #attendence id
        attendenceid_label = Label(
            left_inside_frame,
            text="AttendenceID:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        attendenceid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendenceid_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_attendid,
            width=22,
            font=("times new roman", 13, "bold"),
        )
        attendenceid_entry.grid(row=0, column=1, padx=10, sticky=W)

    # Roll

        datelabel = Label(
            left_inside_frame,
            text="RollNo:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        datelabel.grid(row=0, column=2, padx=4,pady=8)

        roll_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_roll,
            width=22,
            font=("times new roman", 13, "bold"),
        )
        roll_entry.grid(row=0, column=3, pady=5)

        # Name

        datelabel = Label(
            left_inside_frame,
            text="StudentName:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        datelabel.grid(row=1, column=0)

        date_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_name,
            width=22,
            font=("times new roman", 13, "bold"),
        )
        date_entry.grid(row=1, column=1,)


            #Department

        datelabel = Label(
            left_inside_frame,
            text="Department:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        datelabel.grid(row=1, column=2)

        roll_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_dep,
            width=22,
            font=("times new roman", 13, "bold"),
        )
        roll_entry.grid(row=1, column=3, pady=8)

      #Time

        timelabel = Label(
            left_inside_frame,
            text="Time:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        timelabel.grid(row=2, column=0)

        time_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_time,
            width=22,
            font=("times new roman", 13, "bold"),
        )
        time_entry.grid(row=2, column=1, pady=8)


          #Date

        datelabel = Label(
            left_inside_frame,
            text="Date:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        datelabel.grid(row=2, column=2)

        date_entry = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_date,
            width=22,
            font=("times new roman", 13, "bold"),

        )
        date_entry.grid(row=2, column=3, pady=8)


         #Attendence

        datelabel = Label(
            left_inside_frame,
            text="Attendence Status:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        datelabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=23,textvariable=self.var_attendence,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # button frame

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35    )

        import_btn = Button(
            btn_frame,
            command=self.import_csv,
            text="Import csv",
          
            width=24,
            font=("times new roman", 13, "bold"),
            bg="green",
            fg="white",
        )
        import_btn.grid(row=0, column=0)

        export_btn = Button(
            btn_frame,
            command=self.export_csv,
            text="Export csv",
      
            width=24,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        export_btn.grid(row=0, column=1)

        # update_btn = Button(
        #     btn_frame,
        #     text="Update",
           
        #     width=17,
        #     font=("times new roman", 13, "bold"),
        #     bg="blue",
        #     fg="white",
        # )
        # update_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=24,
            font=("times new roman", 13, "bold"),
            bg="red",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)


    # right label frame
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Attendence Information",
            font=("times new roman", 13, "bold"),
        )
        right_frame.place(x=750, y=10, width=720, height=580)
        
        #frame
        table_frame=Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)


        #=======================scroll bar============================

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendencereporttable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendencereporttable.xview)
        
        scroll_y.config(command=self.attendencereporttable.yview)


        self.attendencereporttable.heading("id",text="AttendenceID")
        self.attendencereporttable.heading("roll",text="RollNo")
        self.attendencereporttable.heading("name",text="Name")
        self.attendencereporttable.heading("department",text="Department")
        self.attendencereporttable.heading("time",text="Time")
        self.attendencereporttable.heading("date",text="Date")
        self.attendencereporttable.heading("attendence",text="Attendence")

        self.attendencereporttable["show"]="headings"

        self.attendencereporttable.column("id",width=100)
        self.attendencereporttable.column("roll",width=100)
        self.attendencereporttable.column("name",width=100)
        self.attendencereporttable.column("department",width=100)
        self.attendencereporttable.column("time",width=100)
        self.attendencereporttable.column("date",width=100)
        self.attendencereporttable.column("attendence",width=100)


        self.attendencereporttable.pack(fill=BOTH,expand=1)
        self.attendencereporttable.bind("<ButtonRelease>",self.get_cursor) 
        
#===============fatch data=================
    def fatchdata(self,rows):
        self.attendencereporttable.delete(*self.attendencereporttable.get_children())
        for i in rows:
            self.attendencereporttable.insert("",END,values=i)

# import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fatchdata(mydata)

#export csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+ "successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)} ", parent=self.root)


        #get cursor

    def get_cursor(self,event=""):
        cursor_row=self.attendencereporttable.focus()
        content=self.attendencereporttable.item(cursor_row)
        rows=content["values"]
        self.var_attendid.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendence.set(rows[6])


    def reset_data(self):
        self.var_attendid.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendence.set("")




if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()