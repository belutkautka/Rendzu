import pygame_menu
from pathlib import Path
import pygame
import sys
from Functions import play_game
from Classes import Colors
from Classes import Screen_options

user_name = ''
colors = Colors()
screen_options = Screen_options()


def rules():
    global colors
    global screen_options
    pygame.get_init()
    pygame.display.set_caption('Рэндзю')
    pygame.init()
    pygame.font.init()
    pygame.font.get_init()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                main()
        screen_options.sc.fill(colors.white)
        dog_surf = pygame.image.load(Path('images', 'rule.png'))
        dog_rect = dog_surf.get_rect(
            bottomright=(1100, 600))
        screen_options.sc.blit(dog_surf, dog_rect)
        pygame.display.update()


def scores_list():
    global colors
    global screen_options
    global user_name
    pygame.get_init()
    pygame.display.set_caption('Рэндзю')
    pygame.init()
    pygame.font.init()
    pygame.font.get_init()
    f = open('Scores.txt', 'r')
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                f.close()
                main()
        screen_options.sc.fill(colors.white)
        font = pygame.font.SysFont('', 30)
        d = 50
        for line in f:
            text = font.render(line, True, (35, 200, 100))
            textRect = text.get_rect()
            textRect.center = (250, 20 + d)
            screen_options.sc.blit(text, textRect)
            d += 50
            pygame.display.update()


def play_game_with_save_name():
    global user_name
    play_game(user_name.get_value())


def main():
    global user_name
    global screen_options
    menu = pygame_menu.Menu('Рэндзю', 1000, 750,
                            theme=pygame_menu.themes.THEME_ORANGE)
    user_name = menu.add.text_input('Имя игрока : ', '')
    menu.add.button('Правила', rules)
    menu.add.button('Играть', play_game_with_save_name)
    menu.add.button('Рейтинг', scores_list)
    menu.add.button('Выход', pygame_menu.events.EXIT)
    menu.mainloop(screen_options.sc)


if __name__ == '__main__':
    main()
