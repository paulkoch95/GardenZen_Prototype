# system imports
import random
import sys
import pygame
# own imports
from scenes import scene, menu_scene,title_scene
from sound import sound_engine
from assets.ressources import COLORS, FONT
__version__ = "alpha - 0.01"


# main game loop
def game(width, height, init_scene: scene.Scene, fps_cap):

    pygame.init()

    music = sound_engine.Engine()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(f'Garden Zen Prototype {__version__}')

    clock = pygame.time.Clock()

    active_scene = init_scene()
    font = FONT.pixel_font(30)

    while active_scene != None:

        filtered_events = []
        for event in pygame.event.get():
            filtered_events.append(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Debug way to switch scenes
                if event.key == pygame.K_UP:
                    active_scene = menu_scene.MenueScene()
                if event.key == pygame.K_DOWN:
                    active_scene = title_scene.SplashScreen()

        active_scene.input(filtered_events)
        active_scene.update(clock.get_time())
        active_scene.render(screen)
        active_scene = active_scene.next
        fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        screen.blit(fps, (50, 50))
        clock.tick(60)
        pygame.display.flip()

game(1000, 800, menu_scene.MenueScene, 120)
# game(1000,800, title_scene.SplashScreen, 60)
