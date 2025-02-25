'''import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
running = True

max_x = 500
max_y = 500
x = 10
y = 10
dx = 7
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

pygame.quit()'''

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()

# Circle class
class Circle:
    max_x = 500
    max_y = 500

    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x >= Circle.max_x or self.x <= 0:
            self.dx = -self.dx
        if self.y >= Circle.max_y or self.y <= 0:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# List of circles
circles = [
    Circle(10, 10, 7, 5, 20, (255, 0, 0)),
    Circle(100, 100, 5, 7, 20, (0, 255, 0)),
    Circle(200, 200, 3, 3, 20, (0, 0, 255))
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    for circle in circles:
        circle.update()
        circle.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



