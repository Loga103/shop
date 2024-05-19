

from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

tk=Tk()
tk.title("Sign up/Login")
tk.resizable(height="false",width="false")

image2=Image.open(r"C:\Users\DELL\Downloads\shop3.png")
photo2=ImageTk.PhotoImage(image2)

backgroundlabel=Label(tk,image=photo2)
backgroundlabel.place(x=0,y=0,relwidth=1,relheight=1)

fm1=Frame(tk,bg='pink')   #for signup 
fm1.pack(side=LEFT)

fm2=Frame(tk,bg='pink')  #for login  
fm2.pack(side=RIGHT)



image1=Image.open(r"C:\Users\DELL\Downloads\signup.png")
photo=ImageTk.PhotoImage(image1)

backgroundlabel=Label(fm1,image=photo)
backgroundlabel.place(x=0,y=0,relwidth=1,relheight=1)

image=Image.open(r"C:\Users\DELL\Downloads\login1.png")
photo1=ImageTk.PhotoImage(image)

backgroundlabel=Label(fm2,image=photo1)
backgroundlabel.place(x=0,y=0,relwidth=1,relheight=1)
tk.config(bg="pink")

w=900
h=600
sw=tk.winfo_screenwidth()
sh=tk.winfo_screenheight()
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
tk.geometry("%dx%d+%d+%d" % (w,h,x,y))
tk.iconbitmap(r"C:\Users\DELL\Downloads\shop.ico")

def Database():
        global conn, cursor
        conn = mysql.connector.connect( host = "localhost", 
        user = "root",
        passwd = "Vani@103",
        database="searchshop1",
        auth_plugin="mysql_native_password")
        cursor = conn.cursor()
    
    
def signup():
    Database()
    usen=us.get()
    paen=pa.get()
    
    cursor.execute("SELECT * FROM username WHERE users=%s",(usen,))
    if  cursor.fetchone():
        messagebox.showerror("ERROR","Username already existis.")
    else:
        cursor.execute("INSERT INTO username (users,password) VALUES (%s,%s)",(usen,paen))
        conn.commit()
        labl_result.config(text="now login to your page!", fg="blue")
        messagebox.showinfo("Success","Sign Up successful.")
        
 #       show_login()
    conn.close()
    

lbsignup=Label(fm1,text="Sign Up",font=("times",20),bg='skyblue')
lbsignup.grid(row=1,column=1,sticky=W)     
lbusername=Label(fm1,text="Username",font=("times",20),pady=40,bg='white')
lbusername.grid(row=3,column=0,sticky=W)
lbpassword=Label(fm1,text="Password",font=("times",20),pady=40,bg='white')
lbpassword.grid(row=4,column=0,sticky=W)
labl_result = Label(fm1, text="", font=('arial', 18),bg='white')
labl_result.grid(row=6, column=1,sticky=W)

us=Entry(fm1, font=('times', 15), width=30,bg='pink')
us.grid(row=3, column=1)
pa=Entry(fm1,show="*",font=('times', 15), width=30,bg='pink')
pa.grid(row=4, column=1)


btnsu=Button(fm1,text="Sign Up",fg="black",bg="skyblue",font=("Vineta BT",20),activebackground="green",activeforeground="black",width=6,pady=5,command=signup)
btnsu.grid(row=10, columnspan=2)

Database()
def login():
    def main():

        top3=Toplevel(tk)
        top3.title("SEARCH SHOP")
        
        top3.resizable(height="false",width="false")

        top3.configure(bg="pink")


        w=500
        h=500
        sw=tk.winfo_screenwidth()
        sh=tk.winfo_screenheight()
        x=(sw/2)-(w/2)
        y=(sh/2)-(h/2)
        top3.geometry("%dx%d+%d+%d" % (w,h,x,y))
        top3.iconbitmap(r"C:\Users\DELL\Downloads\shop.ico")

        SHOP=StringVar()
        OWNER=StringVar()
        ID=StringVar()
        DOOR=StringVar()
        CITY=StringVar()
        PIN=StringVar()
        CON=StringVar()
        MAIL=StringVar()
        OPEN=StringVar()
        PRO=StringVar()
        TYPE=StringVar()
        DIS=StringVar()


        def Database():
            global conn, cursor
            conn = mysql.connector.connect( host = "localhost", 
            user = "root",
            passwd = "Vani@103",
            database="searchshop1",
            auth_plugin="mysql_native_password")
            cursor = conn.cursor()


        def registration():

            def comboclick(event):
                data=cbtype.get()
                messagebox.showinfo("message",data)
            def comboclick1(event):
                data1=cbdis.get()
                messagebox.showinfo("message",data1)
            def comboclick2(event):
                data2=cbsta.get()
                messagebox.showinfo("message",data2)  


            def submit():
                Database()
                if SHOP.get() == "" or OWNER.get() == "" or ID.get() == "" or CITY.get() == "" or CON.get() == "" or MAIL.get() == "" :
                    lbl_result.config(text="Please complete the (*) required field!", fg="orange")
                else:
                        cursor.execute("INSERT INTO `registration` (shop_type,shop_name,owner_name,shop_id,door_no,city,district,state,pincode,contact,mail,open_time,products) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (str(cbtype.get()), str(SHOP.get()), str(OWNER.get()), str(ID.get()), str(DOOR.get()), str(CITY.get()), str(cbdis.get()), str(cbsta.get()), str(PIN.get()), str(CON.get()), str(MAIL.get()), str(OPEN.get()), str(PRO.get())))
                        conn.commit()
                        cbtype.set("")
                        SHOP.set("")
                        OWNER.set("")
                        ID.set("")
                        DOOR.set("")
                        CITY.set("")
                        cbdis.set("")
                        cbsta.set("")
                        PIN.set("")
                        CON.set("")
                        MAIL.set("")
                        OPEN.set("")
                        PRO.set("")
                        lbl_result.config(text="Successfully Created!", fg="green")

                conn.close()

            top=Toplevel(tk)
            top.title("Shop Registration")
            top.resizable(height="false",width="false")
            top.configure(bg="pink")

            w=800
            h=700
            sw=top.winfo_screenwidth()
            sh=top.winfo_screenheight()
            x=(sw/2)-(w/2)
            y=(sh/2)-(h/2)
            top.geometry("%dx%d+%d+%d" % (w,h,x,y))

            top.iconbitmap(r"C:\Users\DELL\Downloads\shop.ico")



            frame1=Frame(top,highlightthickness=5,bg='pink')    
            frame1.pack(side=TOP)
            lab=Label(frame1,text="REGISTRATION",font=("times",20),bg='pink')
            lab.grid(row=2,column=3)

            frame2=Frame(top,bg='pink')
            frame2.pack(side=TOP)
            lblty=Label(frame2,text="Shop Type *",font=("times",20),bg='pink')
            lblty.grid(row=3,sticky=W)
            lblna=Label(frame2,text="Shop Name *",font=("times",20),bg='pink')
            lblna.grid(row=4,sticky=W)
            lblow=Label(frame2,text="Owner Name *",font=("times",20),bg='pink')
            lblow.grid(row=5,sticky=W)
            lblid=Label(frame2,text="Shop id *",font=("times",20),bg='pink')
            lblid.grid(row=6,sticky=W)
            lbldo=Label(frame2,text="Door No",font=("times",20),bg='pink')
            lbldo.grid(row=7,sticky=W)
            lblci=Label(frame2,text="City *",font=("times",20),bg='pink')
            lblci.grid(row=8,sticky=W)
            lbldi=Label(frame2,text="District *",font=("times",20),bg='pink')
            lbldi.grid(row=9,sticky=W)
            lblst=Label(frame2,text="State *",font=("times",20),bg='pink')
            lblst.grid(row=10,sticky=W)
            lblpi=Label(frame2,text="Pincode ",font=("times",20),bg='pink')
            lblpi.grid(row=11,sticky=W)
            lblco=Label(frame2,text="Contact *",font=("times",20),bg='pink')
            lblco.grid(row=12,sticky=W)
            lblma=Label(frame2,text="Mail Address *",font=("times",20),bg='pink')
            lblma.grid(row=13,sticky=W)
            lblop=Label(frame2,text="Shop Opening Time(hh:mm)",font=("times",20),bg='pink')
            lblop.grid(row=14,sticky=W)
            lblpr=Label(frame2,text="Products",font=("times",20),bg='pink')
            lblpr.grid(row=15,sticky=W)
            lbl_result = Label(frame2, text="", font=('arial', 18),bg='pink')
            lbl_result.grid(row=17, columnspan=2,sticky=W)


            shop = Entry(frame2, font=('times', 15), textvariable=SHOP, width=20,bg='pink')
            shop.grid(row=4, column=1)
            own = Entry(frame2, font=('times', 15), textvariable=OWNER, width=20,bg='pink')
            own.grid(row=5, column=1)
            shid = Entry(frame2, font=('times', 15), textvariable=ID, width=20,bg='pink')
            shid.grid(row=6, column=1)
            door = Entry(frame2, font=('times', 15), textvariable=DOOR, width=20,bg='pink')
            door.grid(row=7, column=1)
            city = Entry(frame2, font=('times', 15), textvariable=CITY, width=20,bg='pink')
            city.grid(row=8, column=1)
            pinc = Entry(frame2, font=('times', 15), textvariable=PIN, width=20,bg='pink')
            pinc.grid(row=11, column=1)
            cont = Entry(frame2, font=('times', 15), textvariable=CON, width=20,bg='pink')
            cont.grid(row=12, column=1)
            mailid = Entry(frame2, font=('times', 15), textvariable=MAIL, width=20,bg='pink')
            mailid.grid(row=13, column=1)
            openhr = Entry(frame2, font=('times', 15), textvariable=OPEN, width=20,bg='pink')
            openhr.grid(row=14, column=1)
            prodt = Entry(frame2, font=('times', 15), textvariable=PRO, width=20,bg='pink')
            prodt.grid(row=15, column=1)

            cbtype=ttk.Combobox(frame2,width=30,state="readonly")
            cbtype['values']=("cake","icecream","hardwares","stationary","stores","printer press","construction")
            cbtype.current()
            cbtype.bind("<<Combobox Selected>>",comboclick)
            cbtype.grid(row=3,column=1)

            cbdis=ttk.Combobox(frame2,width=30,state="readonly")
            cbdis['values']=("Tiruppur","Salem","Tiruchirapalli","Coimbatore","Ooty","Erode")
            cbdis.current()
            cbdis.bind("<<Combobox Selected>>",comboclick)
            cbdis.grid(row=9,column=1)

            cbsta=ttk.Combobox(frame2,width=30,state="readonly")
            cbsta['values']=("TamilNadu","others")
            cbsta.current()
            cbsta.bind("<<Combobox Selected>>",comboclick)
            cbsta.grid(row=10,column=1)


            btnreg=Button(frame2,text="Register",fg="black",bg="white",font=("Vineta BT",20),activebackground="green",activeforeground="black",command=submit)
            btnreg.grid(row=18,columnspan=2)

            btnclose=Button(top,text="close",fg="white",bg="red",font=("Vineta BT",15),activebackground="skyblue",activeforeground="black",command=top.destroy)
            btnclose.pack(side=BOTTOM)

            lbl_result.config(text="* field is mandatory", fg="orange")


        def Searchshop(): 

            def search():  
                search1=shopty.get()
                search2=district.get()
                Database() 

                query="SELECT shop_name,owner_name,city,contact,mail,products FROM registration WHERE shop_type=%s AND district=%s"
                cursor.execute(query,(search1,search2))
                results = cursor.fetchall()

                if not results:
                    mytree.delete(*mytree.get_children())
                    mytree.insert("","end",text="NO MATCH IS FOUND")

                else:
                    mytree.delete(*mytree.get_children())
                    for row in results:
                        mytree.insert(parent="",index="end",iid=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5]))
                        mytree.pack(expand=True,fill="both")

           #         mytree.insert(parent="",index="end",values=("NO MATCH IS FOUND"))

                conn.close()    




            top1=Toplevel(tk)
            top1.title("Search shop")
            top1.resizable(height="false",width="false")
            top1.configure(bg="pink")

            w=800
            h=600
            sw=top1.winfo_screenwidth()
            sh=top1.winfo_screenheight()
            x=(sw/2)-(w/2)
            y=(sh/2)-(h/2)
            top1.geometry("%dx%d+%d+%d" % (w,h,x,y))

            top1.iconbitmap(r"C:\Users\DELL\Downloads\shop.ico")

            frame1=Frame(top1,highlightthickness=5,bg='pink')    
            frame1.pack(side=TOP)
            lab=Label(frame1,text="SEARCH",font=("times",20),bg='pink')
            lab.grid(row=3,column=3)

            frame2=Frame(top1,bg='pink')
            frame2.pack(side=TOP)
            lblshty=Label(frame2,text="Shop Type",font=("times",20),bg='pink')
            lblshty.grid(row=4,columnspan=2,sticky=W)
            lbldistrict=Label(frame2,text=" District",font=("times",20),bg='pink')
            lbldistrict.grid(row=5,column=1,sticky=W)

            shopty=ttk.Combobox(frame2,width=30,state="readonly")
            shopty['values']=("cake","icecream","hardwares","stationary","stores","printer press","construction")
            shopty.current()
            shopty.grid(row=4,column=2)

            district=ttk.Combobox(frame2,width=30,state="readonly")
            district['values']=("Tiruppur","Salem","Tiruchirapalli","Coimbatore","Ooty","Erode")
            district.current()
            district.grid(row=5,column=2)


            btnser=Button(frame2,text="Search",fg="white",bg="grey",font=("Vineta BT",15),activebackground="lightgreen",activeforeground="black",command=search)
            btnser.grid(row=10,column=2)

            frame3=Frame(top1,bg='pink')
            frame3.pack(side=TOP)

            mytree=ttk.Treeview(frame3)
            mytree["columns"]=["Shop Name","Owner Name","City","Contact","Mail Address","Products"]
            mytree.column("#0",width=0,stretch=NO)
            mytree.column("#1",width=80)
            mytree.column("#2",width=80)
            mytree.column("#3",width=80)
            mytree.column("#4",width=90)
            mytree.column("#5",width=150)
            mytree.column("#6",width=150)

            mytree.heading("#0",text="")
            mytree.heading("#1",text="Shop Name")
            mytree.heading("#2",text="Owner Name")
            mytree.heading("#3",text="City")
            mytree.heading("#4",text="Contact")
            mytree.heading("#5",text="Mail Address")
            mytree.heading("#6",text="Products/Services")

            btnclose=Button(top1,text="close",fg="white",bg="red",font=("Vineta BT",15),activebackground="skyblue",activeforeground="black",command=top1.destroy)
            btnclose.pack(side=BOTTOM)




        btnshop=Button(top3,text="Shop Registration",fg="white",bg="purple",font=("Vineta BT",20),activebackground="green",activeforeground="black",width=15,pady=10,command=registration)
        btnshop.pack(pady=30,padx=30)

        btnsearch=Button(top3,text="Search shop",fg="white",bg="magenta",font=("Vineta BT",20),activebackground="green",activeforeground="black",width=10,pady=10,command=Searchshop)
        btnsearch.pack(pady=30,padx=30)

        btnclose=Button(top3,text="close",fg="white",bg="red",font=("Vineta BT",15),activebackground="skyblue",activeforeground="black",command=tk.destroy)
        btnclose.pack(side=BOTTOM)

    
    Database()
    user=usn.get()
    passw=pan.get()
    
    cursor.execute("SELECT * FROM username WHERE users=%s AND password=%s",(user,passw))
    
    if cursor.fetchone():
        messagebox.showinfo("Login","Login Successfully.Welcome back!")
        main()   
    else:
        messagebox.showerror("Error","Invalid user name or password")
        
    conn.close() 
   
    
global usn,pan

lblogin=Label(fm2,text="Login",font=("times",20),bg='skyblue')
lblogin.grid(row=1,column=1,sticky=W)     
lbusernam=Label(fm2,text="Username *",font=("times",20),bg='white',pady=40)
lbusernam.grid(row=3,column=0,sticky=W)
lbpasswor=Label(fm2,text="Password *",font=("times",20),bg='white',pady=40)
lbpasswor.grid(row=4,column=0,sticky=W)

usn=Entry(fm2, font=('times', 15), width=30,bg='pink')
usn.grid(row=3, column=1)
pan=Entry(fm2,show="*",font=('times', 15), width=30,bg='pink')
pan.grid(row=4, column=1)

btnlo=Button(fm2,text="Login",fg="black",bg="skyblue",font=("Vineta BT",20),activebackground="green",activeforeground="black",width=5,pady=5,command=login)
btnlo.grid(row=20, columnspan=2)

#btnclo=Button(tk,text="close",fg="white",bg="red",font=("Vineta BT",15),activebackground="skyblue",activeforeground="black",width=5,pady=5,command=tk.destroy)
#btnclo.pack(side=BOTTOM)
    



tk.mainloop()
