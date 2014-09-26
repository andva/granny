import pygame
from constants import *

def my_draw_polygon(polygon, body, fixture, screen):
    vertices = [(body.transform * v) * PPM for v in polygon.vertices]
    vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
    pygame.draw.polygon(screen, DEBUG_COLORS[body.type], vertices)


def my_draw_circle(circle, body, fixture, screen):
    position = body.transform * circle.pos * PPM
    position = (position[0], SCREEN_HEIGHT - position[1])
    pygame.draw.circle(screen, DEBUG_COLORS[body.type], [int(x) for x in position], int(circle.radius * PPM))
