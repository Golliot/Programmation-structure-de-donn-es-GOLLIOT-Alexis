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
        return (self.label() == T.label() and self.children() == T.children())
    
    def isFloat(self):
        try:
            float(self.label())
            return True
        except ValueError:
            return False
    
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

    def simplify_Sum(self):
        if self.label() == '+':
            if self.child(0) == Tree('0'):
                return self.child(1)
            if self.child(1) == Tree('0'):
                return self.child(0)
            if self.child(0).isFloat() and self.child(1).isFloat():
                return Tree(str(float(self.child(0).label())+float(self.child(1).label())))
            if self.child(0).is_leaf() and self.child(1).is_leaf() and Tree('X') not in self.children():
                return Tree(str(self.child(0).label()) + '+' + str(self.child(1).label()))
        return Tree(self.label(), *(self.child(i).simplify_Sum() for i in range(self.nb_children())))

    def simplify_Mul(self):
        if self.label() == '*':
            if Tree('0') in self.children(): 
                return Tree('0')
            if self.child(0) == Tree('1'):
                return self.child(1)
            if self.child(1) == Tree('1'):
                return self.child(0)
            if self.child(0).isFloat() and self.child(1).isFloat():
                return Tree(str(float(self.child(0).label())*float(self.child(1).label())))
            if self.child(0).is_leaf() and self.child(1).is_leaf() and Tree('X') not in self.children():
                return Tree(str(self.child(0).label()) + '*' + str(self.child(1).label()))
        return Tree(self.label(), *(self.child(i).simplify_Mul() for i in range(self.nb_children())))
    
    def simplify(self):
        T1 = Tree('null')
        T2 = self
        while T1 != T2:
            T1 = T2
            T2 = T2.simplify_Mul().simplify_Sum()
        return T2
    
    def evaluate(self, x: float) -> float:
        return float(self.substitute(Tree('X'), Tree(str(x))).simplify().label())

T1=Tree('b',Tree('c'),Tree('d'))
T2=Tree('e',Tree('f'),Tree('g'))
T=Tree('a',T1,T2)

print(T)

#Pol = 7+5X+3X^2
Pol = Tree('+', Tree('7'), Tree('+', Tree('*', Tree('5'), Tree('X')), Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X')))))
print(Pol)

Pol_prime = Pol.deriv('X')
print(Pol_prime.simplify())
