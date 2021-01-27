import pygame, sys, random, os, threading, pygame_gui
                                                                         # таймер, окончание

pygame.init()
with open('Map_Pygame.txt', 'r') as mapFile:
    Level_map = [list(line.strip()) for line in mapFile]
Cell_size = 60
pygame.display.set_caption('Pygame_project')
size = width, height = round(len(Level_map) * Cell_size * 1.5), round(len(Level_map[0]) * Cell_size * 1.5)
screen = pygame.display.set_mode(size)
pygame.mixer.music.load('Neizvestno_-_Pikselnaya_muzyka_(iPleer.com) (1).mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)
sound_step = pygame.mixer.Sound('Sound_17237.wav')
background = pygame.image.load('BingWallpaper (2).jpg')
menu_background = pygame.image.load('BingWallpaper (5).jpg')
LEFT = width // 8
TOP = height // 8
Coords_for_players = []
Walls_tile = []
end_game = 0

for x in range(len(Level_map)):
    for y in range(len(Level_map[x])):
        if Level_map[x][y] == '#':
            Walls_tile.append((x, y))
        elif Level_map[x][y] == '@':
            Coords_for_players.append((x, y))
Save_walls = Walls_tile.copy()


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


manager = pygame_gui.UIManager((width, height))
btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((LEFT, (Cell_size * len(Level_map[0]) + 120)), (120, 30)),
                                             text='Exit',
                                             manager=manager)

healthbar = pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect((len(Level_map)
                                                       * 60 + 60, (Cell_size * len(Level_map[0]) + 120)), (120, 30)),
                                                       manager=manager)

label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((len(Level_map)
                                                       * 60 + 60, (Cell_size * len(Level_map[0]) + 240)), (120, 30)),
                                                       manager=manager, text='0:00')


manager_2 = pygame_gui.UIManager((width, height))
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width // 2 - 100, 320), (220, 50)),
                                             text='Начать игру',
                                             manager=manager_2)

exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width // 2 - 100, 400), (220, 50)),
                                             text='Выход',
                                             manager=manager_2)

Time = 6000


class Label():
    def __init__(self):
        self.left = LEFT
        self.top = TOP

    def set_view(self, left, top):
        self.left = left
        self.top = top

    def render(self):
        pygame.draw.rect(screen, pygame.Color('purple'), (width // 2 - 250, 150, 520, 80), 1)
        font = pygame.font.Font(None, 58)
        text = font.render('Man\'s play', True, pygame.Color('black'))
        screen.blit(text, (width // 2 - 125, 170))


class Tile(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename)
        self.image.set_colorkey('white')
        self.mask = pygame.mask.from_surface(self.image)
        for coords in Walls_tile:
            self.rect = self.image.get_rect(topleft=((coords[0] * 60) + LEFT, (coords[1] * 60) + TOP))
            break
        del Walls_tile[0]


class Player(pygame.sprite.Sprite):
    def __init__(self, filename, command, current_health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename).convert_alpha()
        self.image.set_colorkey('white')
        self.mask = pygame.mask.from_surface(self.image)
        self.health_capacity = 200
        self.current_health = current_health
        self.command = command
        self.moves = 5
        for coords in Coords_for_players:
            Level_map[coords[0]][coords[1]] = '.'
            self.rect = self.image.get_rect(topleft=((coords[0] * 60) + LEFT, (coords[1] * 60) + TOP))
            break
        del Coords_for_players[0]
        self.count = False

    def move_down(self):
        if self.moves > 0:
            x = (self.rect.left - board.left) // Cell_size
            y = (self.rect.top - board.top) // Cell_size
            if self.rect.top == (len(Level_map[x]) - 1) * Cell_size + TOP and Level_map[x][0] != '#':
                self.rect[1] = TOP
                self.moves -= 1

            elif self.rect.top == (len(Level_map[x]) - 1) * Cell_size + TOP and Level_map[x][0] == '#':
                pass
            else:
                if Level_map[x][y + 1] == '#':
                    pass
                else:
                    self.rect[1] += 60
                    self.moves -= 1


    def move_up(self):
        if self.moves > 0:
            x = (self.rect.left - board.left) // Cell_size
            y = (self.rect.top - board.top) // Cell_size
            if self.rect.top == TOP and Level_map[x][len(Level_map[x]) - 1] != '#':
                self.rect[1] = (len(Level_map[x]) - 1) * Cell_size + TOP
                self.moves -= 1

            elif self.rect.top == TOP and Level_map[x][len(Level_map[x]) - 1] == '#':
                pass
            else:
                if Level_map[x][y - 1] == '#':
                    pass
                else:
                    self.rect[1] -= 60
                    self.moves -= 1


    def move_right(self):
        if self.moves > 0:
            x = (self.rect.left - board.left) // Cell_size
            y = (self.rect.top - board.top) // Cell_size
            if self.rect.left == (len(Level_map) - 1) * Cell_size + LEFT and Level_map[0][y] != '#':
                self.rect[0] = LEFT
                self.moves -= 1

            elif self.rect.left == (len(Level_map) - 1) * Cell_size + LEFT and Level_map[0][y] == '#':
                pass
            else:
                if Level_map[x + 1][y] == '#':
                    pass
                else:
                    self.rect[0] += 60
                    self.moves -= 1


    def move_left(self):
        if self.moves > 0:
            x = (self.rect.left - board.left) // Cell_size
            y = (self.rect.top - board.top) // Cell_size
            if self.rect.left == LEFT and Level_map[len(Level_map) - 1][y] != '#':
                self.rect[0] = (len(Level_map) - 1) * Cell_size + LEFT
                self.moves -= 1
            elif self.rect.left == LEFT and Level_map[len(Level_map) - 1][y] == '#':
                pass
            else:
                if Level_map[x - 1][y] == '#':
                    pass
                else:
                    self.rect[0] -= 60
                    self.moves -= 1


    def check(self, mouse):
        if self.rect.left <= mouse[0] <= self.rect.left + self.rect.size[0] and self.rect.top <= mouse[1]\
                <= self.rect.top + self.rect.size[0]:
            self.count = True
            self.moves = 5
            healthbar.set_sprite_to_monitor(sprite_to_monitor=sprt)
        else:
            self.count = False

    def attack(self, sprites, go):                                            #Проверяет столкновение только в поле
                                         #С границами пока что не сделал. Если current_health = 0, то персонаж исчезает.
        if self.moves > 0:
            for sprt in sprites:
                if go == 'down':
                    if self.rect.top == (len(Level_map[x]) - 1) * Cell_size + TOP and self.rect.left == sprt.rect.left and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1
                        return True
                    elif self.rect.top + 60 == sprt.rect.top and self.rect.left == sprt.rect.left and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1
                        return True
                    elif self.rect.top + 60 == sprt.rect.top and self.rect.left == sprt.rect.left and sprt.command == self.command:
                        return True
                elif go == 'up':
                    if self.rect.top == TOP and self.rect.left == sprt.rect.left and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1
                        return True
                    elif self.rect.top - 60 == sprt.rect.top and self.rect.left == sprt.rect.left and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1
                        return True
                    elif self.rect.top - 60 == sprt.rect.top and self.rect.left == sprt.rect.left and sprt.command == self.command:
                        return True
                elif go == 'right':
                    if self.rect.left == (len(Level_map) - 1) * Cell_size + LEFT and self.rect.top == sprt.rect.top and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1
                        return True
                    elif self.rect.top == sprt.rect.top and self.rect.left + 60 == sprt.rect.left and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1
                        return True
                    elif self.rect.top == sprt.rect.top and self.rect.left + 60 == sprt.rect.left and sprt.command == self.command:
                        return True
                elif go == 'left':
                    if self.rect.left == LEFT and self.rect.top == sprt.rect.top and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1

                        return True
                    elif self.rect.top == sprt.rect.top and self.rect.left - 60 == sprt.rect.left and sprt.command != self.command:
                        if sprt.current_health - 5 <= 0:
                            sprt.current_health -= 5
                            sprt.kill()
                            self.moves -= 1
                        else:
                            sprt.current_health -= 5
                            self.moves -= 1
                        return True
                    elif self.rect.top == sprt.rect.top and self.rect.left - 60 == sprt.rect.left and sprt.command == self.command:
                        return True




class Point(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename).convert()
        self.image.set_colorkey('white')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=((x * Cell_size) + LEFT, (y * Cell_size) + TOP))
        self.count = 0

    def update(self, player):
        if not pygame.sprite.collide_rect(self, player) and self.count == 0:
            return True
        elif pygame.sprite.collide_rect(self, player):
            self.count += 1
            if player.current_health + 5 <= player.health_capacity:
                player.current_health += 5
            return False
        else:
            return False


def randomiser():
    x = random.randint(0, len(Level_map) - 1)
    y = random.randint(0, len(Level_map[0]) - 1)
    if Level_map[x][y] == '#' or Level_map[x][y] == '@':
        return (4, 0)
    else:
        return (int(x), int(y))


player_1 = Player('kontsepty4.png', 1, 100)
player_2 = Player('kontsepty4.png', 1, 100)
player_3 = Player('man-2.png', 2, 200)
player_4 = Player('man-2.png', 2, 200)

first_command = pygame.sprite.Group()
second_command = pygame.sprite.Group()

first_command.add(player_1)
first_command.add(player_2)

second_command.add(player_3)
second_command.add(player_4)

tiles = pygame.sprite.Group()
for _ in range(len(Walls_tile)):
    tiles.add(Tile('ice_header.png'))
all_sprites = pygame.sprite.Group()
all_sprites.add(player_1)
all_sprites.add(player_2)
all_sprites.add(player_3)
all_sprites.add(player_4)

x, y = randomiser()
point = Point('red-apple.png', x, y)
board = Board()
label = Label()
running = False
start_run = True
clock = pygame.time.Clock()
fps = 30
apple = True
while start_run:
    clock.tick(fps)
    time_delta = clock.tick(fps) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    running = True
                    start_run = False
                if event.ui_element == exit_button:
                    running = False
                    start_run = False
        manager_2.process_events(event)
    pygame.display.flip()
    screen.blit(menu_background, (0, 0))
    manager_2.draw_ui(screen)
    manager_2.update(time_delta)
    label.render()
while running:
    clock.tick(fps)
    end_game += 1
    print(end_game)
    if end_game / 30 == 300:
        running = False
        print(end_game)
    time_delta = clock.tick(fps) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                running = False
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprt in all_sprites:
                sprt.check(event.pos)
        if event.type == pygame.KEYDOWN:
            for sprt in all_sprites:
                if sprt.count:
                    if event.key == pygame.K_s:
                        if not sprt.attack(all_sprites, 'down'):
                            sound_step.play()
                            sprt.move_down()
                            healthbar.set_sprite_to_monitor(sprite_to_monitor=sprt)
                    if event.key == pygame.K_w:
                        if not sprt.attack(all_sprites, 'up'):
                            sound_step.play()
                            sprt.move_up()
                            healthbar.set_sprite_to_monitor(sprite_to_monitor=sprt)
                    if event.key == pygame.K_d:
                        if not sprt.attack(all_sprites, 'right'):
                            sound_step.play()
                            sprt.move_right()
                            healthbar.set_sprite_to_monitor(sprite_to_monitor=sprt)
                    if event.key == pygame.K_a:
                        if not sprt.attack(all_sprites, 'left'):
                            sound_step.play()
                            sprt.move_left()
                            healthbar.set_sprite_to_monitor(sprite_to_monitor=sprt)

        manager.draw_ui(screen)
        for player in all_sprites:
            if point.update(player):
                screen.blit(point.image, point.rect)
            else:
                x, y = randomiser()
                point = Point('red-apple.png', x, y)
        manager.process_events(event)
        pygame.display.flip()
        screen.blit(background, (0, 0))
        count1 = 0
        count2 = 0
        for sprt in all_sprites:
            screen.blit(sprt.image, sprt.rect)
            if sprt.command == 1:
                count1 += 1
            elif sprt.command == 2:
                count2 += 1
        if count1 == 0:
            print('победила 2я команда')
            running = False
        elif count2 == 0:
            print('победила 1я команда')
            running = False
        for sprite in tiles:
            screen.blit(sprite.image, sprite.rect)
        board.render()
        manager.update(time_delta)
pygame.quit()