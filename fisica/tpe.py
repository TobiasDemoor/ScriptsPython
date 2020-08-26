import random
import pandas as pd

UNID = 20000
probFalla = random.random()
probFalla = 0.05
cantFallas = int(UNID*probFalla)
muestras = pd.DataFrame({"costos": [], "malos": [], "buenos": []})

muestras.loc[0] = [1.25*int(UNID*probFalla), 0, 0]
for n in range(1, 30+1):
    unidades = UNID
    costo = n*0.8
    malos = 0
    buenos = 0
    
    for i in range(n):
        unidades -= 1
        if random.random() > (cantFallas-malos)/unidades:
            buenos += 1
        else:
            malos += 1
    
    if malos/(malos+buenos) <= 0.02:
        costo += 1.25*int(cantFallas-malos)
    
    muestras.loc[n] = [costo, malos, buenos]

print(muestras.min().costos)
print(probFalla)
print(muestras)
