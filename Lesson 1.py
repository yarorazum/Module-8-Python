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

'''import pygame

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

pygame.quit()'''

'''import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Shapes")

clock = pygame.time.Clock()

class Shape:
    max_x = 500
    max_y = 500

    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def update(self):
        self.x += self.dx
        self.y += self.dy

        left, right, top, bottom = self.get_bounds()

        if left <= 0 or right >= Shape.max_x:
            self.dx = -self.dx
        if top <= 0 or bottom >= Shape.max_y:
            self.dy = -self.dy

    def get_bounds(self):
        raise NotImplementedError("Subclasses must implement get_bounds")

    def draw(self, screen):
        raise NotImplementedError("Subclasses must implement draw")

class Circle(Shape):
    def __init__(self, x, y, dx, dy, radius, color):
        super().__init__(x, y, dx, dy, color)
        self.radius = radius

    def get_bounds(self):
        left = self.x - self.radius
        right = self.x + self.radius
        top = self.y - self.radius
        bottom = self.y + self.radius
        return left, right, top, bottom

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Square(Shape):
    def __init__(self, x, y, dx, dy, side, color):
        super().__init__(x, y, dx, dy, color)
        self.side = side

    def get_bounds(self):
        left = self.x
        right = self.x + self.side
        top = self.y
        bottom = self.y + self.side
        return left, right, top, bottom

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.side, self.side))

class Triangle(Shape):
    def __init__(self, x, y, dx, dy, width, height, color):
        super().__init__(x, y, dx, dy, color)
        self.width = width
        self.height = height

    def get_bounds(self):
        left = self.x
        right = self.x + self.width
        top = self.y
        bottom = self.y + self.height
        return left, right, top, bottom

    def draw(self, screen):
        points = [
            (self.x, self.y),
            (self.x + self.width, self.y),
            (self.x + self.width // 2, self.y + self.height)
        ]
        pygame.draw.polygon(screen, self.color, points)

shapes = [
    Circle(10, 10, 7, 5, 20, (255, 0, 0)),
    Square(100, 100, 5, 7, 40, (0, 255, 0)),
    Triangle(200, 200, 3, 3, 40, 40, (0, 0, 255))
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    for shape in shapes:
        shape.update()
        shape.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()'''

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Shapes")

clock = pygame.time.Clock()


class Shape:
    max_x = 500
    max_y = 500

    def __init__(self, x, y, dx, dy, color, width, height):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.width = width
        self.height = height

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x + self.width >= Shape.max_x:
            self.dx = -self.dx
        if self.y <= 0 or self.y + self.height >= Shape.max_y:
            self.dy = -self.dy

    def draw(self, screen):
        raise NotImplementedError("Subclasses must implement draw")

class Circle(Shape):
    def __init__(self, x, y, dx, dy, radius, color):
        # For circle, width and height are diameter (2 * radius)
        super().__init__(x, y, dx, dy, color, radius * 2, radius * 2)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.radius, self.y + self.radius), self.radius)

class Square(Shape):
    def __init__(self, x, y, dx, dy, side, color):
        super().__init__(x, y, dx, dy, color, side, side)
        self.side = side

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.side, self.side))

class Triangle(Shape):
    def __init__(self, x, y, dx, dy, width, height, color):
        super().__init__(x, y, dx, dy, color, width, height)
        self.width = width
        self.height = height

    def draw(self, screen):
        points = [
            (self.x, self.y),
            (self.x + self.width, self.y),
            (self.x + self.width // 2, self.y + self.height)
        ]
        pygame.draw.polygon(screen, self.color, points)

shapes = [
    Circle(10, 10, 7, 5, 20, (255, 0, 0)),
    Square(100, 100, 5, 7, 40, (0, 255, 0)),
    Triangle(200, 200, 3, 3, 40, 40, (0, 0, 255))
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    for shape in shapes:
        shape.update()
        shape.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



