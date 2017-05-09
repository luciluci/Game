from Levels import ScreenManager

import localtypes
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode(localtypes.screen_size)
    pygame.display.set_caption("Bird Jumper")

    #player = Player()

    #active_sprite_list = pygame.sprite.Group()

    screen_manager = ScreenManager(screen)

    #current_level = Level_01(player)
    #player.level = current_level

    #player.rect.x = 340
    #player.rect.y = localtypes.SCREEN_HEIGHT - player.rect.height
    #active_sprite_list.add(player)

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
                    screen_manager.key_event_triggered(localtypes.KEY_LEFT)
                    #player.go_left()

                #if event.key == pygame.K_RIGHT:
                #    player.go_right()
                #if event.key == pygame.K_UP:
                #    player.jump()

            if event.type == pygame.KEYUP:
                screen_manager.key_event_triggered(localtypes.KEY_RELEASED)
                #if event.key == pygame.K_LEFT and player.change_x < 0:
                #    player.is_fade_stop = True
                #if event.key == pygame.K_RIGHT and player.change_x > 0:
                #    player.is_fade_stop = True

        #active_sprite_list.update()
        #current_level.update()

        #current_level.shift_world(-5)
        screen_manager.update()
        screen_manager.shit_world()
        screen_manager.draw()

        #screen.fill(localtypes.BLUE)
        #current_level.draw(screen)
        #active_sprite_list.draw(screen)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()