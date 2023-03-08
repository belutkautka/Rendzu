import pygame


class Screen_options:
    def __init__(self):
        self.FPS = 10
        self.sc = pygame.display.set_mode((1000, 750))


class Colors:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.rose = (255, 0, 255)
        self.red = (255, 25, 25)
        self.green = (35, 200, 100)
        self.blue = (100, 20, 200)


class Button:
    def __init__(self, a1, a2, a3, a4, text, is_center):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.color = (0, 0, 0)
        self.font = pygame.font.SysFont('', 40)
        center = (a1[0] + 20, (a1[1] + a3[1]) / 2)
        if is_center:
            center = ((a1[0] + a2[0]) / 2, (a1[1] + a3[1]) / 2)
        self.font_render = self.font.render(text, True, (0, 0, 0))
        self.textRect = self.font_render.get_rect()
        self.textRect.center = center
        self.text = text

    def check_click(self, mouse_pos):
        if self.a1[0] < mouse_pos[0] < self.a2[0] and self.a1[1] < mouse_pos[1] < self.a3[1]:
            return True
        return False

    def draw(self, sc):
        pygame.draw.aaline(sc, self.color,
                           self.a1,
                           self.a2)
        pygame.draw.aaline(sc, self.color,
                           self.a1,
                           self.a3)
        pygame.draw.aaline(sc, self.color,
                           self.a3,
                           self.a4)
        pygame.draw.aaline(sc, self.color,
                           self.a4,
                           self.a2)
        self.font_render = self.font.render(self.text, True, (0, 0, 0))
        sc.blit(self.font_render, self.textRect)


class Text:
    def __init__(self, text, center, font=40, color=(0, 0, 0)):
        self.font = pygame.font.SysFont('', font)
        self.text = text
        self.color = color
        self.font_render = self.font.render(text, True, color)
        self.textRect = self.font_render.get_rect()
        self.textRect.center = center

    def draw(self, sc):
        self.font_render = self.font.render(self.text, True, self.color)
        sc.blit(self.font_render, self.textRect)


class Mouse_clicks:
    def __init__(self):
        self.delete = False
        self.mouse_click = False


class Button_variables:
    def __init__(self, num, d_num):
        self.text = ""
        self.number = num
        self.x = -1
        self.d_number = d_num


class Field:
    def __init__(self, field_size, cell_size, y_begin, x_begin):
        self.field_size = field_size
        self.cell_size = cell_size
        self.y = y_begin
        self.x = x_begin

    def draw(self, sc, cells):
        colors = Colors()
        for i in range(self.field_size):
            for j in range(self.field_size):
                if i < self.field_size - 1 and j < self.field_size - 1:
                    a1 = (self.x + self.cell_size / 2 + self.cell_size * i,
                          self.cell_size / 2 + self.y + self.cell_size * j)
                    a2 = (self.x + self.cell_size / 2 + self.cell_size * (i + 1),
                          self.cell_size / 2 + self.y + self.cell_size * j)
                    a3 = (self.x + self.cell_size / 2 + self.cell_size * i,
                          self.cell_size / 2 + self.y + self.cell_size * (j + 1))
                    a4 = (self.x + self.cell_size / 2 + self.cell_size * (i + 1),
                          self.cell_size / 2 + self.y + self.cell_size * (j + 1))
                    pygame.draw.aaline(sc, (0, 0, 0),
                                       a1,
                                       a2)
                    pygame.draw.aaline(sc, (0, 0, 0),
                                       a1,
                                       a3)
                    pygame.draw.aaline(sc, (0, 0, 0),
                                       a3,
                                       a4)
                    pygame.draw.aaline(sc, (0, 0, 0),
                                       a4,
                                       a2)
                a1 = (self.x + self.cell_size * i,
                      self.y + self.cell_size * j)
                a2 = (self.x + self.cell_size * (i + 1),
                      self.y + self.cell_size * j)
                a3 = (self.x + self.cell_size * i,
                      self.y + self.cell_size * (j + 1))
                center = ((a1[0] + a2[0]) / 2, (a1[1] + a3[1]) / 2)
                if cells[i][j] == 1:
                    pygame.draw.circle(sc, colors.black,
                                       center, 15)
                elif cells[i][j] == 2:
                    pygame.draw.circle(sc, colors.white,
                                       center, 15)
