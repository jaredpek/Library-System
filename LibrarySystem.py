import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import datetime

objls = []
screenResolution = (1920, 1080)  # INPUT SCREEN RESOLUTION HERE
screenWidth, screenHeight = screenResolution[0], screenResolution[1] - 65

db = mysql.connector.connect(host="#",  # INPUT HOST NAME
                             user="#",  # INPUT MYSQL DATABASE USER NAME
                             password="#",  # INPUT MYSQL DATABASE PASSWORD
                             database="library")

mycursor = db.cursor()


# USERINFO TABLE NAME IS userinfo (username, password, fullname)
# BOOKINFO TABLE NAME IS bookinfo (bookid, title, author, state, borrowedby, borrowdate, duedate


def screenreset():
    for item in objls:
        item.destroy()


def setupscreen():
    screen = Tk()
    screen.title("Library System")
    screen.geometry(f"{screenWidth}x{screenHeight}")

    startscreen(screen)

    screen.mainloop()


def startscreen(screen):
    screenreset()

    welcomeLabel = Label(screen, text="Welcome to the Library System", font="calibri, 20", bg="grey", height=2)
    welcomeLabel.pack(side=TOP, fill=X)
    objls.append(welcomeLabel)

    loginButton = Button(screen, text='Login', font="calibri, 17", width=8, height=1, command=lambda: loginscreen(screen))
    loginButton.pack(pady=(60, 0))
    objls.append(loginButton)

    registerButton = Button(screen, text='Register', font="calibri, 17", width=8, height=1, command=lambda: registerscreen(screen))
    registerButton.pack(pady=(40, 0))
    objls.append(registerButton)

    quitButton = Button(screen, text='Quit', font="calibri, 16", width=7, height=1, command=lambda: exit())
    quitButton.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
    objls.append(quitButton)


def loginscreen(screen):
    screenreset()

    instructionsLabel = Label(screen, text="Please Enter Account Login Credentials", font="calibri, 20", bg="grey", height=2)
    instructionsLabel.pack(side=TOP, fill=X)
    objls.append(instructionsLabel)

    credFrame = Frame(screen)
    objls.append(credFrame)

    usernameLabel = Label(credFrame, text="Username: ", font='calibri, 15', width=12, height=1, anchor='w')
    usernameLabel.pack(side=TOP, anchor='w')
    usernameEntry = StringVar()
    usernameField = Entry(credFrame, textvariable=usernameEntry, width=70)
    usernameField.pack(side=TOP, anchor='e', pady=(0, 30))

    passwordLabel = Label(credFrame, text="Password: ", font='calibri, 15', width=12, height=1, anchor='w')
    passwordLabel.pack(side=TOP, anchor='w')
    passwordEntry = StringVar()
    passwordField = Entry(credFrame, textvariable=passwordEntry, width=70, show="*")
    passwordField.pack(side=TOP, anchor='e', pady=(0, 30))

    loginButton = Button(credFrame, text='Login', font="calibri, 16", width=8, height=1, command=lambda: verifyLoginCredentials(screen, usernameEntry.get(), passwordEntry.get()))
    loginButton.pack(side=BOTTOM)

    credFrame.pack(pady=(40, 0))

    backButton = Button(screen, text='Back', font="calibri, 16", width=7, height=1, command=lambda: startscreen(screen))
    backButton.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
    objls.append(backButton)


def verifyLoginCredentials(screen, usernameEntry, passwordEntry):
    if not usernameEntry or not passwordEntry:
        tkinter.messagebox.showinfo('ERROR', 'Please enter login credentials!')
        return 0
    else:
        mycursor.execute(f"select username, password, fullname from userinfo where username = '{usernameEntry}' and password = '{passwordEntry}'")
        credentialSearch = mycursor.fetchall()
        try:
            username, password, fullname = credentialSearch[0][0], credentialSearch[0][1], credentialSearch[0][2]
            tkinter.messagebox.showinfo('SUCCESS', 'Login is Successful!')
            mainScreen(screen, username, fullname)
            return 0
        except:
            tkinter.messagebox.showinfo('ERROR', 'Invalid login credentials... Please try again...')
            return 0


def registerscreen(screen):
    screenreset()

    instructionsLabel = Label(screen, text="To Register A New Account, Key In Credentials", font="calibri, 20", bg="grey", height=2)
    instructionsLabel.pack(side=TOP, fill=X)
    objls.append(instructionsLabel)

    credFrame = Frame(screen)
    objls.append(credFrame)

    usernameLabel = Label(credFrame, text="Username: ", font='calibri, 15', width=12, height=1, anchor='w')
    usernameLabel.pack(side=TOP, anchor='w')
    usernameEntry = StringVar()
    usernameField = Entry(credFrame, textvariable=usernameEntry, width=70)
    usernameField.pack(side=TOP, anchor='e', pady=(0, 30))

    passwordLabel = Label(credFrame, text="Password: ", font='calibri, 15', width=12, height=1, anchor='w')
    passwordLabel.pack(side=TOP, anchor='w')
    passwordEntry = StringVar()
    passwordField = Entry(credFrame, textvariable=passwordEntry, width=70, show="*")
    passwordField.pack(side=TOP, anchor='e', pady=(0, 30))

    firstnameLabel = Label(credFrame, text="First Name: ", font='calibri, 15', width=12, height=1, anchor='w')
    firstnameLabel.pack(side=TOP, anchor='w')
    firstnameEntry = StringVar()
    firstnameField = Entry(credFrame, textvariable=firstnameEntry, width=70)
    firstnameField.pack(side=TOP, anchor='e', pady=(0, 30))

    lastnameLabel = Label(credFrame, text="Last Name: ", font='calibri, 15', width=12, height=1, anchor='w')
    lastnameLabel.pack(side=TOP, anchor='w')
    lastnameEntry = StringVar()
    lastnameField = Entry(credFrame, textvariable=lastnameEntry, width=70)
    lastnameField.pack(side=TOP, anchor='e', pady=(0, 30))

    registerButton = Button(credFrame, text='Register', font="calibri, 16", width=8, height=1, command=lambda: verifyRegisterCredentials(screen, usernameEntry.get(), passwordEntry.get(), firstnameEntry.get(), lastnameEntry.get()))
    registerButton.pack(side=BOTTOM)

    credFrame.pack(pady=(40, 0))

    backButton = Button(screen, text='Back', font="calibri, 16", width=7, height=1, command=lambda: startscreen(screen))
    backButton.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
    objls.append(backButton)


def verifyRegisterCredentials(screen, usernameEntry, passwordEntry, firstnameEntry, lastnameEntry):
    if not usernameEntry or not passwordEntry or not firstnameEntry or not lastnameEntry:
        tkinter.messagebox.showinfo('ERROR', 'Please enter login credentials!')
        return 0
    elif len(usernameEntry) <= 5 or len(passwordEntry) <= 5:
        tkinter.messagebox.showinfo('ERROR', 'Username and Password must have at least 6 characters!')
        return 0
    else:
        mycursor.execute(f"select username from userinfo where username = '{usernameEntry}'")
        credentialSearch = mycursor.fetchall()
        if not credentialSearch:
            fullname = f'{firstnameEntry.lower().capitalize()} {lastnameEntry.lower().capitalize()}'
            mycursor.execute('insert into userinfo (username, password, fullname) values (%s, %s, %s)', (usernameEntry, passwordEntry, fullname))
            db.commit()
            tkinter.messagebox.showinfo('SUCCESS', 'Registration Successful! You will be logged into the system in a moment...')
            mainScreen(screen, usernameEntry, fullname)
            return 0
        else:
            tkinter.messagebox.showinfo('ERROR', 'User already exists! Please use another username.')
            return 0


def mainScreen(screen, username, fullname):
    screenreset()

    timeLabel = Label(screen, text=f"Today's Date: {datetime.date.today()}", font="calibri, 10", bg="#1a1a1a", fg="white", height=1)
    timeLabel.pack(side=TOP, fill=X)
    objls.append(timeLabel)

    welcomeLabel = Label(screen, text=f"  Welcome to the Library, {fullname}!", font="calibri, 18", bg="grey", height=2, anchor='w')
    welcomeLabel.pack(side=TOP, fill=X)
    objls.append(welcomeLabel)

    logoutButton = Button(screen, text='Logout', font="calibri, 16", width=7, height=1, command=lambda: startscreen(screen))
    logoutButton.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
    objls.append(logoutButton)

    borrowButton = Button(screen, text="Borrow", font='calibri, 16', width=8, height=1, command=lambda: bookFunctions(screen, username, 'Borrow', fullname))
    borrowButton.place(x=30, y=320)
    objls.append(borrowButton)

    returnButton = Button(screen, text="Return", font='calibri, 16', width=8, height=1, command=lambda: bookFunctions(screen, username, 'Return', fullname))
    returnButton.place(x=200, y=320)
    objls.append(returnButton)

    extendButton = Button(screen, text="Extend", font='calibri, 16', width=8, height=1, command=lambda: bookFunctions(screen, username, 'Extend', fullname))
    extendButton.place(x=370, y=320)
    objls.append(extendButton)

    searchButton = Button(screen, text="Search", font='calibri, 16', width=8, height=1, command=lambda: searchBooks(screen, username, fullname))
    searchButton.place(x=540, y=320)
    objls.append(searchButton)

    borrowedBookDisplay(screen, username)


def borrowedBookDisplay(screen, username):
    borrowedBooksFrame = Frame(screen)
    borrowedBooksFrame.pack(fill=X, pady=(5, 0), padx=15)
    objls.append(borrowedBooksFrame)

    borrowedBooksLabel = Label(borrowedBooksFrame, text="Borrowed Books:", font='calibri, 15', height=1, anchor='w')
    borrowedBooksLabel.pack(side=TOP, anchor='w')
    objls.append(borrowedBooksLabel)

    borrowedBooksListStyle = ttk.Style()
    borrowedBooksListStyle.theme_use("default")  # SELECT DEFAULT THEME
    borrowedBooksListStyle.configure("Treeview", background="white", foreground="black", rowheight=20, fieldbackground="white")  # CONFIGURE BOOKLIST STYLE
    borrowedBooksListStyle.map("Treeview", background=[("selected", "#4e96c7")])  # SET BOOKLIST STYLE PARAMETERS (WHEN SELECTED, WHAT COLOUR IS COLUMN)

    borrowedBooksList = ttk.Treeview(borrowedBooksFrame, height=8)
    borrowedBooksList['columns'] = ('S/N', 'Title', 'Author', 'Book-ID', 'Borrow Date', 'Due Date')
    borrowedBooksList.tag_configure("overdue", background="#bd6464")  # SET SPECIFIC PARAMETERS (IF FULFIL CONDITION, HIGHLIGHT ROW)

    borrowedBooksList.column("#0", width=0, stretch=NO)
    borrowedBooksList.column("S/N", anchor=CENTER, width=int(40 / 1366 * screenWidth))
    borrowedBooksList.column("Title", anchor=CENTER, width=int(420 / 1366 * screenWidth))
    borrowedBooksList.column("Author", anchor=CENTER, width=int(250 / 1366 * screenWidth))
    borrowedBooksList.column("Book-ID", anchor=CENTER, width=int(200 / 1366 * screenWidth))
    borrowedBooksList.column("Borrow Date", anchor=CENTER, width=int(210 / 1366 * screenWidth))
    borrowedBooksList.column("Due Date", anchor=CENTER, width=int(210 / 1366 * screenWidth))

    borrowedBooksList.heading("#0", text="", anchor=CENTER)
    borrowedBooksList.heading("S/N", text="S/N", anchor=CENTER)
    borrowedBooksList.heading("Title", text="Title", anchor=CENTER)
    borrowedBooksList.heading("Author", text="Author", anchor=CENTER)
    borrowedBooksList.heading("Book-ID", text="Book-ID", anchor=CENTER)
    borrowedBooksList.heading("Borrow Date", text="Borrow Date", anchor=CENTER)
    borrowedBooksList.heading("Due Date", text="Due Date", anchor=CENTER)

    mycursor.execute(f'select * from bookinfo where borrowedby = "{username}" order by bookid')
    search = mycursor.fetchall()
    for i in range(len(search)):  # SN, TITLE, AUTHOR, BOOKID, BORROW DATE, DUE DATE
        tagDetails = ""
        if datetime.date.today() > search[i][-1]:
            tagDetails = "overdue"
        borrowedBooksList.insert(parent='', index='end', iid=f'{i}', text='', values=(f'{i + 1}', f'{search[i][2]}', f'{search[i][3]}', f'{search[i][1]}', f'{search[i][-2]}', f'{search[i][-1]}'), tags=(tagDetails,))

    borrowedBooksList.pack(fill=X)

    dueInstLabel = Label(borrowedBooksFrame, text="*Note: Books that are OVERDUE will be highlighted in RED, please return them (if applicable) before you borrow any other books.", font="calibri, 8", height=1, anchor='w')
    dueInstLabel.pack(side=BOTTOM, anchor='w')


def bookFunctions(screen, username, function, fullname):
    screenreset()
    mainScreen(screen, username, fullname)

    if function == "Borrow":
        mycursor.execute(f'select count(*) from bookinfo where borrowedby = "{username}"')
        qtyBorrowed = mycursor.fetchall()[0][0]
        mycursor.execute(f'select count(*) from bookinfo where borrowedby = "{username}" and (duedate < curdate())')
        qtyDue = mycursor.fetchall()[0][0]
        if int(qtyBorrowed) >= 7:
            tkinter.messagebox.showinfo('ERROR', 'You have borrowed a maximum of 7 books.')
            return 0
        elif int(qtyDue) >= 1:
            tkinter.messagebox.showinfo('ERROR', 'Borrowing is PROHIBITED as you currently have overdue books! Please return them before you are allowed to continue borrowing.')
            return 0

    instLabel = Label(screen, text=f"Enter Book ID To {function} Book", width=50, height=1, font='calibri, 14', anchor='w')
    instLabel.place(x=30, y=370)
    objls.append(instLabel)

    bookIDLabel = Label(screen, text="Book ID: ", width=10, height=1, font='calibri, 14', anchor='w')
    bookIDLabel.place(x=30, y=400)
    objls.append(bookIDLabel)

    bookIdEntry = StringVar()
    bookIdField = Entry(screen, textvariable=bookIdEntry, width=50)
    bookIdField.place(x=125, y=405)
    objls.append(bookIdField)

    confirmButton = Button(screen, text=f"Confirm {function}", width=14, height=1, font='calibri, 10', command=lambda: verifyFunction(screen, username, function, bookIdEntry.get(), fullname))
    confirmButton.place(x=450, y=400)
    objls.append(confirmButton)


def verifyFunction(screen, username, function, bookIdEntry, fullname):
    if function == "Borrow":
        mycursor.execute(f'select * from bookinfo where bookid = "{bookIdEntry.upper()}" and state = "AVAILABLE"')
        search = mycursor.fetchall()
        if len(search) >= 1:
            mycursor.execute(f'select count(*) from bookinfo where borrowedby = "{username}"')
            qtyBorrowed = mycursor.fetchall()[0][0]
            mycursor.execute(f'select count(*) from bookinfo where borrowedby = "{username}" and (duedate < curdate())')
            qtyDue = mycursor.fetchall()[0][0]
            if int(qtyBorrowed) >= 7:
                tkinter.messagebox.showinfo('ERROR', 'You have borrowed a maximum of 7 books.')
                return 0
            elif int(qtyDue) >= 1:
                tkinter.messagebox.showinfo('ERROR', 'Borrowing is PROHIBITED as you currently have overdue books! Please return them before you are allowed to continue borrowing.')
                return 0
            else:
                mycursor.execute(f'update bookinfo set state = "BORROWED", borrowedby = "{username}", borrowdate = "{datetime.date.today()}", duedate = "{datetime.date.today() + datetime.timedelta(days=30)}" where bookid = "{bookIdEntry.upper()}" and state = "AVAILABLE"')
                db.commit()
                mycursor.execute(f'select * from bookinfo where bookid = "{bookIdEntry.upper()}" and state = "BORROWED" and borrowedby = "{username}"')
                search = mycursor.fetchall()
                tkinter.messagebox.showinfo('SUCCESS', f'You have successfully borrowed {search[0][2]}, please return the book by {search[0][-1]}.')
                bookFunctions(screen, username, 'Borrow', fullname)
                return 0
        else:
            mycursor.execute(f'select title, state, borrowedby from bookinfo where bookid = "{bookIdEntry}"')
            search = mycursor.fetchall()
            if len(search) >= 1:
                tkinter.messagebox.showinfo('ERROR', 'Book is currently unavailable...')
                return 0
            else:
                tkinter.messagebox.showinfo('ERROR', 'Please enter valid book details!')
                return 0

    elif function == "Return":
        mycursor.execute(f'select * from bookinfo where bookid = "{bookIdEntry.upper()}" and state = "BORROWED" and borrowedby = "{username}"')
        search = mycursor.fetchall()
        if len(search) >= 1:
            mycursor.execute(f'update bookinfo set state = "AVAILABLE", borrowedby = NULL, borrowdate = NULL, duedate = NULL where bookid = "{bookIdEntry.upper()}" and state = "BORROWED" and borrowedby = "{username}"')
            db.commit()
            mycursor.execute(f'select * from bookinfo where bookid = "{bookIdEntry.upper()}" and state = "AVAILABLE"')
            search = mycursor.fetchall()
            tkinter.messagebox.showinfo('SUCCESS', f'You have successfully returned {search[0][2]}.')
            bookFunctions(screen, username, 'Return', fullname)
            return 0
        else:
            mycursor.execute(f'select title, state, borrowedby from bookinfo where bookid = "{bookIdEntry}"')
            search = mycursor.fetchall()
            if len(search) >= 1:
                tkinter.messagebox.showinfo('ERROR', 'You have not borrowed this book yet...')
                return 0
            else:
                tkinter.messagebox.showinfo('ERROR', 'Please enter valid book details!')
                return 0

    elif function == "Extend":
        mycursor.execute(f'select * from bookinfo where bookid = "{bookIdEntry.upper()}" and state = "BORROWED" and borrowedby = "{username}"')
        search = mycursor.fetchall()
        if len(search) >= 1:
            dateDiff = (search[0][-1] - search[0][-2]).days
            if dateDiff >= 45:
                tkinter.messagebox.showinfo("ERROR", f"Further extension of the due date for {search[0][2]} is PROHITIBTED as you have already extended it once.")
                return 0
            else:
                mycursor.execute(f'update bookinfo set duedate = "{search[0][-1] + datetime.timedelta(days=15)}" where bookid = "{bookIdEntry.upper()}" and state = "BORROWED" and borrowedby = "{username}"')
                db.commit()
                mycursor.execute(f'select * from bookinfo where bookid = "{bookIdEntry.upper()}" and state = "BORROWED" and borrowedby = "{username}"')
                search = mycursor.fetchall()
                tkinter.messagebox.showinfo('SUCCESS', f'You have successfully extended the deadline for {search[0][2]}. Please return {search[0][2]} by {search[0][-1]}.')
                bookFunctions(screen, username, 'Extend', fullname)
                return 0
        else:
            mycursor.execute(f'select title, state, borrowedby from bookinfo where bookid = "{bookIdEntry}"')
            search = mycursor.fetchall()
            if len(search) >= 1:
                tkinter.messagebox.showinfo('ERROR', 'You have not borrowed this book yet...')
                return 0
            else:
                tkinter.messagebox.showinfo('ERROR', 'Please enter valid book details!')
                return 0


def searchBooks(screen, username, fullname):
    screenreset()
    mainScreen(screen, username, fullname)

    instLabel = Label(screen, text=f"Enter Text To Search: ", width=50, height=1, font='calibri, 14', anchor='w')
    instLabel.place(x=30, y=370)
    objls.append(instLabel)

    bookIDLabel = Label(screen, text="Search: ", width=10, height=1, font='calibri, 14', anchor='w')
    bookIDLabel.place(x=30, y=400)
    objls.append(bookIDLabel)

    textEntry = StringVar()
    bookIdField = Entry(screen, textvariable=textEntry, width=50)
    bookIdField.place(x=125, y=405)
    objls.append(bookIdField)

    titleCheck = IntVar()
    searchTitleChkBox = Checkbutton(screen, text="Title", font='calibri, 11', variable=titleCheck)
    searchTitleChkBox.place(x=30, y=430)
    objls.append(searchTitleChkBox)

    authorCheck = IntVar()
    searchAuthorChkBox = Checkbutton(screen, text="Author", font='calibri, 11', variable=authorCheck)
    searchAuthorChkBox.place(x=110, y=430)
    objls.append(searchAuthorChkBox)

    bookidCheck = IntVar()
    searchBookIdChkBox = Checkbutton(screen, text="Book-ID", font='calibri, 11', variable=bookidCheck)
    searchBookIdChkBox.place(x=200, y=430)
    objls.append(searchBookIdChkBox)

    confirmButton = Button(screen, text=f"Confirm Search", width=14, height=1, font='calibri, 10', command=lambda: verifySearch(screen, textEntry.get(), titleCheck.get(), authorCheck.get(), bookidCheck.get(), username, fullname))
    confirmButton.place(x=450, y=400)
    objls.append(confirmButton)


def verifySearch(screen, textEntry, titleCheck, authorCheck, bookidCheck, username, fullname):
    screenreset()
    mainScreen(screen, username, fullname)
    searchBooks(screen, username, fullname)

    conditions = [titleCheck, authorCheck, bookidCheck]
    conditionString = ''
    for i in range(len(conditions)):
        if conditions[i]:
            if i == 0:
                conditionString += f'title like "%{textEntry.upper()}%"'
            elif i == 1:
                conditionString += f'author like "%{textEntry.upper()}%"'
            elif i == 2:
                conditionString += f'bookid like "%{textEntry.upper()}%"'
            conditionString += ' or '
    if not conditionString.strip():
        conditionString = f'title like "%{textEntry.upper()}%" or author like "%{textEntry.upper()}%" or bookid like "%{textEntry.upper()}%"'
    else:
        conditionString = conditionString[:-4]
    try:
        mycursor.execute(f'select title, author, bookid, state from bookinfo where {conditionString} order by bookid')
        search = mycursor.fetchall()
        borrowedInstLabel = Label(screen, text="*Note: Books that are BORROWED will be highlighted in RED and are currently unavailable.", font="calibri, 8", height=1, anchor='w')
        borrowedInstLabel.pack(side=BOTTOM, anchor='w', padx=15)
        objls.append(borrowedInstLabel)
        searchBookDisplay(screen, search)
        return 0
    except:
        return 0


def searchBookDisplay(screen, search):
    displayFrame = Frame(screen)
    displayFrame.pack(fill=X, pady=(140, 0), padx=15)
    objls.append(displayFrame)

    searchResultLabel = Label(displayFrame, text="Search Result:", font='calibri, 15', anchor='w')
    searchResultLabel.pack(side=TOP, fill=X)

    searchBooksFrame = Frame(displayFrame)

    searchBooksListStyle = ttk.Style()
    searchBooksListStyle.theme_use("default")  # SELECT DEFAULT THEME
    searchBooksListStyle.configure("Treeview", background="white", foreground="black", rowheight=20, fieldbackground="white")  # CONFIGURE BOOKLIST STYLE
    searchBooksListStyle.map("Treeview", background=[("selected", "#4e96c7")])  # SET BOOKLIST STYLE PARAMETERS (WHEN SELECTED, WHAT COLOUR IS COLUMN)

    searchBooksScroll = Scrollbar(searchBooksFrame)
    searchBooksScroll.pack(side=RIGHT, fill=Y)

    searchBooksList = ttk.Treeview(searchBooksFrame, yscrollcommand=searchBooksScroll.set, height=50)
    searchBooksList['columns'] = ('S/N', 'Title', 'Author', 'Book-ID', 'Status')
    searchBooksList.tag_configure("borrowed", background="#bd6464")  # SET SPECIFIC PARAMETERS (IF FULFIL CONDITION, HIGHLIGHT ROW)
    searchBooksScroll.config(command=searchBooksList.yview)

    searchBooksList.column("#0", width=0, stretch=NO)
    searchBooksList.column("S/N", anchor=CENTER, width=int(60 / 1366 * screenWidth) - 2)
    searchBooksList.column("Title", anchor=CENTER, width=int(470 / 1366 * screenWidth) - 3)
    searchBooksList.column("Author", anchor=CENTER, width=int(300 / 1366 * screenWidth) - 3)
    searchBooksList.column("Book-ID", anchor=CENTER, width=int(250 / 1366 * screenWidth) - 3)
    searchBooksList.column("Status", anchor=CENTER, width=int(250 / 1366 * screenWidth) - 3)

    searchBooksList.heading("#0", text="", anchor=CENTER)
    searchBooksList.heading("S/N", text="S/N", anchor=CENTER)
    searchBooksList.heading("Title", text="Title", anchor=CENTER)
    searchBooksList.heading("Author", text="Author", anchor=CENTER)
    searchBooksList.heading("Book-ID", text="Book-ID", anchor=CENTER)
    searchBooksList.heading("Status", text="Status", anchor=CENTER)

    for i in range(len(search)):  # SN, TITLE, AUTHOR, BOOKID, STATUS
        tagDetails = ''
        if search[i][-1] == 'BORROWED':
            tagDetails = "borrowed"
        searchBooksList.insert(parent='', index='end', iid=f'{i}', text='', values=(f'{i + 1}', f'{search[i][0]}', f'{search[i][1]}', f'{search[i][2]}', f'{search[i][3]}'), tags=(tagDetails,))

    searchBooksList.pack(fill=BOTH)
    searchBooksFrame.pack(fill=X)


if __name__ == "__main__":
    setupscreen()
