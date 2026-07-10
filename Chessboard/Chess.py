import pygame
import sys

pygame.init()
screen_x, screen_y = 800, 800
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Python Chess")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, screen_x, screen_y))
    pygame.display.flip()
    clock.tick(60)