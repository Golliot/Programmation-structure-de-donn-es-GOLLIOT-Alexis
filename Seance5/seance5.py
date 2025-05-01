from tkinter import Tk, Canvas, Button, Frame, Label

Tab = [2, 1, 1, 0, 2]
listeCouleurs = ['black', 'red', 'blue', 'green']

#Fonction de l'exo 4
def permuteColor(): #J'ai choisi de fixer les grandeurs pour me simplifier la tâche
    global listeCouleurs
    L = listeCouleurs.copy()
    for i in range(4):
        L[i] = listeCouleurs[(i+1) % 4]
    listeCouleurs = L
    entrelacs(canvas, Tab, 4, listeCouleurs, 50, 50)

#Initialisation
root = Tk()
root.geometry("600x400")

#Initialisation des widgets
canvas = Canvas(root, width= 600, height= 400, bg= 'light grey')
UserInterface = Canvas(root, width= 600, height= 150, bg= 'black')
quitter = Button(root, text= 'Quitter', command= exit, fg= 'white', bg= 'dark grey', relief= 'raised')
colors = Button(root, text= 'Colors', command= permuteColor, fg= 'white', bg= 'dark grey', relief= 'raised')
croisements = Label(root, text= 'Croisements', fg= 'white', bg= 'black', relief= 'raised', font= ('Arial', 15))
liste = Label(root, text= (' '+str(Tab)+' '), fg= 'white', bg= 'black', relief= 'raised', font= ('Arial', 15))

#Placement des widgets
quitter.place(x= 125, y= 350, anchor= 'center')
colors.place(x= 475, y= 350, anchor= 'center')
croisements.place(x= 125, y= 280, anchor= 'center')
liste.place(x= 475, y= 280, anchor= 'center')
UserInterface.pack(side= 'bottom')
canvas.pack()

def read_word(canvas, mot, h, w, x0, y0, couleur):
    (x, y) = (x0, y0)
    for c in mot:
        if c != 'H' and c != 'D' and c != 'U':
            print('connard')
            return
        elif c == 'H':
            canvas.create_line(x, y, x + h, y, width= 3, fill= couleur)
            x = x + h
        elif c == 'U':
            canvas.create_line(x, y, x + w, y - h, width= 3, fill= couleur)
            x = x + w
            y = y - h
        elif c == 'D':
            canvas.create_line(x, y, x + w, y + h, width= 3, fill= couleur)
            x = x + w
            y = y + h 


def entrelacs(canvas, Tab, N, couleurs, w, h): #les valeurs de Tab sont entre 0 et N-2
    #On commence par co,vertir Tab en N mots
    permut = {i: i for i in range(N)}
    listeMots = ["H" for i in range(N)]

    for num in Tab:
        for i in range(N):
            if permut[i] == num:
                listeMots[i] += 'DH'
                permut[i] = permut[i] + 1
            elif permut[i] == num + 1:
                listeMots[i] += 'UH'
                permut[i] = permut[i] - 1
            else:
                listeMots[i] += 'HH'
    #On trace les N lignes
    for i in range(N):
        read_word(canvas, listeMots[i], h, w, 0, h*(i+1), couleurs[i])
    return    

Tab = [2, 1, 1, 0, 2]
listeCouleurs = ['black', 'red', 'blue', 'green']

entrelacs(canvas, Tab, 4, listeCouleurs, 50, 50)
root.mainloop()