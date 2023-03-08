import random
import sys
from pathlib import Path

import pygame
import pygame as pg

from Classes import Colors
from Classes import Field
from Classes import Screen_options
from Classes import Text

pygame.display.set_caption('NumberLinks')
pg.init()
colors = Colors()
screen_options = Screen_options()
field = Field(15, 40, 75, 68)
user_name = ''


def save_scores(name, score):
    f = r"Scores.txt"
    with open(f, 'a') as f:
        f.write(f"{str(name)} : {str(score)}\n")


def play_game(name):
    global user_name
    global colors
    global screen_options
    global field
    free_cells = []
    user_name = name
    size = 15
    cells = [[0] * size for i in range(size)]
    for i in range(len(cells)):
        for j in range(len(cells)):
            free_cells.append((i, j))
    mouse_click = False
    pygame.font.init()
    pygame.font.get_init()
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    seconds = 0
    is_player_move = True
    move = (-1, -1)
    play_button = pygame.Rect((700, 300),
                              (250, 100))
    mouse_pos = (0, 0)
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_click = True
        seconds = int((seconds + (pygame.time.get_ticks() - start_ticks)) / 1000)
        time_text = Text(f"{str(seconds // 60)} : {str(seconds % 60)}",
                         (825, 200), 150)
        if mouse_click and is_player_move:
            for i in range(size):
                for j in range(size):
                    a1 = (field.x + field.cell_size * i,
                          field.y + field.cell_size * j)
                    a2 = (field.x + field.cell_size * (i + 1),
                          field.y + field.cell_size * j)
                    a3 = (field.x + field.cell_size * i,
                          field.y + field.cell_size * (j + 1))
                    if a1[0] < mouse_pos[0] < a2[0] and a1[1] < mouse_pos[1] < a3[1] and cells[i][j] == 0:
                        if move != (-1, -1):
                            cells[move[0]][move[1]] = 0
                        move = (i, j)
                        cells[move[0]][move[1]] = 1
        if is_player_move and move != (-1, -1) and play_button.collidepoint(mouse_pos):
            cells[move[0]][move[1]] = 1
            free_cells.remove(move)
            pg.mixer.music.load(Path("music", "button.mp3"))
            pg.mixer.music.play()
            move = (-1, -1)
            is_player_move = False
            is_victory = check_victory(cells, 1)
            if is_victory:
                show_over(Text(f"Вы победили! Время:{seconds} сек", (500, 300), 60, colors.green), True, seconds, clock)
        if not is_player_move:
            move = do_move(free_cells)
            if move == (-1, -1):
                show_over(Text("Ничья", (500, 300)), False, seconds, clock)
            else:
                cells[move[0]][move[1]] = 2
                free_cells.remove(move)
            if check_victory(cells, 2):
                show_over(Text(f"Вы проиграли!", (500, 300), 80, colors.red), False, seconds, clock)
            move = (-1, -1)
            is_player_move = True
            # сделать ход или сказать игра окончена
        draw_elements(screen_options.sc, cells)
        time_text.draw(screen_options.sc)
        pygame.display.update()
        clock.tick(screen_options.FPS)
        mouse_click = False


def draw_elements(sc, cells):
    global screen_options
    global colors
    global field
    sc.fill(colors.white)
    pygame.draw.rect(sc, (125, 75, 20),
                     ((field.x, field.y),
                      (field.cell_size * field.field_size, field.cell_size * field.field_size)))
    field.draw(sc, cells)
    pygame.draw.rect(sc, colors.black,
                     ((700, 300),
                      (250, 100)), 3)
    text = Text(f"Сделать ход", (825, 350), 50)
    text.draw(screen_options.sc)


def do_move(free_cells):
    if len(free_cells) != 0:
        return random.choice(free_cells)
    return -1, -1


def show_over(text, is_win, seconds, clock):
    global colors
    global screen_options
    global user_name
    pg.mixer.music.pause()
    screen_options.sc.fill(colors.white)
    if is_win:
        save_scores(user_name, seconds)
        pg.mixer.music.load(Path("music", "win.mp3"))
        pg.mixer.music.play()
    else:
        pg.mixer.music.load(Path("music", "over.mp3"))
        pg.mixer.music.play()
    for i in range(0, 500):
        screen_options.sc.fill(colors.white)
        text.draw(screen_options.sc)
        pygame.display.update()
        clock.tick(100)

    exit()


def check_victory(cells, color):
    for j in range(len(cells)):
        for i in range(len(cells)):
            if cells[i][j] == color:
                x = i
                y = j
                coordinates_left_down = [(x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3), (x - 4, y + 4)]
                coordinates_right = [(x + 1, y), (x + 2, y), (x + 3, y), (x + 4, y)]
                coordinates_down = [(x, y + 1), (x, y + 2), (x, y + 3), (x, y + 4)]
                coordinates_right_down = [(x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3), (x + 4, y + 4)]
                if (direction_check(cells, color, coordinates_right_down)
                        or direction_check(cells, color, coordinates_left_down)
                        or direction_check(cells, color, coordinates_right)
                        or direction_check(cells, color, coordinates_down)):
                    return True
    return False


def direction_check(cells, color, coordinates):
    for coord in coordinates:
        if not is_correct_coordinate(coord, len(cells)):
            return False
        if cells[coord[0]][coord[1]] != color:
            return False
    return True


def is_correct_coordinate(coordinate, count):
    return 0 <= coordinate[0] < count and 0 <= coordinate[1] < count
