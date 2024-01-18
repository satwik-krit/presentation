# RANDOM COLORS, MASS AND COORDINATES
import random
import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_SPACE
from pymunk.vec2d import Vec2d

RES = WIDTH, HEIGHT = 800,800
FPS = 60
COLORS = ( (241, 196, 15,1.0),(46, 204, 113,1.0), (52, 152, 219,1.0), (142, 68, 173,1.0), (230, 126, 34,1.0) )

def spawn_ball(x,y):
    body_mass = random.randint(5,15)
    body_radius = random.randint(5,15)
    body_moment= pymunk.moment_for_circle(body_mass, 0.0, 10)
    body = pymunk.Body(mass=body_mass,moment=body_moment)
    shape = pymunk.Circle(body, body_radius)
    shape.color = random.choice(COLORS)
    shape.friction = 1.5
    shape.elasticity = 0.7
    body.position = Vec2d(x,y)

    space.add(body, shape)
    return body, shape

def create_segments(space):
    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_1 = pymunk.Segment(segment_body, (0,HEIGHT), (WIDTH, HEIGHT), 10)
    segment_1.elasticity = 0.7
    segment_1.friction = 1
    segment_2 = pymunk.Segment(segment_body, (0,HEIGHT), (0,0), 10)
    segment_2.elasticity = 0.7
    segment_2.friction = 1
    segment_3 = pymunk.Segment(segment_body, (WIDTH,0), (WIDTH, HEIGHT), 10)
    segment_3.elasticity = 0.7
    segment_3.friction = 1

    space.add(segment_2, segment_3, segment_1, segment_body)

pygame.init()
window = pygame.display.set_mode(RES)
space = pymunk.Space()
clock = pygame.time.Clock()

draw_options = pymunk.pygame_util.DrawOptions(window)
space.gravity = Vec2d(0, 80)
space.damping = 0.9

if __name__ == '__main__':
    # GAME LOOP
    create_segments(space)
    spawn_balls = False
    balls = []
    while True:
        window.fill("white")
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                for b_body, b_shape in balls:
                    space.remove(b_body,b_shape)
                balls.clear()
            if event.type == MOUSEBUTTONDOWN:
                spawn_balls = True
            if event.type == MOUSEBUTTONUP:
                spawn_balls =False
            
            if spawn_balls:
                x,y = pygame.mouse.get_pos()
                x += random.randint(-5,5)
                y += random.randint(-5,5)
                new_ball_body, new_ball_shape = spawn_ball(x,y)
                balls.append((new_ball_body, new_ball_shape))
        space.step(0.1)
        space.debug_draw(draw_options)
        dr
        pygame.display.flip()
        clock.tick(FPS)
