import pymunk
import pygame
import pymunk.pygame_util
from pygame.locals import *

window = pygame.display.set_mode((400,400))
space = pymunk.Space()

draw_options = pymunk.pygame_util.DrawOptions(window)

while True:
    window.fill("white")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    space.step(1/60)
    space.debug_draw(draw_options)
    pygame.display.flip()
