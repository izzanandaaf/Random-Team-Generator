import tkinter
import tkinter.messagebox
import random

def main():
    mainform = tkinter.Tk()
    mainform.title("Random Team Generator")
    mainform.maxsize(342,342)
    mainform.minsize(342,342)
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

    def check_my_list():
        if len(memb_list) != 0:
            listform = tkinter.Tk()
            listform.title('My List')
            my_list = tkinter.Label(
                                listform, 
                                text="MY LIST", 
                                font=('',10,'underline')
                                )
            my_list.grid(row=0, column=2, columnspan=2, padx=90, pady=6)
            for n in range(len(memb_list)):
                num_list = tkinter.Label(
                    listform, 
                    text=str(n+1)+'.'
                    )
                num_list.grid(row=(n+1), column=1, sticky=tkinter.W, padx=4)
                name_list = tkinter.Label(
                    listform, 
                    text=str(memb_list[n])
                    )
                name_list.grid(row=(n+1), column=2, sticky=tkinter.W, padx=4)
            listform.mainloop()
        else:
            tkinter.messagebox.showinfo("Error", 'No data added to your list.')
            
    def reset_list():
        if len(memb_list) != 0:
            memb_list.clear()
            tkinter.messagebox.showinfo("Info", 'List has been reset succesfuly.')
        else:
            tkinter.messagebox.showinfo("Error", 'No data found on your list.')

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
                    text="Check list", 
                    command=check_my_list, 
                    width=10
                    )
    b2.grid(row=3, column=3, sticky=tkinter.W+tkinter.E)

    b3 = tkinter.Button(
                    mainform, 
                    text="Reset list", 
                    command=reset_list,
                    width=10
                    )
    b3.grid(row=3, column=4, sticky=tkinter.W+tkinter.E)

    tkinter.Label(mainform, text="").grid(row=4)

    l3 = tkinter.Label(
                    mainform, 
                    text="SETTING", 
                    font=('',10,'underline')
                    )
    l3.grid(row=5, column=1, columnspan=6, sticky=tkinter.W+tkinter.E)

    l4 = tkinter.Label(
                    mainform, 
                    text='Number of Groups: '
                    )
    l4.grid(row=6, column=1, columnspan=4, sticky=tkinter.W+tkinter.E)

    e2 = tkinter.Entry(
                    mainform, 
                    textvariable=var2,
                    width=6
                    )
    e2.grid(row=6, column=4)

    b4 = tkinter.Button(
                    mainform, 
                    text="Start", 
                    width=10, 
                    command=start_random
                    )
    b4.grid(row=7, column=1, columnspan=6, pady=34)

    b5 = tkinter.Button(
                    mainform, 
                    text="i", 
                    width=2, 
                    command=credit
                    )
    b5.grid(row=8, column=1, columnspan=2, sticky=tkinter.W, padx=4, pady=10)

    mainform.mainloop()

if __name__ == '__main__':
    main()