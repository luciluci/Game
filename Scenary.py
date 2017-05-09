from spritesheet_functions import SpriteSheet
import localtypes

import pygame

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("resources/tiles_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

class ButtonBase(pygame.sprite.Sprite):

    def __init__(self, sprite_mouse_out, sprite_mouse_over):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("resources/Menu_Items.png")

        self.image_out = sprite_sheet.get_image(sprite_mouse_out[0],
                                                sprite_mouse_out[1],
                                                sprite_mouse_out[2],
                                                sprite_mouse_out[3])

        self.image_hover = sprite_sheet.get_image(sprite_mouse_over[0],
                                                  sprite_mouse_over[1],
                                                  sprite_mouse_over[2],
                                                  sprite_mouse_over[3])
        self.rect = self.image_out.get_rect()
        self.image = self.image_out

        #mouse over flags
        self.is_mouse_over = False
        self.mouse_over_histoy = False

        #mouse click action type
        self.click_action = localtypes.INVALID_ACTION

    def mouse_over(self, cursor_position):
        self.is_mouse_over = self.rect.collidepoint(cursor_position)

        if self.is_mouse_over == True:
            if self.mouse_over_histoy == False:
                self.image = self.image_hover
                self.mouse_over_histoy = True
        else:
            if self.mouse_over_histoy == True:
                self.image = self.image_out
                self.mouse_over_histoy = False


class PlayButton(ButtonBase):

    def __init__(self, x, y, event_manager):
        ButtonBase.__init__(self, localtypes.PLAY_BUTTON, localtypes.HEART_BUTTON)
        self.rect.x = x
        self.rect.y = y
        self.play_button = pygame.sprite.GroupSingle(self)
        self.event_manager = event_manager

    def draw(self, screen):
        self.play_button.draw(screen)

    def on_click(self):
        if self.is_mouse_over:
            print "PlayButton:Over click"
            self.click_action = localtypes.PLAY_ACTION
            self.event_manager.on_screen_change.fire()
        else:
            print "PlayButton:Outside click"
