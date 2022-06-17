import tkinter
import tkinter.messagebox
import random

def main():
    mainform = tkinter.Tk()
    mainform.title("Random Team Generator")
    mainform.maxsize(342,490)
    mainform.minsize(342,490)
    var1 = tkinter.StringVar()
    var2 = tkinter.StringVar()
    memb_list = []

    def add_to_list():
        if var1.get() != '':
            memb_list.append(var1.get())
            tkinter.messagebox.showinfo("Info", f'"{var1.get()}" added succesfuly.')
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
                resultform = tkinter.Tk()
                resultform.title("Result")
                def dstrbution():
                    num = random.randrange(len(memb_list))
                    if len(checker) == 0:
                        tkinter.Label(
                                    resultform, 
                                    text=memb_list[num]
                                    ).grid(padx=15)
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
                                        resultform, 
                                        text=memb_list[num]
                                        ).grid(padx=15)
                            checker.append(num)
                        else:
                            dstrbution()
                for no_kel in range(int(var2.get())):
                    tkinter.Label(resultform, text='').grid(padx=50)
                    tkinter.Label(
                                resultform, 
                                text=f"TEAM {no_kel+1}", 
                                font=('',10,'bold underline')
                                ).grid(padx=100)
                    if no_kel < overage:
                        for x in range(memb+1):
                            dstrbution()
                    else:
                        for x in range(memb):
                            dstrbution()
                tkinter.Label(resultform, text='').grid(padx=50)
                var2.set('')
                resultform.mainloop()

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

    tkinter.Button(mainform,text="List A",width=15).grid(row=7,column=1,columnspan=6)

    tkinter.Button(mainform,text="List B",width=15).grid(row=8,column=1,columnspan=6)

    tkinter.Button(mainform,text="List C",width=15).grid(row=9,column=1,columnspan=6)

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
