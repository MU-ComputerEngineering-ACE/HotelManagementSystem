from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import os


fields = (
   "ACCOUNT",
   "Full Name", "Address", "Check In date", "Check Out Date","",
   "RESTAURANT MENU",
   "Water Rs.20\-", "Tea  Rs.10\-","Breakfast   Rs.90\-", "Lunch  Rs110\-", "Dinner   Rs150\-", "",
   "LAUNDRY MENU",
   "Shorts  Rs.3\-", "Trousers   Rs.4\-", "Shirt Rs.5\-", "Jeans Rs6\-","Girlsuit  Rs8\-","",
   "GAME MENU",
   "Table tennis  Rs.60\-", "Bowling   Rs.80\-", "Snooker Rs.70\-", "Video games Rs90\-","Pool  Rs50\-","",   
   "ROOM RENT",
   "Type A  Rs.6000\-", "Type B  Rs.5000\-", "Type C  Rs.4000\-", "Type D  Rs.3000\-", "",

)

def makeform(root, fields):
   entries = []
   checks = []
   vars = IntVar()
    


   for i in range(0,len(fields)):
      row = Frame(root)
      

      if i in [0,5,6,12,13,19,20,26,27,32]:
         #row = Frame(root)
         lab = Label(row, width=22, text=fields[i]+" ", anchor='w', font=('calibre',10, 'bold'))
         row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
         lab.pack(side = LEFT)
         continue
      if i>27:
         #row = Frame(root)      
         radio = Radiobutton(row,variable=vars, value= i-27)
         lab = Label(row, width=22, text=fields[i]+" ", anchor='w')
         if i == 28:
            ent = Entry(row)
            ent.insert(0,"")
            ent.pack(side = RIGHT, expand = YES, fill = X)
            entries.append(ent)
            
         row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
         radio.pack(side = LEFT)
         lab.pack(side = LEFT)
         continue
      if i>6:
         #row = Frame(root)
         var = IntVar()
         check = Checkbutton(row,variable=var)
         lab = Label(row, width=22, text=fields[i]+" ", anchor='w')
         ent = Entry(row)
         ent.insert(0,"")
         row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
         check.pack(side = LEFT)
         lab.pack(side = LEFT)
         ent.pack(side = RIGHT, expand = YES, fill = X)
         entries.append(ent)
         checks.append(var)
         continue         
      #row = Frame(root)
      lab = Label(row, width=22, text=fields[i]+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries.append(ent)
   return entries,checks,vars

def submit(entries,checks,vars):
   fullname=entries[0].get()
   address=entries[1].get()
   cindate=str(datetime.strptime(entries[2].get(),'%d-%m-%Y'))
   coutdate=str(datetime.strptime(entries[3].get(),'%d-%m-%Y'))

   with open("perfLog.txt", "a+") as f:
      f.write("\n\nName : %s" %fullname)
      f.write("\nAddress : %s" %address)
      f.write("\nCheck In date : %s" %cindate)
      f.write("\nCheck Out Date : %s" %coutdate)
		
		
		
   
   print("Name : " + fullname)
   print("Address : " + address)
   print("Check In date : " + cindate)
   print("Check Out Date : " + coutdate)

   
   checkentry=[]
   for i in range(0,15):
      checkentry.append(checks[i].get())
   
   checkers=0
   
   if checkentry[0]==1:
      checkers=checkers+20*int(entries[4].get())
   if checkentry[1]==1:
      checkers=checkers+10*int(entries[5].get())
   if checkentry[2]==1:
      checkers=checkers+90*int(entries[6].get())
   if checkentry[3]==1:
      checkers=checkers+110*int(entries[7].get())
   if checkentry[4]==1:
      checkers=checkers+150*int(entries[8].get())

   if checkentry[5]==1:
      checkers=checkers+3*int(entries[9].get())
   if checkentry[6]==1:
      checkers=checkers+4*int(entries[10].get())
   if checkentry[7]==1:
      checkers=checkers+5*int(entries[11].get())
   if checkentry[8]==1:
      checkers=checkers+6*int(entries[12].get())
   if checkentry[9]==1:
      checkers=checkers+8*int(entries[13].get())

   if checkentry[10]==1:
      checkers=checkers+60*int(entries[14].get())
   if checkentry[11]==1:
      checkers=checkers+80*int(entries[15].get())
   if checkentry[12]==1:
      checkers=checkers+70*int(entries[16].get())
   if checkentry[13]==1:
      checkers=checkers+90*int(entries[17].get())
   if checkentry[14]==1:
      checkers=checkers+50*int(entries[18].get())

   messagebox.showinfo("Checkers", "Checkers: %d" %checkers)
   
   print(checkers)
   
   round=0

   if vars.get()==1:
      round=6000*int(entries[19].get())
   if vars.get()==2:
      round=5000*int(entries[19].get())
   if vars.get()==3:
      round=4000*int(entries[19].get())
   if vars.get()==4:
      round=3000*int(entries[19].get())

   total=round+checkers

   print(total) 

def openLog():
   #display Log
   f=open("perfLog.text")
   messagebox.showinfo("Log",f.read())

def exitapp():
   res=messagebox.askquestion("Exit", "Are you sure to exit?")
   if res == 'yes':
      exit()

def clearapp(entries):
   for i in entries:
      print(i)
      #i.delete("1.0", END)
      

   

if __name__ == '__main__':
   root = Tk()
   root.title("HOTEL MANAGEMENT SYSTEM")

   width = root.winfo_screenwidth()
   height = root.winfo_screenheight()
   x = (width / 2) - (800 / 2)
   y = (height / 2) - (650 / 2)
   root.resizable(width=True, height=True)
   root.geometry('%dx%d+%d+%d' % (800, 600, x, y))

   #Create Main Frame.
   main_frame=Frame(root)
   main_frame.pack(fill=BOTH, expand=1)

   #Create a Canvas.
   my_canvas=Canvas(main_frame)
   my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

   #Add ScrollBar to the Canvas.
   my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
   my_scrollbar.pack(side=RIGHT, fill=Y)



   #Configure the Canvas
   my_canvas.configure(yscrollcommand=my_scrollbar.set)
   my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

   #Create Another Frame Inside Canvas
   second_frame = Frame(my_canvas)

   #Add that new frame to a window in the canvas
   my_canvas.create_window((0,0), window=second_frame, anchor="nw")
   
   ents, checks, vars = makeform(second_frame, fields)
   second_frame.bind('<Return>', (lambda event, e = ents: fetch(e)))

   menubar = Menu(second_frame)
   filemenu = Menu(menubar, tearoff=0)
   menubar.add_cascade(label="File", menu=filemenu)
   filemenu.add_command(label="New")
   filemenu.add_command(label="Clear", command=clearapp(ents))
   filemenu.add_command(label="Open Log", command=openLog())
   filemenu.add_separator()
   filemenu.add_command(label="Exit", command=exitapp)

   

   root.config(menu=menubar)
   b1 = Button(second_frame, text = 'Submit',
      command=(lambda e = ents, c= checks, v=vars: submit(e,c,v)))
   b1.pack(side = LEFT, padx = 5, pady = 5)
   
   #b3 = Button(second_frame, text = 'Quit', command = root.quit)
   #b3.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()
