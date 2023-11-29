import time

# Fonction pour afficher l'heure au format hh:mm:ss
def my_function(heure):
    print(f"{heure[0]}:{heure[1]}:{heure[2]}")

# Fonction pour régler l'heure à savoir (hh(12h/24h):mm(60m):ss(60s))
def afficher_heure(heures, minutes, secondes):
    minutes += secondes // 60
    secondes = secondes % 60
    heures += minutes // 60
    minutes = minutes % 60
    heures = heures % 24 
    heures = heures % 12 
    return heures, minutes, secondes

# Programme principal
def main():
# Initialiser l'heure à 9:0:0
    heures, minutes, secondes = 9, 0, 0 

    while True:
# Afficher l'heure actuelle
        my_function((heures, minutes, secondes,))
        

#programme pour pouvoir afficher l'heur arrivé à 9h1m0s.
        if heures == 9 and minutes == 1 and secondes == 0:
         alarme()

# Actualiser l'heure toutes les secondes
        time.sleep(1)
        secondes += 1

# Ajuster l'heure en cas de dépassement, ce qui veut dire que les s ne vont pas au dela de 60s. 
        heures, minutes, secondes = afficher_heure(heures, minutes, secondes) 

#Ajouter une fonction alarme arrivé à 9:1:0
def alarme():
        print("l'heur du rendez-vous et arrivé, il et 9:1:0 !")
    
main()
