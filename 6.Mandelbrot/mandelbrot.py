# Importation des bibliothèques nécessaires
import numpy as np
import pygame
import multiprocessing
from numba import jit

# Définition des paramètres pour l'affichage
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 10000

zoom_factor = 2  # Ajustez ceci pour changer la quantité de zoom

# Define the initial ranges
x_range_initial = xmax - xmin
y_range_initial = ymax - ymin

# Initialiser pygame
pygame.init()
screen = pygame.display.set_mode((width, height))

# Initialiser la police
font = pygame.font.Font('DejaVuSansMono.ttf', 20)

running = True

# Définition de la fonction pour calculer la fractale de Mandelbrot
@jit(nopython=True)
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Création d'une grille de points dans le plan complexe
x = np.linspace(xmin, xmax, width, dtype=np.float64)
y = np.linspace(ymin, ymax, height, dtype=np.float64)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Calcul de la fractale de Mandelbrot en parallèle
num_processors = multiprocessing.cpu_count()
num_batches = 20  # Nombre de lots
batch_size = len(np.ravel(Z)) // num_batches
percent_done = 0

def calculer_mandelbrot(Z, max_iter, num_processors, num_batches, batch_size, font, screen, width):
    with multiprocessing.Pool(processes=num_processors) as pool:
        mandelbrot_set = np.array([], dtype=np.float64)
        for i in range(num_batches):
            start = i * batch_size
            end = start + batch_size if i < num_batches - 1 else None
            batch = np.ravel(Z)[start:end]
            mandelbrot_set = np.append(mandelbrot_set, pool.starmap(mandelbrot, [(c, max_iter) for c in batch]))
            percent_done = (i + 1) / num_batches * 100
            text = font.render(f"{percent_done:.1f}%", True, (255, 255, 255), (0, 0, 0))
            screen.blit(text, (width - text.get_width(), 0))  # Position en haut à droite
            pygame.display.flip()

        mandelbrot_set = np.array(mandelbrot_set).reshape((width, width))

    return mandelbrot_set

def calculer_et_convertir_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, num_processors, num_batches, batch_size, font, screen):
    x = np.linspace(xmin, xmax, width, dtype=np.float64)
    y = np.linspace(ymin, ymax, height, dtype=np.float64)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    mandelbrot_set = calculer_mandelbrot(Z, max_iter, num_processors, num_batches, batch_size, font, screen, width)

    mandelbrot_set_normalized = 255 - (np.log(1 + mandelbrot_set) / np.log(1 + np.nanmax(mandelbrot_set)) * 255)
    mandelbrot_set_normalized = mandelbrot_set_normalized.astype(np.uint8)
    image = pygame.surfarray.make_surface(mandelbrot_set_normalized)
    # Tourner l'image de 90° dans le sens antihoraire
    image = pygame.transform.rotate(image, 90)
    return image

image = calculer_et_convertir_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, num_processors, num_batches, batch_size, font, screen)

# Function to calculate real_zoom
def calculer_real_zoom(xmin, xmax, ymin, ymax, x_range_initial, y_range_initial):
    x_range = xmax - xmin
    y_range = ymax - ymin
    real_zoom = x_range_initial / x_range  # or y_range_initial / y_range
    return real_zoom

# Boucle principale
while running:
    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x = xmin + (xmax - xmin) * x / width
            y = ymax - (ymax - ymin) * y / height
            x_range = xmax - xmin
            y_range = ymax - ymin
            if event.button == 1:  # Bouton gauche de la souris
                # Zoom in
                if real_zoom <= 10**13:
                    xmin = x - x_range / (zoom_factor*2) 
                    xmax = x + x_range / (zoom_factor*2) 
                    ymin = y - y_range / (zoom_factor*2) 
                    ymax = y + y_range / (zoom_factor*2) 
            elif event.button == 3:  # Bouton droit de la souris
                # Zoom out
                xmin = x - x_range * (zoom_factor/2) 
                xmax = x + x_range * (zoom_factor/2) 
                ymin = y - y_range * (zoom_factor/2) 
                ymax = y + y_range * (zoom_factor/2) 

            # Calculer le real_zoom
            new_real_zoom = calculer_real_zoom(xmin, xmax, ymin, ymax, x_range_initial, y_range_initial)

            # Ne recalcule la fractale que si le real_zoom a changé
            if new_real_zoom != real_zoom:
                real_zoom = new_real_zoom
                # Recalculer la fractale de Mandelbrot avec les nouvelles limites
                x = np.linspace(xmin, xmax, width, dtype=np.float64)
                y = np.linspace(ymin, ymax, height, dtype=np.float64)
                X, Y = np.meshgrid(x, y)
                Z = X + 1j * Y
                image = calculer_et_convertir_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, num_processors, num_batches, batch_size, font, screen)

    # Récupérer la position de la souris
    x, y = pygame.mouse.get_pos()
    x = xmin + (xmax - xmin) * x / width
    y = ymax - (ymax - ymin) * y / height

    # Calculate real_zoom
    real_zoom = calculer_real_zoom(xmin, xmax, ymin, ymax, x_range_initial, y_range_initial)

    # Afficher l'image
    screen.blit(image, (0, 0))

    # Afficher la valeur du zoom en haut à droite
    zoom_text = font.render(f"Zoom: {real_zoom:.1e}", True, (255, 255, 255), (0, 0, 0))
    screen.blit(zoom_text, (0, 0))

    # Afficher les coordonnées de la souris
    text = font.render(f"z = {x:.20f} + {y:.20f}.i", True, (255, 255, 255), (0, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height - text.get_height()))

    pygame.display.flip()

pygame.quit()
