import pygame
from Camera import Camera
from Room import Room

running = True


def process_events():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Example Thing')
    surf: pygame.Surface = pygame.display.set_mode((800, 800))

    camera: Camera = Camera(surf)
    room: Room = Room(pygame.Color('aliceblue'), pygame.Rect(200, 200, 20, 30))
    camera.add_drawable(room)

    clock: pygame.time.Clock = pygame.time.Clock()

    while running:
        process_events()

        camera.draw()

        pygame.display.update()

        clock.tick()
