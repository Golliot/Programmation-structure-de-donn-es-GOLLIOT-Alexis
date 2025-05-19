import numpy as np
import random as rd

class Graph_Data:
    def __init__(self, graph, height, width, mass, k_Hooke, k_centre, delta_t, L_0):
        self.graph = graph
        self.height = height
        self.width = width
        self.pos = [np.array([rd.random()*width, rd.random()*height]) for i in range(len(self.graph))]
        self.vit = [np.array([(rd.random()-0.5)*10, (rd.random()-0.5)*10]) for i in range(len(graph))]
        self.mass = mass
        self.k_Hooke = k_Hooke
        self.k_centre = k_centre
        self.delta_t = delta_t
        self.L_0 = L_0
        self.Forces = [np.array([0, 0])]

    def getForceRessort(self):
        Forces_ressort = list()
        for i in range(len(self.graph)):
            F_ressort_i = np.array([0.0, 0.0])
            for j in self.graph[i]:
                L = np.sqrt((self.pos[j][1] - self.pos[i][1])**2 + (self.pos[j][0] - self.pos[i][0])**2)
                F_ressort_i += self.k_Hooke*(L-self.L_0)*np.array([self.pos[j][0]-self.pos[i][0], self.pos[j][1]-self.pos[i][1]])/L
            Forces_ressort.append(F_ressort_i)
        #j'ajoute un ressort au centre pour que les autres ne divergent pas
        y_centre = self.height/2
        x_centre = self.width/2
        for i in range(len(self.graph)):
            L = np.sqrt((y_centre - self.pos[i][1])**2 + (x_centre - self.pos[i][0])**2)
            Forces_ressort[i] += self.k_centre*(L-self.L_0)*np.array([x_centre-self.pos[i][0], y_centre-self.pos[i][1]])/L
        return Forces_ressort
    
    def getForceElec(self):
        Forces_elec = list()
        q = 1000000
        for i in range(len(self.graph)):
            F_elec_i = np.array([0.0, 0.0])
            for j in self.graph[i]:
                r = np.sqrt((self.pos[j][1] - self.pos[i][1])**2 + (self.pos[j][0] - self.pos[i][0])**2)
                F_elec_i += -q**2/r**2*np.array([self.pos[j][0]-self.pos[i][0], self.pos[j][1]-self.pos[i][1]])
        return Forces_elec
                


    def update_pos_vit(self):
        for i in range(len(self.graph)):
            self.vit[i] += (self.Forces[i]/self.mass)*self.delta_t
            self.pos[i] += self.vit[i]*self.delta_t
            self.vit[i] *= 0.99
            self.Forces = self.getForceRessort() + self.getForceElec()