from tkinter import *
from tkinter import messagebox
import pandas as pd
import pass_generator
import pyperclip #lib which make easy to copy and paste
D_BLUE = '#454545'
Light_pur = '#A5D7E8'
BlACK="#000000"
CYAN = '#A5D7E8'
BLUE = '#0B2447'
button_color = '#C0DBEA'
GREEN = "#539165"
window = Tk()
window.minsize(500,500)
window.title("Password Manager")
canva = Canvas(height=500,width=500,bg=Light_pur)
canva.pack()
l1 = Label(text="Password Manager",font=('Arial',18,'bold'),bg=Light_pur)
l1.place(x=145,y=20)
imgloc = PhotoImage(file="lock.png",)
canva.create_image(250,170,image=imgloc)
l2 = Label(text='Website:',font=(14),bg=Light_pur,fg=BlACK)
l2.place(x=55,y=300)
email = Label(text="Email/Username:",font=14,bg=Light_pur,fg=BlACK)
email.place(x=25,y=350)
password_label = Label(text='Password:',font=14,bg=Light_pur,fg=BlACK)
password_label.place(x=45,y=400)
lst1=[]
lst2=[]
lst3=[]
emo ="✔"
entry1 = Entry(width=40)
entry1.place(x=220,y=306)
entry1.focus()
entry2 = Entry(width=40)
entry2.place(x=220,y=355)
entry3 = Entry(width=26)
entry3.place(x=220,y=405)

def save_entry():
    if len(entry1.get())>0 and len(entry2.get())>0 and len(entry3.get())>0and entry1.get()!="Invalid or Empty"and entry2.get()!="Invalid or Empty"and entry3.get()!="Invalid or Empty":
        lst1.append(entry1.get())
        lst2.append(entry2.get())
        lst3.append(entry3.get())
        dict = {"website": lst1,
                "Email": lst2,
                "password": lst3}
        df = pd.DataFrame(dict)
        df.to_csv("pass.csv", mode='a', header=False, index=False)
        print(df)
        website_added = Label(text=f"{entry1.get()} added {emo}", font=('arial',12), bg=Light_pur)
        website_added.place(x=30, y=450)
        window.update()
        window.after(3000, website_added.destroy())
    else:
        messagebox.showinfo(title="Error Occurred",message="Please fill the details correctly")

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def generate_pass():
    # entry3.delete(0,END)
    entry3.insert(0,pass_generator.final_pass)
    pyperclip.copy(pass_generator.final_pass)

generate_button = Button(text="Generate",bg=button_color,fg=BlACK,width=10,activebackground=CYAN,command=generate_pass)
generate_button.place(x=400,y=403)
add =Button(text='Add',bg=button_color,fg=BlACK,width=35,activebackground=CYAN,command=save_entry)
add.place(x=220,y=450)
window.mainloop()


