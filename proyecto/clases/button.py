import pygame
from pygame.surface import Surface
from pygame.font import Font

class Button():
    def __init__(self, text, witdh, heigth, pos, font: Font, screen: Surface):
        self.pressed = False
        self.screen = screen
        self.top_color = "#25D417"
        self.top_rect = pygame.Rect(pos, (witdh, heigth))
        
        self.text_surface = font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)
        
        
    def draw(self):
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, 0, 10)
        self.screen.blit(self.text_surface, self.text_rect)
        
    def check_click(self):
        value_click = False
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = "#6CA464"
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
        else:
            if self.pressed == True:
                value_click = True
                self.pressed = False
            self.top_color = "#25D417"
        return value_click