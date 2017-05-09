from Bosses.ScreenManager import ScreenManager

import localtypes
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode(localtypes.screen_size)
    pygame.display.set_caption("Bird Jumper")

    screen_manager = ScreenManager(screen)

    clock = pygame.time.Clock()
    clock.tick(60)

    done = False

    while not done:
        screen_manager.listen_mouse_over(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                screen_manager.fire_event_click()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    done = True
                if event.key == pygame.K_LEFT:
                    screen_manager.fire_key_event(localtypes.KEY_LEFT)
                if event.key == pygame.K_UP:
                    screen_manager.fire_key_event(localtypes.KEY_UP)
                if event.key == pygame.K_RIGHT:
                    screen_manager.fire_key_event(localtypes.KEY_RIGHT)

            if event.type == pygame.KEYUP:
                screen_manager.fire_key_event(localtypes.KEY_RELEASED)
                #if event.key == pygame.K_LEFT and player.change_x < 0:
                #    player.is_fade_stop = True
                #if event.key == pygame.K_RIGHT and player.change_x > 0:
                #    player.is_fade_stop = True

        screen_manager.update()
        screen_manager.shit_world()
        screen_manager.draw()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()