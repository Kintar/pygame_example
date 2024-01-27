import pygame
from pygame import Vector2 as V2, Vector2
import random
from Camera import Camera
from Room import Room

running: bool = True
movement_vector: pygame.Vector2 = V2(0, 0)
movement_speed: float = 100.0

movement_map: dict[int, pygame.Vector2] = {
    pygame.K_LEFT: V2(1, 0),
    pygame.K_RIGHT: V2(-1, 0),
    pygame.K_UP: V2(0, 1),
    pygame.K_DOWN: V2(0, -1)
}


def process_events() -> None:
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


def handle_movement() -> None:
    global movement_vector
    global movement_map

    pressed: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
    movement_vector = V2(0, 0)
    for key in movement_map.keys():
        if pressed[key]:
            movement_vector += movement_map[key]


def generate_rooms() -> list[Room]:
    room_list: list[Room] = []
    for i in range(200):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)

        point: pygame.Vector2 = V2(x, y)
        rect: pygame.Rect = pygame.Rect(point.x, point.y, 30, 30)

        valid: bool = True

        # test the current room position against all others, reject if there's an overlap
        for r in room_list:
            if r.rect.colliderect(rect):
                valid = False
                break

        if not valid:
            continue

        r = (random.randint(1, 3) * 64) + 63
        g = (random.randint(1, 3) * 64) + 63
        b = (random.randint(1, 3) * 64) + 63

        room_list.append(Room(pygame.Color(r, g, b), rect))

    return room_list


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Example Thing')
    surf: pygame.Surface = pygame.display.set_mode((800, 800))

    camera: Camera = Camera(surf)

    for room in generate_rooms():
        camera.add_drawable(room)

    clock: pygame.time.Clock = pygame.time.Clock()

    while running:
        process_events()
        handle_movement()

        camera.move(movement_vector * clock.get_time() * 0.001 * movement_speed)
        camera.draw()

        pygame.display.update()

        clock.tick()
