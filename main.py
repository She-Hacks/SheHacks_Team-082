import pygame
import random
import math
import sys
pygame.init()

screen = pygame.display.set_mode((800, 600))

points = 0
font = pygame.font.Font('freesansbold.ttf', 38)
pointsX = 10
pointsY = 10



def display_points(x, y):
    score = font.render("Score : " + str(points), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_end():
    message = font.render("Time's up!! Total score : " + str(points), True, (255, 255, 255))
    t = 100
    while t!=0:
      screen.blit(message,(200,300))
      t-=1
   


pygame.display.set_caption("GAME MODE ON ")
icon = pygame.image.load(r'download.jpg')
pygame.display.set_icon(icon)

player_image = pygame.image.load(r'dog-removebg-preview.png')
player_image = pygame.transform.scale(player_image, (100, 100))
playerX = 100
playerY = 400
playerX_change = 0
playerY_change = 0

bone_img = pygame.image.load(r'bone-removebg-preview.png')
bone_img = pygame.transform.scale(bone_img, (100, 100))
boneX = random.randint(50, 700)
boneY = random.randint(50, 100)
boneX_change = 5
boneY_change = 40

background = pygame.image.load('download (1).jpg')
background = pygame.transform.scale(background, (800, 600))

bullet_img = pygame.image.load(r'bullet-removebg-preview.png')
bullet_img = pygame.transform.scale(bullet_img, (50, 50))
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def player(x, y):
    screen.blit(player_image, (x, y))


def bone(x, y):
    screen.blit(bone_img, (x, y))


def successful_hit(boneX, boneY, bulletX, bulletY):
    distance = math.sqrt(math.pow(boneX-bulletX, 2) +
                         math.pow(boneY-bulletY, 2))
    if distance < 26:
        return True
    else:
        return False

PLAY_TIME = 30


running = True
start_time = pygame.time.get_ticks() 
while running:

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("Left key pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                #  print("Right key pressed")
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print("key released")
                playerX_change = 0
    
    

    playerX += playerX_change
    if(playerX >= 700):
        playerX -= 5

    if (playerX < 0):
        playerX += 5

    boneX += boneX_change
    if (boneX >= 700):
        boneX_change = -5
        boneY += boneY_change

    if (boneX < 0):
        boneX_change = 5
        boneY += boneY_change

    if bulletY <= 0:
        bulletY = 400
        bullet_state = 'ready'

    if bullet_state == 'fire':
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if successful_hit(boneX, boneY, bulletX, bulletY) == True:
        bulletY = 400
        bullet_state = 'ready'
        points += 5
        boneX = random.randint(50, 700)
        boneY = random.randint(50, 100)
    
    if (start_time + (PLAY_TIME * 1000) <= pygame.time.get_ticks()):
        game_end()
        running = False
        
        

    display_points(pointsX, pointsY)
    player(playerX, playerY)
    bone(boneX, boneY)
    pygame.display.update()
