import mysql.connector
from tkinter import *
import tkinter.messagebox
import datetime

objls = []

db = mysql.connector.connect(
    host="localhost",
    user="jared",
    password="Bcps2008!",
    database="librarydatabase"
)

mycursor = db.cursor()


# USERINFO TABLE NAME IS Userinfo (username, password)
# BORROWEDBOOKS TABLE NAME IS Borrowedbooks (username, title, author, dateborrowed, duedate, BookID)


def startscreen():
    global screen

    screen = Tk()
    screen.title("Library")
    screen.geometry("646x800")
    screen.resizable(False, False)

    drawstartscreen()

    screen.mainloop()


def drawstartscreen():
    screenreset()

    l1 = Label(screen, text="Please Login or Register to system", font="calibri, 20", bg="grey", width=40, height=2)
    l1.grid(row=1, column=1, columnspan=5)
    objls.append(l1)
    l2 = Label(screen, text="", height=10)
    l2.grid(row=2, column=3)
    objls.append(l2)
    b1 = Button(screen, text="Login", font="calibri, 20", width=7, command=lambda: loginscreen())
    b1.grid(row=3, column=3)
    objls.append(b1)
    l3 = Label(screen, text="", height=5)
    l3.grid(row=4, column=3)
    objls.append(l3)
    b2 = Button(screen, text="Register", font="calibri, 20", command=lambda: registerscreen())
    b2.grid(row=5, column=3)
    objls.append(b2)


def screenreset():
    for x in objls:
        x.destroy()


def registerscreen():
    usernameentry = StringVar()
    passwordentry = StringVar()

    screenreset()

    # DRAW REGISTER SCREEN
    l1 = Label(screen, text="Please enter credentials below", font="calibri, 20", width=40, height=2, bg="grey")
    l1.grid(row=1, column=1, columnspan=5)
    objls.append(l1)
    l2 = Label(screen, text="", height=5)
    l2.grid(row=2, column=3)
    objls.append(l2)

    l3 = Label(screen, text="Username: ", font="calibri, 15")
    l3.grid(row=3, column=2)
    objls.append(l3)
    e1 = Entry(screen, textvariable=usernameentry, width=60)
    e1.grid(row=3, column=3, columnspan=2)
    objls.append(e1)

    l4 = Label(screen, text="", height=3)
    l4.grid(row=4, column=3)
    objls.append(l4)

    l5 = Label(screen, text="Password: ", font="calibri, 15")
    l5.grid(row=5, column=2)
    objls.append(l5)
    e2 = Entry(screen, textvariable=passwordentry, width=60)
    e2.grid(row=5, column=3, columnspan=2)
    objls.append(e2)

    l6 = Label(screen, text="", height=3)
    l6.grid(row=6, column=3)
    objls.append(l6)

    b1 = Button(screen, text="Register", font="calibri, 15", width=7,
                command=lambda: registeruser(usernameentry, passwordentry))
    b1.grid(row=7, column=1, columnspan=5)
    objls.append(b1)

    l7 = Label(screen, text="", height=20)
    l7.grid(row=8, column=3)
    objls.append(l7)

    b2 = Button(screen, text="Back", font="calibri, 12", command=lambda: drawstartscreen())
    b2.grid(row=9, column=1, columnspan=5)
    objls.append(b2)


def registeruser(usernameentry, passwordentry):
    global username

    username = usernameentry.get()
    password = passwordentry.get()

    search = ""
    entry = f"('{username}',)"
    usercredentials = (f"{username}", f"{password}")

    run = True
    while run:
        if len(username) <= 5 or len(password) <= 5:
            tkinter.messagebox.showinfo("ERROR", "Both username and password must be more than 5 characters long!")
            return 0
        else:
            mycursor.execute(f"SELECT username FROM Userinfo WHERE username = '{username}'")
            break

    for x in mycursor:
        search = str(x)

    if entry == search:
        tkinter.messagebox.showinfo("ERROR", "User already exists!")
        return 0

    else:
        mycursor.execute("INSERT INTO Userinfo (username, password) VALUES (%s, %s)", usercredentials)
        db.commit()

        tkinter.messagebox.showinfo("", "Registration Successful! You will now be logged into your account.")

        mycursor.execute("SELECT * FROM Userinfo")
        for x in mycursor:
            print(x)

        mainscreen()


def loginscreen():
    screenreset()

    usernameentry = StringVar()
    passwordentry = StringVar()

    # DRAW LOGIN SCREEN
    l1 = Label(screen, text="Please enter credentials below", font="calibri, 20", width=40, height=2, bg="grey")
    l1.grid(row=1, column=1, columnspan=5)
    objls.append(l1)
    l2 = Label(screen, text="", height=5)
    l2.grid(row=2, column=3)
    objls.append(l2)

    l3 = Label(screen, text="Username: ", font="calibri, 15")
    l3.grid(row=3, column=2)
    objls.append(l3)
    e1 = Entry(screen, textvariable=usernameentry, width=60)
    e1.grid(row=3, column=3, columnspan=2)
    objls.append(e1)

    l4 = Label(screen, text="", height=3)
    l4.grid(row=4, column=3)
    objls.append(l4)

    l5 = Label(screen, text="Password: ", font="calibri, 15")
    l5.grid(row=5, column=2)
    objls.append(l5)
    e2 = Entry(screen, textvariable=passwordentry, width=60)
    e2.grid(row=5, column=3, columnspan=2)
    objls.append(e2)

    l6 = Label(screen, text="", height=3)
    l6.grid(row=6, column=3)
    objls.append(l6)

    b1 = Button(screen, text="Login", font="calibri, 15", width=7,
                command=lambda: verifylogincredentials(usernameentry, passwordentry))
    b1.grid(row=7, column=1, columnspan=5)
    objls.append(b1)

    l7 = Label(screen, text="", height=20)
    l7.grid(row=8, column=3)
    objls.append(l7)

    b2 = Button(screen, text="Back", font="calibri, 12", command=lambda: drawstartscreen())
    b2.grid(row=9, column=1, columnspan=5)
    objls.append(b2)


def verifylogincredentials(usernameentry, passwordentry):
    global username

    username = usernameentry.get()
    password = passwordentry.get()

    search = ""
    entry = f"('{username}', '{password}')"

    if len(username) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo("ERROR", "Please key in your details!")
        return 0
    else:
        mycursor.execute(f"SELECT username, password FROM Userinfo WHERE username = '{username}'")
        for x in mycursor:
            search = str(x)
        if entry == search:
            tkinter.messagebox.showinfo("", "Login Successful!")
            mainscreen()
        else:
            tkinter.messagebox.showinfo("ERROR", "Login Failed... Please try again.")
            return 0


def mainscreen():
    screenreset()

    # DRAW MAIN SCREEN
    mainscreenborrowedbookdisplay()
    mainscreenduebookdisplay()
    mainscreenbuttons()

    datelabel = Label(screen, text=f"Today's Date: {datetime.date.today()}    ", font="calibri, 9", width=92, bg="black", fg="white", anchor="e")
    datelabel.place(x=0, y=0)

    userlabel = Label(screen, text=f" Logged in as: {username}", font="calibri, 9", width=40, bg="black", fg="white", anchor="w")
    userlabel.place(x=0, y=0)


def mainscreenborrowedbookdisplay():
    global lb1, lb2, lb3, lb4, borrowedlist

    mycursor.execute("SELECT * FROM Borrowedbooks ORDER BY duedate DESC, BookID ASC")

    borrowresult = mycursor.fetchall()
    borrowedlist = []
    btitlels = []
    bauthorls = []
    bbookidls = []
    bduedatels = []

    for i in range(len(borrowresult)):
        if username in borrowresult[i]:
            borrowedlist.append(borrowresult[i])

    for i in range(len(borrowedlist)):
        btitlels.append(borrowedlist[i][1])
        bauthorls.append(borrowedlist[i][2])
        bduedatels.append(borrowedlist[i][4])
        bbookidls.append(borrowedlist[i][5])

    bgl = Label(screen, width=90, height=60, bg="black")
    bgl.place(x=0, y=46)
    objls.append(bgl)

    l1 = Label(screen, text="", width=15, height=70, bg="grey")
    l1.place(x=540, y=20)
    objls.append(l1)

    l2 = Label(screen, text="Books Borrowed:", font="calibri, 15", width=49, height=1, bg="grey", anchor="w")
    l2.place(x=0, y=20)
    objls.append(l2)

    # TITLE
    l3 = Label(screen, text="Title:", font="calibri, 13", width=25, height=1, bg="grey", anchor="w")
    l3.place(x=0, y=48)
    objls.append(l3)

    lb1 = Listbox(screen, font="calibri, 12", width=22, height=18)
    lb1.place(x=0, y=74)
    objls.append(lb1)
    for i in range(len(btitlels)):
        lb1.insert(END, btitlels[i])

    sb1 = Scrollbar(screen, orient="vertical")
    sb1.place(x=204, y=74, relheight=0.455)
    objls.append(sb1)

    sb2 = Scrollbar(screen, orient="horizontal")
    sb2.place(x=0, y=421, relwidth=0.312)
    objls.append(sb2)

    lb1.config(yscrollcommand=sb1.set)
    sb1.config(command=borrowdisplayscroll)

    lb1.config(xscrollcommand=sb2.set)
    sb2.config(command=lb1.xview)

    # AUTHOR
    l4 = Label(screen, text="Author:", font="calibri, 13", width=13, height=1, bg="grey", anchor="w")
    l4.place(x=223, y=48)
    objls.append(l4)

    lb2 = Listbox(screen, font="calibri, 12", width=11, height=18)
    lb2.place(x=223, y=74)
    objls.append(lb2)

    for i in range(len(bauthorls)):
        lb2.insert(END, bauthorls[i])

    lb2.config(yscrollcommand=sb1.set)

    sb3 = Scrollbar(screen, orient="horizontal")
    sb3.place(x=223, y=421, relwidth=0.488)
    objls.append(sb3)

    lb2.config(xscrollcommand=sb3.set)
    sb3.config(command=lb2.xview)

    # BOOK ID
    l5 = Label(screen, text="Book ID:", font="calibri, 13", width=13, height=1, bg="grey", anchor="w")
    l5.place(x=329, y=48)
    objls.append(l5)

    lb3 = Listbox(screen, font="calibri, 12", width=12, height=18)
    lb3.place(x=329, y=74)
    objls.append(lb3)

    for i in range(len(bbookidls)):
        lb3.insert(END, bbookidls[i])

    lb3.config(yscrollcommand=sb1.set)

    # DUE DATE
    l6 = Label(screen, text="Due Date:", font="calibri, 13", width=10, height=1, bg="grey", anchor="w")
    l6.place(x=444, y=48)
    objls.append(l6)

    lb4 = Listbox(screen, font="calibri, 12", width=10, height=18)
    lb4.place(x=444, y=74)
    objls.append(lb4)

    for i in range(len(bduedatels)):
        lb4.insert(END, bduedatels[i])

    lb4.config(yscrollcommand=sb1.set)


def borrowdisplayscroll(*args):
    global lb1, lb2, lb3, lb4

    lb1.yview(*args)
    lb2.yview(*args)
    lb3.yview(*args)
    lb4.yview(*args)


def mainscreenduebookdisplay():
    global lb5, lb6, lb7, lb8, duelist

    currentdate = datetime.date.today()

    mycursor.execute(f"SELECT title, author, BookID, duedate FROM Borrowedbooks where username = '{username}' ORDER BY duedate DESC, BookID ASC")

    dueresult = mycursor.fetchall()
    duelist = []
    dtitlels = []
    dauthorls = []
    dbookidls = []
    dduedatels = []

    for i in range(len(dueresult)):
        duedate = dueresult[i][3]
        if duedate <= currentdate:
            duelist.append(dueresult[i])

    for i in range(len(duelist)):
        dtitlels.append(duelist[i][0])
        dauthorls.append(duelist[i][1])
        dduedatels.append(duelist[i][3])
        dbookidls.append(duelist[i][2])

    l7 = Label(screen, text="Books Due:", font="calibri, 15", width=49, height=1, bg="grey", anchor="w")
    l7.place(x=0, y=439)
    objls.append(l7)

    # TITLE
    l8 = Label(screen, text="Title:", font="calibri, 13", width=25, height=1, bg="grey", anchor="w")
    l8.place(x=0, y=467)
    objls.append(l8)

    lb5 = Listbox(screen, font="calibri, 12", width=22, height=15)
    lb5.place(x=0, y=493)
    for i in range(len(dtitlels)):
        lb5.insert(END, dtitlels[i])
    objls.append(lb5)

    sb4 = Scrollbar(screen)
    sb4.place(x=204, y=493, relheight=0.384)
    objls.append(sb4)

    sb5 = Scrollbar(screen, orient="horizontal")
    sb5.place(x=0, y=783, relwidth=0.312)
    objls.append(sb5)

    lb5.config(yscrollcommand=sb4.set)
    sb4.config(command=duedisplayscroll)

    lb5.config(xscrollcommand=sb5.set)
    sb5.config(command=lb5.xview)

    # AUTHOR
    l9 = Label(screen, text="Author:", font="calibri, 13", width=13, height=1, bg="grey", anchor="w")
    l9.place(x=223, y=467)
    objls.append(l9)

    lb6 = Listbox(screen, font="calibri, 12", width=11, height=15)
    lb6.place(x=223, y=493)
    for i in range(len(dauthorls)):
        lb6.insert(END, dauthorls[i])
    objls.append(lb6)

    lb6.config(yscrollcommand=sb4.set)

    sb6 = Scrollbar(screen, orient="horizontal")
    sb6.place(x=223, y=783, relwidth=0.488)
    objls.append(sb6)

    lb6.config(xscrollcommand=sb6.set)
    sb6.config(command=lb6.xview)

    # BOOK ID
    l10 = Label(screen, text="Book ID:", font="calibri, 13", width=13, height=1, bg="grey", anchor="w")
    l10.place(x=329, y=467)
    objls.append(l10)

    lb7 = Listbox(screen, font="calibri, 12", width=12, height=15)
    lb7.place(x=329, y=493)
    for i in range(len(dbookidls)):
        lb7.insert(END, dbookidls[i])
    objls.append(lb7)

    lb7.config(yscrollcommand=sb4.set)

    # DUE DATE
    l11 = Label(screen, text="Due Date:", font="calibri, 13", width=10, height=1, bg="grey", anchor="w")
    l11.place(x=444, y=467)
    objls.append(l11)

    lb8 = Listbox(screen, font="calibri, 12", width=10, height=15)
    lb8.place(x=444, y=493)
    for i in range(len(dduedatels)):
        lb8.insert(END, dduedatels[i])
    objls.append(lb8)

    lb8.config(yscrollcommand=sb4.set)


def duedisplayscroll(*args):
    global lb5, lb6, lb7, lb8

    lb5.yview(*args)
    lb6.yview(*args)
    lb7.yview(*args)
    lb8.yview(*args)


def mainscreenbuttons():
    b1 = Button(screen, text="Logout", font="calibri, 15", width=7, command=lambda: drawstartscreen())
    b1.place(x=550, y=20)
    objls.append(b1)

    b2 = Button(screen, text="Borrow", font="calibri, 15", width=7, height=3, command=lambda: borrowscreen())
    b2.place(x=550, y=220)
    objls.append(b2)

    b3 = Button(screen, text="Return", font="calibri, 15", width=7, height=3, command=lambda: returnscreen())
    b3.place(x=550, y=310)
    objls.append(b3)

    b4 = Button(screen, text="Extend", font="calibri, 15", width=7, height=3, command=lambda: extendscreen())
    b4.place(x=550, y=400)
    objls.append(b4)

    b5 = Button(screen, text="Search", font="calibri, 15", width=7, height=3, command=lambda: searchscreen())
    b5.place(x=550, y=490)
    objls.append(b5)


def borrowscreen():
    screenreset()

    drawborrowscreen()


def drawborrowscreen():
    bookidentry = StringVar()

    b1 = Button(screen, text="Back", font="calibri, 15", command=lambda: mainscreen())
    b1.place(x=570, y=750)
    objls.append(b1)

    l1 = Label(screen, text="Please enter book details", font="calibri, 20", bg="grey", width=40, height=1)
    l1.place(x=0, y=0)
    objls.append(l1)

    l4 = Label(screen, text="Book ID:", font="calibri, 15")
    l4.place(x=130, y=280)
    objls.append(l4)

    e3 = Entry(screen, textvariable=bookidentry, width=50)
    e3.place(x=220, y=285)
    objls.append(e3)

    b2 = Button(screen, text="Borrow Book", font="calibri, 15",
                command=lambda: verifyborrow(bookidentry))
    b2.place(x=260, y=400)
    objls.append(b2)

    if len(duelist) >= 1:
        tkinter.messagebox.showinfo("ERROR", "Borrowing is PROHIBITED! Please return overdue books and pay your fine before you will be allowed to borrow again. Thank You!")
        mainscreen()

    if len(borrowedlist) >= 5:
        tkinter.messagebox.showinfo("ERROR", "You can only borrow a maximum of 5 books!")
        mainscreen()


def verifyborrow(bookidentry):
    bookid = bookidentry.get().upper()

    mycursor.execute("SELECT * FROM Borrowedbooks")
    borrowsearchresult = mycursor.fetchall()

    searchdetails = ""
    mycursor.execute(
        f"SELECT title, author, BookID FROM availablebooks WHERE BookID = '{bookid}'")
    for x in mycursor:
        searchdetails = x

    run = True
    while run:
        if len(searchdetails) == 0:
            if len(bookid) == 0:
                tkinter.messagebox.showinfo("ERROR", "Please enter book details.")
                return 0
            for result in borrowsearchresult:
                if bookid in result:
                    tkinter.messagebox.showinfo("ERROR", "Book is currently unavailable.")
                    return 0
            else:
                tkinter.messagebox.showinfo("ERROR", "Invalid book details! Please try again.")
                return 0
        else:
            break

    title = searchdetails[0]
    author = searchdetails[1]
    bookid = searchdetails[2]

    if len(duelist) >= 1:
        tkinter.messagebox.showinfo("ERROR", "Borrowing is PROHIBITED! Please return overdue books and pay your fine before you will be allowed to borrow again. Thank You!")
        mainscreen()

    elif len(borrowsearchresult) >= 5:
        tkinter.messagebox.showinfo("ERROR", "You can only borrow a maximum of 5 books!")
        mainscreen()

    elif str(searchdetails) == f"('{title}', '{author}', '{bookid}')":
        confirmborrow(title, author, bookid)


def confirmborrow(title, author, bookid):
    borrowdate = datetime.date.today()
    borrowtime = datetime.timedelta(days=30)
    duedate = borrowdate + borrowtime
    borrowdatetext = f"{borrowdate}"
    duedatetext = f"{duedate}"

    entry = [(username, title, author, borrowdatetext, duedatetext, bookid)]

    mycursor.executemany("INSERT INTO Borrowedbooks VALUES (%s, %s, %s, %s, %s, %s)", entry)
    db.commit()

    mycursor.execute(f"DELETE FROM availablebooks WHERE BookID='{bookid}'")
    db.commit()

    tkinter.messagebox.showinfo("", f"Borrow Successful! Do return the book by {duedate}!")

    mycursor.execute("SELECT * FROM Borrowedbooks")
    for x in mycursor:
        print(x)

    borrowscreen()


def returnscreen():
    screenreset()

    drawreturnscreen()


def drawreturnscreen():
    bookidentry = StringVar()

    b1 = Button(screen, text="Back", font="calibri, 15", command=lambda: mainscreen())
    b1.place(x=570, y=750)
    objls.append(b1)

    l1 = Label(screen, text="Please enter book details", font="calibri, 20", bg="grey", width=40, height=1)
    l1.place(x=0, y=0)
    objls.append(l1)

    l4 = Label(screen, text="Book ID:", font="calibri, 15")
    l4.place(x=130, y=280)
    objls.append(l4)

    e3 = Entry(screen, textvariable=bookidentry, width=50)
    e3.place(x=220, y=285)
    objls.append(e3)

    b2 = Button(screen, text="Return Book", font="calibri, 15",
                command=lambda: confirmreturn(bookidentry))
    b2.place(x=260, y=400)
    objls.append(b2)


def confirmreturn(bookidentry):
    bookid = bookidentry.get().upper()

    mycursor.execute("SELECT * FROM availablebooks")
    availablesearchresult = mycursor.fetchall()

    search = ""
    mycursor.execute(
        f"SELECT title, author, BookID FROM Borrowedbooks WHERE username = '{username}' and BookID = '{bookid}'")
    for x in mycursor:
        search = x

    run = True
    while run:
        if len(search) == 0:
            if len(bookid) == 0:
                tkinter.messagebox.showinfo("ERROR", "Please enter book details.")
                return 0
            for result in availablesearchresult:
                if bookid in result:
                    tkinter.messagebox.showinfo("ERROR", "Book has not been borrowed yet.")
                    return 0
            else:
                tkinter.messagebox.showinfo("ERROR", "Invalid book details! Please try again.")
                return 0
        else:
            break

    title = search[0]
    author = search[1]
    bookid = search[2]

    if str(search) == f"('{title}', '{author}', '{bookid}')":
        # GET DUE DATE
        todaydate = datetime.date.today()
        mycursor.execute(f"SELECT duedate FROM Borrowedbooks WHERE BookID = '{bookid}'")
        datesearchresult = mycursor.fetchall()

        duedate = datesearchresult[0][0]
        dayslate = (todaydate - duedate).days
        fine = (dayslate * 0.50)

        if duedate < todaydate:
            tkinter.messagebox.showinfo("",
                                        f"You have been issued a ${fine} fine for returning {title} {dayslate} late.")
            tkinter.messagebox.showinfo("", f"We have received your payment, have a nice day!")
            mycursor.execute(f"DELETE FROM Borrowedbooks WHERE BookID = '{bookid}'")
            db.commit()
            mycursor.execute("INSERT INTO availablebooks VALUES (%s, %s, %s)", (title, author, bookid))
            db.commit()
            returnscreen()
        else:
            mycursor.execute(f"DELETE FROM Borrowedbooks WHERE BookID = '{bookid}'")
            db.commit()
            mycursor.execute("INSERT INTO availablebooks VALUES (%s, %s, %s)", (title, author, bookid))
            db.commit()
            tkinter.messagebox.showinfo("", "Return Successful!")

            mycursor.execute("SELECT * FROM Borrowedbooks")
            for x in mycursor:
                print(x)

            returnscreen()


def extendscreen():
    screenreset()

    drawextendscreen()


def drawextendscreen():
    bookidentry = StringVar()

    b1 = Button(screen, text="Back", font="calibri, 15", command=lambda: mainscreen())
    b1.place(x=570, y=750)
    objls.append(b1)

    l1 = Label(screen, text="Please enter book details", font="calibri, 20", bg="grey", width=40, height=1)
    l1.place(x=0, y=0)
    objls.append(l1)

    l4 = Label(screen, text="Book ID:", font="calibri, 15")
    l4.place(x=130, y=280)
    objls.append(l4)

    e3 = Entry(screen, textvariable=bookidentry, width=50)
    e3.place(x=220, y=285)
    objls.append(e3)

    b2 = Button(screen, text="Extend Loan", font="calibri, 15",
                command=lambda: extendbooksearch(bookidentry))
    b2.place(x=260, y=400)
    objls.append(b2)


def extendbooksearch(bookidentry):
    bookid = bookidentry.get().upper()

    mycursor.execute("SELECT * FROM availablebooks")
    availablesearchresult = mycursor.fetchall()

    searchdetails = ""
    mycursor.execute(
        f"SELECT author, BookID FROM Borrowedbooks WHERE username = '{username}' and BookID = '{bookid}'")
    for x in mycursor:
        searchdetails = x

    run = True
    while run:
        if len(searchdetails) == 0:
            if len(bookid) == 0:
                tkinter.messagebox.showinfo("ERROR", "Please enter book details.")
                return 0
            for result in availablesearchresult:
                if bookid in result:
                    tkinter.messagebox.showinfo("ERROR", "Book has not been borrowed.")
                    return 0
            else:
                tkinter.messagebox.showinfo("ERROR", "Invalid book details! Please try again.")
                return 0
        else:
            break

    author = searchdetails[0]
    bookid = searchdetails[1]

    if str(searchdetails) == f"('{author}', '{bookid}')":
        confirmextend(author, bookid)

    else:
        tkinter.messagebox.showinfo("ERROR", "Invalid book details, please try again.")
        return 0


def confirmextend(author, bookid):
    mycursor.execute(
        f"SELECT username, duedate, dateborrowed FROM Borrowedbooks WHERE username = '{username}' and author = '{author}' and BookID = '{bookid}'")
    searchresult = mycursor.fetchall()

    currentduedate = searchresult[0][1]
    dateborrowed = searchresult[0][2]

    borrowtime = datetime.timedelta(days=15)
    newdate = currentduedate + borrowtime
    print(currentduedate, dateborrowed)
    if (currentduedate - dateborrowed).days >= 45:
        tkinter.messagebox.showinfo("ERROR", f"Extension PROHIBITED! You are only allowed to extend the due-date once!")
        extendscreen()
    else:
        mycursor.execute(f"UPDATE Borrowedbooks SET duedate = '{newdate}' WHERE BookID = '{bookid}'")
        db.commit()
        tkinter.messagebox.showinfo("Extension Successful!", f"Your new due date will be {newdate}")

        mycursor.execute("SELECT * FROM Borrowedbooks")
        for x in mycursor:
            print(x)

        extendscreen()


def searchscreen():
    screenreset()

    getavailablebooks()


def getavailablebooks():
    mycursor.execute("SELECT * FROM availablebooks ORDER BY BookID ASC")

    result = mycursor.fetchall()
    availablelist = []
    atitlels = []
    aauthorls = []
    abookidls = []

    for i in range(len(result)):
        availablelist.append(result[i])

    for i in range(len(availablelist)):
        atitlels.append(availablelist[i][0])
        aauthorls.append(availablelist[i][1])
        abookidls.append(availablelist[i][2])

    drawsearchscreen(atitlels, aauthorls, abookidls)


def drawsearchscreen(atitlels, aauthorls, abookidls):
    global lb1, lb2, lb3

    bgl1 = Label(screen, width=90, height=60, bg="black")
    bgl1.place(x=0, y=26)
    objls.append(bgl1)

    bgl2 = Label(screen, width=90, height=4, bg="grey")
    bgl2.place(x=0, y=745)
    objls.append(bgl2)

    l1 = Label(screen, text="", width=15, height=70, bg="grey")
    l1.place(x=540, y=0)
    objls.append(l1)

    l2 = Label(screen, text="Available Books:", font="calibri, 15", width=49, height=1, bg="grey", anchor="w")
    l2.place(x=0, y=0)
    objls.append(l2)

    # TITLE
    l3 = Label(screen, text="Title:", font="calibri, 13", width=32, height=1, bg="grey", anchor="w")
    l3.place(x=0, y=28)
    objls.append(l3)

    lb1 = Listbox(screen, font="calibri, 12", width=29, height=35)
    lb1.place(x=0, y=54)
    objls.append(lb1)
    for i in range(len(atitlels)):
        lb1.insert(END, atitlels[i])

    sb1 = Scrollbar(screen, orient="vertical")
    sb1.place(x=266, y=54, relheight=0.86)
    objls.append(sb1)

    sb2 = Scrollbar(screen, orient="horizontal")
    sb2.place(x=0, y=725, relwidth=0.41)
    objls.append(sb2)

    lb1.config(yscrollcommand=sb1.set)
    sb1.config(command=searchdisplayscroll)

    lb1.config(xscrollcommand=sb2.set)
    sb2.config(command=lb1.xview)

    # AUTHOR
    l4 = Label(screen, text="Author:", font="calibri, 13", width=17, height=1, bg="grey", anchor="w")
    l4.place(x=285, y=28)
    objls.append(l4)

    lb2 = Listbox(screen, font="calibri, 12", width=15, height=35)
    lb2.place(x=285, y=54)
    objls.append(lb2)

    for i in range(len(aauthorls)):
        lb2.insert(END, aauthorls[i])

    lb2.config(yscrollcommand=sb1.set)

    sb3 = Scrollbar(screen, orient="horizontal")
    sb3.place(x=285, y=725, relwidth=0.392)
    objls.append(sb3)

    lb2.config(xscrollcommand=sb3.set)
    sb3.config(command=lb2.xview)

    # BOOK ID
    l5 = Label(screen, text="Book ID:", font="calibri, 13", width=13, height=1, bg="grey", anchor="w")
    l5.place(x=426, y=28)
    objls.append(l5)

    lb3 = Listbox(screen, font="calibri, 12", width=12, height=35)
    lb3.place(x=426, y=54)
    objls.append(lb3)

    for i in range(len(abookidls)):
        lb3.insert(END, abookidls[i])

    lb3.config(yscrollcommand=sb1.set)

    # BACK BUTTON
    b1 = Button(screen, text="Back", font="calibri, 15", command=lambda: mainscreen())
    b1.place(x=570, y=750)
    objls.append(b1)

    # SEARCH BUTTON
    searchlab = Label(screen, text="Search:", font="calibri, 12", bg="grey")
    searchlab.place(x=350, y=3)
    objls.append(searchlab)

    searchentry = StringVar()
    searchef = Entry(screen, textvariable=searchentry, font="calibri, 13", width=19)
    searchef.place(x=415, y=5)
    objls.append(searchef)

    searchbut = Button(screen, text="Search", font="calibri, 8", width=5, height=1,
                       command=lambda: getsearch(searchentry))
    searchbut.place(x=591, y=5)
    objls.append(searchbut)


def getsearch(searchentry):
    searchtext = searchentry.get().upper()
    mycursor.execute(f"SELECT title, author, BookID FROM availablebooks WHERE title LIKE '%{searchtext}%' or author LIKE '%{searchtext}%' or BookID LIKE '%{searchtext}%' ORDER BY BookID ASC")
    finalsearchresult = mycursor.fetchall()

    stitlels = []
    sauthorls = []
    sbookidls = []

    for i in range(len(finalsearchresult)):
        stitlels.append(finalsearchresult[i][0])
        sauthorls.append(finalsearchresult[i][1])
        sbookidls.append(finalsearchresult[i][2])

    if searchtext == "":
        searchscreen()
    else:
        drawsearchscreen(stitlels, sauthorls, sbookidls)


def searchdisplayscroll(*args):
    global lb1, lb2, lb3

    lb1.yview(*args)
    lb2.yview(*args)
    lb3.yview(*args)


if __name__ == "__main__":
    startscreen()
