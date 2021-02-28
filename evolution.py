import pygame
import random

pygame.init()
pygame.display.set_caption('Game Over')
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
with open(f'map1.txt', 'r') as mapFile:
    Level_map = [list(line.strip()) for line in mapFile]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('mario.png').convert_alpha(screen)



player = Player()
fps = 30
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.move_down()
            if event.key == pygame.K_w:
                player.move_up()
            if event.key == pygame.K_d:
                player.move_right()
            if event.key == pygame.K_a:
                player.move_left()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()