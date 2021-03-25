# Program to make a simple 
# login screen 

from datetime import datetime
import tkinter as tk


root=tk.Tk()
root.title("HOTEL MANAGEMENT SYSTEM")
# setting the windows size
root.geometry("300x300+120+120")

# declaring string variable
# for storing name and password
fullname_var=tk.StringVar()
address_var=tk.StringVar()
cindate_var=tk.StringVar()
coutdate_var=tk.StringVar()


# defining a function that will
# get the name and password and 
# print them on the screen
def submit():
   fullname=fullname_var.get()
   address=address_var.get()
   #yearin, monthin, dayin = map(int,cindate_var.get().split('-'))
   #cindate=datetime.date(yearin,monthin,dayin)
   cindate=str(datetime.strptime(cindate_var.get(),'%d-%m-%Y'))
   #yearout, monthout, dayout = map(int,coutdate_var.get().split('-'))
   #coutdate=datetime.date(yearout,monthout,dayout)
   coutdate=str(datetime.strptime(coutdate_var.get(),'%d-%m-%Y'))
	
   print("Name : " + fullname)
   print("Address : " + address)
   print("Check In date : " + cindate)
   print("Check Out Date : " + coutdate)
	
   fullname_var.set("")
   address_var.set("")
   cindate_var.set("")
   coutdate_var.set("")
	
	
# name using widget Label
fullname_label = tk.Label(root, text = 'Full Name', font=('calibre',10, 'bold'))
address_label = tk.Label(root, text = 'Address', font = ('calibre',10,'bold'))
cindate_label = tk.Label(root, text = 'Check In Date', font = ('calibre',10,'bold'))
coutdate_label = tk.Label(root, text = 'Check Out Date', font = ('calibre',10,'bold'))

# name using widget Entry
fullname_entry = tk.Entry(root,textvariable = fullname_var, font=('calibre',10,'normal'))
address_entry=tk.Entry(root, textvariable = address_var, font = ('calibre',10,'normal'))
cindate_entry=tk.Entry(root, textvariable = cindate_var, font = ('calibre',10,'normal'))
coutdate_entry=tk.Entry(root, textvariable = coutdate_var, font = ('calibre',10,'normal'))

# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
fullname_label.grid(row=0,column=0)
fullname_entry.grid(row=0,column=1)
address_label.grid(row=1,column=0)
address_entry.grid(row=1,column=1)
cindate_label.grid(row=2,column=0)
cindate_entry.grid(row=2,column=1)
coutdate_label.grid(row=3,column=0)
coutdate_entry.grid(row=3,column=1)
sub_btn.grid(row=4,column=1)

# performing an infinite loop 
# for the window to display
root.mainloop()
