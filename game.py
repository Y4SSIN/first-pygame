import pygame
pygame.init()

# Creating the window of the game
screenWidth = 750
screenHeight = 480
win = pygame.display.set_mode((screenWidth, screenHeight))

walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')

# Giving the game a title
pygame.display.set_caption("My First Python Game")

clock = pygame.time.Clock()

# Default values
x = 50
y = 400
characterWidth = 64
characterHeight = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redraw_game_window():
    global walkCount

    # fill the screen before drawing the new character
    win.blit(bg, (0, 0))
    # drawing the charater
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    # refresh the display and show the character
    pygame.display.update()

# Main loop
run = True
while run:
    clock.tick(27)

    # check if certain events have happened
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # check which key has been pressed and the coordinates with the velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - characterWidth - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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
    
    redraw_game_window()

pygame.quit()
