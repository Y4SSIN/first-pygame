import pygame
pygame.init()

# Creating the window of the game
win = pygame.display.set_mode((750, 500))

# Giving the game a title
pygame.display.set_caption("My First Python Game")

# default values
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    # check if certain events have happened
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # check which key has been pressed and the coordinates with the velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # fill the screen before drawing the new rectangle
    win.fill((0, 0, 0))
    # drawing the charater
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # refresh the display and show the character
    pygame.display.update()

pygame.quit()
