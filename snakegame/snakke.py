import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

red = 255,0,0
white = 255,255,255
black = 0,0,0
green=87,197,3

mouse = pygame.image.load("frog.png")
mouseWidth = mouse.get_width()
mouseHeight = mouse.get_height()

coinSound = pygame.mixer.Sound('point.wav')
'''bg_music = pygame.mixer.Sound("bg_music.wav")
bg_music.play(-1)
bg_music.set_volume(0.5)'''
def homeScreen():
    bg_img = pygame.image.load("snake.jpg")
    font = pygame.font.Font("font_2.ttf",50)
    text = font.render("Press SPACE to Start Game", True, green)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play()

        screen.blit(bg_img, (0,0))
        screen.blit(text, (50,450))
        pygame.display.update()
def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,black,[snakeList[i][0],
                                     snakeList[i][1],50,50])

def score(c):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score : {}".format(c), True, white)
    screen.blit(text, (450,10))

def gameOver():
    font = pygame.font.SysFont(None, 100)
    text_1 = font.render("Game Over", True, red)
    text_2 = font.render("Press SPACE to Play Again",True,white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    homeScreen()

        screen.blit(text_1, (200,400))
        screen.blit(text_2, (50,100))
        pygame.display.update()


def play():
    bgimage = pygame.image.load("back.jpg")
    x = 0
    y = 0
    moveX = 0
    moveY = 0

    snakeLength = 1
    snakeList = []

    mouseX = random.randint(0, width - mouseWidth)
    mouseY = random.randint(0, height - mouseHeight)

    FPS = 100
    clock = pygame.time.Clock()
    count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 4
                    moveY = 0
                elif event.key == pygame.K_LEFT:
                    moveX = -4
                    moveY = 0
                elif event.key == pygame.K_DOWN:
                    moveY = 4
                    moveX = 0
                elif event.key == pygame.K_UP:
                    moveY = -4
                    moveX = 0

        screen.blit(bgimage,(0,0))

        # screen.blit(img,(rect.x, rect.y))
        rect = pygame.draw.rect(screen,black,[x,y,50,50])
        screen.blit(mouse, (mouseX, mouseY))
        mouseRect = pygame.Rect(mouseX, mouseY, mouseWidth, mouseHeight)
        x += moveX
        y += moveY

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        snake(snakeList)

        for each in snakeList[:-1]:
            if snakeList[-1] == each:
                # print("Game Over")
                gameOver()

        if mouseRect.colliderect(rect):
            rect.width += 10
            mouseX = random.randint(0, width - mouseWidth)
            mouseY = random.randint(0, height - mouseHeight)
            snakeLength += 20
            FPS += 5
            coinSound.play()
            count += 1
        score(count)

        if x > width:
            x = -50
        elif x < -50:
            x = width
        elif y > height:
            y = -50
        elif y < -50:
            y = height

        pygame.display.update()
        clock.tick(FPS)
homeScreen()
