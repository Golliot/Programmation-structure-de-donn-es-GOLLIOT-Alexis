f = open("C:\\Users\\alexi\\OneDrive\\Documents\\Alexis\\Mines Nancy\\1A\\Cours\\Prog structure données\\Séance 1\\frenchssaccent.dic")

Lexique=[]

for ligne in f:
    Lexique.append(ligne[0:len(ligne)-1])
f.close()

##EXO 1 et 2

def verif(tirage,mot):
    T=list(tirage)
    i = 0
    while i<len(mot):
        if mot[i] not in T:
            return False
        T.remove(mot[i])
        i+=1
    return True

def liste_mots_possibles(lexique,tirage):
    Res=[]
    for mot in lexique:
        if verif(tirage,mot):
            Res.append(mot)
    return Res

def mot_le_plus_long(lexique,tirage):
    N=0
    Res=''
    for mot in liste_mots_possibles(lexique,tirage):
        if len(mot)>N:
            N=len(mot)
            Res=mot
    return Res

##EXO 3

#On utilise un dictionnare

Valeurs = {}
Valeurs.update(dict.fromkeys(['a','e','i','l','n','o','r','s','t','u'],1))
Valeurs.update(dict.fromkeys(['d','g','m'],2))
Valeurs.update(dict.fromkeys(['b','c','p'],3))
Valeurs.update(dict.fromkeys(['f','h','v'],4))
Valeurs.update(dict.fromkeys(['j','q'],8))
Valeurs.update(dict.fromkeys(['k','w','x','y','z'],10))
Valeurs['?']=0

def score(mot):
    S=0
    for lettre in mot:
        S+=Valeurs[lettre]
    return S

def max_score(lexique,tirage):
    liste=liste_mots_possibles(lexique,tirage)
    Max=0
    Res=''
    i=0
    while i<len(liste):
        if score(liste[i])>Max:
            Max=score(liste[i])
            Res=liste[i]
        i+=1
    return (Res,Max)


##EXO 4

def verif_joker(tirage,mot):
    T=list(tirage)
    i=0
    while i<len(mot):
        if mot[i] not in T:
            if '?' in T:
                T.remove('?')
            else :
                return False
        else:
            T.remove(mot[i])
        i+=1
    return True

def liste_mots_possibles_joker(lexique,tirage):
    Res=[]
    for mot in lexique:
        if verif_joker(tirage,mot):
            Res.append(mot)
    return Res

def score_joker(mot,tirage):
    S=0
    for lettre in mot:
        S+=Valeurs[lettre]
    if not verif(tirage,mot):
        S=S-1                   #ne fonctionne pas s'il y a plus de 1 joker
    return S



def max_score_joker(lexique,tirage):
    liste=liste_mots_possibles_joker(lexique,tirage)
    Max=0
    Res=''
    i=0
    while i<len(liste):
        if score(liste[i])>Max:
            Max=score_joker(liste[i],tirage)
            Res=liste[i]
        i+=1
    return (Res,Max)
















