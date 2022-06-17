from fileinput import filename
import tkinter
import tkinter.messagebox
from tkinter import ttk
import random
import csv
import os

def main():
    mainform = tkinter.Tk()
    mainform.title("Random Team Generator")
    mainform.maxsize(342,490)
    mainform.minsize(342,490)
    var1 = tkinter.StringVar()
    var2 = tkinter.StringVar()
    memb_list = []
    path = os.path.dirname(os.path.realpath(__file__))

    def use_listA():
        memb_list.clear()
        all_list = open("{}\\list_library\\datalistA.csv".format(path),"r")
        csv_reader = csv.reader(all_list)
        for row in csv_reader:
            for i in range(len(row)):
                memb_list.append(row[i])
        if len(memb_list) == 0:
            tkinter.messagebox.showinfo("Info", '"List A" is still empty.\nYour list is now empty.')
        else:
            tkinter.messagebox.showinfo("Info", 'You are now using the data stored in the "List A".')
    def use_listB():
        memb_list.clear()
        all_list = open("{}\\list_library\\datalistB.csv".format(path),"r")
        csv_reader = csv.reader(all_list)
        for row in csv_reader:
            for i in range(len(row)):
                memb_list.append(row[i])
        if len(memb_list) == 0:
            tkinter.messagebox.showinfo("Info", '"List B" is still empty.\nYour list is now empty.')
        else:
            tkinter.messagebox.showinfo("Info", 'You are now using the data stored in the "List B".')
    def use_listC():
        memb_list.clear()
        all_list = open("{}\\list_library\\datalistC.csv".format(path),"r")
        csv_reader = csv.reader(all_list)
        for row in csv_reader:
            for i in range(len(row)):
                memb_list.append(row[i])
        if len(memb_list) == 0:
            tkinter.messagebox.showinfo("Info", '"List C" is still empty.\nYour list is now empty.')
        else:
            tkinter.messagebox.showinfo("Info", 'You are now using the data stored in the "List C".')
    def save_listA():
        if len(memb_list) == 0:
            A = open("{}\\list_library\\datalistA.csv".format(path),'r+')
            A.truncate(0)
        else:
            with open("{}\\list_library\\datalistA.csv".format(path), 'w', newline='') as sA:
                writerA = csv.writer(sA)
                writerA.writerow(memb_list)
        tkinter.messagebox.showinfo("Info", 'Data saved in "List A" successfuly.')
    def save_listB():
        if len(memb_list) == 0:
            B = open("{}\\list_library\\datalistB.csv".format(path),'r+')
            B.truncate(0)
        else:
            with open("{}\\list_library\\datalistB.csv".format(path), 'w',newline='') as sB:
                writerB = csv.writer(sB)
                writerB.writerow(memb_list)
        tkinter.messagebox.showinfo("Info", 'Data saved in "List B" successfuly.')
    def save_listC():
        if len(memb_list) == 0:
            C = open("{}\\list_library\\datalistC.csv".format(path),'r+')
            C.truncate(0)
        else:
            with open("{}\\list_library\\datalistC.csv".format(path), 'w',newline='') as sC:
                writerC = csv.writer(sC)
                writerC.writerow(memb_list)
        tkinter.messagebox.showinfo("Info", 'Data saved in "List C" successfuly.')
    def add_to_list():
        if var1.get() != '':
            memb_list.append(var1.get())
            tkinter.messagebox.showinfo("Info", f'"{var1.get()}" added succesfully.')
            var1.set('')
        else:
            tkinter.messagebox.showinfo("Error", 'No data added.')
    def edit_list():
        def del_all():
            my_listbox.delete(0,"end")
            memb_list.clear()
            tkinter.messagebox.showinfo("Info", 'All data deleted succesfuly.')
        def del_selection():
            if len(my_listbox.curselection()) == 0:
                tkinter.messagebox.showinfo("Info", 'You have not selected any data to delete.')
            else:
                for data in reversed(my_listbox.curselection()):
                    my_listbox.delete(data)
                    memb_list.pop(data)
                tkinter.messagebox.showinfo("Info", 'Selected data deleted succesfuly.')
        if len(memb_list) != 0:
            listform = tkinter.Tk()
            listform.title('My List')
            listform.maxsize(215,350)
            listform.minsize(215,350)
            judul = tkinter.Label(
                                listform, 
                                text="MY LIST", 
                                font=('',10,'bold')
                                )
            judul.pack(pady=10)
            my_frame = tkinter.Frame(listform)
            my_sb = tkinter.Scrollbar(my_frame,orient="vertical")
            my_listbox = tkinter.Listbox(my_frame,width=28,yscrollcommand=my_sb.set,selectmode="extended")
            my_sb.config(command=my_listbox.yview)
            my_sb.pack(side="right",fill="y")
            my_frame.pack()
            my_listbox.pack()
            f_btn = tkinter.Frame(listform)
            f_btn.pack()
            delbtn = tkinter.Button(f_btn,text='Delete Item(s)',width=11,command=del_selection)
            delbtn.pack(side='left',anchor='w')
            delallbtn = tkinter.Button(f_btn,text='Delete All',width=11,command=del_all)
            delallbtn.pack()
            tkinter.Label(listform,text="").pack()
            tkinter.Label(listform,text="Save as:").pack()
            f_btn2 = tkinter.Frame(listform)
            f_btn2.pack()
            saA = tkinter.Button(f_btn2,text='List A',width=11,command=save_listA)
            saA.pack(side='left',anchor='w')
            saB = tkinter.Button(f_btn2,text='List B',width=11,command=save_listB)
            saB.pack(side='right',anchor='w')
            saB = tkinter.Button(listform,text='List C',width=11,command=save_listC)
            saB.pack()
            for item in memb_list:
                my_listbox.insert("end", item)
            listform.mainloop()
        else:
            tkinter.messagebox.showinfo("Error", 'No data added to your list.')

    def start_random():
        if len(memb_list) == 0:
            tkinter.messagebox.showinfo("Error", 
                'Your list is still empty.\nPlease check your list again and enter your data into the list!')
        elif var2.get() == '':
            tkinter.messagebox.showinfo("Error", 'You must set the number of group(s).')
        elif var2.get() != '':
            try:
                cek_tipe = int(var2.get())
            except ValueError:
                tkinter.messagebox.showinfo("Error", 'You can only set the number of group with integers from 1 or above.')
            if int(var2.get()) <= 0:
                tkinter.messagebox.showinfo("Error", 'You can only set the number of group with integers from 1 or above.')
            elif int(var2.get()) > len(memb_list):
                tkinter.messagebox.showinfo("Error", 'The number of groups cannot exceed the number of registered names.')
            elif int(var2.get()) > 0:
                memb = len(memb_list) // int(var2.get())
                overage = len(memb_list) % int(var2.get())
                checker = []
                tkinter.messagebox.showinfo("Info", 'Randomization successful.')
                root = tkinter.Tk()
                root.title("Groups Board")
                root.maxsize(400, 450)
                root.minsize(400, 450)
                frame1 = tkinter.Frame(root)
                frame1.pack(fill="both", expand=1)
                canvas1 = tkinter.Canvas(frame1)
                canvas1.pack(side="left", fill="both", expand=1)
                sb2 = ttk.Scrollbar(frame1, orient="vertical", command=canvas1.yview)
                sb2.pack(side="right", fill="y")
                canvas1.configure(yscrollcommand=sb2.set)
                canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
                secframe = tkinter.Frame(canvas1)
                canvas1.create_window((0,0), window=secframe, anchor="nw")
                def dstrbution():
                    num = random.randrange(len(memb_list))
                    if len(checker) == 0:
                        tkinter.Label(
                                    secframe, 
                                    text=memb_list[num],
                                    width=46
                                    ).pack()
                        checker.append(num)
                    else:
                        for i in range(len(checker)):
                            if num == checker[i]:
                                cek = False
                                break
                            else:
                                cek = True
                        if cek:
                            tkinter.Label(
                                        secframe, 
                                        text=memb_list[num],
                                        width=46
                                        ).pack()
                            checker.append(num)
                        else:
                            dstrbution()
                tkinter.Label(secframe, text='GROUPS BOARD', width=25, font=('', 16, "bold")).pack(pady=10)
                for no_kel in range(int(var2.get())):
                    tkinter.Label(
                                secframe, 
                                text=f"TEAM {no_kel+1}", 
                                font=('',10,'bold underline'),
                                width=46
                                ).pack()
                    if no_kel < overage:
                        for x in range(memb+1):
                            dstrbution()
                    else:
                        for x in range(memb):
                            dstrbution()
                    tkinter.Label(secframe, text='', width=46).pack()
                var2.set('')
                root.mainloop()

    def credit():
        crdt_txt = (
'''Created by:
> Erwin Agil Nur Rohmat
> Izzananda Adimas Faza
> Kanaya Aurellia Hanieputri
> Maulidan Mirza Tsany Gozali
> Najwa Mumtaz'''
        )
        tkinter.messagebox.showinfo("Credit", crdt_txt)

    l1 = tkinter.Label(
                    mainform, 
                    text="RANDOM TEAM GENERATOR", 
                    font=('', 16, "bold italic")
                    )
    l1.grid(row=0, column=1, columnspan=6, sticky=tkinter.W+tkinter.E, pady=18)

    l2 = tkinter.Label(
                    mainform, 
                    text="INPUT", 
                    font=('',10,'underline')
                    )
    l2.grid(row=1, column=1, columnspan=6, sticky=tkinter.W+tkinter.E)

    e1 = tkinter.Entry(
                    mainform, 
                    textvariable=var1,
                    width=48
                    )
    e1.grid(row=2, column=1, columnspan=5, padx=4)

    b1 = tkinter.Button(
                    mainform, 
                    text=" + ", 
                    command=add_to_list
                    )
    b1.grid(row=2, column=6, sticky=tkinter.W)

    b2 = tkinter.Button(
                    mainform, 
                    text="Check my list", 
                    command=edit_list, 
                    width=15
                    )
    b2.grid(row=3, column=1, columnspan=6)

    tkinter.Label(mainform, text="").grid(row=4)

    l3 = tkinter.Label(
                    mainform, 
                    text="LIBRARY", 
                    font=('',10,'underline')
                    )
    l3.grid(row=5, column=1, columnspan=6, sticky=tkinter.W+tkinter.E)

    l3 = tkinter.Label(
                    mainform, 
                    text="Select the saved list that you will use!"
                    )
    l3.grid(row=6, column=1, columnspan=6, sticky=tkinter.W+tkinter.E)

    tkinter.Button(mainform,text="List A",width=15,command=use_listA).grid(row=7,column=1,columnspan=6)

    tkinter.Button(mainform,text="List B",width=15,command=use_listB).grid(row=8,column=1,columnspan=6)

    tkinter.Button(mainform,text="List C",width=15,command=use_listC).grid(row=9,column=1,columnspan=6)

    tkinter.Label(mainform, text="").grid(row=10)

    tkinter.Label(mainform, text="SETTING", font=('',10,'underline')).grid(row=11, column=1, columnspan=6, sticky=tkinter.W+tkinter.E)
    
    l4 = tkinter.Label(
                    mainform, 
                    text='Number of Groups:'
                    )
    l4.grid(row=12, column=3, sticky=tkinter.W)

    e2 = tkinter.Entry(
                    mainform, 
                    textvariable=var2,
                    width=11
                    )
    e2.grid(row=12, column=3, columnspan=2, sticky=tkinter.E)
    
    b4 = tkinter.Button(
                    mainform, 
                    text="Start", 
                    width=10, 
                    command=start_random
                    )
    b4.grid(row=13, column=1, columnspan=6, pady=34)

    b5 = tkinter.Button(
                    mainform, 
                    text="i", 
                    width=2, 
                    command=credit
                    )
    b5.grid(row=14, column=1, columnspan=2, sticky=tkinter.W, padx=4, pady=10)

    mainform.mainloop()


if __name__ == '__main__':
    main()