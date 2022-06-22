
from methods import *

keep_going = True

while keep_going:
    choice = input("Seleziona opzione: 1-Leggi numeri | 2-Inserisci giocata | 3-Resetta Dati | 4-Esci ")
    choice = int(choice)

    if(choice == 1):
        readNumbers()
    elif(choice == 2):
        insertNumbers()
    elif(choice == 3):
        resetData()
    elif(choice == 4):
        keep_going = False
    else:
        print("Opzione non in lista")


