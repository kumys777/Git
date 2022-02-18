import pygame
from random import randint

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    screen.fill(pygame.Color('blue'))
    pygame.display.flip()
    running = True
    st = 0
    st2 = 1
    clock = pygame.time.Clock()
    fps = 30
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                st = 0
                st2 = 0
                a1 = randint(0, 255)
                a2 = randint(0, 255)
                a3 = randint(0, 255)
        while st2 != 1:
            pygame.draw.circle(screen, (a1, a2, a3), pos, st)
            pygame.display.flip()
            st += 10
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    st2 = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.display.flip()
                    pos = event.pos
                    st = 0
                    screen.fill(pygame.Color('blue'))
                    a1 = randint(0, 255)
                    a2 = randint(0, 255)
                    a3 = randint(0, 255)
    pygame.quit()