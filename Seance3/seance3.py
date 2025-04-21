##EXo 1
from __future__ import annotations

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
    
    def __eq__(self, T):
        return str(self) == str(T)
    
    #Chaque noeud qui n'est pas une feuille a 2 enfants: 
    #3x^2+5X+7 a pour représentation: +(7,+(*(5,X),*(3,*(X,X))))
    def deriv(self, var: str):
        if self.is_leaf():
            if self.label() == var:
                return Tree('1')
            else:
                return Tree('0')
        if self.label() == '+':
            return Tree('+', self.child(0).deriv(var), self.child(1).deriv(var))
        if self.label() == '*':
            return Tree('+',Tree('*', self.child(0).deriv(var), self.child(1)), Tree('*', self.child(0), self.child(1).deriv(var)))

    def substitute(self, t1: Tree, t2: Tree) -> Tree:
        if self == t1:
            return t2
        return Tree(self.label(), *(self.child(i).substitute(t1, t2) for i in range(self.nb_children())))
        
T1=Tree('b',Tree('c'),Tree('d'))
T2=Tree('e',Tree('f'),Tree('g'))
T=Tree('a',T1,T2)

print(str(T))

#Pol = 7+5X+3X^2
Pol = Tree('+', Tree('7'), Tree('+', Tree('*', Tree('5'), Tree('X')), Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X')))))
print(str(Pol))
print(str(Pol.deriv('X')))

t=Tree('+', Tree('a'), Tree('X'))
print(str(t.substitute(Tree('X'), Tree('b'))))