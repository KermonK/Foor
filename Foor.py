import pygame

# Pygame'i käivitamine
pygame.init()

# Akna suurus
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Akna pealkiri
pygame.display.set_caption("Foor - Kermon Kopli")

# Värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

# Peamine tsükkel
running = True
while running:
    screen.fill(BLACK)  # Taustavärv

    # Foori taust (hall ristkülik)
    pygame.draw.rect(screen, GRAY, (100, 10, 100, 270), 1)  # Ristkülik õige suuruse ja asukohaga

    # Valgusfoori tuled
    pygame.draw.circle(screen, RED, (150, 60), 40)  # Punane tuli
    pygame.draw.circle(screen, YELLOW, (150, 145), 40)  # Kollane tuli
    pygame.draw.circle(screen, GREEN, (150, 230), 40)  # Roheline tuli

    # Ürituste käsitlemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Uuendab ekraani

pygame.quit()