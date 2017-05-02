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

class MenuItems(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("resources/Menu_Items.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                           sprite_sheet_data[1],
                                           sprite_sheet_data[2],
                                           sprite_sheet_data[3])
        self.rect = self.image.get_rect()

class PlayButton:

    def __init__(self, x, y):
        play_sprite = MenuItems(localtypes.PLAY_BUTTON)
        play_sprite.rect.x = x
        play_sprite.rect.y = y
        self.play_button = pygame.sprite.GroupSingle(play_sprite)

    def draw(self, screen):
        self.play_button.draw(screen)

