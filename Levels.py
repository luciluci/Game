from Scenary import Platform, PlayButton
from utilities import EventManager
from Bird import Player

import pygame
import localtypes

class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.event_manager = EventManager.Broadcaster()
        self.main_menu = MainMenu(self.event_manager)
        self.level01 = Level_01(self.event_manager)

        self.levels = [self.main_menu, self.level01]
        self.level_index = 0

        self.current_level = self.levels[self.level_index]

        self.register_to_events()

    def register_to_events(self):
        self.event_manager.on_screen_change += self.next_screen
        self.event_manager.on_key_press += self.key_event_triggered

    def next_screen(self):
        self.level_index += 1
        self.current_level = self.levels[self.level_index%len(self.levels)]
        self.draw()

    def draw(self):
        self.current_level.draw(self.screen)

    def fire_event_click(self):
        self.event_manager.on_click.fire()

    def key_event_triggered(self, key):
        self.event_manager.on_key_press.fire(key)

    def shit_world(self):
        if self.current_level.level_type == localtypes.LEVEL_TYPE_LEVELS:
            self.current_level.shift_world(-5)

    def update(self):
        if self.current_level.level_type == localtypes.LEVEL_TYPE_LEVELS:
            self.current_level.update()

    def listen_mouse_over(self, cursor_pos):
        if self.current_level.level_type == localtypes.LEVEL_TYPE_MAIN_MENU:
            self.current_level.mouse_over(cursor_pos)


class MainMenu:
    def __init__(self, event_manager):
        #self.event_manager = EventManager.Broadcaster()
        self.event_manager = event_manager
        self.background = pygame.image.load("resources/background_01.png").convert()
        self.play_button = PlayButton(100, 100)
        self.register_event()

        self.level_type = localtypes.LEVEL_TYPE_MAIN_MENU

    def register_event(self):
        self.event_manager.on_click += self.play_button.on_click

    def unregister_event(self):
        self.event_manager.on_click -= self.play_button.on_click

    #def fire_events(self):
    #    self.event_manager.on_click.fire()

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.play_button.draw(screen)

    def mouse_over(self, cursor_position):
        self.play_button.mouse_over(cursor_position)

class Level:

    def __init__(self, event_manager):
        self.platform_list = None

        self.background = None

        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()

        self.player = Player(self.platform_list)
        self.player.rect.x = 340
        self.player.rect.y = localtypes.SCREEN_HEIGHT - self.player.rect.height

        self.event_manager = event_manager

        self.level_type = localtypes.LEVEL_TYPE_LEVELS

    def update(self):
        self.platform_list.update()
        self.player.update()

    def draw(self, screen):
        screen.fill(localtypes.BLUE)
        screen.blit(self.background, (self.world_shift // 3,0))
        self.platform_list.draw(screen)
        self.player.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
        if self.world_shift >= self.level_limit:
            self.world_shift += shift_x
            # Go through all the sprite lists and shift
            for platform in self.platform_list:
                platform.rect.x += shift_x

            #for enemy in self.enemy_list:
            #    enemy.rect.x += shift_x

    def trigger_end_level(self):
        self.event_manager.on_screen_change.fire()

    def register_to_events(self):
        self.event_manager.on_key_press += self.key_press_action

    def key_press_action(self, key):
        if key == localtypes.KEY_UP:
            self.player.jump()
        elif key == localtypes.KEY_RIGHT:
            self.player.go_right()
        elif key == localtypes.KEY_LEFT:
            self.player.go_left()
        elif key == localtypes.RELEASE_KEY:
            if self.player.change_x is not 0:
                self.player.is_fade_stop = True
        else:
            print "Unknown key action"


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, event_manager):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, event_manager)

        self.background = pygame.image.load("resources/background_01.png").convert()
        self.background.set_colorkey(localtypes.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [[localtypes.GRASS_LEFT, 500, 500],
                 [localtypes.GRASS_MIDDLE, 570, 500],
                 [localtypes.GRASS_RIGHT, 640, 500],
                 [localtypes.GRASS_LEFT, 800, 400],
                 [localtypes.GRASS_MIDDLE, 870, 400],
                 [localtypes.GRASS_RIGHT, 940, 400],
                 [localtypes.GRASS_LEFT, 1000, 500],
                 [localtypes.GRASS_MIDDLE, 1070, 500],
                 [localtypes.GRASS_RIGHT, 1140, 500],
                 [localtypes.STONE_PLATFORM_LEFT, 1120, 280],
                 [localtypes.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [localtypes.STONE_PLATFORM_RIGHT, 1260, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            #block.player = self.player
            self.platform_list.add(block)

        #self.player.platform_list = self.platform_list

        # Add a custom moving platform
        #block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        #block.rect.x = 1350
        #block.rect.y = 280
        #block.boundary_left = 1350
        #block.boundary_right = 1600
        #block.change_x = 1
        #block.player = self.player
        #block.level = self
        #self.platform_list.add(block)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(localtypes.screen_size)
    pygame.display.set_caption("Bird Jumper")
    clock = pygame.time.Clock()
    clock.tick(60)


    screen_manager = ScreenManager(screen)
    #mm = MainMenu()
    done = False

    while not done:
        #mm.mouse_over(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    done = True
            if event.type == pygame.MOUSEBUTTONUP:
                #print "mouse pressed at: ", pygame.mouse.get_pos()
                #mm.fire_events()
                screen_manager.fire_event_click()

        #mm.draw(screen)
        screen_manager.draw()

        pygame.display.flip()