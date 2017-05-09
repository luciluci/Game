from EventManager import Broadcaster
from Levels import MainMenu, Level_01

import localtypes

class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.event_manager = Broadcaster()
        self.main_menu = MainMenu(self.event_manager)
        self.level01 = Level_01(self.event_manager)

        self.levels = [self.main_menu, self.level01]
        self.level_index = 0

        self.current_level = self.levels[self.level_index]

        self.register_to_events()

    def register_to_events(self):
        self.event_manager.on_screen_change += self.next_screen
        self.current_level.register_events()

    def next_screen(self):
        print "next screen triggered"
        #unregister current level from events
        self.current_level.unregister_events()
        self.level_index += 1

        #Change current level and register it to own events
        self.current_level = self.levels[self.level_index%len(self.levels)]
        self.current_level.draw(self.screen)
        self.current_level.register_events()

    def draw(self):
        self.current_level.draw(self.screen)

    def fire_event_click(self):
        self.event_manager.on_click.fire()

    def fire_key_event(self, key):
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

