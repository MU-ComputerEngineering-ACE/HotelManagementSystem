 

from tkinter import *

fields = ("Water Rs.20\-", "Tea  Rs.10\-", "Breakfast   Rs.90\-", "Lunch  Rs110\-", "Dinner   Rs150\-")





def makeform(root, fields):
   entries = []
   checks = []
   for i in range(0,len(fields)):
      row = Frame(root)
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
      
   return entries,checks
# defining a function that will


def submit(entries,checks):
   ansentry=[]
   checkentry=[]
   for i in range(0,len(fields)):
      ansentry.append(entries[i].get())
      checkentry.append(checks[i].get())
   s=0
   if checkentry[0]==1:
      s=s+20*int(ansentry[0])
   if checkentry[1]==1:
      s=s+10*int(ansentry[1])
   if checkentry[2]==1:
      s=s+90*int(ansentry[2])
   if checkentry[3]==1:
      s=s+110*int(ansentry[3])
   if checkentry[4]==1:
      s=s+150*int(ansentry[4])
   print(s)
   
	
	

if __name__ == '__main__':
   root = Tk()
   ents,checks = makeform(root, fields)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'Submit',
      command=(lambda e = ents,c = checks: submit(e,c)))
   b1.pack(side = LEFT, padx = 5, pady = 5)
   
   b3 = Button(root, text = 'Quit', command = root.quit)
   b3.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()
