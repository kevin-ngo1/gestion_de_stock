import pygame
import pygame_gui
from pygame.locals import *
from Bouton import Button
import sys
from Produit import Product

class Interface_Del():
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 400, 350
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Ajouter un produit")

        self.clock = pygame.time.Clock()
        self.gui_manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))
        self.id_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(150, 100, 200, 30),
                                                               manager=self.gui_manager)

        validate_button = Button("Valider", (120, 230), (30, 35),self.validate, color="#00a331")
        self.product_instance = Product()

        running=True
        while running:
            time_delta = self.clock.tick(30) / 1000.0

            for event in pygame.event.get():
                if event.type == QUIT:

                    running = False

                self.gui_manager.process_events(event)
                validate_button.handle_event(event)

            self.gui_manager.update(time_delta)
            self.screen.fill((255, 255, 255))
            self.gui_manager.draw_ui(self.screen)
            self.draw_text("Id du produit :", 19, 105)
            validate_button.draw(self.screen)

            if not running:
                pygame.display.set_mode((1200, 600))

            pygame.display.flip()

    def draw_text(self, text, x, y):
        font = pygame.font.Font(None, 28)
        text_surface = font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, (x, y))

    def validate(self):
        id = self.id_input.get_text()
        
        print("Id :", id)

        self.product_instance.delete_product(id)

        pygame.quit()
        sys.exit()
