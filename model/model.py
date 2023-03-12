import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [9, 6]
plt.rc('font', size=14)
from thermo.chemical import Chemical as chem

# Elementi v materialu

# class material:

#     def __init__(self, wC, wH, wO, wN, wS, wCl, wHg, wpepel, wH2O):
#         self.wC = wC
#         self.wH = wH
#         self.wO = wO
#         self.wN = wN
#         self.wS = wS
#         self.wCl = wCl
#         self.wHg = wHg
#         self.wpepel = wpepel
#         self.wH2O = wH2O

#         self.total = self.wC + self.wH + self.wO + self.wN + self.wS + self.wCl + self.wHg + self.wH2O + self.wpepel

#         self.LHV = 33.9 * self.wC + 121.4 * (self.wH - (self.wO / 8)) + 10.5 * self.wS - 2.5 * self.wH2O
#         self.HHV = self.LHV + 22.34 * self.wH + 2.5 * self.wH2O

#     def return_list(self):
#         return np.array([self.wC, self.wH, self.wO, self.wN, self.wS, self.wCl, self.wHg, self.wpepel, self.wH2O])

#     def simulation_material(self):
#         faktor_povecanja = 5
#         nC = self.wC * 100 / 12 * faktor_povecanja
#         nH = self.wH * 100 / 1 * faktor_povecanja
#         nO = self.wO * 100 / 16 * faktor_povecanja 
#         return np.array([nC, nH, nO])
    
#     def molski_delez(self):
    
def check_toatal(x):
    return(sum(x))

def calculate_simulation_material(delezi):
    faktor_povecanja = 5
    nC = delezi[0] * 100 / 12 * faktor_povecanja
    nH = delezi[1] * 100 / 1  * faktor_povecanja
    nO = delezi[2] * 100 / 16 * faktor_povecanja
    return(np.array([nC, nH, nO]))
        
wC = 44.63
wH = 7.49
wO = 22.63
wN = 0.18
wS = 1.51
wCl = 0.29
wHg = 0
wPepel = 13.27
wH2O = 10


masni_procenti = np.array([wC, wH, wO, wN, wS, wCl, wHg, wPepel, wH2O])    
masni_delezi = masni_procenti / 100
print(check_toatal(masni_delezi))
#wet_material = material(*masni_delezi)
#wet_table = wet_material.return_list()
#dry_table = wet_table / (1 - wet_material.wH2O)
#dry_table[-1] = 0
#dry_material = material(*dry_table)
masni_delezi_dry = masni_delezi / (1 - (wH2O / 100))
masni_delezi_dry[-1] = 0

simulation_material_actual = calculate_simulation_material(masni_delezi_dry)
simulation_material_rounded = np.round(simulation_material_actual)
simulation_material_rounded = simulation_material_rounded.astype(int)
simulation_material_str = f"C{simulation_material_rounded[0]}H{simulation_material_rounded[1]}O{simulation_material_rounded[2]}"
print(simulation_material_str)

# Reakcije
#Oksidacija:
#CxHyOz + ((x-z)/2)O2 -> xCO + (y/2)H2
def oksidacija(reaktant):
    mO2 = (reaktant[0] - reaktant[2]) / 2
    
    mCO = reaktant[0]
    mH2 = reaktant[1] / 2
    to_return = np.array([mO2, mCO, mH2])
    #to_return = to_return.astype(int)
    return(to_return)
    
oksidacija_moli = oksidacija(simulation_material_rounded)
oksidacija_str = (simulation_material_str + f" + {oksidacija_moli[0]} O2 -> {oksidacija_moli[1]} CO + {oksidacija_moli[2]} H2")
print("Oksidacija: " + oksidacija_str)

#Hidroliza:
#CxHyOz + (x-z)H2O -> xCO + ((y/2)+(x-z))H2
def hidroliza(reaktant):
    mH2O = reaktant[0] - reaktant[2]
    
    mCO = reaktant[0]
    mH2 = ((reaktant[1] / 2) + (reaktant[0] - reaktant[2]))
    to_return = np.array([mH2O, mCO, mH2])
    return(to_return)

hidroliza_moli = hidroliza(simulation_material_rounded)
hidroliza_str = (simulation_material_str + f" + {hidroliza_moli[0]} H2O -> {hidroliza_moli[1]} CO + {hidroliza_moli[2]} H2")
print("Hidroliza: " + hidroliza_str)

#Oksidacija CO:
#CO + 0.5 O2 -> CO2
oksidacija_CO_str = "CO + 0.5 O2 -> CO2"

#Nastajanje katranov:
def reakcija_katranov(nC, nH, nO):
    mC7H8 = np.round(nC / 7)
    












