import pygame
import os


parentDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)  # Parent directory for project
dataDir = os.path.join(parentDir, "data")  # Enter data folder
iconDir = os.path.join(dataDir, "roomba.png")  # Get icon path

screen = pygame.display.set_mode((500, 300))

pygame.init()

#### Create a canvas on which to display everything ####
window = (700, 700)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background,(255,0,255),(0, 0,700,700))
#### Populate the surface with objects to be displayed ####

#### Blit the surface onto the canvas ####
screen.blit(background, (0,0))
#### Blit the surface onto the canvas ####

#### Update the the display and wait ####
clock = pygame.time.Clock()
pygame.display.flip()
done = False
x, y, angle = 0, 0, 0


image = pygame.image.load(iconDir)
rotated_image = image

while True:
    clock.tick(60)

    # old_rec = rotated_image.get_rect()
    # print(old_rec)

    rotated_image = pygame.transform.scale(rotated_image, (150, 150))
    old_rec = rotated_image.get_rect()
    print(old_rec,"               ",end='')
    rotated_image = pygame.transform.rotate(image, angle)
    old_rec = rotated_image.get_rect()
    print(old_rec,"               ",end='')
    rotated_image = pygame.transform.scale(rotated_image, (150, 150))
    old_rec = rotated_image.get_rect()
    print(old_rec)
    # rotated_image = pygame.transform.scale(rotated_image, (50, 50))

    angle += 1
    screen.blit(background, (0, 0))
    screen.blit(rotated_image, (0, 0))
    pygame.display.flip()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#### Update the the display and wait ####

pygame.quit()