import pygame
pygame.init()
from assets.ressources import FONT, COLORS


class Button(pygame.sprite.Sprite):

    def __init__(self, ui: pygame.sprite.Group, text, pos, dim, connect=None):

        super().__init__(ui)

        self.text = text
        self.font = FONT.pixel_font(60)
        self.image = pygame.Surface(self.font.size(self.text))
        self.rect = pygame.rect.Rect(pos, self.image.get_size())
        print(self.rect)

        # button text to be displayed
        self.text = text

        # functiont to be called upon clicking the button
        self.connect = connect
        # rectangle representing the buttons extended dimensions

        # color speci for button
        self.hover_color = COLORS.RED
        self.normal_color = COLORS.WHITE
        self.current_bg_color = self.normal_color

        # if true, mouse is on nutton and left mousebutton is pressed down
        self.pressed = False

        # representation of text rendering to be displayed on top of button
        self.draw()

    def draw(self):
        """
        All rendering task for the button go here, no logic is being done here regarding input!
        :return:
        """
        self.image = pygame.Surface(self.font.size(self.text), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.current_bg_color, ((0,0),(self.image.get_size())))
        self.image.blit(self.font.render(self.text, True, COLORS.BLACK), (0,0))

    def input(self, events):
            """
            Check if mouse is inside of button rectangle and check it is has been clicked and released,
            if true, buttons click event is being called by the assigned connect method
            :return:
            """
            mouse = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse):
                self.current_bg_color = self.hover_color
                self.draw()
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                    self.color = COLORS.GREEN
                else:
                    if self.pressed == True:
                        self.connect()
            else:
                self.current_bg_color = self.normal_color
                self.draw()