import pygame
import random

# Set game window

res = (300,200)
win = pygame.display.set_mode(res)
pygame.display.set_caption("First Game")


# Set font
pygame.font.init()
font = pygame.font.SysFont('Arial', 20, True, False)
text_roll = font.render('Roll', True, (0,0,0))

# Set images
dices = [pygame.image.load('Assets/dice_1.png'), pygame.image.load('Assets/dice_2.png'), pygame.image.load('Assets/dice_3.png'), pygame.image.load('Assets/dice_4.png'), pygame.image.load('Assets/dice_5.png'), pygame.image.load('Assets/dice_6.png')]
bg = pygame.image.load('Assets/bg.jpg')

# Variables
number1 = 0
number2 = 0
click = pygame.mouse.get_pressed()


def roll_dices():
	global number1
	global number2
	number1 = random.randint(0,5)
	number2 = random.randint(0,5)
	

def redrawGameWindow():
	win.blit(bg, (0,0))
	pygame.draw.rect(win, btn_color,(150 - 50/2, 50, 50, 20))
	text = font.render('The result is ' + str((number1 + 1) + (number2 +1 )), True, (0, 0, 0))
	win.blit(text_roll, (150-50/2,50))
	win.blit(dices[number1], (100,100))
	win.blit(dices[number2], (150,100))
	win.blit(text, (80,150))
	
	pygame.display.update()


#Main Loop
run = True


while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if mouse[0] >= 150 - 50/2 and mouse[0] <= 150 - 50/2 + 50 and mouse[1] >= 50 and mouse[1] <= 100 :
				roll_dices()
				
				

	mouse = pygame.mouse.get_pos()
	
	if mouse[0] >= 150 - 50/2 and mouse[0] <= 150 - 50/2 + 50 and mouse[1] >= 50 and mouse[1] <= 100 :
		btn_color = (255,0,0)
	else:
		btn_color = (0,255,0)

	pygame.display.update()
	redrawGameWindow()

pygame.quit()
