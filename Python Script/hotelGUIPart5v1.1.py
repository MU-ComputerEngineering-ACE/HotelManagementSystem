 

from tkinter import *

fields = ("Type A  Rs.6000\-", "Type B  Rs.5000\-", "Type C  Rs.4000\-", "Type D  Rs.3000\-")





def makeform(root, fields):
   entries = []
   var = IntVar()
   for i in range(0,len(fields)):
      row = Frame(root)
      
      radio = Radiobutton(row,variable=var, value= i+1)
      lab = Label(row, width=22, text=fields[i]+" ", anchor='w')
      if i == 0:
          ent = Entry(row)
          ent.insert(0,"")
          ent.pack(side = RIGHT, expand = YES, fill = X)
          entries.append(ent)
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      radio.pack(side = LEFT)
      lab.pack(side = LEFT)
      
      
   return entries,var
# defining a function that will


def submit(entries,var):
   if var.get()==1:
      print(6000*int(entries[0].get()))
   if var.get()==2:
      print(5000*int(entries[0].get()))
   if var.get()==3:
      print(4000*int(entries[0].get()))
   if var.get()==4:
      print(3000*int(entries[0].get()))
   
	
	

if __name__ == '__main__':
   root = Tk()
   ents,var = makeform(root, fields)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'Submit',
      command=(lambda e = ents,v = var: submit(e,v)))
   b1.pack(side = LEFT, padx = 5, pady = 5)
   
   b3 = Button(root, text = 'Quit', command = root.quit)
   b3.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()
