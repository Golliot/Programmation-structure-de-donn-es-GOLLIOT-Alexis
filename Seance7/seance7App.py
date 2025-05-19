from tkinter import Tk, Label, Canvas
from seance7Data import *

class Graph_App:
    def __init__(self, data: Graph_Data):
        self.__data = data
        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width= self.__data.width, height= self.__data.height, bg= 'light grey')
        
        self.__running = False
        self.__root.bind('<KeyPress-f>', self.start_action)
        self.__root.bind('<KeyRelease-f>', self.stop_action)
        self.__root.focus_set()

    
    def run_forever(self):
        self.draw()
        self.__root.mainloop()
    
    def draw(self):
        self.__canvas.delete("all")
        for i in range(len(self.__data.graph)):
            for j in self.__data.graph[i]:
                x0= self.__data.pos[i][0]
                y0= self.__data.pos[i][1]
                x1= self.__data.pos[j][0]
                y1= self.__data.pos[j][1]

                
                self.__canvas.create_line(x0, y0, x1, y1)
        
        i = 0
        for (x, y) in self.__data.pos:
            self.__canvas.create_oval(x-10,y-10,x+10,y+10,fill="#f3e1d4")
            self.__canvas.create_text(x, y, text= str(i), font=('Arial', 12))
            i += 1
        self.__canvas.pack()
    
    def start_action(self, event):
        if not self.__running:
            self.__running = True
            self.press_f_to_update()

    def stop_action(self, event):
        self.__running = False
    
    def press_f_to_update(self):
        if self.__running:
            self.__data.update_pos_vit()
            self.draw()
            self.__root.after(1, self.press_f_to_update)




if __name__ == '__main__':
    Adj = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
    G = Graph_App(Graph_Data(Adj, 600, 1000, 10, 10, 100, 0.01, 200))
    G.run_forever()