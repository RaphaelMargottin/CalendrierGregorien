#import de l'objet datetime
from datetime import datetime

#Recupération de la date de l'utilisateur et initialisation des variables
result = input("Calcul du jour de la semaine gregorienne correspondant à la date (sous la forme JJMMAAAA) : ")
dDate = datetime.strptime(result, '%d%m%Y')
iAA = int(dDate.strftime('%y'))
iDay = int(dDate.strftime('%d'))
iMonth = int(dDate.strftime('%m'))
isBissex = False

# 1) 2) Ajoute du quart de l'année
iCal = (iAA + (iAA / 4))

## 3) On ajoute au calcul la valeur du jour du mois
iCal += iDay

## 4) On test le mois et on ajoute la valeur correspondante
if 2 == iMonth:
    iCal += 3
elif iMonth == 3:
    iCal += 3
elif iMonth == 4:
    iCal += 6
elif iMonth == 5:
    iCal += 1
elif iMonth == 6:
    iCal += 4
elif iMonth == 7:
    iCal += 6
elif iMonth == 8:
    iCal += 2
elif iMonth == 9:
    iCal += 5
elif iMonth == 11:
    iCal += 3
elif iMonth == 12:
    iCal += 5

##Test de l'année bissextile ou non
iYear = int(dDate.strftime('%Y'))

if iYear % 400 == 0:
    isBissex = True
elif iYear % 100 == 0:
    isBissex = False
elif iYear % 4 == 0:
    isBissex = True

if isBissex:
    if iMonth == 1 or iMonth == 2:
        iCal = iCal - 1

## 6) Ajout selon le siècle
tmp = iYear - iAA
if tmp == 1600:
    iCal += 6
elif tmp == 1700:
    iCal += 4
elif tmp == 1800:
    iCal += 2
elif tmp == 1900:
    iCal += 0
elif tmp == 2000:
    iCal += 6
elif tmp == 2100:
    iCal += 4

## 7) Division par 7 => Reste
iCal = iCal % 7

## Résultat et affichage21031

listJ = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

indx = len(listJ)
for i in range(len(listJ)):
    if i == int(iCal):
        print(listJ[i])
        break