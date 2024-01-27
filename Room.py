import pygame

from Camera import Drawable


class Room(Drawable):
    """Defines a simple rectangle of a given color, used as a room in this demo"""
    def __init__(self, color: pygame.Color, size: pygame.Rect, pos: pygame.Vector2 = (0, 0)):
        super().__init__(size, pos)
        self.size: pygame.Rect = size
        self.color: pygame.Color = color
        self.image: pygame.Surface = pygame.Surface((size.w, size.h))
        self.image.fill(self.color)


