# Visualiseur de la fractale de Mandelbrot

Ce programme est un visualiseur interactif de l'ensemble de Mandelbrot. Il permet à l'utilisateur de zoomer et de dézoomer sur l'ensemble de Mandelbrot en utilisant la souris. 
Les coordonnées de la souris dans le plan complexe et le niveau de zoom sont affichés en temps réel.

![Image de l'ensemble de Mandelbrot](mandelbrot.png)

## Fonctionnalités

- Affichage de l'ensemble de Mandelbrot
- Zoom avant et arrière avec la souris
- Affichage des coordonnées de la souris dans le plan complexe et du niveau de zoom

## Bibliothèques utilisées

- pygame : utilisée pour l'affichage graphique et la gestion des événements de la souris.
- numpy : utilisée pour les calculs numériques, notamment pour créer une grille de points dans le plan complexe.
- multiprocessing : utilisée pour paralléliser le calcul de l'ensemble de Mandelbrot, ce qui permet d'accélérer les calculs en utilisant tous les cœurs du processeur.
- numba : utilisée pour accélérer les calculs en compilant à la volée certaines fonctions Python en code machine.

## Amélioration de la rapidité des calculs

Le calcul de l'ensemble de Mandelbrot est une opération coûteuse en termes de calculs. Pour améliorer les performances, ce programme utilise plusieurs techniques :

- Parallélisation : Le calcul de l'ensemble de Mandelbrot est divisé en plusieurs lots qui sont calculés en parallèle par différents cœurs du processeur. Cela est réalisé grâce à la bibliothèque multiprocessing.

- Compilation Just-In-Time (JIT) : La fonction mandelbrot est compilée en code machine à la volée lors de son premier appel grâce à la bibliothèque numba. Cela permet d'accélérer les calculs en évitant l'interprétation du code Python.

- Utilisation de numpy : Les opérations sur les tableaux sont réalisées avec numpy, qui est optimisé pour les calculs numériques sur des tableaux de grande taille.
