from tkinter import Tk
from tkinter.ttk import Notebook, Frame, Label
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
tab_control = Notebook(window)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
 
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
 
lbl1 = Label(tab1, text= 'label1')
lbl1.grid(column=0, row=0)
 
lbl2 = Label(tab2, text= 'label2')
lbl2.grid(column=0, row=0)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()