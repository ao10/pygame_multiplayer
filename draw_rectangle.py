#!/usr/bin/env python3
import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    pygame.display.set_caption('Multiplayer Game')
    clock = pygame.time.Clock()

    start = (0, 0)
    size = (0, 0)
    drawing = False

    running = True
    while running:
        # Process player inputs
        for event in pygame.event.get():
            print(event)
            # Do logical updates here
            if event.type == QUIT:
                running = False
                raise SystemExit
            elif event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                drawing = False
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
            screen.fill("gray")
            pygame.draw.rect(screen, "red", (start, size), 2)
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
