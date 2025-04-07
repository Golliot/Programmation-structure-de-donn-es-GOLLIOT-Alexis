class Poly :
    
    def __init__(self,liste):   #On donne liste=[p_0,p_1,...,p_n]
        self.coeffs = liste
    
    def __str__(self):
        s=''
        n=len(self.coeffs)
        for i in range(n-1):
            signe = ''
            if self.coeffs[n-i-1] == 1:
                signe = ''
            elif self.coeffs[n-i-1] < 0:
                signe = str(self.coeffs[n-i-1]) + 'X^' + str(n-i-1)
            elif self.coeffs[n-i-1] > 0:
                signe = ' +' + str(self.coeffs[n-i-1]) + 'X^' + str(n-i-1)
            s=s + signe 
        signe = ''
        if self.coeffs[0] == 0:
                signe = ''
        elif self.coeffs[0] < 0:
            signe = str(self.coeffs[0])
        elif self.coeffs[0] > 0:
            signe = ' +' + str(self.coeffs[0])
        s=s + signe 
        return s

    def __add__(self,pol):
        c1=self.coeffs
        c2=pol.coeffs
        while len(c1)<len(c2):
            c1.append(0)
        while len(c2)<len(c1):
            c2.append(0)
        c=[c1[k]+c2[k] for k in range(len(c2))]
        return Poly(c)
    
    def scalar(self,c):
        liste = [c*self.coeffs[i] for i in range(len(self.coeffs))]
        return Poly(self,liste)


p1=Poly([4,-5,0,4,6])
p2=Poly([6,2,7])
print(str(p1)) 
print(str(p2)) 
print(str(p1+p2))

##Exo2

class equiv :
   
    #les éléments de liste doivent être entiers
    def __init__(self,n,q,coeffs):   
        self.n = n
        self.q = q

        #on réduit les monomes de degré >n-1
        self.coeffs = [coeffs[k] for k in range(min(n,len(coeffs)))]
        
        for i in range(len(self.coeffs),len(coeffs)):
            self.coeffs[i%n] += -coeffs[i]
        #on réduit les coeffs à nouveau modulo n
        self.coeffs = [self.coeffs[i]%q for i in range(len(self.coeffs))]

    def __str__(self):
        s=''
        n=len(self.coeffs)
        for i in range(n-1):
            signe = ''
            if self.coeffs[n-i-1] == 0:
                signe = ''
            elif self.coeffs[n-i-1] < 0:
                signe = str(self.coeffs[n-i-1]) + 'X^' + str(n-i-1)
            elif self.coeffs[n-i-1] > 0:
                signe = ' +' + str(self.coeffs[n-i-1]) + 'X^' + str(n-i-1)
            s=s + signe 
        signe = ''
        if self.coeffs[0] == 0:
                signe = ''
        elif self.coeffs[0] < 0:
            signe = str(self.coeffs[0])
        elif self.coeffs[0] > 0:
            signe = ' +' + str(self.coeffs[0])
        s=s + signe 
        return s

    def rescale(self,r):
        for k in range(len(self.coeffs)):
            self.coeffs[k] = self.coeffs[k]%r



p3=equiv(4,5,[7,4,9,11,3])
print(str(p3))
p3.rescale(3)
print(str(p3))