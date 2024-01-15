# COLLISIONS
import random
import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from pymunk.vec2d import Vec2d

RES = WIDTH, HEIGHT = 400, 400
FPS = 60
BOX_WIDTH, BOX_HEIGHT = 20, 20
BLUE, GREEN, ORANGE, YELLOW, BROWN, PINK, RED = 

pygame.init()
window = pygame.display.set_mode(RES)
space = pymunk.Space()
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(window)

space.gravity = Vec2d(0, 800)

def create_box(space):
    ...

def create_boxes(space):
    # Spawn boxes in random places
    boxes = []

    rects = [
        ()
    ]
    
    return boxes

if __name__ == '__main__':
    # GAME LOOP
    boxes = create_boxes(space)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

        space.step(1/FPS)
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(FPS)

                

