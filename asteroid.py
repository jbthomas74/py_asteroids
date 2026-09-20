import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        rotated_vector = self.velocity.rotate(angle)
        rotated_vector2 = self.velocity.rotate(-1 * angle)
        newrad = self.radius - ASTEROID_MIN_RADIUS
        newasteroid1 = Asteroid(self.position.x, self.position.y, newrad)
        newasteroid1.velocity = rotated_vector * 1.2
        newasteroid2 = Asteroid(self.position.x, self.position.y, newrad)
        newasteroid2.velocity = rotated_vector2 * 1.2
