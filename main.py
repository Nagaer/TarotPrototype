import pygame
from pygame.constants import QUIT


def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('TarotPrototype')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return


if __name__ == '__main__': main()