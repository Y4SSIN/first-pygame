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

class Player(object):
    def __init__(self, x, y, characterWidth, characterHeight):
        self.x = x
        self. y = y
        self.characterWidth = characterWidth
        self.characterHeight = characterHeight
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0],(self.x, self.y))

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redraw_game_window():
    # Fill the screen before drawing the new character
    win.blit(bg, (0, 0))
    man.draw(win)

    for bullet in bullets:
        bullet.draw(win)
    # Refresh the display and show the character
    pygame.display.update()

man = Player(300, 410, 64, 64)

# Main loop
run = True
bullets = []
while run:
    clock.tick(27)

    # Check if certain events have happened
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 750 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    # Check which key has been pressed and the coordinates with the velocity
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:    
            bullets.append(Projectile(round(man.x + man.characterWidth // 2), round(man.y + man.characterHeight // 2), 6, (65,105,225), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.characterWidth - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    
    redraw_game_window()

pygame.quit()
