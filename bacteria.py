#!/usr/bin/env python3
# @author: Marco Baturan
# GNU All-Permissive License
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
# Imports

import sys, pygame, time

# setup
pygame.init()
icon = pygame.image.load('icon_bacteria.png')  # Icon of app
pygame.display.set_icon(icon)
pygame.display.set_caption('Bacteria 1.0')  # Title of app
size = width, height = 300, 300
day = 93, 155, 155
night = 42, 46, 75
screen = pygame.display.set_mode(size)

a = 0  # A side
b = 150  # B side


#
# clase visor: pseudo-codigo a borrar una vez hecho todo
#
#     variables:hambre, pos-inicial, pos-final, come, fotosíntesis
#     métodos: generar ventana, generar cinco recuadros para variables


class Bacteria(pygame.sprite.Sprite):
    """Create bacteria.

        This object create a bacteria which can detect position of light in screen, and move soft to light for
        start photosynthesis in first place. The second method is search food deposit by user with a mouse click.
        Detect the position of food and take it.

    """

    def __init__(self):
        # variables
        pygame.sprite.Sprite.__init__(self)  # Super class for reference to move the sprite.
        self.hungry = 0
        self.new_pos = (0, 0)
        self.food = (0, 0)
        self.light = (0, 0)
        # Charge picture and initial position of bacteria.
        self.image = pygame.image.load("bacteria.gif")
        self.rect = self.image.get_rect()
        self.init_pos = self.rect.move(50, 50)

    def detect_light(self, a, b):
        """Detect light

            Detect the position of light and move the bacteria.

        """
        self.rect.x = a
        self.rect.y = b

    def detect_food(self, food):
        """Detect food.

            Detect the position of food and move the bacteria.
        """
        self.rect.x = food[0]
        self.rect.y = food[1]
        pass

    def detect_hungry(self, t=100):
        """Detect hungry or fault of energy."""

        t = t / 2
        while t:
            time.sleep(1)
            t -= 1
        print('Call feed function!')


bacteria = Bacteria()
bacteria.rect.x = 50
bacteria.rect.x = 50
player_list = pygame.sprite.Group()
player_list.add(bacteria)
while True:
    for event in pygame.event.get():
        # Detect every separated 'if' like independent event
        if event.type == pygame.QUIT:  # Close simulation.
            print('Exit because you click X.')
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:  # Close simulation.
            if event.key == ord('q'):
                print('Exit because you press q.')
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # A revisar para la próxima.
            print('In event loop:', event.pos, event.button)
            food = event.pos
            bacteria.detect_food(food)  # TODO: Make put food in screen and bacteria found it.

    screen.fill(day)
    screen.fill(night, (a, 0, 150, 300))  # draw the night side
    time.sleep(5)  # Swap the value position of day and night
    a, b = b, a
    # follow a, 100
    bacteria.update()
    bacteria.detect_light(a, b)
    player_list.draw(screen)
    pygame.display.update()
    pygame.display.flip()
