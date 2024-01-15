# TEMPLATE
import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from pymunk.vec2d import Vec2d

RES = WIDTH, HEIGHT = 400, 400
FPS = 60
COLORS = ( (241, 196, 15,1.0),(46, 204, 113,1.0), (52, 152, 219,1.0), (142, 68, 173,1.0), (230, 126, 34,1.0) )

pygame.init()
window = pygame.display.set_mode(RES)
space = pymunk.Space()
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(window)
space.gravity = Vec2d(0, 800)

if __name__ == '__main__':
    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

        space.step(1/FPS)
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(FPS)

                
