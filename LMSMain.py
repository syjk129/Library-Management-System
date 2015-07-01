
from tkinter import *
import re
import urllib.request
import base64
import pymysql
from tkinter import messagebox
import datetime as clock


class Gateway:
    def __init__(self, root):


        self.root = root
        self.username = StringVar()
        self.password = StringVar()
        self.confirmpassword = StringVar()
        self.currentuser = ''

        #-----CreateProfileVariables-----#
        self.dob = StringVar()
        self.dob.set('YYYY-MM-DD')
        self.email = StringVar()
        self.address = StringVar()
        self.lastname = StringVar()
        self.firstname= StringVar()
        self.gender = StringVar()
        self.faculty = StringVar()
        self.department = StringVar()

        #Download and prep the IMAGE
        self.image = None
        response = urllib.request.urlopen("http://www.cc.gatech.edu/classes/AY2015/cs2316_fall/codesamples/techlogo.gif")
        data = response.read()
        response.close()
        img = base64.encodebytes(data)
        self.image = PhotoImage(data=img)

        #---------LOGIN PAGE---------#
        self.root.title("Login")
        l = Label(self.root, image=self.image)
        l.pack()

        #USERNAME
        frame1 = Frame(self.root)
        frame1.pack()
        Label(frame1,text="Username:").pack(side=LEFT, anchor=E)
        self.loginusername = Entry(frame1, width=30, textvariable=self.username)
        self.loginusername.pack(side=LEFT)
        Label(frame1,text="          ").pack(side=LEFT, anchor=E)

        #PASSWORD
        frame2 = Frame(self.root)
        frame2.pack()
        Label(frame2,text="Password:").pack(side=LEFT, anchor=E)
        self.loginpassword = Entry(frame2, width=30, textvariable=self.password)
        self.loginpassword.pack(side=LEFT)
        Label(frame2,text="         ").pack(side=LEFT, anchor=E)

        #LOGIN BUTTONS
        frame3 = Frame(self.root)
        frame3.pack(fill=BOTH, expand=True)
        Button(frame3,text="Exit",     command=self.root.destroy).pack(side=RIGHT)
        Button(frame3,text="Login",    command=self.LoginCheck).pack(side=RIGHT)
        Button(frame3,text="Register", command=self.switch).pack(side=RIGHT)


        #----------New User Registration Page------------#
        self.root21 = Toplevel()
        self.root21.title("New User Registration")

        # url = "http://www.or.gatech.edu/images/isye-icon.gif"
        #
        #
        #
        # response = urllib.request.urlopen(url)
        # data = response.read()
        # response.close()
        #
        # img = base64.encodebytes(data)
        # image = PhotoImage(data=img)

        #image
        L = Label(self.root21, image=self.image)
        L.pack()

        #USERNAME
        framez = Frame(self.root21)
        framez.pack(fill=BOTH, expand=True)
        Label(framez,text="Username:            ").pack(side=LEFT)
        self.regusername = Entry(framez, width=30, textvariable=self.username)
        self.regusername.pack(side=LEFT)

        #PASSWORD
        framec = Frame(self.root21)
        framec.pack(fill=BOTH, expand=True)
        Label(framec,text="Password:             ").pack(side=LEFT)
        self.regpassword = Entry(framec, width=30, textvariable=self.password)
        self.regpassword.pack(side=LEFT)

        #CONFIRMPASSWORD
        framed = Frame(self.root21)
        framed.pack(fill=BOTH, expand=True)
        Label(framed,text="Confirm Password:").pack(side=LEFT, anchor=E)
        self.regconfirmpassword = Entry(framed, width=30, textvariable=self.confirmpassword)
        self.regconfirmpassword.pack(side=LEFT)

        #BUTTONS
        framee = Frame(self.root21)
        framee.pack(fill=BOTH, expand=True)
        Button(framee,text="Register", command=self.RegisterNew).pack(side=RIGHT)
        Button(framee,text="Cancel", command=self.switch2122).pack(side=RIGHT)
        self.root21.withdraw()

        #------Create Profile Page------#
        self.root22 = Toplevel()
        self.root22.title('Create Profile')


        L = Label(self.root22, image=self.image)
        L.pack()
        framet = Frame(self.root22)
        framet.pack()
        frametl = Frame(framet)
        frametl.pack(side=RIGHT)
        frametr =Frame(framet)
        frametr.pack(side=RIGHT)

        frametl1 = Frame(frametl)
        frametl1.pack(fill=BOTH, expand=True)
        self.regfirstname = Entry(frametl1, width=30, textvariable=self.firstname)
        self.regfirstname.pack(side=RIGHT)
        Label(frametl1,text="First Name:").pack(side=RIGHT)


        frametl2 = Frame(frametl)
        frametl2.pack(fill=BOTH, expand=True)
        self.regdob = Entry(frametl2, width=30, textvariable=self.dob)
        self.regdob.pack(side=RIGHT)
        Label(frametl2,text="D.O.B:").pack(side=RIGHT)


        frametl3 = Frame(frametl)
        frametl3.pack(fill=BOTH, expand=True)
        self.regemail = Entry(frametl3, width=30, textvariable=self.email)
        self.regemail.pack(side=RIGHT)
        Label(frametl3,text="Email:").pack(side=RIGHT)


        frametl4 = Frame(frametl)
        frametl4.pack(fill=BOTH, expand=True)
        self.regaddress = Entry(frametl4, width=30, textvariable=self.address)
        self.regaddress.pack(side=RIGHT)
        Label(frametl4,text="Address:").pack(side=RIGHT)



        frametr1 = Frame(frametr)
        frametr1.pack(fill=BOTH, expand=True)
        self.reglastname = Entry(frametr1, width=30, textvariable=self.lastname)
        self.reglastname.pack(side=RIGHT)
        Label(frametr1,text="Last Name:").pack(side=RIGHT)


        frametr2 = Frame(frametr)
        frametr2.pack(fill=BOTH, expand=True)
        Radiobutton(frametr2, text='MALE', variable=self.gender,value='M').pack(side=RIGHT)
        Radiobutton(frametr2, text='FEMALE', variable=self.gender,value='F').pack(side=RIGHT)
        Label(frametr2,text="    Gender:").pack(side=RIGHT)

        frametr3 = Frame(frametr)
        frametr3.pack(fill=BOTH, expand=True)
        Radiobutton(frametr3, text = "Yes", variable=self.faculty, value = "Y").pack(side=RIGHT)
        Radiobutton(frametr3, text = "No", variable=self.faculty, value = "N").pack(side=RIGHT)
        Label(frametr3,text="       Faculty:").pack(side=RIGHT)



        frametr4 = Frame(frametr)
        frametr4.pack(fill=BOTH, expand=True)
        self.department.set("") # default value
        self.regdepartment= OptionMenu(frametr4, self.department,"","CS","Chem","Math","Engineering","Physics")
        self.regdepartment.pack(side=RIGHT,expand=True,fill=BOTH)
        Label(frametr4,text="Department:").pack(side=RIGHT)




        def createProfile():
            dob = self.dob.get()
            email = self.email.get()
            address = self.address.get()
            username = self.username.get()
            lastname = self.lastname.get()
            firstname = self.firstname.get()
            gender = self.gender.get()
            faculty = self.faculty.get()
            department = self.department.get()

            if dob == '' or \
                            email == '' or \
                            address == '' or \
                            lastname == '' or \
                            firstname == '' or \
                            gender == '' or \
                            faculty == '':

                valid = False
                messagebox.showerror("Missing items.", "Please fill out all forms")

            else:
                if faculty == 'Y' and department == '':
                    valid=False
                    messagebox.showerror("Department is null","Since you are a faculty, please specify a department.")
                else:
                    valid = True

            if len(re.findall('([0-9]{4}-[01][0-9]-[0123][0-9])',dob))!=1:
                valid=False
                messagebox.showerror("Invalid Date","Date of birth must be formatted as YYYY-MM-DD.")

            #Insert info into database, remember .commit()
            if valid:
                c = self.Connect()
                sql = "INSERT INTO Student_Faculty (username, name, email, address, dob, gender, faculty, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                c.execute(sql,(username, firstname + " " + lastname, email, address, dob, gender, faculty, department))
                self.db.commit()
                c.close()

                #confirm registration, hide reg window and present create profile window
                messagebox.showinfo("Success","You have successfully created your profile, please log in.")
                self.clear()
                self.root22.withdraw()
                self.root.deiconify()



        frametr5 = Frame(self.root22)
        frametr5.pack(expand=True,fill=BOTH)
        Button(frametr5,text='Submit',command=createProfile).pack(side=RIGHT)
        Button(frametr5,text='Cancel',command=self.switch22).pack(side=RIGHT)

        self.root22.withdraw()

    def Homepage(self):

        #---variables---#
        self.isbn=StringVar()
        self.title=StringVar()
        self.author=StringVar()

        self.root3 = Toplevel() #creates the 'Homepage' window.
        self.root3.title("GT Library Management System")

        #---menu---#
        self.root3.left = Frame(self.root3,relief=GROOVE,bd=4,pady=2,padx=2) #creates a frame and grounds the frame inside the 'Homepage' window(self.root3)
        self.root3.left.pack(side=LEFT,expand=True,fill=BOTH) #builds it

        self.root3.right = Frame(self.root3)
        self.root3.right.pack(side=LEFT,anchor=N,expand=True,fill=BOTH)

        self.root3.topright=Frame(self.root3.right,relief=GROOVE,bd=4,padx=2,pady=2,)
        self.root3.topright.pack(expand=True,fill=X,anchor=N)
        self.root3.bottomright=Frame(self.root3.right,relief=GROOVE,bd=4,padx=2,pady=2,)
        self.root3.bottomright.pack(side=BOTTOM,expand=True,fill=BOTH)

        Label(self.root3.left,text='CHECK IN/OUT',bg='blue',fg='yellow',font='Helvetica 16').pack(expand=True,fill=X)

        self.root3.one = Frame(self.root3.left)
        self.root3.one.pack()
        Button(self.root3.one, text= 'Return Book',width=20, command=self.switch38).pack(expand=True, fill=BOTH,side=LEFT)
        Button(self.root3.one, text= 'Checkout',width=20, command=self.switch37).pack(expand=True, fill=BOTH,side=LEFT)

        Label(self.root3.left,text='OPTIONS',bg='blue',fg='yellow',font='Helvetica 16').pack(expand=True,fill=X)

        self.root3.two = Frame(self.root3.left)
        self.root3.two.pack()
        Button(self.root3.two, text= 'Request Book Extension',width=20, command=self.switch34).pack(expand=True, fill=BOTH,side=LEFT)
        Button(self.root3.two, text= 'Track Book Location',width=20, command=self.switch36).pack(expand=True, fill=BOTH,side=LEFT)

        self.root3.three = Frame(self.root3.left)
        self.root3.three.pack()
        Button(self.root3.three, text= 'Lost/Damaged Book',width=20, command=self.switch39).pack(expand=True, fill=BOTH,side=LEFT)
        Button(self.root3.three, text= 'Future Hold Request',width=20, command=self.switch35).pack(expand=True, fill=BOTH,side=LEFT)

        Label(self.root3.left,text='REPORTS',bg='blue',fg='yellow',font='Helvetica 16').pack(expand=True,fill=X)

        self.root3.five = Frame(self.root3.left)
        self.root3.five.pack()
        Button(self.root3.five, text= 'Popular Books',width=20, command=self.switch312).pack(expand=True, fill=BOTH,side=LEFT)
        Button(self.root3.five, text= 'Frequent Users', width=20,command=self.switch313).pack(expand=True, fill=BOTH,side=LEFT)

        self.root3.six = Frame(self.root3.left)
        self.root3.six.pack(expand=True,fill=BOTH)
        Button(self.root3.six, text= 'Damaged Books',width=20, command=self.switch314).pack(expand=True, fill=BOTH,side=LEFT)
        Button(self.root3.six, text= 'Popular Subjects',width=20, command=self.switch315).pack(expand=True, fill=BOTH,side=LEFT)

        ##--------------[        SEARCH           ]---------------##
        ##-------------[           BOX           ]----------------##

        self.searchField=StringVar()
        self.searchField.set('')
        self.searchValue=StringVar()
        self.searchValue.set('')

        def bookSearch():
            field = self.searchField.get()
            value = self.searchValue.get()

            if field !='':
                if value !='':
                    c = self.Connect()

                    ##------[ GET (isbn, title, edition, is_book_on_reserve) of every book that matches the search parameters ]-----##
                    sql="SELECT DISTINCT  isbn, title, edition, is_book_on_reserve FROM Book NATURAL JOIN Authors WHERE "+field+" LIKE %s"
                    c.execute(sql, ("%" + value + "%",))

                    books = c.fetchall()
                    self.db.commit()
                    c.close()

                    if len(books)==0:
                        messagebox.showinfo('No Results', 'Your search returned no results, please try again.')
                    else:

                        ##-----[ Check Availability for the books, Pack those results in a tuple of tuples for displaying ]-----##
                        self.allresults = []
                        for book in books:
                            c=self.Connect()
                            sql = 'SELECT COUNT(*) FROM BookCopy NATURAL JOIN Book WHERE isbn = %s AND is_on_hold = %s AND is_checked_out = %s AND is_damaged = %s'
                            c.execute(sql,(str(book[0]),'N','N','0'))
                            self.db.commit()
                            copies_available=c.fetchone()
                            c.close()
                            self.allresults.append((book[0],book[1],book[2],book[3],copies_available[0]))

                        ##----[build the gui to display hold results]----##
                        self.rootsearchresults = Toplevel()
                        gui=self.rootsearchresults

                        #--variables--#
                        gui.sql =self.allresults
                        gui.selection = StringVar()

                        def placehold():

                            #--data grab--#
                            sql ="SELECT copy_num FROM BookCopy NATURAL JOIN Book WHERE isbn = %s AND is_on_hold = 'N' AND is_checked_out = 'N' AND is_damaged = '0' AND is_book_on_reserve = 'N' LIMIT 1;"
                            c = self.Connect()
                            print('gui.selection.get()= '+gui.selection.get())
                            c.execute(sql,(gui.selection.get()))
                            gui.copynum = c.fetchone()
                            gui.copynum = gui.copynum[0]
                            print(gui.copynum)

                            sql="UPDATE BookCopy SET is_on_hold = 'Y' WHERE isbn = %s AND copy_num = %s LIMIT 1;"
                            c.execute(sql,(gui.selection.get(),gui.copynum))
                            self.db.commit()

                            sql="INSERT INTO Issues ( username, isbn, copy_num, date_of_issue, return_date) VALUES (%s,%s, %s, %s, %s)"

                            c.execute(sql,(self.username.get(),gui.selection.get(),gui.copynum, gui.holddate.get(),gui.returndate.get()))
                            self.db.commit()

                            sql="SELECT issue_id FROM Issues WHERE username = %s AND isbn = %s AND copy_num=%s AND date_of_issue = %s"
                            c.execute(sql,(self.username.get(),gui.selection.get(),gui.copynum, gui.holddate.get()))
                            gui.id = c.fetchone()
                            gui.id = gui.id[0]
                            c.close()

                            messagebox.showinfo("Hold Placed!","You have successfully placed a hold on your book. Please record your issues ID for future use: "+str(gui.id))

                            gui.destroy()






                        gui.title('GT Library Management System')
                        gui.header = Label(gui,text='HOLD REQUEST FOR A BOOK',bg='blue',fg='yellow',font='Helvetica 16',width=60)
                        gui.header.pack(expand=True,fill=X)

                        gui.topframe=Frame(gui,pady=15,padx=15,bd=2,relief=FLAT)
                        gui.topframe.pack(expand=True,fill=BOTH)

                        gui.bottomframe=Frame(gui,pady=15,padx=15,bd=2,relief=FLAT)
                        gui.bottomframe.pack(expand=True,fill=BOTH)



                        gui.topheader = Frame(gui.topframe)
                        gui.topheader.pack()
                        gui.headerselect=Label(gui.topheader,width=5,text='SELECT',justify=CENTER,bg='grey',relief=SUNKEN)
                        gui.headerselect.pack(side=LEFT)
                        gui.headerisbn=Label(gui.topheader,width=18,text='ISBN',justify=CENTER,bg='grey',relief=SUNKEN)
                        gui.headerisbn.pack(side=LEFT)
                        gui.headertitle=Label(gui.topheader,width=30,text='TITLE',justify=CENTER,bg='grey',relief=SUNKEN)
                        gui.headertitle.pack(side=LEFT)
                        gui.headeredition=Label(gui.topheader,width=10,text='EDITION',justify=CENTER,bg='grey',relief=SUNKEN)
                        gui.headeredition.pack(side=LEFT)
                        gui.headercopiesavailable=Label(gui.topheader,width=10,text='# AVAILABLE',justify=CENTER,bg='grey',relief=SUNKEN)
                        gui.headercopiesavailable.pack(side=LEFT)

                        created=False;

                        for item in gui.sql:



                            if item[3]=='N':
                                gui.frame=Frame(gui.topframe)
                                gui.frame.pack()
                                Radiobutton(gui.frame,value = item[0],anchor=E,variable=gui.selection,padx=10).pack(side=LEFT,expand=True,fill=Y)
                                Label(gui.frame,width=18,text=str(item[0]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                                Label(gui.frame,width=30,text=str(item[1]),justify=CENTER,wraplength=250,relief=SUNKEN).pack(side=LEFT)
                                Label(gui.frame,width=10,text=str(item[2]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                                Label(gui.frame,width=10,text=str(item[4]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                            else:
                                if created==False:
                                    gui.bottomheader = Frame(gui.bottomframe)
                                    gui.bottomheader.pack()
                                    Label(gui.bottomheader,text='BOOKS ON RESERVE',bg='blue',fg='yellow',font='Helvetica 16',width=60).pack(expand=True,fill=X)
                                    Label(gui.bottomheader,width=18,text='ISBN',justify=CENTER,bg='grey',relief=SUNKEN).pack(side=LEFT)
                                    Label(gui.bottomheader,width=30,text='TITLE',justify=CENTER,bg='grey',relief=SUNKEN).pack(side=LEFT)
                                    Label(gui.bottomheader,width=10,text='EDITION',justify=CENTER,bg='grey',relief=SUNKEN).pack(side=LEFT)
                                    Label(gui.bottomheader,width=10,text='# AVAILABLE',justify=CENTER,bg='grey',relief=SUNKEN).pack(side=LEFT)
                                    created = True

                                gui.frame = Frame(gui.bottomframe)
                                gui.frame.pack()

                                Label(gui.frame,width=18,text=str(item[0]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                                Label(gui.frame,width=30,text=str(item[1]),justify=CENTER,wraplength=250,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                                Label(gui.frame,width=10,text=str(item[2]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                                Label(gui.frame,width=10,text=str(item[4]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)


                        gui.entryframe = Frame(gui.topframe)
                        gui.entryframe.pack()

                        gui.holddate = StringVar()
                        gui.returndate=StringVar()

                        gui.currentdate = clock.datetime.today()
                        gui.holddate.set(str(clock.datetime.strftime(gui.currentdate,'%Y-%m-%d'))) #a string with current date as 'YYYY-MM-DD'

                        gui.currentdateplus17 = clock.datetime.today() + clock.timedelta(days=17)
                        gui.returndate.set(str(clock.datetime.strftime(gui.currentdateplus17,'%Y-%m-%d')))


                        Label(gui.entryframe,text='Hold Request Date :').pack(side=LEFT)
                        gui.holddateentry = Entry(gui.entryframe,bg='grey',textvariable=gui.holddate,width=10)
                        gui.holddateentry.pack(side=LEFT)

                        Label(gui.entryframe,text='Estimated Return Date :').pack(side=LEFT)
                        gui.returndateentry = Entry(gui.entryframe,bg='grey',textvariable=gui.returndate,width=10)
                        gui.returndateentry.pack(side=LEFT)


                        gui.buttonframe = Frame(gui.topframe)
                        gui.buttonframe.pack()
                        gui.cancelButton=Button(gui.buttonframe,text='Return To LMS',pady=15,command=gui.destroy)
                        gui.cancelButton.pack(side=LEFT)
                        gui.submitButton=Button(gui.buttonframe,text='Submit',pady=15,command=placehold)
                        gui.submitButton.pack(side=LEFT)


                else:
                    messagebox.showerror('Input Required','You must enter a search input.')
            else:
                messagebox.showerror('Selection Required','You must select a search field.')


        topone = Frame(self.root3.topright)
        topone.pack(expand=True,fill=BOTH)
        Label(topone,text='SEARCH FOR A BOOK',bg='blue',fg='yellow',font='Helvetica 16').pack(expand=True,fill=X)

        toptwo = Frame(self.root3.topright)
        toptwo.pack(expand=True,fill=BOTH)
        self.getsearchValue = Entry(toptwo, width=30, textvariable=self.searchValue)
        self.getsearchValue.pack()

        topthree = Frame(self.root3.topright)
        topthree.pack(expand=True,fill=BOTH)

        Radiobutton(topthree, text = "ISBN", variable=self.searchField, value = "isbn").pack(side=RIGHT)
        Radiobutton(topthree, text = "TITLE", variable=self.searchField, value = "title").pack(side=RIGHT)
        Radiobutton(topthree, text = "AUTHOR", variable=self.searchField, value = "author_name").pack(side=RIGHT)
        self.searchField.set('ISBN')

        topfour = Frame(self.root3.topright)
        topfour.pack(expand=True,fill=BOTH)
        Button(topfour,text='Search',font='20',command=bookSearch).pack(expand=True,fill=BOTH)

        ##--------------[        LOG OFF           ]---------------##
        ##-------------[           AREA           ]----------------##

        bottomone = Frame(self.root3.bottomright)
        bottomone.pack(expand=True,fill=BOTH,side=BOTTOM)
        Button(bottomone,text='Close LMS',command=self.root.destroy).pack(side=RIGHT,expand=True,fill=BOTH)
        Label(bottomone, image=self.image).pack(side=RIGHT)
        Button(bottomone,text='Log Off',command=self.logoff).pack(side=RIGHT,expand=True,fill=BOTH)

    def Logout(self):
        #closes the Homepage window and returns the
        self.root3.destroy()

        self.root.deiconify()
        pass

    def LoginCheck(self):
        usrname = self.username.get()#get credentials from the login entries
        passwrd = self.password.get()
        self.currentuser = self.username.get()

        #clear out credentials after retrieval
        self.clear2()

        c=self.Connect()#create the database connection object
        sql = "SELECT username, password FROM User WHERE username= %s AND password= %s"
        a = c.execute(sql, (usrname, passwrd))

        contains = False
        if a != 0:
            for item in c:#check all the possible matches for
                if item[0]==usrname:
                    if item[1]==passwrd:
                        contains=True

        if contains:
            messagebox.showinfo("Login Successful", "Welcome to the Library Management System.")
            self.root.withdraw()
            self.Homepage()

        else:
            messagebox.showerror("Login Unsuccessful","Not found, please enter a different username/password")
        c.close()

    #-------GUI Switches-------#
    def switch2122(self):
        self.root21.withdraw()
        self.root22.deiconify()

    def switch22(self):
        self.eraseUser(self.username.get())
        self.clear()
        self.root22.withdraw()
        self.root.deiconify()

    def switch34(self):
        self.root4 = Toplevel()
        gui=self.root4

        #--variables--#
        gui.issueID = StringVar()
        gui.originalcheckoutDate = StringVar()
        gui.currentextensionDate=StringVar()
        gui.currentreturnDate=StringVar()
        gui.newextensionDate=StringVar()
        gui.newestimatedreturnDate = StringVar()

        gui.title('GT Library Management System')
        gui.header = Label(gui,text='REQUEST EXTENSION ON A BOOK',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.frame1=Frame(gui,pady=20,padx=160)
        gui.frame1.pack(expand=True,fill=BOTH)
        gui.submitissueID = Button(gui.frame1,text='Submit',command=gui.issueID.get)
        gui.submitissueID.pack(side=RIGHT)
        gui.getissueID = Entry(gui.frame1,width=18, textvariable=gui.issueID)
        gui.getissueID.pack(side=RIGHT)
        gui.issueIDlabel = Label(gui.frame1,text="Enter your issue ID :")
        gui.issueIDlabel.pack(side=RIGHT)


        gui.line = Label(gui,bg='blue',width=60)
        gui.line.pack(expand=True,fill=X)

        gui.frame2=Frame(gui,pady=5,padx=15)
        gui.frame2.pack(expand=True,fill=BOTH)
        gui.originalcheckoutDatelabel = Label(gui.frame2,text="Original Checkout Date :")
        gui.originalcheckoutDatelabel.pack(side=LEFT)
        gui.getoriginalcheckoutDate = Entry(gui.frame2,width=18, textvariable=gui.originalcheckoutDate)
        gui.getoriginalcheckoutDate.pack(side=LEFT)

        gui.frame3=Frame(gui,pady=5,padx=15)
        gui.frame3.pack(expand=True,fill=BOTH)
        gui.getcurrentreturnDate = Entry(gui.frame3, width=18, textvariable=gui.currentreturnDate)
        gui.getcurrentreturnDate.pack(side=RIGHT)
        gui.currentreturnDatelabel = Label(gui.frame3,text="Current Return Date :")
        gui.currentreturnDatelabel.pack(side=RIGHT)
        gui.currentextensionDatelabel = Label(gui.frame3,text="Current Extension Date :")
        gui.currentextensionDatelabel.pack(side=LEFT)
        gui.getcurrentextensionDate = Entry(gui.frame3, width=18, textvariable=gui.currentextensionDate)
        gui.getcurrentextensionDate.pack(side=LEFT)

        gui.frame4=Frame(gui,pady=5,padx=15)
        gui.frame4.pack(expand=True,fill=BOTH)
        gui.getnewestimatedreturnDate = Entry(gui.frame4, width=13, textvariable=gui.newestimatedreturnDate)
        gui.getnewestimatedreturnDate.pack(side=RIGHT)
        gui.newestimatedreturnDatelabel = Label(gui.frame4,text="New Estimated Return Date :")
        gui.newestimatedreturnDatelabel.pack(side=RIGHT)
        gui.getnewextensionDate = Entry(gui.frame4, width=18, textvariable=gui.newextensionDate)
        gui.getnewextensionDate.pack(side=RIGHT)
        gui.newextensionDatelabel = Label(gui.frame4,text="New Extension Date :")
        gui.newextensionDatelabel.pack(side=RIGHT)


        gui.frame4=Frame(gui,pady=5,padx=15)
        gui.frame4.pack(expand=True,fill=BOTH)
        gui.cancelbutton = Button(gui.frame4,text='Cancel',width=16,command=gui.destroy)
        gui.cancelbutton.pack(side=RIGHT)
        gui.submitbutton = Button(gui.frame4,text='Submit',width=16,command=print(gui.issueID.get()))
        gui.submitbutton.pack(side=RIGHT)

    def switch35(self):
        self.root5 = Toplevel()
        gui=self.root5

        #--variables--#
        gui.isbn = StringVar()
        gui.copyNumber = StringVar()
        gui.expectedAvailableDate=StringVar()

        gui.title('GT Library Management System')
        gui.header = Label(gui,text='FUTURE HOLD REQUEST FOR A BOOK',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.frame1=Frame(gui,pady=15,padx=160)
        gui.frame1.pack(expand=True,fill=BOTH)
        gui.locateIsbn = Button(gui.frame1,text='Request',command=gui.isbn.get)
        gui.locateIsbn.pack(side=RIGHT)
        gui.getIsbn = Entry(gui.frame1,width=18, textvariable=gui.isbn)
        gui.getIsbn.pack(side=RIGHT)
        gui.isbnLabel = Label(gui.frame1,text="ISBN :")
        gui.isbnLabel.pack(side=RIGHT)


        gui.line = Label(gui,bg='blue',width=60)
        gui.line.pack(expand=True,fill=X)

        gui.frame2=Frame(gui,pady=5,padx=15)
        gui.frame2.pack(expand=True,fill=BOTH)
        gui.getcopyNumber = Entry(gui.frame2,width=18,state='readonly',readonlybackground='grey', textvariable=gui.copyNumber)
        gui.getcopyNumber.pack(side=RIGHT)
        gui.copyNumberlabel = Label(gui.frame2,text="Copy Number :")
        gui.copyNumberlabel.pack(side=RIGHT)
        gui.getexpectedAvailableDate = Entry(gui.frame2, width=18,state='readonly',readonlybackground='grey', textvariable=gui.expectedAvailableDate)
        gui.getexpectedAvailableDate.pack(side=RIGHT)
        gui.expectedAvailableDatelabel = Label(gui.frame2,text="Expected Available Date :")
        gui.expectedAvailableDatelabel.pack(side=RIGHT)

        gui.frame3=Frame(gui,pady=5,padx=15)
        gui.frame3.pack(expand=True,fill=BOTH)
        gui.confirmbutton = Button(gui.frame3,text='Confirm',width=16,command=gui.destroy)
        gui.confirmbutton.pack(side=RIGHT)
        gui.cancelbutton = Button(gui.frame3,text='Cancel',width=16,command=gui.destroy)
        gui.cancelbutton.pack(side=RIGHT)

    def switch36(self):
        self.root6 = Toplevel()
        gui=self.root6

        #--variables--#
        gui.isbn = StringVar()
        gui.floorNumber = StringVar()
        gui.shelfNumber=StringVar()
        gui.aisleNumber=StringVar()
        gui.subject=StringVar()

        gui.title('GT Library Management System')
        gui.header = Label(gui,text='TRACK BOOK LOCATION',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.frame1=Frame(gui,pady=15,padx=160)
        gui.frame1.pack(expand=True,fill=BOTH)
        gui.locateIsbn = Button(gui.frame1,text='Locate',command=gui.isbn.get)
        gui.locateIsbn.pack(side=RIGHT)
        gui.getIsbn = Entry(gui.frame1,width=18, textvariable=gui.isbn)
        gui.getIsbn.pack(side=RIGHT)
        gui.isbnLabel = Label(gui.frame1,text="ISBN :")
        gui.isbnLabel.pack(side=RIGHT)


        gui.line = Label(gui,bg='blue',width=60)
        gui.line.pack(expand=True,fill=X)

        gui.frame2=Frame(gui,pady=5,padx=15)
        gui.frame2.pack(expand=True,fill=BOTH)
        gui.floorNumberlabel = Label(gui.frame2,text="Floor Number :")
        gui.floorNumberlabel.pack(side=LEFT)
        gui.getfloorNumber = Entry(gui.frame2,width=18, textvariable=gui.floorNumber)
        gui.getfloorNumber.pack(side=LEFT)
        gui.getshelfNumber = Entry(gui.frame2, width=18, textvariable=gui.shelfNumber)
        gui.getshelfNumber.pack(side=RIGHT)
        gui.shelfNumberlabel = Label(gui.frame2,text="Shelf Number :")
        gui.shelfNumberlabel.pack(side=RIGHT)


        gui.frame3=Frame(gui,pady=5,padx=15)
        gui.frame3.pack(expand=True,fill=BOTH)
        gui.getSubject = Entry(gui.frame3, width=18, textvariable=gui.subject)
        gui.getSubject.pack(side=RIGHT)
        gui.subjectlabel = Label(gui.frame3,text="Subject :")
        gui.subjectlabel.pack(side=RIGHT)
        gui.aisleNumberlabel = Label(gui.frame3,text="Aisle Number :")
        gui.aisleNumberlabel.pack(side=LEFT)
        gui.getaisleNumber = Entry(gui.frame3, width=18, textvariable=gui.aisleNumber)
        gui.getaisleNumber.pack(side=LEFT)



        gui.frame4=Frame(gui,pady=5,padx=15)
        gui.frame4.pack(expand=True,fill=BOTH)
        gui.cancelbutton = Button(gui.frame4,text='Cancel/Back',width=16,command=gui.destroy)
        gui.cancelbutton.pack(side=RIGHT)

    def switch37(self):
        self.root7 = Toplevel()
        gui=self.root7

        #--variables--#
        gui.isbn = StringVar()
        gui.copyNumber = StringVar()
        gui.userName=StringVar()
        gui.checkoutDate=StringVar()
        gui.estimatedreturnDate=StringVar()

        gui.title('GT Library Management System')
        gui.header = Label(gui,text='Book Checkout',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.frame1=Frame(gui,pady=5,padx=15)
        gui.frame1.pack(expand=True,fill=BOTH)
        gui.getcopyNumber = Entry(gui.frame1, width=15, textvariable=gui.copyNumber)
        gui.getcopyNumber.pack(side=RIGHT)
        gui.copynumberlabel = Label(gui.frame1,text="Copy Number :").pack(side=RIGHT)
        gui.isbnlabel = Label(gui.frame1,text="            ISBN :").pack(side=LEFT)
        gui.getisbn = Entry(gui.frame1, width=20, textvariable=gui.isbn)
        gui.getisbn.pack(side=LEFT)


        gui.frame2=Frame(gui,pady=5,padx=15)
        gui.frame2.pack(expand=True,fill=BOTH)
        gui.getuserName = Entry(gui.frame2, width=15, textvariable=gui.userName)
        gui.getuserName.pack(side=RIGHT)
        gui.usernamelabel = Label(gui.frame2,text="Username :").pack(side=RIGHT)

        gui.frame3=Frame(gui,pady=5,padx=15)
        gui.frame3.pack(expand=True,fill=BOTH)
        gui.getestimatedreturnDate = Entry(gui.frame3, width=15, textvariable=gui.checkoutDate)
        gui.getestimatedreturnDate.pack(side=RIGHT)
        gui.estimatedreturnDatelabel = Label(gui.frame3,text="        Estimated Return Date :").pack(side=RIGHT)
        gui.checkoutDate = Label(gui.frame3,text="Checkout Date :").pack(side=LEFT)
        gui.getcheckoutDate = Entry(gui.frame3, width=20, textvariable=gui.checkoutDate)
        gui.getcheckoutDate.pack(side=LEFT)

        gui.frame4=Frame(gui,pady=5,padx=15)
        gui.frame4.pack(expand=True,fill=BOTH)
        gui.cancelbutton = Button(gui.frame4,text='Cancel',width=16,command=gui.destroy).pack(side=RIGHT)
        gui.returnbutton = Button(gui.frame4,text='Checkout',width=16,command=print(gui.isbn.get())).pack(side=RIGHT)

    def switch38(self):
        self.root8 = Toplevel()
        gui=self.root8

        #--variables--#
        gui.isbn = StringVar()
        gui.copyNumber = StringVar()
        gui.damaged=StringVar()
        gui.userName=StringVar()

        def query():
            sql1='UPDATE Issues SET return_date=GETDATE() WHERE isbn=%s AND copynumber=%s AND username=%s'
            sql2='UPDATE BookCopy SET is_checked_out=%s WHERE isbn=%s AND copy=%s'


        gui.title('GT Library Management System')
        gui.header = Label(gui,text='RETURN BOOK',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.frame1=Frame(gui,pady=5,padx=15)
        gui.frame1.pack(expand=True,fill=BOTH)
        gui.getcopyNumber = Entry(gui.frame1, width=15, textvariable=gui.copyNumber)
        gui.getcopyNumber.pack(side=RIGHT)
        gui.copynumberlabel = Label(gui.frame1,text="Copy Number :").pack(side=RIGHT)
        gui.isbnlabel = Label(gui.frame1,text="ISBN :").pack(side=LEFT)
        gui.getisbn = Entry(gui.frame1, width=20, textvariable=gui.isbn)
        gui.getisbn.pack(side=LEFT)

        gui.frame2=Frame(gui,pady=5,padx=15)
        gui.frame2.pack(expand=True,fill=BOTH)
        gui.getdamaged = Entry(gui.frame2, width=15, textvariable=gui.damaged)
        gui.getdamaged.pack(side=RIGHT)
        gui.damagedlabel = Label(gui.frame2,text="Damaged ? :").pack(side=RIGHT)

        gui.frame3=Frame(gui,pady=5,padx=15)
        gui.frame3.pack(expand=True,fill=BOTH)
        gui.getuserName = Entry(gui.frame3, width=15, textvariable=gui.userName)
        gui.getuserName.pack(side=RIGHT)
        gui.usernamelabel = Label(gui.frame3,text="Username :").pack(side=RIGHT)

        gui.frame4=Frame(gui,pady=5,padx=15)
        gui.frame4.pack(expand=True,fill=BOTH)
        gui.cancelbutton = Button(gui.frame4,text='Cancel',width=16,command=gui.destroy).pack(side=RIGHT)
        gui.returnbutton = Button(gui.frame4,text='Return',width=16,command=print(gui.query())).pack(side=RIGHT)

    def switch39(self):
        self.root9 = Toplevel()
        gui=self.root9

        #--variables--#
        gui.isbn = StringVar()
        gui.copyNumber = StringVar()
        gui.currentTime=StringVar()
        gui.lastUser = StringVar()
        gui.amount = StringVar()

        gui.title('GT Library Management System')
        gui.header = Label(gui,text='LOST/DAMAGED BOOK',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.frame1=Frame(gui,pady=15,padx=15)
        gui.frame1.pack(expand=True,fill=BOTH)

        gui.getcopyNumber = Entry(gui.frame1,width=10, textvariable=gui.copyNumber)
        gui.getcopyNumber.pack(side=RIGHT)
        gui.copyNumberlabel = Label(gui.frame1,text="    Copy Number :")
        gui.copyNumberlabel.pack(side=RIGHT)
        gui.getIsbn = Entry(gui.frame1,width=18, textvariable=gui.isbn)
        gui.getIsbn.pack(side=RIGHT)
        gui.isbnLabel = Label(gui.frame1,text="ISBN :")
        gui.isbnLabel.pack(side=RIGHT)

        gui.frame2=Frame(gui,padx=15)
        gui.frame2.pack(expand=True,fill=BOTH)
        gui.isbnLabel = Label(gui.frame2,text='      Current Time :')
        gui.isbnLabel.pack(side=LEFT)
        gui.getcurrentTime = Entry(gui.frame2,width=18, textvariable=gui.currentTime,state='readonly',readonlybackground='grey')
        gui.getcurrentTime.pack(side=LEFT)

        gui.frame3=Frame(gui,pady=15)
        gui.frame3.pack()
        gui.lastUserButton = Button(gui.frame3,text='Get Last User',command=gui.lastUser.get)
        gui.lastUserButton.pack()


        gui.line = Label(gui,bg='blue',width=60)
        gui.line.pack(expand=True,fill=X)

        gui.frame4=Frame(gui,pady=5,padx=15)
        gui.frame4.pack(expand=True,fill=BOTH)
        gui.getlastUserlabel = Label(gui.frame4,text="  Last User of the Book :")
        gui.getlastUserlabel.pack(side=LEFT)
        gui.getlastUser = Entry(gui.frame4, width=18,state='readonly',readonlybackground='grey', textvariable=gui.lastUser)
        gui.getlastUser.pack(side=LEFT)

        gui.frame5=Frame(gui,pady=5,padx=15)
        gui.frame5.pack(expand=True,fill=BOTH)
        gui.getamountlabel = Label(gui.frame5,text="Amount to be charged :")
        gui.getamountlabel.pack(side=LEFT)
        gui.getamount = Entry(gui.frame5, width=18, textvariable=gui.amount)
        gui.getamount.pack(side=LEFT)

        gui.frame6=Frame(gui,pady=5,padx=15)
        gui.frame6.pack(expand=True,fill=BOTH)
        gui.submitbutton = Button(gui.frame6,text='Submit',width=16,command=gui.destroy)
        gui.submitbutton.pack(side=RIGHT)
        gui.cancelbutton = Button(gui.frame6,text='Cancel',width=16,command=gui.destroy)
        gui.cancelbutton.pack(side=RIGHT)

    def switch312(self):
        self.root12 = Toplevel()
        gui=self.root12

        #--variables--#
        gui.sql ="SELECT * FROM PopularBookReport WHERE Month = '1' OR Month = '2' ORDER BY Month ASC, number DESC LIMIT 6"

        c = self.Connect()
        c.execute(gui.sql)
        gui.report = c.fetchall()
        c.close()

        gui.title('GT Library Management System')
        gui.header = Label(gui,text='POPULAR BOOKS REPORT',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.mainframe=Frame(gui,pady=15,padx=15)
        gui.mainframe.pack(expand=True,fill=BOTH)

        gui.header = Frame(gui.mainframe)
        gui.header.pack()
        gui.headermonth=Label(gui.header,width=10,text='MONTH',justify=CENTER,bg='grey',relief=SUNKEN)
        gui.headermonth.pack(side=LEFT)
        gui.headertitle=Label(gui.header,width=30,text='TITLE',justify=CENTER,bg='grey',relief=SUNKEN)
        gui.headertitle.pack(side=LEFT)
        gui.headercheckouts=Label(gui.header,width=10,text='# CHECKOUTS',justify=CENTER,bg='grey',relief=SUNKEN)
        gui.headercheckouts.pack(side=LEFT)

        for item in gui.report:
            gui.frame=Frame(gui.mainframe)
            gui.frame.pack()
            Label(gui.frame,width=10,text=str(item[0]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
            Label(gui.frame,width=30,text=str(item[1]),justify=CENTER,wraplength=250,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
            Label(gui.frame,width=10,text=str(item[2]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)

        gui.cancelButton=Button(gui.mainframe,text='Return To LMS',pady=15,command=gui.destroy)
        gui.cancelButton.pack(side=BOTTOM)

    def switch313(self):

        #--data grab--#
        sql ="SELECT * FROM FrequentUserReport WHERE (Month = '1' OR Month = '2')AND numCheckout>=10  ORDER BY Month ASC, numCheckout DESC LIMIT 10"

        c = self.Connect()
        c.execute(sql)
        report = c.fetchall()
        print(report)
        c.close()
        print(len(report))

        if len(report)==0:
            messagebox.showwarning('Report Unavailable','There are no frequent users to report.')
        else:
            self.root13 = Toplevel()
            gui=self.root13
            gui.report=report
            gui.title('GT Library Management System')
            gui.header = Label(gui,text='FREQUENT USERS REPORT',bg='blue',fg='yellow',font='Helvetica 16',width=60)
            gui.header.pack(expand=True,fill=X)

            gui.mainframe=Frame(gui,pady=15,padx=15)
            gui.mainframe.pack(expand=True,fill=BOTH)

            gui.header = Frame(gui.mainframe)
            gui.header.pack()
            gui.headermonth=Label(gui.header,width=10,text='MONTH',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headermonth.pack(side=LEFT)
            gui.headertitle=Label(gui.header,width=30,text='USERNAME',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headertitle.pack(side=LEFT)
            gui.headercheckouts=Label(gui.header,width=10,text='# CHECKOUTS',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headercheckouts.pack(side=LEFT)

            for item in gui.report:
                gui.frame=Frame(gui.mainframe)
                gui.frame.pack()
                Label(gui.frame,width=10,text=str(item[0]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                Label(gui.frame,width=30,text=str(item[1]),justify=CENTER,wraplength=250,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                Label(gui.frame,width=10,text=str(item[2]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)

            gui.cancelButton=Button(gui.mainframe,text='Return To LMS',pady=15,command=gui.destroy)
            gui.cancelButton.pack(side=BOTTOM)

    def switch314(self):
        self.root14 = Toplevel()
        gui=self.root14



        def showReport():
            report = [];

            #--data grab--#
            gui.m = self.month2num(gui.month.get());

            sql ="SELECT (Subject,number) FROM DamagedBookReport WHERE Month = %s AND Subject = %s"

            print(gui.m)
            print(gui.subject1.get())

            c = self.Connect()
            c.execute(sql,(gui.m,gui.subject1.get()))
            report.append(c.fetchall())

            c.execute(sql,(gui.m,gui.subject2.get()))
            report.append(c.fetchall())

            c.execute(sql,(gui.m,gui.subject3.get()))
            report.append(c.fetchall())

            print(report)
            c.close()
            print(len(report))

            gui.mainframebottom=Frame(gui,pady=15,padx=15)
            gui.mainframebottom.pack(expand=True,fill=BOTH)

            gui.header = Frame(gui.mainframebottom)
            gui.header.pack()
            gui.headermonth=Label(gui.header,width=10,text='MONTH',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headermonth.pack(side=LEFT)
            gui.headertitle=Label(gui.header,width=10,text='SUBJECT',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headertitle.pack(side=LEFT)
            gui.headercheckouts=Label(gui.header,width=10,text='# DAMAGED',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headercheckouts.pack(side=LEFT)

            for item in report:
                gui.frame=Frame(gui.mainframebottom)
                gui.frame.pack()

                Label(gui.frame,width=10,text=str(item[0]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                Label(gui.frame,width=10,text=str(item[1]),justify=CENTER,wraplength=250,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                Label(gui.frame,width=10,text=str(item[2]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)

            gui.cancelButton=Button(gui.mainframebottom,text='Return To LMS',pady=15,command=gui.destroy)
            gui.cancelButton.pack(side=BOTTOM)


        gui.title('GT Library Management System')
        gui.header = Label(gui,text='DAMAGED BOOKS REPORT',bg='blue',fg='yellow',font='Helvetica 16',width=60)
        gui.header.pack(expand=True,fill=X)

        gui.mainframetop=Frame(gui,pady=15,padx=15)
        gui.mainframetop.pack(expand=True,fill=BOTH)

        gui.mainframemiddle=Frame(gui,pady=15,padx=15)
        gui.mainframemiddle.pack(expand=True,fill=BOTH)

        gui.topframe1 = Frame(gui.mainframetop)
        gui.topframe1.pack()

        Label(gui.topframe1,text="SUBJECT",padx=5).pack(side=LEFT)
        gui.subject1 = StringVar()
        gui.subject1.set("")# default value
        gui.selectsubject1 = OptionMenu(gui.topframe1, gui.subject1,"         ","Business","Children","Computer","Law","Science")
        gui.selectsubject1.config(width=10)
        gui.selectsubject1.pack(side=LEFT,expand=True,fill=BOTH)

        Label(gui.topframe1,text="SUBJECT",padx=5).pack(side=LEFT)
        gui.subject2 = StringVar()
        gui.subject2.set("")# default value
        gui.selectsubject2 = OptionMenu(gui.topframe1, gui.subject2,"         ","Business","Children","Computer","Law","Science")
        gui.selectsubject2.config(width=10)
        gui.selectsubject2.pack(side=LEFT,expand=True,fill=BOTH)

        Label(gui.topframe1,text="SUBJECT",padx=5).pack(side=LEFT)
        gui.subject3 = StringVar()
        gui.subject3.set("")# default value
        gui.selectsubject3 = OptionMenu(gui.topframe1, gui.subject3,"         ","Business","Children","Computer","Law","Science")
        gui.selectsubject3.config(width=10)
        gui.selectsubject3.pack(side=LEFT,expand=True,fill=BOTH)

        gui.topframe2 = Frame(gui.mainframetop)
        gui.topframe2.pack()

        Label(gui.topframe2,text="MONTH",padx=5).pack(side=LEFT)
        gui.month = StringVar()
        gui.month.set("")# default value
        gui.selectmonth = OptionMenu(gui.topframe2, gui.month,'          ','Janurary','February','March','April','May','June','July','August','September','October','November','December')
        gui.selectmonth.config(width=10)
        gui.selectmonth.pack(side=LEFT,expand=True,fill=BOTH)

        Button(gui.mainframemiddle,text='Show Report',pady=15,command=showReport).pack(side=BOTTOM)

    def switch315(self):
        #--data grab--#
        sql ="SELECT * FROM PopularSubjectReport WHERE Month = '1' OR Month = '2' ORDER BY Month ASC, num_checkout DESC LIMIT 6"

        c = self.Connect()
        c.execute(sql)
        report = c.fetchall()
        c.close()
        if len(report)==0:
            messagebox.showwarning('Report Unavailable','There is not enough data to compile a report.')
        else:
            self.root15 = Toplevel()
            gui=self.root15
            gui.report=report
            gui.title('GT Library Management System')
            gui.header = Label(gui,text='POPULAR SUBJETS REPORT',bg='blue',fg='yellow',font='Helvetica 16',width=60)
            gui.header.pack(expand=True,fill=X)

            gui.mainframe=Frame(gui,pady=15,padx=15)
            gui.mainframe.pack(expand=True,fill=BOTH)

            gui.header = Frame(gui.mainframe)
            gui.header.pack()
            gui.headermonth=Label(gui.header,width=20,text='MONTH',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headermonth.pack(side=LEFT)
            gui.headertitle=Label(gui.header,width=20,text='SUBJECT',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headertitle.pack(side=LEFT)
            gui.headercheckouts=Label(gui.header,width=20,text='# CHECKOUTS',justify=CENTER,bg='grey',relief=SUNKEN)
            gui.headercheckouts.pack(side=LEFT)

            for item in gui.report:
                gui.frame=Frame(gui.mainframe)
                gui.frame.pack()
                Label(gui.frame,width=20,text=str(item[0]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                Label(gui.frame,width=20,text=str(item[1]),justify=CENTER,wraplength=250,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)
                Label(gui.frame,width=20,text=str(item[2]),justify=CENTER,relief=SUNKEN).pack(side=LEFT,expand=True,fill=Y)

            gui.cancelButton=Button(gui.mainframe,text='Return To LMS',pady=15,command=gui.destroy)
            gui.cancelButton.pack(side=BOTTOM)

    #-------random functions------#

    def clear(self):
        self.lastname.set("")
        self.username.set("")
        self.password.set("")
        self.confirmpassword.set("")

    def clear2(self):
        self.lastname.set("")
        self.password.set("")
        self.confirmpassword.set("")

    def RegisterNew(self):

        valid = True
        #get register entries and put them into database
        username = self.username.get()
        password = self.password.get()
        confirmpassword = self.confirmpassword.get()



        #make sure username/password entries have values
        if username=='' or password=='' or confirmpassword=='':
            valid = False
            messagebox.showerror("Missing items.", "You must specify a username, password, and confirm password. ")

        else:
            if len(username)>30:
                valid=False
                messagebox.showerror("Invalid Username","Username too long. Must be 30 characters or less.")
            else:
                #make sure password has one upper case letter and one number
                if True:
                    #check to make sure passwords match
                    if password != confirmpassword:
                        valid = False
                        messagebox.showerror("Password error", "Password and confirm password must match.")
                    else:
                        #check for a duplicate username in the database
                        c=self.Connect()
                        sql = "SELECT * FROM User WHERE Username= %s"
                        a= c.execute(sql,username)
                        if a>0:
                            valid=False
                            messagebox.showerror("Username taken", "Please select another username...")
        #Insert info into database, remember .commit()
        if valid:
            c = self.Connect()
            sql = "INSERT INTO User (username, password) VALUES (%s, %s)"
            c.execute(sql,(username, password))
            self.db.commit()
            c.close()

            #confirm registration, hide reg window and present create profile window
            messagebox.showinfo("Success","You have successfully registered you must now create a profile.")
            self.root21.withdraw()
            self.root22.deiconify()

    def switch(self):
        self.clear2()
        self.root.withdraw()
        self.root21.deiconify()

    def Connect(self):
        #this points to the connection object, this way we can get a cursor from db.cursor()
        try:
            self.db = pymysql.connect(
                db='cs4400_Group_60',
                user='cs4400_Group_60',
                passwd='XoYOzC_l',
                host='academic-mysql.cc.gatech.edu'
            )
            c=self.db.cursor()
            return c
        except:
            messagebox.showerror("No connection!", "Can't connect to the database. Please check the internet connection.(If you're not on GTwifi, is your VPN running?)")
            return None
    def logoff(self):
        self.root3.destroy()
        self.clear()

    def eraseUser(self,x):
        username = x
        c = self.Connect()
        sql = "DELETE FROM User WHERE Username = %s"
        c.execute(sql,(username))
        print(c.fetchone)
        self.db.commit()
        c.close()

    def month2num(self,x):
        table = (('1','January'),('2','February'),('3','March'),('4','April'),('5','May'),('6','June'),('7','July'),('8','August'),('9','September'),('10','October'),('11','November'),('12','December'));
        for item in table:
            if x==item[1]:
                return item[0];

win = Tk()
app = Gateway(win)
win.mainloop()
