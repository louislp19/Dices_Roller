import pygame
import random

screen_width = 300
screen_height = 200


win = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("First Game")

pygame.font.init()

font = pygame.font.SysFont('Arial', 20, True, False)

bg = pygame.image.load('Assets/bg.jpg')

dices = [pygame.image.load('Assets/dice_1.png'), pygame.image.load('Assets/dice_2.png'), pygame.image.load('Assets/dice_3.png'), pygame.image.load('Assets/dice_4.png'), pygame.image.load('Assets/dice_5.png'), pygame.image.load('Assets/dice_6.png')]

number1 = random.randint(0,5)
number2 = random.randint(0,5)


text = font.render('The result is ' + str((number1 + 1) + (number2 +1 )), True, (0, 0, 0))
text_roll = font.render('Roll', True, (0,0,0))

click = pygame.mouse.get_pressed()

print(click)

def redrawGameWindow():
	win.blit(bg, (0,0))
	pygame.draw.rect(win, (255,0,0),(150 - 50/2, 50, 50, 20))
	win.blit(dices[number1], (100,100))
	win.blit(dices[number2], (150,100))
	win.blit(text_roll, (150-50/2,50))
	win.blit(text, (80,150))
	pygame.display.update()


#Main Loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
            
    redrawGameWindow()

pygame.quit()