from tkinter import *
from tkinter import messagebox
#=============================================
root =Tk()
root.title("Number System Convertor")
root.geometry('1220x700')
root.resizable(False,False)
# ==============================================
num=StringVar()
binlbl=StringVar()
delbl=StringVar()
hexlbl=StringVar()
octlbl=StringVar()
base=StringVar()
# ==============================================
def clear():
    num.set('')
    base.set('')
    binlbl.set('')
    delbl.set('')
    hexlbl.set('')
    octlbl.set('')
# ================================================
def exit():
    if messagebox.askyesno('Exit',"Do You Really Want To Exit?"):
        root.destroy()

# ==============================================
def convert_to_decimal(number: str, base: int) -> int:    
    return int(number, base)
# ===============================================
def convert():
    if num.get()=="" or base.get()==0:
        messagebox.showerror("Error","You Must Fill both the Number and base filled !")
    else:
        if base.get()=='10':
            dec=convert_to_decimal(num.get(),10) 
        elif base.get()=='2':
            dec=convert_to_decimal(num.get(),2)         
        elif base.get()=='16':
            dec=convert_to_decimal(num.get(),16)
        elif base.get()=='8':
            dec=convert_to_decimal(num.get(),8)
        delbl.set(str(dec)) 
        binlbl.set(str(bin(dec)))
        hexlbl.set(str(hex(dec)))
        octlbl.set(str(oct(dec)))   

# ===============================================
Label(root,text='Coversion System',bg="#A9A9A9",font=('times new rommon',60,'bold'),fg='Black',relief=RIDGE).pack()

num_lbl=Label(root,text="Number : ",font=("times new rommon",30,"bold"),fg="Black").place(x=100,y=150)
num_ent=Entry(root,font=("times new rommon",20),width=15,textvariable=num).place(x=300,y=160)

num_lbl2=Label(root,text="Base : ",font=("times new rommon",30,"bold"),fg="Black").place(x=700,y=150)
num_ent2=Entry(root,font=("times new rommon",20),width=15,textvariable=base).place(x=850,y=160)

num_lbl3=Label(root,text="Decimal : ",font=("times new rommon",30,"bold"),fg="Black").place(x=100,y=250)
num_ent3=Entry(root,font=("times new rommon",20),width=15,state="readonly",textvariable=delbl).place(x=300,y=260)

num_lbl4=Label(root,text="Binary : ",font=("times new rommon",30,"bold"),fg="Black").place(x=100,y=350)
num_ent4=Entry(root,font=("times new rommon",20),width=15,state="readonly",textvariable=binlbl).place(x=300,y=360)

num_lbl5=Label(root,text="Hexa : ",font=("times new rommon",30,"bold"),fg="Black").place(x=100,y=450)
num_ent5=Entry(root,font=("times new rommon",20),width=15,state="readonly",textvariable=hexlbl).place(x=300,y=460)

num_lbl6=Label(root,text="Octal : ",font=("times new rommon",30,"bold"),fg="Black").place(x=100,y=550)
num_ent6=Entry(root,font=("times new rommon",20),width=15,state="readonly",textvariable=octlbl).place(x=300,y=560)

btn_con=Button(root,bg="#A9A9A9",text="Convert",font=("times new rommon",40,"bold"),width=7,fg="Black",command=convert).place(x=850,y=260)

btn_clr=Button(root,bg="#A9A9A9",text="Clear",font=("times new rommon",40,"bold"),width=7,fg="Black",command=clear).place(x=850,y=400)

btn_ex=Button(root,bg="#A9A9A9",text="Exit",font=("times new rommon",40,"bold"),width=7,fg="Black",command=exit).place(x=850,y=540)

root.mainloop()