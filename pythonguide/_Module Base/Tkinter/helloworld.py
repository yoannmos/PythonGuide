import tkinter

window = tkinter.Tk()

# label
label = tkinter.Label(window, text="Helloooo")
label2 = tkinter.Label(window, text="Texte par défaut", bg="yellow")

# button
button = tkinter.Button(window, text="close", command=window.quit)

# checkbutton
checkbutton = tkinter.Checkbutton(window, text="New?")

# radiobutton
value = tkinter.StringVar() 
bouton1 = tkinter.Radiobutton(window, text="Oui", variable=value, value=1)
bouton2 = tkinter.Radiobutton(window, text="Non", variable=value, value=2)

#entry
value = tkinter.StringVar() 
value.set("texte par défaut")
entry = tkinter.Entry(window, textvariable=str, width=30)

# lists
lists = tkinter.Listbox(window)
lists.insert(1, "Python")
lists.insert(2, "PHP")
lists.insert(3, "jQuery")
lists.insert(4, "CSS")
lists.insert(5, "Javascript")

# canvas
canvas = tkinter.Canvas(window, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")

# create_arc()        :  arc de cercle
# create_bitmap()     :  bitmap
# create_image()      :  image
# create_line()       :  ligne
# create_oval()       :  ovale
# create_polygon()    :  polygone
# create_rectangle()  :  rectangle 
# create_text()       :  texte
# create_window()     :  fenetre



label.pack()
label2.pack()
tkinter.Button(window, text="ALALALALA", cursor="circle").pack()
button.pack()
checkbutton.pack()
bouton1.pack()
bouton2.pack()
entry.pack()
lists.pack()
canvas.pack()

window.mainloop()
