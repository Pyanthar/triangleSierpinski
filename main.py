import math

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


# Création d'un graphique vide avec les données
fig, ax = plt.subplots()
scatter = ax.scatter([], [], s=1)

# Ajout de titre et de labels pour les axes
ax.set_title("Triangleception")
ax.set_xlabel("Axe X")
ax.set_ylabel("Axe Y")





nbpoints = 100000
points = []

futurpoints= []

#Triangle de base
Tailletriangle = 100
pointA = (0, 0)
pointB = (Tailletriangle, 0)
pointC = (Tailletriangle / 2, Tailletriangle * math.sqrt(3) / 2)
points = [pointA, pointB, pointC]

# Fixer les limites de l'échelle des axes
ax.set_xlim(-Tailletriangle/10, Tailletriangle+Tailletriangle/10)
ax.set_ylim(-Tailletriangle/10, Tailletriangle-Tailletriangle/10)

# Fonction pour mettre à jour les points à chaque image de l'animation
def update(frame):
    if frame < len(futurpoints):
        #print(frame)
        #print(points)
        points.append(futurpoints[frame])
        scatter.set_offsets(points)
        print(frame)
    else:
        points.clear()
    return scatter,

def start_anim():
    # Création de l'animation avec une image toutes les 500 millisecondes
    ani = FuncAnimation(fig, update, frames=len(futurpoints) + 1, interval=1, blit=True)

    # Affichage de l'animation
    plt.show()

def center(point1, point2):

    x1, y1 = point1
    x2, y2 = point2
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2
    return x_center, y_center


#calcul du premier point
futurpoints.append(center(pointA, pointB))

for i in range(nbpoints):
    choix = random.randint(1, 3)
    if choix == 1:
        pointrandom = pointA
    elif choix == 2:
        pointrandom = pointB
    else:
        pointrandom = pointC

    nouveaupoint = center(futurpoints[i], pointrandom)
    futurpoints.append(nouveaupoint)
    #print(nouveaupoint)
    print(i)
# animation
start_anim()


