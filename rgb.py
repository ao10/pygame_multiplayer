#!/usr/bin/env python3
import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    pygame.display.set_caption('Multiplayer Game')
    clock = pygame.time.Clock()
    # surface = pygame.image.load('foo.png').convert()
    rect = pygame.Rect(10, 20, 30, 30)

    running = True
    while running:
        # Process player inputs
        for event in pygame.event.get():
            print(event)
            # Do logical updates here
            if event.type == pygame.QUIT:
                running = False
                raise SystemExit
            if event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    screen.fill("red")
                elif event.key == pygame.K_g:
                    screen.fill("green")
        # Render the graphics here.
        pygame.display.flip() # Refresh on-screen display
        clock.tick(60)        # Wait until next frame (at 60 FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
