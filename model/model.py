import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [9, 6]
plt.rc('font', size=14)
from thermo.chemical import Chemical as chem

# Elementi v materialu

class material:

    def __init__(self, wC, wH, wO, wN, wS, wCl, wHg, wpepel, wH2O):
        self.wC = wC
        self.wH = wH
        self.wO = wO
        self.wN = wN
        self.wS = wS
        self.wCl = wCl
        self.wHg = wHg
        self.wpepel = wpepel
        self.wH2O = wH2O

        self.total = self.wC + self.wH + self.wO + self.wN + self.wS + self.wCl + self.wHg + self.wH2O + self.wpepel

        self.LHV = 33.9 * self.wC + 121.4 * (self.wH - (self.wO / 8)) + 10.5 * self.wS - 2.5 * self.wH2O
        self.HHV = self.LHV + 22.34 * self.wH + 2.5 * self.wH2O

    def return_list(self):
        return np.array([self.wC, self.wH, self.wO, self.wN, self.wS, self.wCl, self.wHg, self.wpepel, self.wH2O])

    def simulation_material(self):
        faktor_povecanja = 1
        nC = self.wC * 100 / 12 * faktor_povecanja
        nH = self.wH * 100 / 1 * faktor_povecanja
        nO = self.wO * 100 / 16 * faktor_povecanja 
        return np.array([nC, nH, nO])



masni_procenti = np.array([44.63, 7.49, 22.63, 0.18, 1.51, 0.29, 0, 13.27, 10])
masni_delezi = masni_procenti / 100
wet_material = material(*masni_delezi)
wet_table = wet_material.return_list()
dry_table = wet_table / (1 - wet_material.wH2O)
dry_table[-1] = 0
dry_material = material(*dry_table)


print(dry_material.simulation_material())

m = chem("C6H8O2")
print(m.Hf)











