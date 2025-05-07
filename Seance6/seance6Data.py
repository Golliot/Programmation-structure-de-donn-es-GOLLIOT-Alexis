import random as rd

max_fils = 7
max_croisements = 10

class Data:
    
    def __init__(self, nb_lines: int, colors: list, tab: list):
        self.__nb_lines = nb_lines
        self.__colors = colors
        self.__tab = tab

    def nb_lines(self):
        return self.__nb_lines
    
    def colors(self):
        return self.__colors

    def tab(self):
        return self.__tab

    def permute_colors(self):
        L = self.__colors.copy()
        for i in range(len(self.__colors)):
            L[i] = self.__colors[(i+1) % self.__nb_lines]
        self.__colors = L
    
    def random_change(self):
        self.__nb_lines = rd.randint(2, max_fils)
        nb_croisements = rd.randint(0, max_croisements)
        self.__tab = [rd.randint(0, self.__nb_lines-1) for i in range(nb_croisements)]
        self.__colors = ["#{:06x}".format(rd.randint(0, 0xFFFFFF)) for i in range(self.__nb_lines)]
