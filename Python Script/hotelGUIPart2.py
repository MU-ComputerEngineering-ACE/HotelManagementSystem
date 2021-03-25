 

from tkinter import *

root=Tk()
root.title("HOTEL MANAGEMENT SYSTEM")
# setting the windows size
root.geometry("300x300+120+120")

# declaring string variable

first_CheckButtonVariable= IntVar()
seccond_CheckButtonVariable= IntVar()
third_CheckButtonVariable= IntVar()
fourth_CheckButtonVariable= IntVar()
fifth_CheckButtonVariable= IntVar()
firstButtonVariable=IntVar()
seccondButtonVariable=IntVar()
thirdButtonVariable=IntVar()
fourthButtonVariable=IntVar()
fifthButtonVariable=IntVar()

# defining a function that will

def submit():
   s=0
   if first_CheckButtonVariable.get()==1:
      s=s+20*firstButtonVariable.get()
   if seccond_CheckButtonVariable.get()==1:
      s=s+10*seccondButtonVariable.get()
   if third_CheckButtonVariable.get()==1:
      s=s+90*thirdButtonVariable.get()
   if fourth_CheckButtonVariable.get()==1:
      s=s+110*fourthButtonVariable.get()
   if fifth_CheckButtonVariable.get()==1:
      s=s+150*fifthButtonVariable.get()
   print(s)
     
   
	
	
# name using widget Label
main_label1 = Label(root, text = 'RESTAURANT MENU', font=('calibre',10, 'bold'))
main_label2 = Label(root, text = 'Quantity', font=('calibre',10, 'bold'))
first_label= Label(root, text="Water Rs.20\-", font=('calibre',10,'normal'))
seccond_label= Label(root, text="Tea  Rs.10\-", font=('calibre',10,'normal'))
third_label= Label(root, text="Breakfast   Rs.90\-", font=('calibre',10,'normal'))
fourth_label= Label(root, text="Lunch  Rs110\-", font=('calibre',10,'normal'))
fifth_label= Label(root, text="Dinner   Rs150\-", font=('calibre',10,'normal'))

# name using widget Entry
first_checkbutton = Checkbutton(root,variable = first_CheckButtonVariable)
seccond_checkbutton = Checkbutton(root,variable = seccond_CheckButtonVariable)
third_checkbutton = Checkbutton(root,variable = third_CheckButtonVariable)
fourth_checkbutton = Checkbutton(root,variable = fourth_CheckButtonVariable)
fifth_checkbutton = Checkbutton(root,variable = fifth_CheckButtonVariable)
firstamount_entry=Entry(root,textvariable=firstButtonVariable,font=('calibre',10,'normal'))
seccondamount_entry=Entry(root,textvariable=seccondButtonVariable,font=('calibre',10,'normal'))
thirdamount_entry=Entry(root,textvariable=thirdButtonVariable,font=('calibre',10,'normal'))
fourthamount_entry=Entry(root,textvariable=fourthButtonVariable,font=('calibre',10,'normal'))
fifthamount_entry=Entry(root,textvariable=fifthButtonVariable,font=('calibre',10,'normal'))
# creating a button using the widget 
# Button that will call the submit function 
sub_btn=Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
main_label1.grid(row=0,column=0)
main_label2.grid(row=0,column=2)
first_checkbutton.grid(row=1,column=0)
first_label.grid(row=1,column=1)
firstamount_entry.grid(row=1,column=2)
seccond_checkbutton.grid(row=2,column=0)
seccond_label.grid(row=2,column=1)
seccondamount_entry.grid(row=2,column=2)
third_checkbutton.grid(row=3,column=0)
third_label.grid(row=3,column=1)
thirdamount_entry.grid(row=3,column=2)
fourth_checkbutton.grid(row=4,column=0)
fourth_label.grid(row=4,column=1)
fourthamount_entry.grid(row=4,column=2)
fifth_checkbutton.grid(row=5,column=0)
fifth_label.grid(row=5,column=1)
fifthamount_entry.grid(row=5,column=2)
sub_btn.grid(row=6,column=0)

# performing an infinite loop 
# for the window to display
root.mainloop()
