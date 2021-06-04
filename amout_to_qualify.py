from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Exception Handling")
root.geometry("500x300")

x = StringVar()

lab1 = Label(root, text = "Please enter amount in your account:")
lab1.place(x=20, y=10)
lab2 = Label(root, text = "R")
lab2.place(x=20, y=40)
ent1 = Entry(root)
ent1.place(x=35, y=40)


def qualify():
    try:
        x = int(ent1.get())

        if x >= 3000:
            messagebox.showinfo("STATUS FEEDBACK","Congratulations. Your Qualify to go to Malaysia")
            root.destroy()
            import error_handling_exercise

    except ValueError:
        messagebox.showinfo("ERROR","Please Enter Valid integer")
        ent1.delete(0, END)

    else:
        if x < 3000:
            messagebox.showinfo("STATUS FEEDBACK", "Sorry, You Don`t Have Enough, You Can`t Go To Malaysia, Please Try Again Next Time")
            root.destroy()
            import error_handling_exercise


btn = Button(root, text = "Check Qualification", command = qualify)
btn.place(x=20, y=90)

root.mainloop()
