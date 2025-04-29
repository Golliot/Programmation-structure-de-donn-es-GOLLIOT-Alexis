#Fonctions de hachage
import matplotlib.pyplot as plt

def listePremiersElements(L: list) -> list: #L est une liste de couples
    return [L[i][0] for i in range(len(L))]

def horner(var: str) -> int:
    h = 0
    for c in var:
        h = 33*h + ord(c)
    return h

def hNaive(var: str) -> int:
    return sum(ord(c) for c in var)



class Hashtable:

    def __init__(self, hashFun, length):
        self.__hashFun = hashFun
        self.__length = length
        self.__values = [None for i in range(length)]
        self.__nbElements = 0

    def getValues(self):
        return self.__values

    def put(self, key, value): #bien différencier l'argument value et la méthode values
        if self.__nbElements > 2*self.__length:
            self.resize()
        indice = self.__hashFun(key) % self.__length
        if self.__values[indice] == None:
            self.__values[indice] = [(key, value)]
        else:
            verifClé = False
            for i in range(len(self.__values[indice])):
                if self.__values[indice][i][0] == key:
                    verifClé = True
                    self.__values[indice][i][1] == value
            if not verifClé:
                self.__values[indice].append((key, value))
                self.__nbElements += 1
        
    def get(self, key):
        indice = self.__hashFun(key) % self.__length
        L = self.__values[indice]
        if L == None:
            return None
        for i in range(len(L)):
            if L[i][0] == key:
                return L[i][1]
    
    def repartition(self):
        y = [0 for i in range(self.__length)]
        
        for i in range(self.__length):
            if self.__values[i] is not None:
                y[i] = len(self.__values[i])
        x = range(self.__length)
        
        width = 1/1.5
        plt.bar(x, y, width, color = "blue")
        plt.show()
        return        

    def resize(self):
        new_ht = Hashtable(self.__hashFun, 2*self.__length)
        for i in range(self.__length):
            if self.__values[i] is not None:
                for j in range(len(self.__values[i])):
                    new_ht.put(self.__values[i][j][0], self.__values[i][j][1])
        
        self.__values = new_ht.__values
        self.__length = new_ht.__length
        self.__nbElements = new_ht.__nbElements
        return
    
    
f = open("frenchssaccent.dic")

Lexique = []
for ligne in f:
    Lexique.append(ligne[0:len(ligne)-1])

f.close()

H1 = Hashtable(hNaive, 320)

for i in range(len(Lexique)):
    H1.put(Lexique[i], len(Lexique[i]))

H1.repartition()

H2 = Hashtable(horner, 320)

for i in range(len(Lexique)):
    H2.put(Lexique[i], len(Lexique[i]))


H2.repartition()
