import pygame
import click
from pygame.constants import QUIT

WIDTH = 1024
HEIGHT = 768
TITLE = 'TarotPrototype'
FULSCREEN = False


@click.command()
@click.option('-s', '--size', default=(WIDTH, HEIGHT))
@click.option('-t', '--title', default=TITLE)
@click.option('--fullscreen', is_flag=True, default=FULSCREEN)
def main(size, title, fullscreen):
    pygame.init()
    if fullscreen:
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    background = pygame.image.load('image.png')
    background_rect = background.get_rect(bottomright=size)
    screen.blit(background, background_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return


if __name__ == '__main__':
    main()
