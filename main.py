import pygame
from pygame.constants import QUIT

WIDTH = 1024
HEIGHT = 768
TITLE = 'TarotPrototype'


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return


if __name__ == '__main__':
    main()
