from tkinter import *

root = Tk()
root.title("Authentification")
root.geometry("500x300")

username = StringVar()
password = StringVar()

lab1 = Label(root, text = 'Please Enter Login Details')
lab1.place(x=160, y=5)

lab2 = Label(root, text = "Username")
lab2.place(x=210, y=50)
ent1 = Entry(root)
ent1.place(x=165, y=70)

lab3 = Label(root, text = "Password")
lab3.place(x=210, y=120)
ent2 = Entry(root, show = "*")
ent2.place(x=165, y=140)

def login():
    from tkinter import messagebox
    username = ["Ayyoob", "Abdul-Malik", "Uthmaan", "Zipho"]
    password = ["0000","1111", "2222", "3333"]
    found = False

    for x in range(len(username)):
        if ent1.get() == username[x] and ent2.get() == password[x]:
            found = True
    
    if found == True:
        messagebox.showinfo("STATUS", "Access Granted!")
        root.destroy()
        import amout_to_qualify

    else:
        messagebox.showinfo("ERROR INFO", "Access Denied!!!")
        ent1.delete(0, END)
        ent2.delete(0, END)

def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)

def exit():
    root.destroy()

btn1 = Button(root, text = "Login", command = login)
btn1.place(x=210, y=165)
btn2 = Button(root, text ="Clear", command = clear)
btn2.place(x=70, y=200)
btn3 = Button(root, text = "Exit", command = exit)
btn3.place(x=370, y=200)



root.mainloop()
