import pygame
from player import *
from circleshape import *
from constants import *
from asteroid import *
from asteroidfield import *
import sys

def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    print(f"Asteroids count: {len(asteroids)}")
    print(f"Updatables count: {len(updatables)}")
    print(f"Drawables count: {len(drawables)}")

    clock = pygame.time.Clock()
    dt = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for drawable in drawables:
            drawable.draw(screen)
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print ("Game Over!")
                sys.exit()
        clock.tick(60)
        dt = clock.tick(60)/1000
        pygame.display.flip()

if __name__ == "__main__":
    main()