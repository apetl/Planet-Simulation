import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU # 1AU = 100 pixels
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, colour, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distanceToSun

        self.xVel = 0
        self.yVel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        pygame.draw.circle(win, self.color, (x, y), self.radius)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

main()
