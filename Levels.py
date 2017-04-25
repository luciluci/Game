from Scenary import Platform

import pygame
import localtypes

class Level:

    def __init__(self, player):
        self.platform_list = None
        self.enemy_list = None

        self.background = None

        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        screen.fill(localtypes.BLUE)
        screen.blit(self.background, (self.world_shift // 3,0))
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

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
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        #block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

