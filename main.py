import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    my_font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    kills = 0

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("You quit")
                return
            
        for thing in updatable:
            thing.update(dt)

        screen.blit(pygame.image.load("space.png"), (0,0))  # Replace space.png for with your image for a different background

        text_surface = my_font.render(f"Score: {str(kills)}", True, (255,255,255))
        screen.blit(text_surface, (0,SCREEN_HEIGHT-20))

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                print(f"Final score: {kills}")
                pygame.quit()
                return
            
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    kills += 1
                    asteroid.split()
        

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
