from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")

        # variables

        self.var_dep = StringVar()
        self.var_cource = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        # self.var_photo=StringVar()
        # self.var_radio1=StringVar()
        
        # first image
        img = Image.open(r"C:\college image\si.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"C:\college image\ii.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"C:\college image\si.jpg")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # background image
        img3 = Image.open(r"C:\college image\lnct1.jpeg")
        img3 = img3.resize((1550, 720), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimage3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # attendence heading
        title_lbl = Label(
            bg_img,
            text="STUDENT SECTION",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=660)

        # left label frame
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 13, "bold"),
        )
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\college image\aa.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimage_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # current course
        current_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Detail",
            font=("times new roman", 13, "bold"),
        )
        current_frame.place(x=5, y=135, width=720, height=150)

        # department
        dep_label = Label(
            current_frame,
            text="Department",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            current_frame,
            textvariable=self.var_dep,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        dep_combo["values"] = (
            "Select Department",
            "Computer",
            "IT",
            "Civil",
            "BCA",
            "MCA",
            "Btech",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # cource
        cource_label = Label(
            current_frame,
            text="Cource",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        cource_label.grid(row=0, column=2, padx=10, sticky=W)

        cource_combo = ttk.Combobox(
            current_frame,
            textvariable=self.var_cource,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        cource_combo["values"] = ("Select Cource", "Computer", "FE", "CA", "AIDA", "BE")
        cource_combo.current(0)
        cource_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year

        year_label = Label(
            current_frame, text="Year", font=("times new roman", 13, "bold"), bg="white"
        )
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(
            current_frame,
            textvariable=self.var_year,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        year_combo["values"] = (
            "Select Year",
            "2020-22",
            "2021-23",
            "2022-25",
            "2023-26",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester

        semester_label = Label(
            current_frame,
            text="Semester",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(
            current_frame,
            textvariable=self.var_sem,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=20,
        )
        semester_combo["values"] = (
            "Select Semester",
            "Semester-1",
            "Semester-2",
            "Semester-3",
            "Semester-4",
            "Semester-5",
            "Semester-6",
        )
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information
        class_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Class Student Information",
            font=("times new roman", 13, "bold"),
        )
        class_frame.place(x=5, y=250, width=720, height=300)

        # student id
        studentid_label = Label(
            class_frame,
            text="StudentID:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        studentid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentid_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_id,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        studentid_entry.grid(row=0, column=1, padx=10, sticky=W)
        # student name

        studentname_label = Label(
            class_frame,
            text="StudentName:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        studentname_label.grid(row=0, column=2, padx=10, sticky=W)

        studentname_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_name,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        classdiv_label = Label(
            class_frame,
            text="ClassDivision:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        classdiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # classdiv_entry=ttk.Entry(class_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        # classdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(
            class_frame,
            textvariable=self.var_div,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=18,
        )
        div_combo["values"] = ("SelectDivision", "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll number

        roll_label = Label(
            class_frame,
            text="RollNumber:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        roll_label.grid(row=1, column=2, padx=10, sticky=W)

        roll_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_roll,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender

        gender_label = Label(
            class_frame,
            text="Gender:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # gender_entry=ttk.Entry(class_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(
            class_frame,
            textvariable=self.var_gender,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=18,
        )
        gender_combo["values"] = ("SelectGender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB

        dob_label = Label(
            class_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white"
        )
        dob_label.grid(row=2, column=2, padx=10, sticky=W)

        dob_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email

        Email_label = Label(
            class_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white"
        )
        Email_label.grid(row=3, column=0, padx=10, sticky=W)

        Email_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # phone number

        phone_label = Label(
            class_frame,
            text="PhoneNumber:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        phone_label.grid(row=3, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address

        address_label = Label(
            class_frame,
            text="Address:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        address_label.grid(row=5, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        address_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Teacher name

        teacher_label = Label(
            class_frame,
            text="TeacherName:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        teacher_label.grid(row=5, column=2, padx=10, sticky=W)

        teacher_entry = ttk.Entry(
            class_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        teacher_entry.grid(row=5, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(
            class_frame, variable=self.var_radio1, text="Take photo sample", value="YES"
        )
        radio1.grid(row=6, column=0)

        radio2 = ttk.Radiobutton(
            class_frame, variable=self.var_radio1, text="No photo sample", value="NO"
        )
        radio2.grid(row=6, column=1)

        # button frame

        btn_frame = Frame(class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35    )

        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        # 2nd down button

        btn_frame1 = Frame(class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        takephoto_btn = Button(
            btn_frame1,
            command=self.generate_dataset,
            text="Take Photo Sample",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        takephoto_btn.grid(row=0, column=0)

        update_photo_btn = Button(
            btn_frame1,
            text="Update Photo Sample ",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_photo_btn.grid(row=0, column=1)

        # right label frame
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Information",
            font=("times new roman", 13, "bold"),
        )
        right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"C:\college image\pp.jpg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimage_right = ImageTk.PhotoImage(img_right)

        bg_img = Label(right_frame, image=self.photoimage_right)
        bg_img.place(x=5, y=0, width=720, height=130)

        # ======search system=========
        search_frame = LabelFrame(
            right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 13, "bold"),
        )
        search_frame.place(x=5, y=135, width=700, height=70)

        search_label = Label(
            search_frame,
            text="Search By:",
            font=("times new roman", 13, "bold"),
            bg="red",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=15,
        )
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=15, font=("times new roman", 13, "bold")
        )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(
            search_frame,
            text="Search",
            width=12,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(
            search_frame,
            text="Show All",
            width=12,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        showall_btn.grid(row=0, column=4, padx=4)

        # Table frame

        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "cource",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("cource", text="cource")
        self.student_table.heading("year", text="year")
        self.student_table.heading("sem", text="semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Div")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo_Sample")
        self.student_table["show"] = "headings"
        

        self.student_table.column("dep", width=100)
        self.student_table.column("cource", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fatch_data()
        

    # function decleration

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Ayush11325@",
                    database="face",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_cource.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        # self.var_photo.get(),
                        self.var_radio1.get()
                    )
                )

                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student Details has bend added Successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)} ", parent=self.root)

    # ==================fatch data===========================

    def fatch_data(self):

        conn = mysql.connector.connect(
            host="localhost", username="root", password="Ayush11325@", database="face"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
                conn.commit()

        conn.close()

    # =============get cursor================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_cource.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

        # update function

    def update_data(self):

        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ) :
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:

            try:
                Upadate=messagebox.askyesno("Update","Do you want to Update this student details",parent=self.root)
                if Upadate>0:

                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Ayush11325@",
                        database="face")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Department=%s,cource=%s,year=%s,semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where StudentID=%s",(
                                                                                                                                                            
                        self.var_dep.get(),
                        self.var_cource.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get(),
                        ))
                                                                                                                                                     

                else:
                    if not Upadate:
                        return

                messagebox.showinfo(
                    "Success",
                    "Student detail successfully Update Completed",
                    parent=self.root 
                )
                conn.commit()
                self.fatch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                


            #delete function

    def delete_data(self):

        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required ",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student ",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Ayush11325@",
                        database="face",
                    )
                    my_cursor = conn.cursor()
                    sql="delete from student where StudentID =%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fatch_data()
                conn.close()

                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
                    
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)

#=======================reset==========================
    def reset_data(self):
        
         self.var_dep.set("Select Department"),
         self.var_cource.set("Select Cource"),
         self.var_year.set("Select Year"),
         self.var_sem.set("Select Semester"),
         self.var_id.set(""),
         self.var_name.set(""),
         self.var_div.set("Select Division"),
         self.var_roll.set(""),
         self.var_gender.set("Select Gender"),
         self.var_dob.set(""),
         self.var_email.set(""),
         self.var_phone.set(""),
         self.var_address.set(""),
         self.var_teacher.set(""),
         self.var_radio1.set("")

#===============Generate Data set Or take a sample photo====================

    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
         ) :
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:

            try:
                 
                conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Ayush11325@",
                        database="face")
                my_cursor = conn.cursor()
                
        
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1

                my_cursor.execute(
                "update student set Department=%s,cource=%s,year=%s,semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where StudentID=%s",
                 (
                                                                                                                                    self.var_dep.get(),
                                                                                                                                    self.var_cource.get(),
                                                                                                                                    self.var_year.get(),
                                                                                                                                    self.var_sem.get(),
                                                                                                                                    self.var_name.get(),
                                                                                                                                    self.var_div.get(),
                                                                                                                                    self.var_roll.get(),
                                                                                                                                    self.var_gender.get(),
                                                                                                                                    self.var_dob.get(),
                                                                                                                                    self.var_email.get(),
                                                                                                                                    self.var_phone.get(),
                                                                                                                                    self.var_address.get(),
                                                                                                                                    self.var_teacher.get(),
                                                                                                                                    self.var_radio1.get(),
                                                                                                                                    self.var_id.get()==id+1
                                                                                                                                 )
                                                                                                                             ) 
                
                conn.commit()
                self.fatch_data()
                self.reset_data()
                conn.close()


# ==============================load predefine data on face frontal from opencv========================================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(grey,1.3,5)
                    #scalling factor=1.3 
                    #minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    # cropped_face = face_cropped(my_frame)

                    if face_cropped(my_frame) is not None:
                        img_id+=1

                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face) 
                        cv2.putText(face, str(img_id), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets Completed")

            
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)









if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
