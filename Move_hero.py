import pygame


pygame.init()
pygame.display.set_caption('Move_hero')
image = pygame.image.load('mario_start.jpg')
with open(f'map1.txt', 'r') as mapFile:
    Level_map = [list(line.strip()) for line in mapFile]
Cell_size = 60
size = width, height = round(len(Level_map) * Cell_size * 1.5), round(len(Level_map[0]) * Cell_size * 1.5)
screen = pygame.display.set_mode(size)
LEFT = width // 8
TOP = height // 8


class Board:
    def __init__(self):
        self.left = LEFT
        self.top = TOP

    def set_view(self, left, top):
        self.left = left
        self.top = top

    def render(self):
        for x in range(len(Level_map)):
            for y in range(len(Level_map[x])):
                self.s_x = self.left + Cell_size * x
                self.s_y = self.top + Cell_size * y
                if Level_map[x][y] == '.':
                    pygame.draw.rect(screen, pygame.Color('blue'), (self.s_x, self.s_y, Cell_size, Cell_size), 1)
                elif Level_map[x][y] == '#':
                    pygame.draw.rect(screen, pygame.Color('blue'), (self.s_x, self.s_y, Cell_size, Cell_size))


class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename).convert_alpha()
        self.image.set_colorkey('white')
        self.mask = pygame.mask.from_surface(self.image)


board = Board()
player = Player('mario.png')
running = True
start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = False
        screen.blit(image, (0, 0))
        pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
    pygame.display.flip()
    board.render()
pygame.quit()