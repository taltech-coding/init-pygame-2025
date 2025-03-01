"""This file holds everything responsible for representing a button."""
import pygame
from pygame import SurfaceType

from resources import font
import time

class Button:
    """
    Class representing the button in the Fruit Ninja game.
    """
    def __init__(self, text, text_color, x, y, color, hover_color, action=None, padding=(20, 10)):
        """
        Initialize the Button object with provided values.

        :param text:
        :param text_color:
        :param x:
        :param y:
        :param color:
        :param hover_color:
        :param action:
        :param padding:
        """
        self.text = text
        self.text_color = text_color
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.last_pressed = False
        self.delay = 0.2

        text_surf = font.render(self.text, True, self.text_color)
        self.text_width = text_surf.get_width()
        self.text_height = text_surf.get_height()

        self.width = self.text_width + padding[0] * 2
        self.height = self.text_height + padding[1] * 2

        self.x = x - self.width // 2
        self.y = y - self.height // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self, screen: SurfaceType) -> None:
        """
        Draw the button on the game screen.

        :param screen: to draw the button on
        """
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, current_color, self.rect)

        text_surf = font.render(self.text, True, self.text_color)
        text_x = self.rect.centerx - self.text_width // 2
        text_y = self.rect.centery - self.text_height // 2
        screen.blit(text_surf, (text_x, text_y))
        
        if self.rect.collidepoint(mouse_pos) and not click and self.last_pressed and self.action:
            current_time = time.time()
            if current_time - self.last_pressed > self.delay:
                self.action()
                self.last_pressed = current_time
        self.last_pressed = click
