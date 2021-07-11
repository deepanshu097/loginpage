from tkinter_page import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("accepted")

Label(root, text = "registration form",font = "ar 15 bold").grid(row = 0, cloumn = 3)

first_name = Label(root, text = "first name")
last_name = Label(root, text = "last name")
gender = Label(root, text = "gender")
phone = label(root, text = "phone")
payment_mode = Label(root, text = "payment mode")\

first_name.grid(row=1,column=2)
last_name.grid(row=2,column=2)
gender.grid(row=3,column=2)
phone.grid(row=4,column=2)
payment_mode.grid(row=5,column=2)

first_namevalue = StringVar
last_namevalue = StringVar
gendervalue = StringVar
phonevalue = StringVar
payment_mode_namevalue = StringVar
checkvalue = IntVar

first_nameentry = Entry(root, textvariable =first_namevalue)
last_nameentry = Entry(root, textvariable =last_namevalue)
genderentry = Entry(root, textvariable =gendervalue)
phoneentry = Entry(root, textvariable =phonevaluevalue)
payment_modeentry = Entry(root, textvariable =payment_modevalue)

first_nameentry.grid(row=1,column=3)
last_nameentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
phoneentry.grid(row=4,column=3)
payment_modeentryentry.grid(row=5,column=3)

checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6,column=3)

Button (text= "submit", command=getvals).grid(row=7,column=3)

root.mainloop()
