# BASIC SETUP
import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_SPACE

RES = WIDTH, HEIGHT = 800,800
FPS = 60

pygame.init()
window = pygame.display.set_mode(RES)
space = pymunk.Space()
clock = pygame.time.Clock()

if __name__ == '__main__':
    # GAME LOOP
    while True:
        window.fill("white")
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()
        
        space.step(0.1)
        pygame.display.flip()
        clock.tick(FPS)
