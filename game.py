import pygame
pygame.init()

# Creating the window of the game
screenWidth = 700
screenHeight = 480
win = pygame.display.set_mode((screenWidth, screenHeight))

walkRight = [pygame.image.load('assets/images/mage/R1.png'), pygame.image.load('assets/images/mage/R2.png'), pygame.image.load('assets/images/mage/R3.png'), pygame.image.load('assets/images/mage/R4.png'), pygame.image.load('assets/images/mage/R5.png'), pygame.image.load('assets/images/mage/R6.png'), pygame.image.load('assets/images/mage/R7.png'), pygame.image.load('assets/images/mage/R8.png'), pygame.image.load('assets/images/mage/R9.png')]
walkLeft = [pygame.image.load('assets/images/mage/L1.png'), pygame.image.load('assets/images/mage/L2.png'), pygame.image.load('assets/images/mage/L3.png'), pygame.image.load('assets/images/mage/L4.png'), pygame.image.load('assets/images/mage/L5.png'), pygame.image.load('assets/images/mage/L6.png'), pygame.image.load('assets/images/mage/L7.png'), pygame.image.load('assets/images/mage/L8.png'), pygame.image.load('assets/images/mage/L9.png')]
bg = pygame.image.load('assets/images/background/graveyard.jpg')
char = pygame.image.load('assets/images/mage/standing.png')

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
        self.hitbox = (self.x + 15, self.y + 10, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0],(self.x, self.y))
        self.hitbox = (self.x + 15, self.y + 10, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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

class Enemy(object):
    walkRight = [pygame.image.load('assets/images/skeleton/R1E.png'), pygame.image.load('assets/images/skeleton/R2E.png'), pygame.image.load('assets/images/skeleton/R3E.png'), pygame.image.load('assets/images/skeleton/R4E.png'), pygame.image.load('assets/images/skeleton/R5E.png'), pygame.image.load('assets/images/skeleton/R6E.png'), pygame.image.load('assets/images/skeleton/R7E.png'), pygame.image.load('assets/images/skeleton/R8E.png'), pygame.image.load('assets/images/skeleton/R9E.png')]
    walkLeft = [pygame.image.load('assets/images/skeleton/L1E.png'), pygame.image.load('assets/images/skeleton/L2E.png'), pygame.image.load('assets/images/skeleton/L3E.png'), pygame.image.load('assets/images/skeleton/L4E.png'), pygame.image.load('assets/images/skeleton/L5E.png'), pygame.image.load('assets/images/skeleton/L6E.png'), pygame.image.load('assets/images/skeleton/L7E.png'), pygame.image.load('assets/images/skeleton/L8E.png'), pygame.image.load('assets/images/skeleton/L9E.png')]

    def __init__(self, x, y, enemyWidth, enemyHeight, end):
        self.x = x
        self.y = y
        self.enemyWidth = enemyWidth
        self.enemyHeight = enemyHeight
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 15, self.y + 12, 28, 48)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 15, self.y + 12, 28, 48)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0  ]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print('hit')
        

def redraw_game_window():
    # Fill the screen before drawing the new character
    win.blit(bg, (0, 0))
    man.draw(win)
    skeleton.draw(win)

    for bullet in bullets:
        bullet.draw(win)
    # Refresh the display and show the character
    pygame.display.update()

man = Player(300, 385, 64, 64)
skeleton = Enemy(50, 385, 64, 64, 650)
# Main loop
run = True
bulletCooldown = 0
bullets = []
while run:
    clock.tick(27)

    if bulletCooldown > 0:
        bulletCooldown += 1
    if bulletCooldown > 3:
        bulletCooldown = 0
    

    # Check if certain events have happened
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < skeleton.hitbox[1] + skeleton.hitbox[3] and bullet.y + bullet.radius > skeleton.hitbox[1]:
            if bullet.x + bullet.radius > skeleton.hitbox[0] and bullet.x - bullet.radius < skeleton.hitbox[0] + skeleton.hitbox[2]:
                skeleton.hit()
                bullets.pop(bullets.index(bullet))
        if bullet.x < 750 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    # Check which key has been pressed and the coordinates with the velocity
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bulletCooldown == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:    
            bullets.append(Projectile(round(man.x + man.characterWidth // 2), round(man.y + man.characterHeight // 2), 6, (206,23,79), facing))

        bulletCooldown = 1

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
            man.y -= (man.jumpCount ** 2) * 0.3 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    
    redraw_game_window()

pygame.quit()
