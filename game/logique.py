import pygame

pygame.init()

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Créer une fenêtre
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jeu de combat stick")

# Définir les variables pour le personnage
x = 50
y = 50
width = 40
height = 60
vel = 5

# Boucle de jeu
run = True
while run:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Gestion des mouvements du personnage
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 700 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel

    # Afficher le personnage
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (x, y, width, height))
    pygame.display.update()

# Quitter le jeu
pygame.quit()
