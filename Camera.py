import pygame
from pygame import Vector2


class Drawable:
    """Drawable represents something that can be drawn on the screen, containing a position and a size

    This class exists just for consistency when using the Camera class to draw items to the screen."""
    def __init__(self, size: pygame.Rect, pos: pygame.Vector2 = (0, 0)):
        """Constructor for Drawable

        :param size: pygame.Rect: size of the Drawable in pixels
        :param pos: pygame.Vector2: location of the Drawable in 2d space. Defaults to Vector2(0, 0)"""

        self.pos: pygame.Vector2 = pos
        self.rect: pygame.Rect = size
        self.image: pygame.Surface = pygame.Surface((size.width, size.height))

    def set_image(self, image: pygame.Surface, fill_color: pygame.Color = pygame.Color('black'), scale: bool = True):
        """set the image used for this drawable

        Automatically scales the image to this Drawable's size unless the scale parameter is False"""
        self.image.fill(fill_color)
        if scale:
            image = pygame.transform.scale(image, (self.rect.width, self.rect.height))

        self.image.blit(image, (0, 0))

    def move(self, delta: pygame.Vector2) -> None:
        # Change our position
        self.pos += delta


class Camera:
    """Camera represents our view into the game

    This class is used to draw any Drawables, instead of blitting directly onto a Surface. This allows us to move the
    view around the world independently of the contents of the world."""

    def __init__(self, screen: pygame.Surface):
        """Constructor for Camera

        :param screen: the surface we'll draw onto when draw is called"""

        self.screen: pygame.Surface = screen
        self.pos: pygame.Vector2 = pygame.Vector2(0, 0)
        self.rect = screen.get_rect()

        self.drawables: list[Drawable] = []

    def add_drawable(self, drawable: Drawable) -> None:
        self.drawables.append(drawable)

    def remove_drawable(self, drawable: Drawable) -> None:
        self.drawables.remove(drawable)

    def move(self, delta: Vector2) -> None:
        self.pos += delta
        self.rect.move_ip(delta)

    def draw(self) -> None:
        for drawable in self.drawables:
            # this is our transform function
            screen_rect = drawable.rect.move(self.pos)

            # if the camera's rect doesn't contain the new position, then just move on
            if not self.rect.colliderect(screen_rect):
                continue

            # if we got here, at least PART of our screen_rect is inside our draw space, so draw the drawable
            self.screen.blit(drawable.image, (screen_rect.x, screen_rect.y))

