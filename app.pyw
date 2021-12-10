#import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor

#import path checking module
from pathlib import Path

#import time and datetime module
import datetime
from time import *

#import db
import pymongo

#import os for system operation
import os

#import smtp and email.message for otp
import smtplib
from email.message import EmailMessage

#import random and it's stuff
from random import choice, randint

#import pyscreenshot for saving drawing notes
import pyscreenshot

#import webbrowser for browsing work
import webbrowser as wb

#lists for storing important temp data
#otp store list
otp_otp = []

#note store list
content = []

#subject of the note store list
subject = []

#new password store list
new_password = []

#username store list
old_username = []

#username store list for showing on label
user = []

#mongo db client
client = pymongo.MongoClient("mongodb+srv://Rishabh__Coder:d5NGwvRpwA8dX3p@cluster0.pcozu.mongodb.net/test?authSource=admin&replicaSet=atlas-11zmxy-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")

#login/register choice page start
def first_page():
    root = Tk()
    root.title('Free Pages Desktop')
    root.iconbitmap('./icon.ico')
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.x_co = int((screen_width / 2) - (550 / 2))
    root.y_co = int((screen_height / 2) - (400 / 2)) - 80
    root.geometry(f"550x400+{root.x_co}+{root.y_co}")

    root.config(bg="black")
    
    def close_this_page():
        root.destroy()
    
    Label1 = Label(root, text="Free Pages", width=25,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10)
    
    Button1 = Button(root, cursor = "hand2",text='Create Account', bg='navy', fg="#00FF89", command=lambda:{close_this_page(),create_account_page()}, font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button1.place(x=200, y=140, width=200)
    Button2 = Button(root,cursor="hand2", text='Login', bg='navy', fg="#00FF89", command=lambda:{close_this_page(), login_account_page()},font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button2.place(x=200, y=180, width=200)
    
    root.resizable(0, 0)
    root.mainloop()
#login/register choice page end

#register account page if user doesn't have an account start
def create_account_page():
    roo = Tk()
    roo.title('Free Pages Desktop')
    roo.geometry('1920x1080')
    roo.iconbitmap('./icon.ico')
    screen_width, screen_height = roo.winfo_screenwidth(), roo.winfo_screenheight()
    roo.x_co = int((screen_width / 2) - (550 / 2))
    roo.y_co = int((screen_height / 2) - (400 / 2)) - 80
    roo.geometry(f"550x400+{roo.x_co}+{roo.y_co}")

    roo.config(bg="black")

    def create_account():
        global client
        db = client['free_page']
        collection = db['Users']
        find = collection.count_documents({'Username':E1.get(),'Password':E2.get()})
        if find==1:
            Label4.config(text="User Already Exist",bg="red")
        elif find<=0:
            try:
                time = datetime.datetime.now()
                db = client['free_page']
                collection = db['Users']
                insertvalue = [
                {'Username':E1.get(),'Password':E2.get(),"Date":time.strftime("%d-%m-%y")},
                ]
                collection.insert_many(insertvalue)
                roo.destroy()
                first_page()
            except:
                Label4.config(text="Network Error", bg="red")
                first_page()
    def back():
        roo.destroy()
        first_page()
        
    Label1 = Label(roo, text="Create Account", width=25,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10)
    Label2 = Label(roo, text="Username", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=100, width = 200, height = 50)
    Label4 = Label(roo, text="",width=20,font=('calibri',13),bg='black')
    Label4.place(x=205,y=360)

    E1 = Entry(roo)
    E1.place(x=220,y=100,height=50,width=200)

    Label3 = Label(roo, text="Password", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=190, width = 200, height = 50)

    E2 = Entry(roo)
    E2.place(x=220,y=190,height=50,width=200)

    B1 = Button(roo, cursor = "hand2",text='Create Account', bg='navy', fg="#00FF89", command=create_account, font=('times', 15, ' bold '),activebackground = "#00FF89")
    B1.place(x=100, y=300, width=200)
    B2 = Button(roo, cursor = "hand2",text='Home Page', bg='navy', fg="#00FF89", command=back, font=('times', 15, ' bold '),activebackground = "#00FF89")
    B2.place(x=300, y=300, width=200)

    roo.resizable(0, 0)
#register account page if user doesn't have an account end

#login account page if user already have an account start
def login_account_page():
    ro = Tk()
    ro.title('Free Pages Desktop')
    ro.iconbitmap('./icon.ico')
    screen_width, screen_height = ro.winfo_screenwidth(), ro.winfo_screenheight()
    ro.x_co = int((screen_width / 2) - (550 / 2))
    ro.y_co = int((screen_height / 2) - (400 / 2)) - 80
    ro.geometry(f"550x400+{ro.x_co}+{ro.y_co}")

    ro.config(bg="black")

    def back():
        ro.destroy()
        first_page()
    def login():
        global client
        db = client['free_page']
        collection = db['Users']
        find = collection.count_documents({'Username':E1.get(),'Password':E2.get()})
        if find==1:
            open('C:\\FreePage\\acc.txt', 'a').close()
            u = open('C:\\FreePage\\acc_username.txt', 'w')
            u.write(E1.get())
            u.close()
            p = open('C:\\FreePage\\acc_password.txt', 'w')
            p.write(E2.get())
            p.close()
            user.append(E1.get())
            ro.destroy()
            main_note_page()
        else:
            E1.config(text="")
            E2.config(text="")
            Label4.config(text="User Not Verified",bg="red")

    Label1 = Label(ro, text="Login", width=25,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10)
    Label2 = Label(ro, text="Username", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=100, width = 200, height = 50)
    Label3 = Label(ro, text="Password", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=190, width = 200, height = 50)
    Label4 = Label(ro, text="",width=20,font=('calibri',13),bg='black')
    Label4.place(x=205,y=360)

    E1 = Entry(ro)
    E1.place(x=220,y=100,height=50,width=200)

    E2 = Entry(ro)
    E2.place(x=220,y=190,height=50,width=200)

    B1 = Button(ro, cursor = "hand2",text='Login', bg='navy', fg="#00FF89", command=login, font=('times', 15, ' bold '),activebackground = "#00FF89")
    B1.place(x=100, y=300, width=200)
    B2 = Button(ro, cursor = "hand2",text='Home Page', bg='navy', fg="#00FF89", command=back, font=('times', 15, ' bold '),activebackground = "#00FF89")
    B2.place(x=300, y=300, width=200)

    ro.mainloop()
    ro.resizable(0, 0)
#Login account page if user already have an account end

#Main app page if verification is done start
def main_note_page():
    m1 = Tk()
    m1.title('Free Pages Desktop')
    try:
        m1.iconbitmap('icon.ico')
    except:
        os.chdir('./')
        m1.iconbitmap('icon.ico')
    m1.geometry('1920x1080')
    m1.config(bg="black")
    m1.state("zoomed")

    def close():
        m1.destroy() 

    Label1 = Label(m1, text="Free Pages", width=50,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10, width=1400)
    Label2 = Label(m1, text="Welcome "+str(user).replace('[', "").replace("'", "").replace(']', "").strip() , width=30, height=1, fg="white", bg="black",font=('segou UI', 15, ' bold italic'))
    Label2.place(x=790, y=60)

    Button1 = Button(m1, cursor = "hand2",text='Add Notes', bg='navy', fg="#00FF89", command=lambda:{close(), add_note_page()} ,font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button1.place(x=600, y=140, width=200)
    Button2 = Button(m1,cursor="hand2", text='View Notes', bg='navy', fg="#00FF89", command=lambda:{close(), view_note_page()}, font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button2.place(x=600, y=260, width=200)
    Button3 = Button(m1,cursor="hand2", text='Manage Account', bg='navy', fg="#00FF89", command=lambda:{close(), account_manage_page()}, font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button3.place(x=600, y=320, width=200)
    Button4 = Button(m1,cursor="hand2", text='Logout', bg='navy', fg="#00FF89", command=lambda:{close(), logout()}, font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button4.place(x=600, y=380, width=200)
    Button5 = Button(m1,cursor="hand2", text='Draw', bg='navy', fg="#00FF89", command=lambda:{close(), paint_note()}, font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button5.place(x=600, y=200, width=200)
    Button6 = Button(m1,cursor="hand2", text='About Me', bg='navy', fg="#00FF89", command=lambda:{about_me()}, font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button6.place(x=10, y=100, width=200)
    Button7 = Button(m1,cursor="hand2", text='About App', bg='navy', fg="#00FF89", command=lambda:{about_app()}, font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button7.place(x=10, y=140, width=200)

    def about_me():
        wb.open_new('https://rishabhkeshri.000webhostapp.com/index.html')
    def about_app():
        wb.open('https://rishab1804.github.io/FreePages.github.io')

    m1.mainloop()
#Main app page if verification is done end

#Add note page start
def add_note_page():
    m2 = Tk()
    m2.title('Free Pages Desktop')
    m2.iconbitmap('./icon.ico')
    m2.config(bg="black")
    m2.state("zoomed")

    def back():
        m2.destroy()
        main_note_page()

    #main function
    def add_notes():
            global client
            if Entry1.get() == "" or Entry1.get() == " ":
                Label3.config(text="Subject is required.", bg="red")
            elif Entry1.get() == "Subject" or Entry1.get() == "subject" or Entry1.get() == "'" or Entry1.get() == '"' or Entry1.get == "{" or Entry1.get == "[" or Entry1.get() == '}' or Entry1.get == ']':
                Label3.config(text="Subject can never be a 'subject, notes, upostrophies, brackets", bg="red")
            elif Text1.get("1.0", "end-1c") == "Notes" or Text1.get("1.0", "end-1c") == "notes" or Text1.get("1.0", "end-1c") == "Subject" or Text1.get("1.0", "end-1c") == "subject":
                Label3.config(text="Notes body can never be a 'note'", bg="red")
            else:
                try:
                    u = open('C:\\FreePage\\acc_username.txt', 'r')
                    u_get = u.read()
                    u.close()
                    db = client['free_page']
                    collection = db[u_get]
                    time = datetime.datetime.now()
                    subject_to_be = Entry1.get()
                    add_note = [
                    {"Subject":subject_to_be, "Notes":Text1.get("1.0","end-1c")},
                    ]
                    collection.insert_many(add_note)
                    Label3.config(text="Notes Saved", bg="green")
                except Exception as E:
                    Label3.config(text="Error Occured While Saving Notes", bg="red")
                    print(E)

    Label1 = Label(m2, text="Free Pages", width=50,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10, width=1400)
    Label3 = Label(m2, text="",width=50,font=('calibri',13),bg='black')
    Label3.place(x=560,y=500)

    Entry1 = Entry(m2, bg='#00FF89', fg="#8B13F3", font=('times', 13, ' bold '))
    Entry1.place(x=600,y=80,height=25,width=165)

    Text1 = Text(m2,borderwidth = 1, width=70,height=13, bg='#00FF89', fg="#8B13F3", font=('times', 13, ' bold '))
    Text1.place(x=380,y=130)

    Button1 = Button(m2, cursor = "hand2", command=add_notes, text='Save', bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button1.place(x=500, y=400, width=200)
    Button2 = Button(m2, cursor = "hand2", command=back, text='Back', bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button2.place(x=700, y=400, width=200)

    m2.mainloop()
#Add note page end

#View note page start
def view_note_page():
    m3 = Tk()
    m3.title('Free Pages Desktop')
    m3.config(bg="black")
    m3.state("zoomed")
    m3.iconbitmap('./icon.ico')

    #fetch from mongo db
    def database_fetcher():
        global client
        u1 = open('C:\\FreePage\\acc_username.txt', 'r')
        u1_get = u1.read()
        u1.close()
        db = client['free_page']
        collection = db[u1_get]
        param = insert()
        fetch_step_1 = collection.find_one({'Subject':param},{'_id':0,'Notes':1}) 
        try:
            content.clear()
        except:
            pass
        fetch_step_2 = str(fetch_step_1).replace("\n", "\r").replace('{', "").replace("'", "").replace('Notes',"").replace("'", "").replace(':', "").replace('\\n', '\n').replace('\n', '\n').replace('}', "")
        content.append(fetch_step_2)
        open('C:\\FreePage\\note_content.txt', 'a').close()
        note_content = open('C:\\FreePage\\note_content.txt', 'a')
        note_content.write(fetch_step_2)
        note_content.close()
        open('C:\\FreePage\\subject_content.txt', 'a').close()
        subject_content = open('C:\\FreePage\\subject_content.txt', 'a')
        subject_content.write(param)
        subject_content.close()
        m3.destroy()
        open_note_page()
    
    def open_note_page():
        m4 = Tk()
        m4.title('Free Pages Desktop')
        m4.config(bg="black")
        m4.state("zoomed")
        m4.iconbitmap('./icon.ico')

        def back():
            subject.clear()
            m4.destroy()
            view_note_page()

        note_body = open('C:\\FreePage\\note_content.txt', 'r')
        note_get = note_body.read()
        note_body.close()

        subeject_body = open('C:\\FreePage\\subject_content.txt', 'r')
        subject_get = subeject_body.read()
        subeject_body.close()

        Text2 = Text(m4,borderwidth = 1, width=500,height=25, bg='#00FF89', fg="#8B13F3", font=('times', 13, ' bold '))
        Text2.insert(1.0, note_get.strip())
        Text2.place(x=0,y=30)
        
        Entry1 = Entry(m4, bg='#00FF89', fg="#8B13F3", font=('times', 13, ' bold '))
        Entry1.place(x=600,y=0,height=25,width=165)
        Entry1.insert(END, subject_get)

        Notif = Label(m4, text="", bg="black", fg="black", width=30,)
        Notif.place(x=460,y=520)

        try:
            os.remove('C:\\FreePage\\note_content.txt')
        except FileNotFoundError:
            os.mkdir('C:\\FreePage')
        try:
            os.remove('C:\\FreePage\\subject_content.txt')
        except FileNotFoundError:
            os.mkdir('C:\\FreePage')

        def save_change():
            global client
            subject_fetch = str(subject).replace('[', "").replace("'", "").replace(']', "").strip()
            u1 = open('C:\\FreePage\\acc_username.txt', 'r')
            u1_get = u1.read()
            u1.close()
            try:    
                db = client['free_page']
                collection = db[u1_get]
                collection.update_one({"Subject":subject_fetch.strip()}, {"$set":{"Notes":Text2.get("1.0", "end"), "Subject":Entry1.get()}})
                Notif.config(text="Saved Changes", bg="green",font=('calibri',13,'bold'))
                subject.clear()
                subject.append(Entry1.get())
            except Exception as E:
                Notif.config(text="Error occured while saving", fg="red", font=('calibri',13,'bold'))
                print(E)

        Button1 = Button(m4, cursor = "hand2", text='Save Changes', command=save_change, bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
        Button1.place(x=400, y=600, width=200)
        Button2 = Button(m4, cursor = "hand2", text='Back', command=back ,bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
        Button2.place(x=600, y=600, width=200)

    def view_notes():
        global client
        try:
            listbox1.delete(0,'end')
        except:
            pass
        try:
            u1 = open('C:\\FreePage\\acc_username.txt', 'r')
            u1_get = u1.read()
            u1.close()
            db = client['free_page']
            collection = db[u1_get]
            find = collection.count_documents({})
            if find>=1: 
                cursor = collection.find({}, {"_id":0, "Subject":1})
                for documents in cursor:
                    listbox1.insert(END, documents)
                Button2.place(x=900, y=200, width=200)
                Button4.place(x=900, y=300, width=200)
                listbox1.place(x=50, y=200)
            elif find<=0:
                m3.destroy()
                add_note_page()
        except Exception as e:
            print(e)

    def note_delete():
        global client
        try:
            u1_________________ = open('C:\\FreePage\\acc_username.txt', 'r')
            u1________get = u1_________________.read()
            u1_________________.close()
            db = client['free_page']
            collection = db[u1________get]
            param______ = insert()
            note_be_deleted = { "Subject": param______}
            collection.delete_one(note_be_deleted)
            selection = listbox1.curselection()
            listbox1.delete(selection[0])
            messagebox.showinfo("Free Pages","Note has been deleted.") 
        except Exception as E:
            print(E)
            messagebox.showerror("Free Pages","Error deleting note.")  

    def insert():
        for i in listbox1.curselection():
            mall = str(listbox1.get(i)).replace("{", "").replace("Subject", "").replace(":", "").replace("'",'').replace("'",'').replace('}', '')
            return mall.strip()
    def insert_list():
        for i in listbox1.curselection():
            mall_main = str(listbox1.get(i)).replace("{", "").replace("Subject", "").replace(":", "").replace("'",'').replace("'",'').replace('}', '')
            try:
                subject.append(mall_main)
            except:
                pass

    def back():
        m3.destroy()
        main_note_page()

    Label1 = Label(m3, text="Free Pages", width=50,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10, width=1400)

    Button1 = Button(m3, cursor = "hand2", command=view_notes, text='View Notes', bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button1.place(x=600, y=100, width=200)
    Button2 = Button(m3, cursor="hand2",command=lambda:{insert(),insert_list(),database_fetcher()}, text='Open', bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button3 = Button(m3, cursor="hand2",command=back, text='Back', bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button3.place(x=600, y=400, width=200)
    Button4 = Button(m3, cursor="hand2",command=lambda:{note_delete()}, text='Delete', bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")

    listbox1 = Listbox(m3, font=(
            'arial', 13, 'bold'), width=90, height=8)

    m3.mainloop()
#View note page end

#Change password page
def account_manage_page():
    
    def change_password():
        
        def change_password_feature():
            try:
                otp_otp.clear()
            except:
                pass

            otp_list = []
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for char in range(randint(4,6)):
                otp_list += choice(numbers)

            password = ""
            for char in otp_list:
                password += char

            otp_otp.append(password)

            m7 = Tk()
            m7.title('Free Pages Desktop')
            m7.config(bg="black")
            m7.iconbitmap('./icon.ico')
            screen_width, screen_height = m7.winfo_screenwidth(), m7.winfo_screenheight()
            m7.x_co = int((screen_width / 2) - (550 / 2))
            m7.y_co = int((screen_height / 2) - (400 / 2)) - 80
            m7.geometry(f"550x400+{m7.x_co}+{m7.y_co}")
            m7.resizable(0,0)

            Label1 = Label(m7, text="Free Pages", width=25,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10)
            Label2 = Label(m7, text="Email", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=100, width = 200, height = 50)
            Notif = Label(m7, text="",bg="black",width=30,height=1,font=('segou UI', 18,'bold italic'))
            Notif.place(x=120,y=300)
            Label5 = Label(m7, text="OTP", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic'))
            
            E1_ = Entry(m7)
            E1_.place(x=220,y=100,height=50,width=200)
            E2_ = Entry(m7)

            otp = str(otp_otp).replace('[', "").replace("'", "").replace(']', "").strip()

            def change():
                global client
                try:
                    new_password_fetch = str(new_password).replace('[', "").replace("'", "").replace(']', "").strip()
                    old_username_fetch = str(old_username).replace('[', "").replace("'", "").replace(']', "").strip()
                    db = client['free_page']
                    collection = db['Users']
                    find = collection.count_documents({})
                    if find<=0: 
                        Notif.config(text="User not exists", bg="red")
                    elif find>=1:
                        data_base_insert_new_password = collection.update_one({"Username":old_username_fetch}, {"$set":{"Password":new_password_fetch}})
                        os.remove('C:\\FreePage\\acc_password.txt')
                        p_new = open('C:\\FreePage\\acc_password.txt', 'w')
                        p_new.write(new_password_fetch)
                        p_new.close()
                        Notif.config(text="Password Changed Succesfully", bg="green", font=('calibri',20,'bold'))
                        m7.destroy()
                        main_note_page()
                except:
                    Notif.config(text="Error Occured while changing password", bg="red")
                    
            def verify_otp():
                if E2_.get() == otp:
                    change()
                else:
                    Notif.config(text="Wrong OTP", bg="red")

            def send_otp():
                try:
                    msg = EmailMessage()
                    username = 'keshririshabh849@gmail.com'
                    password = 'R1shabh__76'
                    to = E1_.get()
                    subject = 'Free Pages Change Password OTP'
                    body = f"""Dear {to},
We hope you and your family is good in this pandemic time.
We have been requested a password change request from your account.
This is the OTP - {otp}.
If you have not requested for a password change, kindly ignore this message and don't share this otp with any one.
Thanks and Regards,
Free Pages"""
                    msg['Subject'] = subject
                    msg['from'] = username
                    msg['to'] = to
                    msg.set_content(body)
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(username, password)
                    server.send_message(msg)
                    Notif.config(text="Otp has been sent succesfully.", bg="green")
                    B2_.config(state="normal")
                    Label5.place(x=0,y=190, width = 200, height = 50)
                    E2_.place(x=220,y=190,height=50,width=200)
                except Exception as e:
                    Notif.config(text="Internal Server Error", bg="red")
                    print(e)

            B1_ = Button(m7, cursor = "hand2",text='Send OTP',command=send_otp, bg='navy', fg="#00FF89",font=('times', 15, ' bold '),activebackground = "#00FF89")
            B1_.place(x=40, y=350, width=200)
            B2_ = Button(m7, state=DISABLED, cursor = "hand2",text='Verify OTP',command=lambda:{verify_otp()}, bg='navy', fg="#00FF89",font=('times', 15, ' bold '),activebackground = "#00FF89")
            B2_.place(x=300, y=350, width=200)

        m6 = Tk()
        m6.title('Free Pages Desktop')

        m6.config(bg="black")    
        m6.iconbitmap('./icon.ico')
        screen_width, screen_height = m6.winfo_screenwidth(), m6.winfo_screenheight()
        m6.x_co = int((screen_width / 2) - (550 / 2))
        m6.y_co = int((screen_height / 2) - (400 / 2)) - 80
        m6.geometry(f"550x400+{m6.x_co}+{m6.y_co}")
        m6.resizable(0,0)

        Label1 = Label(m6, text="Free Pages", width=25,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10)
        Label2 = Label(m6, text="Username", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=100, width = 200, height = 50)
        Label3 = Label(m6, text="Password", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=190, width = 200, height = 50)
        Label4 = Label(m6, text="New Password", width=8,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 18, ' bold italic')).place(x=0,y=280, width = 200, height = 50)

        Entry1_ = Entry(m6)
        Entry1_.place(x=220,y=100,height=50,width=200)

        Entry2_ = Entry(m6)
        Entry2_.place(x=220,y=190,height=50,width=200)

        Entry3_ = Entry(m6)
        Entry3_.place(x=220,y=280,height=50,width=200)

        def new_password_username_insert():
            db = client['free_page']
            collection = db['Users']
            find = collection.count_documents({'Username':Entry1_.get(),'Password':Entry2_.get()})
            if find==1:
                new_password.append(Entry3_.get())
                old_username.append(Entry1_.get())
                m6.destroy()
                change_password_feature()
            else:
                mbox = messagebox.showwarning("showwarning", "Username or Password is incorrect")
                if mbox:
                    Entry1_.delete(0,END)
                    Entry2_.delete(0,END)
                    Entry3_.delete(0,END)

        B1 = Button(m6, cursor = "hand2",text='Change Password',command=new_password_username_insert, bg='navy', fg="#00FF89",font=('times', 15, ' bold '),activebackground = "#00FF89")
        B1.place(x=110, y=350, width=200)
        B1 = Button(m6, cursor = "hand2",text='Home Page',command=lambda:{m6.destroy(), main_note_page()}, bg='navy', fg="#00FF89",font=('times', 15, ' bold '),activebackground = "#00FF89")
        B1.place(x=300, y=350, width=200)

        
    m5 = Tk()
    m5.title('Free Pages Desktop')
    m5.config(bg="black")
    m5.state("zoomed")
    m5.iconbitmap('./icon.ico')


    def close():
        m5.destroy()

    def back():
        main_note_page()

    def log_out():
        user.clear()
        otp_otp.clear()
        content.clear()
        new_password.clear()
        old_username.clear()
        os.remove('C:\\FreePage\\acc_username.txt')
        os.remove('C:\\FreePage\\acc_password.txt')
        os.remove('C:\\FreePage\\acc.txt')
        first_page()
        
    Label1 = Label(m5, text="Free Pages", width=50,height=1,fg="#00FF89",bg="#8B13F3",font=('segou UI', 28, ' bold italic')).place(x=-10,y=10, width=1400)

    Button1 = Button(m5, cursor = "hand2", text='Change Password',command=lambda:{close(), change_password()}, bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button1.place(x=300, y=200, width=200)
    Button2 = Button(m5, cursor = "hand2", text='Logout',command=lambda:{close(), log_out()}, bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button2.place(x=800, y=200, width=200)
    Button3 = Button(m5, cursor = "hand2", text='Back',command=lambda:{close(), back()}, bg='navy', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
    Button3.place(x=570, y=400, width=200)

    m5.mainloop()

#Logout page
def logout():
    root_______ = Tk()
    root_______.withdraw()
    mbox = messagebox.askyesno("Free Pages", "Do you really want to logout?")
    if mbox:
        user.clear()
        otp_otp.clear()
        content.clear()
        new_password.clear()
        old_username.clear()
        os.remove('C:\\FreePage\\acc_username.txt')
        os.remove('C:\\FreePage\\acc_password.txt')
        os.remove('C:\\FreePage\\acc.txt')
        root_______.destroy()
        first_page()
    else:
        root_______.destroy()
        main_note_page()
  
#Hand note page
def paint_note():
    class Paint(object):
    
        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'black'

        def __init__(self):
            self.root = Tk()
            self.root.title('Free Pages Desktp')
            self.root.state("zoomed")
            self.root.iconbitmap('./icon.ico')
            self.root.config(bg="white")

            self.pen_button = Button(self.root, text='Pen',fg="#00FF89",bg="#8B13F3",command=self.use_pen)
            self.pen_button.place(x=50, y=10)

            self.color_button = Button(self.root, text='Colour',fg="#00FF89",bg="#8B13F3", command=self.choose_color)
            self.color_button.place(x=200, y=10)

            self.eraser_button = Button(self.root, text='Eraser',fg="#00FF89",bg="#8B13F3", command=self.use_eraser)
            self.eraser_button.place(x=350,y=10)

            self.subject_entry = Entry(self.root)
            self.subject_entry.place(x=550, y=10, width=200)

            self.save_button = Button(self.root, text='Save',fg="#00FF89",bg="#8B13F3", command=self.save)
            self.save_button.place(x=850, y=10)

            self.back_button = Button(self.root, text='Back',fg="#00FF89", bg="#8B13F3", command=self.back)
            self.back_button.place(x=1000, y=10)

            self.choose_size_button = Scale(self.root, from_=1, to=10,fg="#00FF89",bg="#8B13F3", orient=HORIZONTAL)
            self.choose_size_button.grid(row=0, column=4)

            self.c = Canvas(self.root, bg='white', width=1300, height=600)
            self.c.grid(row=1, columnspan=5)

            self.setup()

        def setup(self):
            self.old_x = None
            self.old_y = None
            self.line_width = self.choose_size_button.get()
            self.color = self.DEFAULT_COLOR
            self.eraser_on = False
            self.active_button = self.pen_button
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)

        def use_pen(self):
            self.activate_button(self.pen_button)

        def use_brush(self):
            self.activate_button(self.brush_button)

        def choose_color(self):
            self.eraser_on = False
            self.color = askcolor(color=self.color)[1]

        def save(self):
            try:
                image_path = Path('C://FreePage',self.subject_entry.get()+'.png')
                if image_path.is_file():
                    ______root_______ = Tk()
                    ______root_______.withdraw()
                    mbox_2 = messagebox.askyesno("Free Pages", "Notes exist with a same subject. Do you want to replace it?")
                    if mbox_2:
                        os.remove(self.subject_entry.get()+'.png')
                        image = pyscreenshot.grab(bbox=(1,100,1921,1003))
                        image.save('C://FreePage//Draws'+self.subject_entry.get()+'.png')

                        ______root_______.destroy()
                    else:
                        image = pyscreenshot.grab(bbox=(1,100,1921,1003))
                        image.save('C://FreePage//Draws'+self.subject_entry.get()+'.png')
                        ______root_______.destroy()
                elif not image_path.is_file():
                    image = pyscreenshot.grab(bbox=(1,100,1921,1003))
                    image.save('C://FreePage//Draws'+self.subject_entry.get()+'.png')
            except:
                pass

        def back(self):
            os.chdir('./')
            self.root.destroy()
            main_note_page()

        def use_eraser(self):
            self.activate_button(self.eraser_button, eraser_mode=True)

        def activate_button(self, some_button, eraser_mode=False):
            self.active_button.config(relief=RAISED)
            some_button.config(relief=SUNKEN)
            self.active_button = some_button
            self.eraser_on = eraser_mode

        def paint(self, event):
            self.line_width = self.choose_size_button.get()
            paint_color = 'white' if self.eraser_on else self.color
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                width=self.line_width, fill=paint_color,
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.old_x = event.x
            self.old_y = event.y

        def reset(self, event):
            self.old_x, self.old_y = None, None

    Paint()

#when app runs this code should be executed first then rest
if __name__ == '__main__':
    path = Path('C:\\FreePage')
    if path.is_dir():
        pass
    else:
        os.mkdir('C:\\FreePage')
        
    path2 = Path("C:\\FreePage\\acc.txt")
    path3 = Path("C:\\FreePage\\acc_username.txt")
    path4 = Path("C:\\FreePage\\acc_password.txt")
    path5 = Path("C:\\FreePage\\note_content.txt")

    if path3.is_file():
        u_append = open('C:\\FreePage\\acc_username.txt', 'r')
        u_append_get = u_append.read()
        user.clear()
        user.append(u_append_get) 
        u_append.close()
    else:
        pass
    
    if path2.is_file() and path4.is_file():
        main_note_page()
    else:
        first_page()

    if path5.is_file():
        os.remove(path5)
    else:
        pass
 