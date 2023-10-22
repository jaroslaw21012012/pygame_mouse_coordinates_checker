import pygame, sys, time
from pygame.locals import *

pygame.init()


FPS = 30
WIDTH = int(input("Your WIDTH: "))
HEIGHT = int(input("YOUR HEIGHT: "))

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PMC - PYGAME MOUSE COORDINATS")





#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (230, 230, 230, 10)


BG_COLOR = WHITE





points = []



draw = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                points = []
                print(points)
                draw = False
            if keys[pygame.K_RETURN]:
                if len(points) > 2:
                    print("drawing")
                    draw = True
                else:
                    print("where point")
            if keys[pygame.K_s]:
                with open("saved_coordinates.txt", "w") as f:
                    for point in points:
                        f.write(f"x={point[0]}, y={point[1]}\n")
                print("SAVED!")
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            point = (x, y)
            points.append(point)
            print(points)


    DISPLAYSURF.fill(BG_COLOR)
    pygame.draw.line(DISPLAYSURF, GRAY, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 3)
    pygame.draw.line(DISPLAYSURF, GRAY, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 3)
    if draw:
        draw_points = tuple(points)
        pygame.draw.polygon(DISPLAYSURF, BLACK, draw_points, 9)
    else:
        for point in points:
            pygame.draw.circle(DISPLAYSURF, GREEN, point, 5, 9)

    pygame.display.update()
    pygame.time.Clock().tick(FPS)