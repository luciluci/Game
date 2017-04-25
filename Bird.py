import pygame
import localtypes

player_width = 40
player_height = 40

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        frame1 = pygame.Surface([player_width, player_height])
        frame1.fill(localtypes.RED)
        frame2 = pygame.Surface([player_width, player_height])
        frame2.fill(localtypes.BLACK)

        self.images.append(frame1)
        self.images.append(frame2)

        self.index = 0
        self.image = self.images[self.index]

        #self.rect = pygame.Surface([player_width, player_height])#self.image.get_rect()
        self.rect = self.image.get_rect()

        #Change vector
        self.change_x = 0
        self.change_y = 0

        self.level = None

        self.is_fade_stop = False

    def update(self):
        self.apply_gravity()
        self.apply_horizontal_fade()

        self.rect.x += self.change_x

        colision_sprite = pygame.sprite.spritecollideany(self, self.level.platform_list, False)
        if colision_sprite:
            print "COLLISION"

        # for block in block_hit_list:
        #     # If we are moving right,
        #     # set our right side to the left side of the item we hit
        #     if self.change_x > 0:
        #         self.rect.right = block.rect.left
        #     elif self.change_x < 0:
        #         # Otherwise if we are moving left, do the opposite.
        #         self.rect.left = block.rect.right

        self.rect.y += self.change_y

        # for block in block_hit_list:
        #
        #     # Reset our position based on the top/bottom of the object.
        #     if self.change_y > 0:
        #         self.rect.bottom = block.rect.top
        #     elif self.change_y < 0:
        #         self.rect.top = block.rect.bottom
        #
        #     # Stop our vertical movement
        #     self.change_y = 0

        #print "(X:%d, Y:%d)" %(self.rect.x, self.rect.y)
        #print "(CH_X:%d, CH_Y:%d)" %(self.change_x, self.change_y)

    def apply_horizontal_fade(self):
        if self.is_fade_stop == True:
            self.fade_stop()
            if self.change_x <= 0.3 and self.change_x >= -0.3:
                self.change_x = 0
                self.is_fade_stop = False


    def apply_gravity(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += localtypes.EARTH_GRAVITY

        # See if we are on the ground.
        if self.rect.y >= localtypes.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = localtypes.SCREEN_HEIGHT - self.rect.height
        if self.rect.y <= 0:
            print "WARNING! ceiling reached"

    def jump(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.change_y = -10

    def fade_stop(self):
        if self.change_x < 0:
            self.change_x += 0.4
        elif self.change_x > 0:
            self.change_x -= 0.4

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
