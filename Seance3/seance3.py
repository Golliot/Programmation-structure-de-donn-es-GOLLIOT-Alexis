##EXo 1

class Tree :

    def __init__(self, label, *children):
        self.__label=label
        self.__children=children
    
    def label(self):
        return self.__label
    
    def children(self):
        return self.__children
    
    def nb_children(self):
        return len(self.__children)
    
    def child(self, i: int):
        return self.__children[i]
    
    def is_leaf(self):
        return (len(self.__children)==0)
    
    def depth(self):
        if self.is_leaf():
             return(0)
        return (1+self.child(0).depth())
    
    def __str__(self):  
        if self.is_leaf():
            return self.label()
        s="".join([self.child(i).__str__()+','  for i in range(self.nb_children())]) 
        return self.label() + '(' + s[:-1] + ')'    

T1=Tree('b',Tree('c'),Tree('d'))
T2=Tree('e',Tree('f'),Tree('g'))
T=Tree('a',T1,T2)

print(str(T))
