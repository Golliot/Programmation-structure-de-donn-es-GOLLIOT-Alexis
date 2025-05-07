from tkinter import Tk, Canvas, Button, Frame, Label
from seance6Data import *

class App:

    def __init__(self, data: Data):
        self.__data = data
        
        self.__root = Tk()
        self.__root.geometry("1000x500")
        
        self.__permuter = Button(self.__root, text= 'Permutter', command= lambda: (self.__data.permute_colors(), self.redraw()), fg= 'white', bg= 'dark grey', relief= 'raised')
        self.__quitter = Button(self.__root, text= 'Quitter', command= self.__root.destroy, fg= 'white', bg= 'dark grey', relief= 'raised')
        self.__canvas = Canvas(self.__root, width= 1000, height= 400, bg= 'light grey')
        self.__random = Button(self.__root, text= 'Entrelac aléatoire', command= lambda: (self.__data.random_change(), self.redraw()), fg= 'white', bg= 'dark grey', relief= 'raised')

    def run_forever(self):
        self.redraw()
        self.__root.mainloop()
    
    def read_word(self, x0, y0, mot, couleur):
        h, w = 50, 50
        (x, y) = (x0, y0)
        for c in mot:
            if c != 'H' and c != 'D' and c != 'U':
                print('connard')
                return
            elif c == 'H':
                self.__canvas.create_line(x, y, x + h, y, width= 3, fill= couleur)
                x = x + h
            elif c == 'U':
                self.__canvas.create_line(x, y, x + w, y - h, width= 3, fill= couleur)
                x = x + w
                y = y - h
            elif c == 'D':
                self.__canvas.create_line(x, y, x + w, y + h, width= 3, fill= couleur)
                x = x + w
                y = y + h
    
    def entrelacs(self):
        permut = {i: i for i in range(self.__data.nb_lines())}
        listeMots = ["H" for i in range(self.__data.nb_lines())]

        for num in self.__data.tab():
            for i in range(self.__data.nb_lines()):
                if permut[i] == num:
                    listeMots[i] += 'DH'
                    permut[i] = permut[i] + 1
                elif permut[i] == num + 1:
                    listeMots[i] += 'UH'
                    permut[i] = permut[i] - 1
                else:
                    listeMots[i] += 'HH'
    
        for i in range(self.__data.nb_lines()):
            self.read_word(0, 50*(i+1), listeMots[i], self.__data.colors()[i])
        return 
    
    def permute(self):
        self.__data.permute_colors()
        self.redraw()
    
    def redraw(self):
        self.__canvas.delete("all")
        self.__permuter.place(x= 500, y=450, anchor= 'center')
        self.__quitter.place(x= 125, y=450, anchor= 'center')
        self.__random.place(x= 875, y= 450, anchor= 'center')
        self.__canvas.pack()
        self.entrelacs()
    



if __name__ == '__main__':
    app = App(Data(4, ['black', 'red', 'blue', 'green'], [2, 1, 1, 0, 2]))
    app.run_forever()