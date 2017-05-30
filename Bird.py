from spritesheet_functions import SpriteSheet

import pygame
import localtypes

player_width = 40
player_height = 40

class Player(pygame.sprite.Sprite):
    def __init__(self, platform_list):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        frame1 = pygame.Surface([player_width, player_height])
        frame1.fill(localtypes.RED)
        frame2 = pygame.Surface([player_width, player_height])
        frame2.fill(localtypes.BLACK)

        sprite_sheet = SpriteSheet("resources/rsz_flyinggamecharacter.png")

        image_1 = sprite_sheet.get_image(localtypes.BIRD_SCENE_1[0],
                                         localtypes.BIRD_SCENE_1[1],
                                         localtypes.BIRD_SCENE_1[2],
                                         localtypes.BIRD_SCENE_1[3])
        image_2 = sprite_sheet.get_image(localtypes.BIRD_SCENE_2[0],
                                         localtypes.BIRD_SCENE_2[1],
                                         localtypes.BIRD_SCENE_2[2],
                                         localtypes.BIRD_SCENE_2[3])
        image_3 = sprite_sheet.get_image(localtypes.BIRD_SCENE_3[0],
                                         localtypes.BIRD_SCENE_3[1],
                                         localtypes.BIRD_SCENE_3[2],
                                         localtypes.BIRD_SCENE_3[3])
        image_4 = sprite_sheet.get_image(localtypes.BIRD_SCENE_4[0],
                                         localtypes.BIRD_SCENE_4[1],
                                         localtypes.BIRD_SCENE_4[2],
                                         localtypes.BIRD_SCENE_4[3])

        self.images.append(image_1)
        self.images.append(image_2)
        self.images.append(image_3)
        self.images.append(image_4)
        #self.images.append(frame1)
        #self.images.append(frame2)

        self.image = self.images[0]

        #self.rect = pygame.Surface([player_width, player_height])#self.image.get_rect()
        self.rect = self.image.get_rect()

        #Change vector
        self.change_x = 0
        self.change_y = 0

        self.platform_list = platform_list

        self.is_fade_stop = False

        self.player_single_group = pygame.sprite.GroupSingle(self)

        #Number of updates/steps afeter jump is pressed,
        #used to change the image of the character from one frame to the other
        self.nrUpdatesAfterJump = 0

    def update(self):
        self.apply_gravity()
        self.apply_horizontal_fade()

        self.rect.x += self.change_x

        colision_sprite = pygame.sprite.spritecollideany(self, self.platform_list, False)
        #if colision_sprite:
            #print "COLLISION"

        self.rect.y += self.change_y

        #if self.change_y < 2 and self.change_y > 1:# and self.imageChanged == False:
        #    self.image = self.images[1]
        #    print "Change"
            #self.imageChanged = True

        if self.change_y != 0:
            self.nrUpdatesAfterJump += 1
            if self.nrUpdatesAfterJump == 3:
                self.image = self.images[3]
            #if self.nrUpdatesAfterJump == 4:
            #    self.image = self.images[2]
            #if self.nrUpdatesAfterJump == 5:
            #    self.image = self.images[3]
            if self.nrUpdatesAfterJump == 6:
                self.image = self.images[0]

        #print self.change_y

    def apply_horizontal_fade(self):
        if self.is_fade_stop == True:
            self.fade_stop()
            if self.change_x <= 0.3 and self.change_x >= -0.3:
                self.change_x = 0
                self.is_fade_stop = False

    def draw(self, screen):
        self.player_single_group.draw(screen)


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
        # See if we reached the ceiling.
        if self.rect.y <= 0:
            print "WARNING! ceiling reached"

    def jump(self):
        print "JUMP"
        self.nrUpdatesAfterJump = 0
        #self.index += 1
        #if self.index >= len(self.images):
        #    self.index = 0
        self.image = self.images[0]
        self.change_y = -localtypes.JUMP_AMPLITUDE

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
