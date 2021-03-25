 

import tkinter as tk

root=tk.Tk()
root.title("HOTEL MANAGEMENT SYSTEM")
# setting the windows size
root.geometry("300x300+120+120")

# declaring string variable

first_CheckButtonVariable= tk.IntVar()
seccond_CheckButtonVariable= tk.IntVar()
third_CheckButtonVariable= tk.IntVar()
fourth_CheckButtonVariable= tk.IntVar()
fifth_CheckButtonVariable= tk.IntVar()
firstButtonVariable=tk.IntVar()
seccondButtonVariable=tk.IntVar()
thirdButtonVariable=tk.IntVar()
fourthButtonVariable=tk.IntVar()
fifthButtonVariable=tk.IntVar()

# defining a function that will

def submit():
   s=0
   if first_CheckButtonVariable.get()==1:
      s=s+3*firstButtonVariable.get()
   if seccond_CheckButtonVariable.get()==1:
      s=s+4*seccondButtonVariable.get()
   if third_CheckButtonVariable.get()==1:
      s=s+5*thirdButtonVariable.get()
   if fourth_CheckButtonVariable.get()==1:
      s=s+6*fourthButtonVariable.get()
   if fifth_CheckButtonVariable.get()==1:
      s=s+8*fifthButtonVariable.get()
   print(s)  
   
	
	
# name using widget Label
main_label1 = tk.Label(root, text = 'GAME MENU', font=('calibre',10, 'bold'))
main_label2 = tk.Label(root, text = 'Quantity', font=('calibre',10, 'bold'))

# name using widget Entry
first_checkbutton = tk.Checkbutton(root,variable = first_CheckButtonVariable, text="Shorts  Rs.3\-", font=('calibre',10,'normal'))
seccond_checkbutton = tk.Checkbutton(root,variable = seccond_CheckButtonVariable, text="Trousers    Rs.4\-", font=('calibre',10,'normal'))
third_checkbutton = tk.Checkbutton(root,variable = third_CheckButtonVariable, text="Shirt Rs.5\-", font=('calibre',10,'normal'))
fourth_checkbutton = tk.Checkbutton(root,variable = fourth_CheckButtonVariable, text="Jeans Rs6\-", font=('calibre',10,'normal'))
fifth_checkbutton = tk.Checkbutton(root,variable = fifth_CheckButtonVariable, text="Girlsuit  Rs8\-", font=('calibre',10,'normal'))
firstamount_entry=tk.Entry(root,textvariable=firstButtonVariable,font=('calibre',10,'normal'))
seccondamount_entry=tk.Entry(root,textvariable=seccondButtonVariable,font=('calibre',10,'normal'))
thirdamount_entry=tk.Entry(root,textvariable=thirdButtonVariable,font=('calibre',10,'normal'))
fourthamount_entry=tk.Entry(root,textvariable=fourthButtonVariable,font=('calibre',10,'normal'))
fifthamount_entry=tk.Entry(root,textvariable=fifthButtonVariable,font=('calibre',10,'normal'))
# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
main_label1.grid(row=0,column=0)
main_label2.grid(row=0,column=1)
first_checkbutton.grid(row=1,column=0)
firstamount_entry.grid(row=1,column=1)
seccond_checkbutton.grid(row=2,column=0)
seccondamount_entry.grid(row=2,column=1)
third_checkbutton.grid(row=3,column=0)
thirdamount_entry.grid(row=3,column=1)
fourth_checkbutton.grid(row=4,column=0)
fourthamount_entry.grid(row=4,column=1)
fifth_checkbutton.grid(row=5,column=0)
fifthamount_entry.grid(row=5,column=1)
sub_btn.grid(row=6,column=0)

# performing an infinite loop 
# for the window to display
root.mainloop()
