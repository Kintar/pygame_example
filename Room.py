import pygame

from Camera import Drawable


class Room(Drawable):
    """Defines a simple rectangle of a given color, used as a room in this demo"""
    def __init__(self, color: pygame.Color, location: pygame.Rect):
        super().__init__(location, pygame.Vector2(location.x, location.y))
        self.size: pygame.Rect = location
        self.color: pygame.Color = color
        self.image: pygame.Surface = pygame.Surface((location.w, location.h))
        self.image.fill(self.color)


