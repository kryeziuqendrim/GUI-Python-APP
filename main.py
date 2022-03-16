import csv
from tkinter import *
from tkinter import ttk
import pandas as pd
from pandas import *
from tkinter import messagebox



class Main(object):
    def __init__(self,root):

        #Label and Input -- Path --
        label_path = Label(root, text="Enter the File path:",bg='white', font=(("Arial"),10)).grid(row=0, column=0, pady=10, sticky=E)
        self.PathEntry = Entry(root,width=40,bd=3)
        self.PathEntry.grid(row=0,padx=5 , column=1,sticky=W,columnspan=2)

        #Label -- Year --
        label_year = Label(root, text="Year:", bg='white', font=(("Arial"),10)).grid(row=2, column=0, sticky=E,columnspan=1)

        #Select-Input -- ComboBox --
        select_input = StringVar()
        self.comboBox = ttk.Combobox(root, width=10, textvariable=select_input, state='readonly')
        self.comboBox['values'] = (1,2,3,4,5)
        self.comboBox.grid(row=2, column=1,pady=15,padx=5, sticky=W)

        #Label and input -- Departments --
        label_department = Label(root, text='Department:',bg='white', font=(("Arial"),10)).grid(row=2,column=2, sticky=E)
        self.input_department = Entry(root, width=40, bd=3, relief=SUNKEN)
        self.input_department.grid(row=2, column=3, sticky=W, padx=35 )

        #Button --Displat and Clear and Save--
        self.button_display = Button(root, text='Display', width=5 ,command=self.display_fun)
        self.button_display.grid(row=4, column=0,sticky=W+E, pady=25,padx=5)
        self.button_clear = Button(root, text='Clear',width=5 , command=self.clean)
        self.button_clear.grid(row=4, column=1, sticky=W+E,pady=25,padx=5)
        self.button_save = Button(root, text='Save', width=5)
        self.button_save.grid(row=4, column=2, sticky=W+E,pady=25,padx=5)
        # self.button_save.bind("<Button-1>", self.funct_save)

        #Label --Warning and Courses--
        label_warning = Label(root, text='Warnings:',bg='white', font=(("Arial"),10)).grid(row=5,column=0, sticky=W, pady=15)
        label_courses = Label(root, text='Courses:',bg='white', font=(("Arial"),10)).grid(row=5,column=3, sticky=W, pady=15)

        #Listbox --Warning and Courses--
        self.Listbox_warning = Listbox(root,width=65,height=14, selectmode=MULTIPLE)
        self.Listbox_warning.place(x=2, y=220)
        self.Listbox_courses = Listbox(root,width=65,height=14, selectmode=MULTIPLE)
        self.Listbox_courses.place(x=400, y=220)
        self.Listbox_courses.bind("<<ListboxSelect>>", self.callback)

        self.a = []
        self.bb = []
        self.bbb = []
        self.bbbb = []


    def display_fun(self):
        self.Listbox_courses.delete(0,END)
        try:
            a = self.PathEntry.get()
            a = open(str(a), 'r')

            for row in a:
                self.a.append(row)
                rows_list = row.split(',')[0]
                row_list = rows_list.split(' ')[0]
                row_list2 = rows_list.split(' ')[1][0]

                if (row_list.startswith(self.input_department.get().upper()) and row_list.endswith(self.input_department.get().upper())) and row_list2.startswith((self.comboBox.get())):
                    list2 = self.Listbox_courses.get(0, END)
                    if row not in list2:
                        self.Listbox_courses.insert('end', row)
                        # print(row.split(',')[2])


        except EXCEPTION:
            messagebox.showinfo("Error!", "Something is wrong")
        # finally:OSError
        #     self.Listbox_courses.delete(0, END)



    def callback(self,event):
        try:
            self.arrays = []
            selection1 = event.widget.curselection()
            for i in selection1:
                self.selected2 = event.widget.get(i)
                list2 = self.Listbox_warning.get(0, END)
                selected4 = self.selected2.split(',')[2]
                selected5 = selected4.split(' ')[0]
                if selection1 and (len(selection1) <= 6):
                    selected3 = self.selected2.split(',')[0]
                    selected7 = self.selected2.split(',')[2]
                    #print(selected7)
                    if ('Added ' + selected3) not in list2:
                        self.Listbox_warning.insert(0, ('Added '+ selected3))


            def funct_save():
                global funct_save

                f = open('timefile.csv', 'w')
                writer = csv.writer(f)

                for a in self.Listbox_warning.get(0, END):
                    a= a[6:]
                    #print(a)
                    for e in self.a:
                        s = e.split(',')[0]
                        s = s.split(' ')[0]
                        c=e.split(',')[0]
                        c= c.split(' ')[1]
                        #print(c)
                        #print(self.s)
                        if a.startswith(s) and a.endswith(c):
                            self.arrays.append(e)

                writer.writerow(self.arrays)
                #print(self.arrays)

            self.button_save.config(command=funct_save)


            if len(event.widget.curselection()) >= 6:
                self.hello()

        except EXCEPTION:
            messagebox.showinfo('Error!', 'Something is wrong!')


    def hello(self):
        messagebox.showinfo('Wrong!', 'Carefully you selected more than 6!')
    def clean(self):
        #self.Listbox_courses.delete(0, END)
        self.Listbox_warning.delete(0, END)
def main():
    root = Tk()
    app = Main(root)
    root.title("GUI PROJECT")
    root.geometry("800x450+300+100")
    root.config(bg='#72FF2C')
    root.mainloop()

if __name__ == '__main__':
    main()
