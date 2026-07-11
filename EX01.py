import pymunk
import pymunk.pygame_util
import pygame

import numpy as np
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt

pygame.init()
screen = pygame.display.set_mode((600, 400))

clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 981)

body = pymunk.Body(1, 100)
body.position = (300, 50)

shape = pymunk.Poly.create_box(body, (50, 50))
space.add(body, shape)

draw_options = pymunk.pygame_util.DrawOptions(screen)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    space.step(1/60)

    space.debug_draw(draw_options)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()