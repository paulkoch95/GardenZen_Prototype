import pygame
pygame.init()
from assets import colors
from ui import ui_component

class Button(ui_component.UIComponent):

    def __init__(self, surface: pygame.surface, text,pos, dim, connect=None):
        ui_component.UIComponent.__init__(self)
        # own render context
        self.surface = surface

        self.pos = pos
        self.dim = dim
        # button text to be displayed
        self.text = text
        # functiont to be called upon clicking the button
        self.connect = connect
        # rectangle representing the buttons extended dimensions
        self.button_rect = pygame.Rect(pos,dim)

        # color speci for button
        self.hover_color = colors.RED
        self.normal_color = colors.WHITE
        self.color = self.normal_color

        # if true, mouse is on nutton and left mousebutton is pressed down
        self.pressed = False

        # representation of text rendering to be displayed on top of button
        self.font = pygame.font.Font(None, 30)
        self.text_surface = self.font.render(self.text,True, colors.BLACK)
        if self.text_surface.get_width() < self.dim[0]:
            self.button_rect.width = self.button_rect.width+self.text_surface.get_width()

    def draw(self):
        """
        All rendering task for the button go here, no logic is being done here regarding input!
        :return:
        """
        pygame.draw.rect(self.surface,self.color, self.button_rect)
        self.surface.blit(self.text_surface,(self.button_rect.center))

    def check_click(self):
        """
        Check if mouse is inside of button rectangle and check it is has been clicked and released,
        if true, buttons click event is being called by the assigned connect method
        :return:
        """
        mouse = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.color = colors.GREEN
            else:
                if self.pressed == True:
                    #self.connect()
                    try:
                        self.connect()
                    except Exception as e:
                        print(f"Error calling function from ui component: {e}")
                    self.pressed = False
        else:
            self.color = self.normal_color