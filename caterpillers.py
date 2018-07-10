import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
brown = (125,64,0)

pygame.display.set_caption('Caterpillers')

icon = pygame.image.load('caterpiller_icon.png')
pygame.display.set_icon(icon)

display_width = 800
display_height = 600

block_size_x = 20
block_size_y = 20



img = pygame.image.load('caterpiller_head.png')
img_body = pygame.image.load('caterpiller_body.png')
img_apple = pygame.image.load('RedApple.png')

clock = pygame.time.Clock()

direction = "right"

small_font = pygame.font.SysFont('Ravie',20)
medium_font = pygame.font.SysFont('Ravie',30)
large_font = pygame.font.SysFont('Ravie',45)
ex_l_font = pygame.font.SysFont('Ravie',80)



def Pause():
    paused = True
    while paused:
        gameDisplay.fill(white)
        pygame.display.update()
        message_to_screen('Paused', green, -100, ex_l_font)
        message_to_screen('Press c to Continue or q to quit', brown, 100, small_font)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    paused = False
            pygame.display.update()
            clock.tick(15)


def front_page():
    gameDisplay.fill(white)
    pygame.display.update()
    message_to_screen('Welcome to Caterpillers', green, -100, large_font)
    message_to_screen('In this game the caterpiller have to eate the apples', green, -20, small_font)
    message_to_screen('You can pause any time by pressing P', green, 20, small_font)
    message_to_screen('Press c to play again or q to quit', brown, 100, small_font)
    pygame.display.update()
    intro = False
    while not intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = True
    pygame.display.update()
    clock.tick(15)
    
def caterpiller(caterpillerlist,block_size_x,block_size_y):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = pygame.transform.rotate(img, 0)
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    

    gameDisplay.blit(head, (caterpillerlist[-1][0], caterpillerlist[-1][1])) 
    
    for XnY in caterpillerlist[:-1]:
        
       gameDisplay.blit(img_body, (XnY[0],XnY[1]))
    
def text_objects(msg, color, font_size):
    text_surface = font_size.render(msg, True, color)
    return text_surface, text_surface.get_rect()

def message_to_screen(msg,color, y_position, font_size):
    text_surface, text_rect = text_objects(msg, color, font_size)
    text_rect.center = display_width/2,(display_height/2) + y_position
    gameDisplay.blit(text_surface, text_rect)
        
def gameloop():
    global direction
    gameExit = False
    gameOver = False

    score = 0

    Frames_per_second = 10

    caterpillerlist = []
    caterpillerLength = 1
    
    lead_x_change=0
    lead_y_change=0

    lead_x = display_width/2
    lead_y = display_height/2

    rand_Apple_x = round(random.randint(0,(display_width-(block_size_x)))/10.00)*10.00
    rand_Apple_y = round(random.randint(0,(display_height-(block_size_y)))/10.00)*10.00
    apple_size_x = 30
    apple_size_y = 30
                         
    

    while gameExit == False:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over", red, -50, ex_l_font)
            message_to_screen("Press c to play again or q to quit", green, 10, medium_font)
            message_to_screen("your score is "+str(score), green, 60, small_font)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        gameloop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = "left"
                    lead_x_change = -block_size_x
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = "right"
                    lead_x_change = block_size_x
                    lead_y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = "up"
                    lead_y_change = -block_size_y
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = "down"
                    lead_y_change = block_size_y
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    Pause()
        if lead_x >= (display_width-block_size_x) or lead_x <= 0 or lead_y >= (display_height-block_size_y) or lead_y <= 0:
            gameOver = True
            lead_x_change = 0
            lead_y_change = 0
        if lead_x >=rand_Apple_x and lead_x <= (rand_Apple_x+20) or (lead_x + block_size_x) > rand_Apple_x and (lead_x + block_size_x) < (rand_Apple_x+20):
            if lead_y >= rand_Apple_y and lead_y <= (rand_Apple_y+20) or (lead_y + block_size_y) > rand_Apple_y and (lead_y + block_size_y) < (rand_Apple_y+20):
                rand_Apple_x = round(random.randint(0,(display_width-(apple_size_x)))/block_size_x)*block_size_x
                rand_Apple_y = round(random.randint(0,(display_height-(apple_size_y)))/block_size_y)*block_size_y
                caterpillerLength +=1
                Frames_per_second +=0.5
                score +=1

            
          
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)
        gameDisplay.blit(img_apple, (rand_Apple_x,rand_Apple_y))
        
        
        caterpillerhead = []
        caterpillerhead.append(lead_x)
        caterpillerhead.append(lead_y)
        caterpillerlist.append(caterpillerhead)

        if len(caterpillerlist) > caterpillerLength:
            del caterpillerlist[0]

        for each_segment in caterpillerlist[:-1]:
            if each_segment == caterpillerhead:
                gameOver = True
        
        caterpiller(caterpillerlist,block_size_x,block_size_y)

        text = small_font.render("Score: "+str(score), True, brown)
        gameDisplay.blit(text, [0,0])
        
        pygame.display.update()
        clock.tick(Frames_per_second)

front_page()
gameloop()
pygame.quit()
quit()

