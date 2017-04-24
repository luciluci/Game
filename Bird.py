import pygame
import localtypes

player_width = 40
player_height = 40

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([player_width, player_height])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()

        #Change vector
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.apply_gravity()

        self.rect.x += self.change_x
        self.rect.y += self.change_y


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

    def jump(self):
        self.change_y = -10

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

#class Level(object):

#    def draw(self):
#        screen.fill(BLUE)
