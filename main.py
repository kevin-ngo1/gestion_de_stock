import pygame
import sys
from Bouton import Button
from Produit import Product
from Interface_ajouter import Interface_Add
from Interface_supp import Interface_Del
from Interface_modifier import Interface_Change

pygame.init()

WIDTH, HEIGHT = 1200, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inventaire du magasin Photo Vintage")

#Variables
green="#00a331"
red="#cf3838"
orange="#ad921a"

#Boutons
add_button = Button("Ajouter", (50, 170), (30, 35),Interface_Add, color=green)
rem_button = Button("Supprimer", (50, 300),(15, 35), Interface_Del, color=red)
mod_button = Button("Modifier", (50, 430),(30, 35), Interface_Change, color=orange)
product_instance = Product()

#Texte et images
font = pygame.font.Font(None, 33)
image = pygame.image.load("picture/logo.png")
image = pygame.transform.scale(image, (200,130))
title_font = pygame.font.Font(None, 48)
title_text = title_font.render("Inventaire du magasin d'appareils photo Vintage", True, (0, 0, 0))
title_rect = title_text.get_rect(center=(WIDTH // 2 + 50, 70))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        add_button.handle_event(event)
        rem_button.handle_event(event)
        mod_button.handle_event(event)

    screen.fill((255, 255, 255))
    screen.blit(title_text, title_rect)
    screen.blit(image, (0, 0))
    add_button.draw(screen)
    rem_button.draw(screen)
    mod_button.draw(screen)

    pygame.draw.line(screen, (0, 0, 0), (0, 130), (WIDTH, 130), 10)

    products = product_instance.get_all_products()
    
    if products:
        y_position = 180
        for product in products:
            product_text = f"ID : {product[0]} | Nom : {product[1]} | Description : {product[2]} | Prix : {product[3]} Euros | Quantité: {product[4]} | Catégorie ID: {product[5]}"
            product_surface = font.render(product_text, True, (0, 0, 0))
            screen.blit(product_surface, (250, y_position))
            y_position += 20

    pygame.display.flip()

pygame.quit()
sys.exit()
