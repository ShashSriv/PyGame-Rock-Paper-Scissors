#Initializes Pygame
import pygame
import random
pygame.init()

#Initalizes drawing window (var = screen)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('Rock Paper Scissors Shoot!!!')

#Initializes rock/paper/scissor rectangles
rock_button = pygame.Rect(SCREEN_WIDTH/4-75, SCREEN_HEIGHT/2, 150, 50)
paper_button = pygame.Rect(SCREEN_WIDTH/2-75, SCREEN_HEIGHT/2, 150, 50)
scissor_button = pygame.Rect(SCREEN_WIDTH-SCREEN_WIDTH/4-75, SCREEN_HEIGHT/2, 150, 50)

#initalizes colors
grey = (128, 128, 128)
yellow = (253,255,0)
red = (200,0,0)
black = (0,0,0)
green = (0, 255, 0)

#intializes image
imp = pygame.image.load("RPS_home_pic.jpg")
imp = pygame.transform.scale(imp, (700,350))

#initalizes text for r/p/s rectangles
font = pygame.font.Font('freesansbold.ttf', 32)
rock_text = font.render('Rock', True, black)
paper_text = font.render('Paper', True, black)
scissor_text = font.render('Scissor', True, black)
win_text = font.render('You Win', True, green)
tie_text = font.render('Its a Tie', True, yellow)
lose_text = font.render('You Lose', True, red)
computer_text = font.render('', True, black)

ai = ["rock", "paper", "scissors"]
ai_choice = ""
player = 0
outcome = 0
win_case = 0

def win_check():
    global outcome
    global ai
    global player
    global ai_choice
    if (ai_choice== ai[0]) :
        if player == 1 :
            outcome = 3
        if player == 2 :
            outcome = 1
        if player == 3 :
            outcome = 2
    if (ai_choice == ai[1]) :
        if player == 1 :
            outcome = 2
        if player == 2 :
            outcome = 3
        if player == 3 :
            outcome = 1
    if (ai_choice == ai[2]) :
        if player == 1 :
            outcome = 1
        if player == 2 :
            outcome = 2
        if player == 3 :
            outcome = 3
    return outcome

#Keeps prgramming running until user hits exit window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #screen fill
        screen.fill((150,150,255))

        #Draw an Image
        screen.blit(imp, (SCREEN_HEIGHT/2-350, SCREEN_HEIGHT/8-75))
    
        #Draw Buttons
        pygame.draw.rect(screen, grey , rock_button)
        pygame.draw.rect(screen, yellow, paper_button)
        pygame.draw.rect(screen, red, scissor_button)

        screen.blit(rock_text, (rock_button.centerx-40, rock_button.centery-15))
        screen.blit(paper_text, (paper_button.centerx-40, paper_button.centery-15))
        screen.blit(scissor_text, (scissor_button.centerx-55, scissor_button.centery-15))

        #button that evaluates whcih button is clicked and starts a game each time the mouse is clicked on a specific choice
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if rock_button.collidepoint(mouse_pos):
                player = 1
                ai_choice = ai[random.randint(0,2)]
                computer_text = font.render(f'The computer chose {ai_choice}', True, black)
                if(win_check() == 1):
                    win_case = 1
                if(win_check() == 2):
                    win_case = 2
                if(win_check() == 3):
                    win_case = 3
            elif paper_button.collidepoint(mouse_pos):
                player = 2
                ai_choice = ai[random.randint(0,2)]
                computer_text = font.render(f'The computer chose {ai_choice}', True, black)
                if(win_check() == 1):
                    win_case = 1
                if(win_check() == 2):
                    win_case = 2
                if(win_check() == 3):
                    win_case = 3
            elif scissor_button.collidepoint(mouse_pos):
                player = 3
                ai_choice = ai[random.randint(0,2)]
                computer_text = font.render(f'The computer chose {ai_choice}', True, black)
                if(win_check() == 1):
                    win_case = 1
                if(win_check() == 2):
                    win_case = 2
                if(win_check() == 3):
                    win_case = 3
        
        #Prints Computers choice 
        screen.blit(computer_text, (SCREEN_WIDTH/2-200,550))

        #Prints Game outcome
        if win_case == 1:
            screen.blit(win_text, (SCREEN_WIDTH/2 - 75,700))
        elif win_case == 2:
            screen.blit(lose_text, (SCREEN_WIDTH/2 - 75,700))
        elif win_case == 3:
            screen.blit(tie_text, (SCREEN_WIDTH/2 - 75,700))
            

        pygame.display.flip()

        

pygame.quit()
