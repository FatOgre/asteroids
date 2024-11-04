import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x ,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(ASTEROID_MIN_SPLIT_ANG, ASTEROID_MAX_SPLIT_ANG)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = self.velocity.rotate(-angle) * 1.2
