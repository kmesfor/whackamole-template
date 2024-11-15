import random

import pygame
from pygame import Color


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_pos = (0, 0)
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (get_square_from_coordinates(event.pos)) == get_square_from_coordinates(mole_pos):
                        mole_pos=get_coordinates_from_square((random.randrange(0, 20), random.randrange(0, 16)))

            screen.fill("light green")
            draw_grid(screen, mole_image, mole_pos)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

def draw_grid(screen, mole_image, mole_pos):
    for i in range(20):
        pygame.draw.line(screen, Color(0, 0, 0), (i * 32, 0), (i * 32, 512), 1)
    for j in range(16):
        pygame.draw.line(screen, Color(0, 0, 0), (0, j * 32), (640, j * 32), 1)
    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos[0],mole_pos[1])))

def get_square_from_coordinates(cords):
    return cords[0] // 32, cords[1]  // 32

def get_coordinates_from_square(square):
    return square[0]*32, square[1]*32

if __name__ == "__main__":
    main()
