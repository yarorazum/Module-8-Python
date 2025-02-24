

"""max_x = 500
max_y = 500

x = 10
y = 10

dx = 1
dy = 1

def draw_circle(x,y):
    print((x, y))

while True:
    x += dx
    y += dy
    if x > max_x or x <= 0:
        dx = -dx
    if y > max_y or y <= 0:
        dy = -dy

    draw_circle(x, y)"""

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()

running = True

max_x = 500
max_y = 500
x = 10
y = 10
dx = 5
dy = 5
radius = 20
ball_color = (255, 255, 255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx
    y += dy

    if x >= max_x or x <= 0:
        dx = -dx
    if y >= max_y or y <= 0:
        dy = -dy

    screen.fill("purple")

    pygame.draw.circle(screen, ball_color, (x, y), radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

