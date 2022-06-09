# FS23 beta
import pygame

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN2 = pygame.display.set_mode((WIDTH + 200, HEIGHT))
pygame.display.set_caption("FS 23 beata!")
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw():
    WIN.fill(WHITE)
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            keys_press = pygame.key.get_pressed()
            if keys_press[pygame.K_z]:
                if event.type == pygame.QUIT:
                    run = False

            if event.type == pygame.QUIT:
                pass
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
