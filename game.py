import pygame
pygame.init()

# Creating the window of the game
screenWidth = 750
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))

# Giving the game a title
pygame.display.set_caption("My First Python Game")

# default values
x = 50
y = 440
characterWidth = 40
characterHeight = 60
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)

    # check if certain events have happened
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # check which key has been pressed and the coordinates with the velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - characterWidth - vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # fill the screen before drawing the new rectangle
    win.fill((0, 0, 0))
    # drawing the charater
    pygame.draw.rect(win, (255, 0, 0), (x, y, characterWidth, characterHeight))
    # refresh the display and show the character
    pygame.display.update()

pygame.quit()
