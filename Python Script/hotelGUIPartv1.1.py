from tkinter import *
from datetime import datetime


fields = ('ACCOUNT','Full Name', 'Address', 'Check In date', 'Check Out Date')

def makeform(root, fields):
   entries = []
   for i in range(0,len(fields)):
      if i == 0:
         row = Frame(root)
         lab = Label(row, width=22, text=fields[i]+" ", anchor='w', font=('calibre',10, 'bold'))
         row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
         lab.pack(side = LEFT)
         continue
               
      row = Frame(root)
      lab = Label(row, width=22, text=fields[i]+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries.append(ent)
   return entries

def submit(entries):
   fullname=entries[0].get()
   address=entries[1].get()
   cindate=str(datetime.strptime(entries[2].get(),'%d-%m-%Y'))
   coutdate=str(datetime.strptime(entries[3].get(),'%d-%m-%Y'))
   print("Name : " + fullname)
   print("Address : " + address)
   print("Check In date : " + cindate)
   print("Check Out Date : " + coutdate)
   
   

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'Submit',
      command=(lambda e = ents: submit(e)))
   b1.pack(side = LEFT, padx = 5, pady = 5)
   
   b3 = Button(root, text = 'Quit', command = root.quit)
   b3.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()
