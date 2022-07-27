from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from datetime import datetime

class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Social Media user database")
        self.root.geometry("1538x790+0+0")
        self.root.resizable(False, False)
        self.loginform()
        # self.email_txt = 'diyas@gmail.com'
        # self.appscreen()
        self.user_id = ""
        self.pid = 0

    def loginform(self):
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, height=790, width=1538)
        self.img = ImageTk.PhotoImage(file="images.jfif")
        img = Label(Frame_login, image=self.img).place(x=0, y=0, width=1538, height=790)
        frame_input = Frame(self.root, bg='white')
        frame_input.place(x=570, y=130, height=450, width=350)
        label1 = Label(frame_input, text="Login Here", font=('impact', 32, 'bold'),fg="black", bg='white')
        label1.place(x=75, y=20)
        label2 = Label(frame_input, text="Email", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label2.place(x=30, y=95)
        self.email_txt = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.email_txt.place(x=30, y=145, width=270, height=35)
        label3 = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label3.place(x=30, y=195)
        self.password = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)
        btn1 = Button(frame_input, command=self.forgetPasswordScreen, text="forgot password?", cursor='hand2', font=('calibri', 10), bg='white', fg='black', bd=0)
        btn1.place(x=125, y=305)
        btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2", font=("times new roman", 15),
                      fg="white", bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=90, y=340)
        btn3 = Button(frame_input, command=self.Register, text="Not Registered?register", cursor="hand2",
                      font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=110, y=390)

    def login(self):
        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                      database='miniproject')
                cur = con.cursor()
                cur.execute('select * from users where email_id=%s and password=%s'
                            , (self.email_txt.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Username And Password'
                                         , parent=self.root)
                    self.loginclear()
                    self.email_txt.focus()
                else:
                    self.appscreen()
                    con.close()

            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                     , parent=self.root)

    def Register(self):
        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=0, y=0, height=780, width=1586)
        self.img = ImageTk.PhotoImage(file="images.jfif")
        img = Label(Frame_login1, image=self.img).place(x=0, y=0, width=1586, height=780)
        frame_input2 = Frame(self.root, bg='white')
        frame_input2.place(x=500, y=100, height=600, width=680)
        label1 = Label(frame_input2, text="Register Here", font=('impact', 32, 'bold'), fg="black", bg='white')
        label1.place(x=185, y=20)
        label2 = Label(frame_input2, text="Username", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label2.place(x=30, y=95)
        self.entry = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry.place(x=30, y=145, width=270, height=35)
        label3 = Label(frame_input2, text="Last Name", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label3.place(x=320, y=95)
        self.entry2 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry2.place(x=320, y=145, width=270, height=35)
        label4 = Label(frame_input2, text="Email Id", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label4.place(x=30, y=195)
        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry3.place(x=30, y=245, width=270, height=35)
        label5 = Label(frame_input2, text="Phone Number", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label5.place(x=320, y=195)
        self.entry4 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry4.place(x=320, y=245, width=270, height=35)
        label6 = Label(frame_input2, text="City", font=("Goudy old style", 20, "bold"), fg='orangered',
                       bg='white')
        label6.place(x=30, y=295)
        self.entry5 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry5.place(x=30, y=345, width=270, height=35)
        label7 = Label(frame_input2, text="Date of birth (YYYY-MM-DD)", font=("Goudy old style", 20, "bold"), fg='orangered',
                       bg='white')
        label7.place(x=320, y=295)
        self.entry6 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry6.place(x=320, y=345, width=270, height=35)
        label8 = Label(frame_input2, text="Gender (M/F)", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label8.place(x=30, y=395)
        self.entry7 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry7.place(x=30, y=445, width=270, height=35)
        label9 = Label(frame_input2, text="Password", font=("Goudy old style", 20, "bold"), fg='orangered',
                       bg='white')
        label9.place(x=320, y=395)
        self.entry8 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry8.place(x=320, y=445, width=270, height=35)
        btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2",
                      font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=225, y=520)
        btn3 = Button(frame_input2, command=self.loginform, text="Already Registered?Login", cursor="hand2",
                      font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=245, y=570)

    def register(self):
        if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "" \
                or self.entry6.get() == "" or self.entry8.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Deepa@93258", database="miniproject")
                cur = con.cursor()
                cur.execute("select * from users where email_id=%s", self.entry3.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already Exist,Please try with another Email", parent=self.root)
                    self.regclear()
                    self.entry.focus()
                else:
                    cur.execute("insert into users(email_id, phone_no, password, firstName, lastName, city, dob, gender)"
                                " values(%s, %s, %s, %s, %s, %s, %s, %s)", (self.entry3.get(), self.entry4.get(),
                                                                                             self.entry8.get(), self.entry.get(),
                                                                                             self.entry2.get(), self.entry5.get(),
                                                                                             self.entry6.get(), self.entry7.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Succesfull", parent=self.root)
                    self.regclear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def forgetPasswordScreen(self):
        Frame_login2 = Frame(self.root, bg="white")
        Frame_login2.place(x=0, y=0, height=780, width=1586)
        self.img = ImageTk.PhotoImage(file="images.jfif")
        img = Label(Frame_login2, image=self.img).place(x=0, y=0, width=1586, height=780)
        frame_input3 = Frame(self.root, bg='white')
        frame_input3.place(x=570, y=130, height=450, width=450)
        label1 = Label(frame_input3, text="Forgot Password", font=('impact', 32, 'bold'), fg="black", bg='white')
        label1.place(x=75, y=20)
        label2 = Label(frame_input3, text="Email", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label2.place(x=30, y=95)
        self.email_txt1 = Entry(frame_input3, font=("times new roman", 15, "bold"), bg='lightgray')
        self.email_txt1.place(x=30, y=145, width=270, height=35)
        label3 = Label(frame_input3, text="Enter new Password", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label3.place(x=30, y=195)
        self.password1 = Entry(frame_input3, font=("times new roman", 15, "bold"), bg='lightgray')
        self.password1.place(x=30, y=245, width=270, height=35)
        btn2 = Button(frame_input3, text="Forgot Password", command=self.forgotPassword, cursor="hand2", font=("times new roman", 15),
                      fg="white", bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=90, y=340)
        btn3 = Button(frame_input3, command=self.loginform, text="Remembered Password?Login", cursor="hand2",
                      font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=110, y=390)

    def forgotPassword(self):
        if self.email_txt1.get() == "" or self.password1.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                      database='miniproject')
                cur = con.cursor()
                cur.execute('select * from users where email_id=%s'
                            , (self.email_txt1.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Email id'
                                         , parent=self.root)
                    self.forgotclear()
                    self.email_txt1.focus()
                else:
                    cur.execute('update users set password = %s where email_id = %s', (self.password1.get(),
                                                                                       self.email_txt1.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Change of Password Succesfull", parent=self.root)
                    self.forgotclear()

            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                     , parent=self.root)

    def appscreen(self):
        Frame_login3 = Frame(self.root, bg="white")
        Frame_login3.place(x=0, y=0, height=780, width=1586)

        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                  database='miniproject')
            cur = con.cursor()
            cur.execute('select firstName from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            c = "Hi! Welcome " + b[0].title() + " to Social Media User Database"
            label1 = Label(Frame_login3, text=c, font=('times new roman', 32, 'bold'),
                           fg="black", bg='white')
            label1.place(x=375, y=100)
            label2 = Label(Frame_login3, text="Number of followings", font=('times new roman', 14),
                           fg="black", bg='white')
            label2.place(x=235, y=160)

            cur.execute('select numberOfFollowing(%s)', (self.email_txt.get()))
            a = cur.fetchone()
            label3 = Label(Frame_login3, text=a,
                               font=('times new roman', 14),
                               fg="black", bg='white')
            label3.place(x=540, y=160)
            label4 = Label(Frame_login3, text="Number of Posts", font=('times new roman', 14),
                           fg="black", bg='white')
            label4.place(x=235, y=190)

            cur.execute('select numberOfPosts(%s)', (self.email_txt.get()))
            a = cur.fetchone()
            label5 = Label(Frame_login3, text=a,
                           font=('times new roman', 14),
                           fg="black", bg='white')
            label5.place(x=540, y=190)


        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                 , parent=self.root)


        btn2 = Button(Frame_login3, text="Logout", command=self.loginform, cursor="hand2", font=("times new roman",
                                                                                                15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=1300, y=10)
        btn3 = Button(Frame_login3, text="My data", command=self.mydataPage, cursor="hand2", font=("times new roman",
                                                                                                15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn3.place(x=660, y=290)
        btn4 = Button(Frame_login3, text="My Posts", command=self.myPost,cursor="hand2", font=("times new roman",
                                                                                 15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn4.place(x=660, y=340)
        btn5 = Button(Frame_login3, text="Create Posts", command=self.post_content ,cursor="hand2", font=("times new roman",
                                                                          15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn5.place(x=660, y=390)
        btn5 = Button(Frame_login3, text="View Users", command=self.followusers, cursor="hand2",
                      font=("times new roman",
                            15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn5.place(x=660, y=440)
        btn6 = Button(Frame_login3, text="View Following", command=self.viewFollowing, cursor="hand2",
                      font=("times new roman",
                            15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn6.place(x=660, y=490)
        btn7 = Button(Frame_login3, text="Post comments", command=self.ViewPost, cursor="hand2",
                      font=("times new roman",
                            15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn7.place(x=660, y=540)

    def mydataPage(self):
        Frame_login4 = Frame(self.root, bg="white")
        Frame_login4.place(x=0, y=0, height=780, width=1586)
        self.img = ImageTk.PhotoImage(file="images.jfif")
        img = Label(Frame_login4, image=self.img).place(x=0, y=0, width=1586, height=780)
        frame_input4 = Frame(self.root, bg='white')
        frame_input4.place(x=320, y=30, height=700, width=1000)
        label1 = Label(frame_input4, text="My Data", font=('impact', 32, 'bold'), fg="black", bg='white')
        label1.place(x=150, y=20)
        label2 = Label(frame_input4, text="Name: -", font=(25), fg="black", bg='white')
        label2.place(x=80, y=100)
        label3 = Label(frame_input4, text="Email Id: -", font=(25), fg="black", bg='white')
        label3.place(x=80, y=140)
        label4 = Label(frame_input4, text="Phone number: -", font=(25), fg="black", bg='white')
        label4.place(x=80, y=180)
        label5 = Label(frame_input4, text="City: -", font=(25), fg="black", bg='white')
        label5.place(x=80, y=220)
        label6 = Label(frame_input4, text="Date of birth: -", font=(25), fg="black", bg='white')
        label6.place(x=80, y=260)
        label7 = Label(frame_input4, text="Gender: -", font=(25), fg="black", bg='white')
        label7.place(x=80, y=300)
        label8 = Label(frame_input4, text="Age: -", font=(25), fg="black", bg='white')
        label8.place(x=80, y=340)
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                  database='miniproject')
            cur = con.cursor()
            cur.execute('select firstName from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            cur.execute('select lastName from users where email_id=%s', (self.email_txt.get()))
            c = cur.fetchone()
            self.name = b[0].title() + " " + c[0].title()
            label21 = Label(frame_input4, text=self.name, font=(25), fg="black", bg='white')
            label21.place(x=155, y=100)
            label31 = Label(frame_input4, text=self.email_txt.get(), font=(25), fg="black", bg='white')
            label31.place(x=175, y=140)
            cur.execute('select phone_no from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            self.phone_no = b[0]
            label41 = Label(frame_input4, text=self.phone_no, font=(25), fg="black", bg='white')
            label41.place(x=230, y=180)
            btn3 = Button(frame_input4, command=lambda * args: self.editProfilePage('phone_no'), text="Edit Phone no.", cursor="hand2",
                          font=("calibri", 14), bg='orangered', fg="black", bd=0)
            btn3.place(x=450, y=180)
            cur.execute('select city from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            self.city = b[0]
            label5 = Label(frame_input4, text=self.city, font=(25), fg="black", bg='white')
            label5.place(x=140, y=220)
            btn4 = Button(frame_input4, command=lambda * args: self.editProfilePage('city'), text="Edit City", cursor="hand2",
                          font=("calibri", 14), bg='orangered', fg="black", bd=0)
            btn4.place(x=450, y=220)
            cur.execute('select dob from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            self.dob = b[0]
            label61 = Label(frame_input4, text=self.dob, font=(25), fg="black", bg='white')
            label61.place(x=200, y=260)
            btn5 = Button(frame_input4, command=lambda * args: self.editProfilePage('dob'), text="Edit Date of birth", cursor="hand2",
                          font=("calibri", 14), bg='orangered', fg="black", bd=0)
            btn5.place(x=450, y=260)
            cur.execute('select gender from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            self.gender = b[0]
            label71 = Label(frame_input4, text=self.gender, font=(25), fg="black", bg='white')
            label71.place(x=180, y=300)
            cur.execute('select age from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            self.age = b[0]
            label81 = Label(frame_input4, text=self.age, font=(25), fg="black", bg='white')
            label81.place(x=150, y=340)
            btn1 = Button(frame_input4, command=self.appscreen, text="Back", cursor="hand2",
                          font=("calibri", 14), bg='white', fg="black", bd=0)
            btn1.place(x=180, y=390)


        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                 , parent=self.root)

    def myPost(self):
        Frame_login5 = Frame(self.root, bg="white")
        Frame_login5.place(x=0, y=0, height=780, width=1586)
        # self.img = ImageTk.PhotoImage(file="images.jfif")
        # img = Label(Frame_login5, image=self.img).place(x=0, y=0, width=1586, height=780)
        frame_input5 = Frame(self.root, bg='white')
        frame_input5.place(x=570, y=130, height=750, width=1000)
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                  database='miniproject')
            cur = con.cursor()
            cur.execute('select user_id from users where email_id = %s',self.email_txt.get())
            self.user_id = cur.fetchone()
            cur.execute('select post_date, post_content from posts where posted_user_id = %s', (self.user_id))
            b = cur.fetchall()
            label1 = Label(frame_input5, text="My Posts", font=('impact', 32, 'bold'), fg="black", bg='white')
            label1.place(x=150, y=20)
            i = 0
            for post in b:
                for j in range(len(post)):
                    e = Label(frame_input5, font=15, text=post[j])
                    a = 80+j*150
                    b = 100+i*50
                    e.place(x = a, y = b)
                i=i+1

            btn1 = Button(frame_input5, command=self.appscreen, text="Back", cursor="hand2",
                          font=("calibri", 14), bg='white', fg="black", bd=0)
            btn1.place(x=180, y=390)
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                 , parent=self.root)

    def post_content(self):
        post_content = Frame(self.root, bg="white")
        post_content.place(x=0, y=0, height=780, width=1586)
        label3 = Label(post_content, text="Enter Content", font=("Goudy old style", 15, "bold"), fg='orangered',
                       bg='white')
        label3.place(x=300, y=100)
        self.content = Entry(post_content, font=("times new roman", 15, "bold"), bg='lightgray')
        self.content.place(x=500, y=100, width=500)
        post1 = Button(post_content, command=self.succpost, text="Post", cursor="hand2", font=("times new roman", 15),
                       fg="Black", bg="orangered", bd=0, width=15, height=1)
        post1.place(x=1050, y=90)
        btn1 = Button(post_content, command=self.appscreen, text="Back", cursor="hand2",
                      font=("calibri", 14), bg='white', fg="black", bd=0)
        btn1.place(x=750, y=390)

    def succpost(self):
        if self.content.get() == "":
            messagebox.showerror("Error", "Enter some content", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                      database='miniproject')
                cur = con.cursor()
                cur.execute('select user_id from users where email_id=%s',(self.email_txt.get()))
                b = cur.fetchone()
                self.user_id = b[0]
                a = str(datetime.today()).split()[0]
                cur.execute('insert into posts(posted_user_id, post_date, post_content) values(%s, %s, %s)', (self.user_id, a, self.content.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Successful", "Content posted Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                     , parent=self.root)

        self.content.delete(0, END)

    def followusers(self):
        Frame_login6 = Frame(self.root, bg="white")
        Frame_login6.place(x=0, y=0, height=780, width=1586)
        frame_input6 = Frame(self.root, bg='white')
        frame_input6.place(x=570, y=130, height=750, width=600)
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                  database='miniproject')
            cur = con.cursor()
            tt = 'select firstName, lastName, users.user_id from users where user_id not in (select friend_id from ' \
                 'follow, users where follow.user_id = users.user_id and email_id = "%s") and email_id != ' \
                 '"%s"'%(self.email_txt.get(), self.email_txt.get())
            cur.execute(tt)
            b = cur.fetchall()

            label1 = Label(frame_input6, text="Users", font=('impact', 32, 'bold'), fg="black", bg='white')
            label1.place(x=150, y=20)
            i = 0
            f = 0
            for post in b:
                e = Label(frame_input6, font=15, text=str(post[2]) + " " + post[0].title() + " " + post[1].title(), bg='white')
                # a = 80+j*150
                f = 100 + i * 50
                e.place(x=80, y=f)
                i = i + 1
            e1 = Label(frame_input6, font=15, text='Enter the user id of user you want to follow: -')
            e1.place(x = 0, y = f+60)
            self.ui = Entry(frame_input6, font=("times new roman", 15, "bold"), bg='lightgray')
            self.ui.place(x=100, y=f+120, width=100)
            btn2 = Button(frame_input6, command=lambda *args: self.follow(self.ui.get()), text="Follow", cursor="hand2",
                          font=("calibri", 14), bg='orangered', fg="black", bd=0)
            btn2.place(x=260, y=f+120)
            btn1 = Button(frame_input6, command=self.appscreen, text="Back", cursor="hand2",
                          font=("calibri", 14), bg='white', fg="black", bd=0)
            btn1.place(x=170, y=550)
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                 , parent=self.root)

    def follow(self, f):
        self.f = f
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258', database='miniproject')
            cur = con.cursor()
            cur.execute('select user_id from users where email_id=%s', (self.email_txt.get()))
            b = cur.fetchone()
            self.user_id = b[0]
            a = str(datetime.today()).split()[0]
            cur.execute('insert into follow(user_id,friend_id) values(%s, %s)', (self.user_id, self.f))
            con.commit()
            con.close()
            messagebox.showinfo("Successful", "Followed Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}', parent=self.root)
        self.ui.delete(0, END)
    def editProfilePage(self, value):
        post_content = Frame(self.root, bg="white")
        post_content.place(x=0, y=0, height=780, width=1586)
        label3 = Label(post_content, text="Enter New Value", font=("Goudy old style", 15, "bold"), fg='orangered',
                       bg='white')
        label3.place(x=300, y=100)
        self.new_value = Entry(post_content, font=("times new roman", 15, "bold"), bg='lightgray')
        self.new_value.place(x=500, y=100, width=500)
        post1 = Button(post_content,command=lambda * args: self.editProfile(value), text="Submit", cursor="hand2", font=("times new roman", 15),
                       fg="Black", bg="orangered", bd=0, width=15, height=1)
        post1.place(x=1050, y=90)
        btn1 = Button(post_content, command=self.mydataPage, text="Back", cursor="hand2",
                      font=("calibri", 14), bg='white', fg="black", bd=0)
        btn1.place(x=750, y=390)

    def editProfile(self, value):
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                  database='miniproject')
            cur = con.cursor()
            txt = 'update users set  %s = "%s" where users.email_id = "%s"'%(value, self.new_value.get(), self.email_txt.get())
            cur.execute(txt)
            con.commit()
            con.close()
            messagebox.showinfo("Successful", "Edited Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                 , parent=self.root)
        self.new_value.delete(0, END)

    def viewFollowing(self):
        Frame_login7 = Frame(self.root, bg="white")
        Frame_login7.place(x=0, y=0, height=780, width=1586)
        frame_input7 = Frame(self.root, bg='white')
        frame_input7.place(x=570, y=130, height=750, width=600)
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                  database='miniproject')
            cur = con.cursor()
            tt = 'select firstName, lastName, users.user_id from users where user_id in (select friend_id from ' \
                 'follow, users where follow.user_id = users.user_id and email_id = "%s") and email_id != ' \
                 '"%s"' % (self.email_txt.get(), self.email_txt.get())
            cur.execute(tt)
            b = cur.fetchall()

            # b = set(b)
            # b = list(b)
            label1 = Label(frame_input7, text="You are following to ", font=('impact', 32, 'bold'), fg="black", bg='white')
            label1.place(x=150, y=20)
            i = 0
            f = 0
            for post in b:
                e = Label(frame_input7, font=15, text=str(post[2]) + " " + post[0].title() + " " + post[1].title(),
                          bg='white')
                # a = 80+j*150
                f = 100 + i * 50
                e.place(x=80, y=f)
                i = i + 1
            btn1 = Button(frame_input7, command=self.appscreen, text="Back", cursor="hand2",
                          font=("calibri", 14), bg='white', fg="black", bd=0)
            btn1.place(x=170, y=550)
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                 , parent=self.root)

    def ViewPost(self):
        Frame_login8 = Frame(self.root, bg="white")
        Frame_login8.place(x=0, y=0, height=780, width=1586)
        frame_input8 = Frame(self.root, bg='white')
        frame_input8.place(x=570, y=10, height=750, width=1000)
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                  database='miniproject')
            cur = con.cursor()
            cur.execute('select user_id from users where email_id = %s', self.email_txt.get())
            userId = cur.fetchone()
            cur.execute('select post_id, post_date, post_content from posts, follow where posts.posted_user_id = follow.friend_id and follow.user_id = %s',userId)
            b = cur.fetchall()
            label1 = Label(frame_input8, text="Posts", font=('impact', 32, 'bold'), fg="black", bg='white')
            label1.place(x=150, y=20)
            i = 0
            l = 0

            for post in b:
                a = 80
                for j in range(len(post)):
                    e = Label(frame_input8, font=15, text=post[j])
                    if j == 1:
                        a += j*100
                    else:
                        a += j * 100
                    l = 100 + i * 50
                    e.place(x=a, y=l)
                i = i + 1

            btn1 = Button(frame_input8, command=self.appscreen, text="Back", cursor="hand2",
                          font=("calibri", 14), bg='orangered', fg="black", bd=0)
            btn1.place(x=180, y=l+180)
            label2 = Label(frame_input8, text="Enter Post id: -", font=(14), fg="black", bg='white')
            label2.place(x=20, y=l+120)
            self.id1 = Entry(frame_input8, font=("times new roman", 15, "bold"), bg='lightgray')
            self.id1.place(x=250, y=l+120, width=300)
            btn2 = Button(frame_input8, command=self.post_comment, text="Post Comment", cursor="hand2",
                          font=("calibri", 14), bg='orangered', fg="black", bd=0)
            btn2.place(x=600, y=l+120)
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                 , parent=self.root)

    def post_comment(self):
        if self.id1.get() == "":
            messagebox.showerror("Error", "Enter some content", parent=self.root)
        else:
            pi = self.id1.get()
            post_com = Frame(self.root, bg="white")
            post_com.place(x=0, y=0, height=780, width=1586)
            label3 = Label(post_com, text="Enter Comment", font=("Goudy old style", 15, "bold"), fg='orangered',
                           bg='white')
            label3.place(x=300, y=100)
            self.comment = Entry(post_com, font=("times new roman", 15, "bold"), bg='lightgray')
            self.comment.place(x=500, y=100, width=500)
            post1 = Button(post_com, command=lambda * args: self.succcom(pi), text="Post", cursor="hand2", font=("times new roman", 15),
                           fg="Black", bg="orangered", bd=0, width=15, height=1)
            post1.place(x=1050, y=90)
            btn1 = Button(post_com, command=self.ViewPost, text="Back", cursor="hand2",
                          font=("calibri", 14), bg='white', fg="black", bd=0)
            btn1.place(x=750, y=390)
        self.id1.delete(0, END)

    def succcom(self, pi):
        if self.comment.get() == "":
            messagebox.showerror("Error", "Enter some comment", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Deepa@93258',
                                      database='miniproject')
                cur = con.cursor()
                cur.execute('select user_id from users where email_id=%s', (self.email_txt.get()))
                b = cur.fetchone()
                self.user_id = b[0]
                print(pi)
                pid = int(pi)
                print(pid)
                a = str(datetime.today()).split()[0]
                t1 = 'insert into post_comments(post_id, commented_user_id, commented_date, coment_content) values('+str(pid)+','+str(self.user_id)+\
                     ',"'+a+'", '+'"'+self.comment.get()+'")'
                cur.execute(t1)
                con.commit()
                con.close()
                messagebox.showinfo("Successful", "Comment posted Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                     , parent=self.root)

        self.comment.delete(0, END)

    def regclear(self):
        self.entry.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def loginclear(self):
        self.email_txt.delete(0, END)
        self.password.delete(0, END)

    def forgotclear(self):
        self.email_txt1.delete(0, END)
        self.password1.delete(0, END)


root = Tk()
ob = Login(root)
root.mainloop()