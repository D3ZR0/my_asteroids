from constants import *
import pygame
from player import *
from asteroid import *
from AsteroidField import *
import sys
from shot import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_1 =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(drawable)
    print("Hello from my-asteroids!")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for i in asteroid:
            if i.collide_detect(player_1):
                print("Game Over!")
                sys.exit()
        for i in asteroid:
            for j in shots:
                if i.collide_detect(j):
                    i.split()
                    j.kill()
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0


if __name__ == "__main__":
    main()


