 

import tkinter as tk

root=tk.Tk()
root.title("HOTEL MANAGEMENT SYSTEM")
# setting the windows size
root.geometry("300x300+120+120")

# declaring string variable

RadioButtonVariable= tk.IntVar()
AmountEntryVariable=tk.IntVar()


# defining a function that will

def submit():
   if RadioButtonVariable.get()==1:
      print(6000*AmountEntryVariable.get())
   if RadioButtonVariable.get()==2:
      print(5000*AmountEntryVariable.get())
   if RadioButtonVariable.get()==3:
      print(4000*AmountEntryVariable.get())
   if RadioButtonVariable.get()==4:
      print(3000*AmountEntryVariable.get())
   
    
   
	
	
# name using widget Label
main_label1 = tk.Label(root, text = 'ROOM RENT', font=('calibre',10, 'bold'))
main_label2 = tk.Label(root, text = 'For How Many Nights Do You Want To Stay', font=('calibre',10, 'bold'))

# name using widget Entry
first_radiobutton = tk.Radiobutton(root,variable = RadioButtonVariable, value = 1 , text="Type A  Rs.6000\-", font=('calibre',10,'normal'))
seccond_radiobutton = tk.Radiobutton(root,variable = RadioButtonVariable, value = 2 , text="Type B  Rs.5000\-", font=('calibre',10,'normal'))
third_radiobutton = tk.Radiobutton(root,variable = RadioButtonVariable, value = 3 , text="Type C  Rs.4000\-", font=('calibre',10,'normal'))
fourth_radiobutton = tk.Radiobutton(root,variable = RadioButtonVariable, value = 4 , text="Type D  Rs.3000\-", font=('calibre',10,'normal'))

amount_entry=tk.Entry(root,textvariable=AmountEntryVariable,font=('calibre',10,'normal'))
# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
main_label1.grid(row=0,column=0)
main_label2.grid(row=0,column=1)
first_radiobutton.grid(row=1,column=0)
seccond_radiobutton.grid(row=2,column=0)
third_radiobutton.grid(row=3,column=0)
fourth_radiobutton.grid(row=4,column=0)
amount_entry.grid(row=1,column=1)

sub_btn.grid(row=5,column=0)

# performing an infinite loop 
# for the window to display
root.mainloop()
