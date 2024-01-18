# SPAWN BALLS ON CLICK
import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_SPACE
from pymunk.vec2d import Vec2d

RES = WIDTH, HEIGHT = 800,800
FPS = 60

def spawn_ball(x,y):
    body_mass = 10
    body_radius = 10
    body_moment= pymunk.moment_for_circle(body_mass, 0.0, 10)
    body = pymunk.Body(mass=body_mass,moment=body_moment)
    shape = pymunk.Circle(body, body_radius)
    shape.friction = 1.5
    shape.elasticity = 0.7
    body.position = Vec2d(x,y)

    space.add(body, shape)
    return body, shape

pygame.init()
window = pygame.display.set_mode(RES)
space = pymunk.Space()
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(window)
space.gravity = Vec2d(0, 80)
space.damping = 0.9

if __name__ == '__main__':
    # GAME LOOP
    spawn_balls = False
    balls = []
    while True:
        window.fill("white")
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                spawn_balls = True
            if event.type == MOUSEBUTTONUP:
                spawn_balls =False
            
            if spawn_balls:
                x,y = pygame.mouse.get_pos()
                new_ball_body, new_ball_shape = spawn_ball(x,y)
                balls.append((new_ball_body, new_ball_shape))
        space.step(0.1)
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(FPS)
