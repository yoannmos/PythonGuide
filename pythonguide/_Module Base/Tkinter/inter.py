import tkinter

fenetre = tkinter.Tk()

# fonction appellée lorsque l'utilisateur presse une touche
def clavier(event):
    global coords

    touche = event.keysym

    if touche == "Up":
        coords = (coords[0], coords[1] - 10)
    elif touche == "Down":
        coords = (coords[0], coords[1] + 10)
    elif touche == "Right":
        coords = (coords[0] + 10, coords[1])
    elif touche == "Left":
        coords = (coords[0] -10, coords[1])
    # changement de coordonnées pour le rectangle
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)

# création du canvas
canvas = tkinter.Canvas(fenetre, width=250, height=250, bg="ivory")
# coordonnées initiales
coords = (0, 0)
# création du rectangle
rectangle = canvas.create_rectangle(0,0,25,25,fill="violet")
# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()

fenetre.mainloop()