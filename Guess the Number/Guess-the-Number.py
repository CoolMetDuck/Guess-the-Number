import pygame
import sys
import getpass
import random
import socket
import time



pygame.init()

user = getpass.getuser()
computer = socket.gethostname()
print(computer)
print(user)
randNumber = random.randint(0,100)


number = 0
num2 = number

num3 = 0

timesRegen1X = 15

failNum = 0

failTextNum = 0

red = (196, 20, 20)

green = (83,140,12)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Number guessing game by CoolMetDuck")

regenum2 = 0

wonNum = 0
##################Images ##########################################################################################################
image = pygame.image.load("C:\\Users\\saima\\OneDrive\\Desktop\\Guess the Number\\assets\\slimeLeft.svg")
pygame.display.set_icon(image)

arrowLeftIMG = pygame.image.load("C:\\Users\saima\\OneDrive\Desktop\\Guess the Number\\assets\\triangle.svg")
arrowLeftIMG = pygame.transform.scale(arrowLeftIMG, (30,30))
arrowLeftIMG = pygame.transform.rotate(arrowLeftIMG, 315)

arrowRightIMG = pygame.image.load("C:\\Users\saima\\OneDrive\Desktop\\Guess the Number\\assets\\triangle.svg")
arrowRightIMG = pygame.transform.scale(arrowRightIMG, (30,30))
arrowRightIMG = pygame.transform.rotate(arrowRightIMG, 135)
###################################################################################################################################



###blits##
##### fonts #############################################################
scoreText = pygame.font.Font(None, 70)
scoreText1 = scoreText.render("Guess the number!", True, (0,0,0))

subText = pygame.font.Font(None,40)
subText1 = subText.render("(Numbers between 0 - 100)", True, (0,0,0))

textNum = pygame.font.Font(None,70)

TooLow = pygame.font.Font(None,70)
TooLow1 = TooLow.render(f"Too Low! ({num2})", True, red)

TooHigh = pygame.font.Font(None, 70)
TooHigh1 = TooHigh.render(f"Too High! ({num2})", True, red)

Equal = pygame.font.Font(None, 70)
Equal1 = Equal.render(f"Correct! ({num2})", True, green)


getUser = pygame.font.Font(None, 30)
getUser1 = getUser.render(f"User: {user}", True, (0,0,0))

regenNumText = pygame.font.Font(None, 27)
regenNumText1 = regenNumText.render("Regenerate number", True, (0,0,0))

CheckNumText = pygame.font.Font(None, 35)
CheckNumText1 = CheckNumText.render("Check Number", True, (255,255,255))

NotCheckedTXT = pygame.font.Font(None, 70)
NotCheckedTXT1 = NotCheckedTXT.render("Not Checked", True, (0,0,0))

CheckedNumTXT = pygame.font.Font(None, 30)
CheckedNumTXT1 = CheckedNumTXT.render(f"Number of times checked: {num3}/10", True, (0,0,0))
CheckedNumTXT2 = CheckedNumTXT.render(f"Number of times checked: {num3}/10", True, red)
CheckedNumTXT3 = CheckedNumTXT.render(f"Number of times checked: {num3}/10", True, (0,0,0))

exitTXT = pygame.font.Font(None, 60)
exitTXT1 = exitTXT.render("Exit", True, (0,0,0))


timesRegen = pygame.font.Font(None, 30)
timesRegen1 = timesRegen.render(f"Number of times regenerated: {regenum2}", True, (0,0,0))
timesRegen2 = timesRegen.render("Number of times regenerated: 9999+", True, (0,0,0))

failNumText = pygame.font.Font(None, 30)
failNumText1 = failNumText.render(f"Number of times failed: {failTextNum}", True, (0,0,0))

timesWonTXT = pygame.font.Font(None, 30)
timesWonTXT1 = timesWonTXT.render(f"Number of times won: {wonNum}", True, (0,0,0))

########################################################################

########rects or objects##############


ArrowLeftButton = pygame.Rect(200,400,75,75)
ArrowLeftButtonOutline = pygame.Rect(200,400,75,75)

ArrowRightButton = pygame.Rect(400,400,75,75)
ArrowRightButtonOutline = pygame.Rect(400,400,75,75)

RegenNumButton = pygame.Rect(500, 300, 200, 75)
RegenNumButtonOutline = pygame.Rect(500,300,200,75)

CheckButton = pygame.Rect(500,400,200,75)
CheckButtonOutline = pygame.Rect(500,400,200,75)

exitButton = pygame.Rect(640,500, 150, 75)
exitButtonOutline = pygame.Rect(640,500, 150, 75)




#######################################################################

####outside blits###################

screen.blit(TooHigh1,(350,400))

screen.blit(TooLow1,(350,400))

screen.blit(Equal1,(350,400))
###################################

####variables#############
TooEXE = 0

TooEXEX = 250

TooEXEY = 500

MouseCursor = 0

TooNum = 0

TooRegenNum = 0



#########################


while True:
    screen.fill("grey")

    ###################Dynamic texts#########################################
    textNum1 = textNum.render(f"{number}", True, (0,0,0))

    TooHigh1 = TooHigh.render(f"Too High! ({num2})", True, red)
    TooLow1 = TooLow.render(f"Too Low! ({num2})", True, red)
    Equal1 = Equal.render(f"Correct! ({num2}) ", True, green)
    NotCheckedTXT1 = NotCheckedTXT.render("Not Checked", True, (0,0,0))

    CheckedNumTXT1 = CheckedNumTXT.render(f"Number of times checked: {num3}/10", True, (0,0,0))
    CheckedNumTXT2 = CheckedNumTXT.render(f"Number of times checked: {num3}/10", True, red)
    CheckedNumTXT3 = CheckedNumTXT.render(f"Number of times checked: {num3}/10", True, (0,0,0))

    
    timesRegen1 = timesRegen.render(f"Number of times regenerated: {regenum2}", True, (0,0,0))
    timesRegen2 = timesRegen.render("Number of times regenerated: 9999+", True, (0,0,0))
    ##########################################################################

    #############if statmets#################################################
    if TooEXE == 1:
        
        screen.blit(TooLow1,(TooEXEX,TooEXEY))

    elif TooEXE == 2:
        screen.blit(Equal1,(TooEXEX,TooEXEY))


    elif TooEXE == 3:
        
        screen.blit(TooHigh1,(TooEXEX,TooEXEY))
                
    elif TooEXE == 0:
        screen.blit(NotCheckedTXT1,(TooEXEX,TooEXEY))

        

    
    if MouseCursor == 0:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    elif MouseCursor == 1:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 

    if TooNum == 1:
        screen.blit(CheckedNumTXT2, (15,300))


    elif TooNum == 0:
        screen.blit(CheckedNumTXT1, (15,300))    

    elif TooNum == 2:
        screen.blit(CheckedNumTXT3,(15,300))    
           

    if TooRegenNum == 0:
        screen.blit(timesRegen1, (timesRegen1X,350))


    elif TooRegenNum == 1:
        screen.blit(timesRegen2, (timesRegen1X,350))
            

 #############################################################################   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if ArrowLeftButtonOutline.collidepoint(event.pos):
                
                
                
                number-=1
                textNum1 = textNum.render(f"{number}", False, (0,0,0))
                if number < 0:
                    number+=1
                
                
                        


            if ArrowRightButtonOutline.collidepoint(event.pos):
                number+=1
                textNum1 = textNum.render(f"{number}", False, (0,0,0))

                if number > 100:
                    number-= 1

                

            if RegenNumButtonOutline.collidepoint(event.pos):
                randNumber = random.randint(0,100)
                num3 = 0
                TooNum = 0
                number = 0
                TooEXE = 0
                regenum2+=1
                failTextNum+=1
                if failTextNum > 9999:
                    failNumText1 = failNumText.render(f"Number of times failed: 9999+", True, (0,0,0))
                    screen.blit(failNumText1, (15, 485))

                else:
                    failNumText1 = failNumText.render(f"Number of times failed: {failTextNum}", True, (0,0,0))
                    screen.blit(failNumText1, (15, 485))

                if regenum2 > 9999:
                    TooRegenNum = 1
                    print(TooRegenNum)

                else:
                    TooRegenNum = 0    
                
                
                        
            
            if CheckButtonOutline.collidepoint(event.pos):
                num3+=1
                if num3> 10:
                    NotCheckedTXT1 = NotCheckedTXT.render("Not Checked", True, (0,0,0))
                    screen.blit(NotCheckedTXT1,(TooEXEX,TooEXEY))
                    num3 = 10
                    TooNum = 1
                    failTextNum+=1
                    failNumText1 = failNumText.render(f"Number of times failed: {failTextNum}", True, (0,0,0))
                    screen.blit(failNumText1, (15, 485))
                    randNumber = random.randint(0,100)
                    regenum2+=1
                    num3 = 0
                    TooNum = 0
                    number = 0
                    TooEXE = 0
                    if failTextNum > 9999:
                        failNumText1 = failNumText.render(f"Number of times failed: 9999+", True, (0,0,0))
                        screen.blit(failNumText1, (15, 485))

                    else:
                        failNumText1 = failNumText.render(f"Number of times failed: {failTextNum}", True, (0,0,0))
                        screen.blit(failNumText1, (15, 485))
                    
                    
                    

                if num3 == 10 and number == randNumber:
                    randNumber = random.randint(0,100)
                    TooNum = 2
                    num3 = 0
                    TooNum = 0
                    number = 0
                    TooEXE = 0
                    wonNum+=1
                    regenum2+=1
                    timesWonTXT1 = timesWonTXT.render(f"Number of times won: {wonNum}", True, (0,0,0))
                    screen.blit(timesWonTXT1, (15,550))

                    
                        
                    
                if number > randNumber:
                    TooEXE = 3
                    num2 = number

                elif number == randNumber:
                    randNumber = random.randint(0,100)
                    

                    TooEXE = 2
                    num3 = 0
                    TooNum = 0
                    number = 0
                    TooEXE = 0
                    wonNum+=1
                    regenum2+=1
                    
                    if wonNum > 9999:

                        timesWonTXT1 = timesWonTXT.render(f"Number of times won: 9999+", True, (0,0,0))
                        screen.blit(timesWonTXT1, (15,550))
                    
                    else:
                        timesWonTXT1 = timesWonTXT.render(f"Number of times won: {wonNum} ", True, (0,0,0))
                        screen.blit(timesWonTXT1, (15,550))

                 
                    
                    num2 = number
                    if num3 == 0:
                        TooEXE = 0

                    
                   
                    
                    


                else:
                    TooEXE = 1
                    num2 = number
                    if num3 == 0:
                        TooEXE = 0      


                if number == 0 and randNumber == 0:
                    screen.blit(Equal1, (TooEXEX,TooEXEY))
                    num2 = number
                    randNumber = random.randint(0,100)
                    num3 = 0
                    TooNum = 0
                    number = 0
                    TooEXE = 0
                    if wonNum > 9999:

                        timesWonTXT1 = timesWonTXT.render(f"Number of times won: 9999+", True, (0,0,0))
                        screen.blit(timesWonTXT1, (15,550))
                    
                    else:
                        timesWonTXT1 = timesWonTXT.render(f"Number of times won: {wonNum} ", True, (0,0,0))
                        screen.blit(timesWonTXT1, (15,550))

                elif number == 0 and number < randNumber:
                     screen.blit(TooLow1, (TooEXEX,TooEXEY))
                     num2 = number          

            if exitButtonOutline.collidepoint(event.pos):
                sys.exit()



        if event.type == pygame.MOUSEMOTION:
            if ArrowLeftButtonOutline.collidepoint(pygame.mouse.get_pos()) or ArrowRightButtonOutline.collidepoint(pygame.mouse.get_pos()) or RegenNumButtonOutline.collidepoint(pygame.mouse.get_pos()) or CheckButtonOutline.collidepoint(pygame.mouse.get_pos()) or exitButtonOutline.collidepoint(pygame.mouse.get_pos()):
                MouseCursor = 1

            else:
                MouseCursor = 0

        
         
                       


                

   ##########text Blits####################             
    screen.blit(scoreText1, (170, 100))

    screen.blit(subText1,(200,200))

    screen.blit(textNum1, (350,300))

    screen.blit(getUser1, (15, 575))
    
    screen.blit(failNumText1, (15, 485))
    
    screen.blit(timesWonTXT1, (15,550))
    

    

    #########################################

    

    ##############rects or objects################################
    pygame.draw.rect(screen,"black", ArrowLeftButton)
    pygame.draw.rect(screen,"white",ArrowLeftButtonOutline, 5)

    pygame.draw.rect(screen, "black", ArrowRightButton)
    pygame.draw.rect(screen, "white", ArrowRightButtonOutline,5)

    pygame.draw.rect(screen,"white",RegenNumButton)
    pygame.draw.rect(screen,"black",RegenNumButtonOutline,5)

    pygame.draw.rect(screen, "black", CheckButton)
    pygame.draw.rect(screen, "white", CheckButtonOutline, 5)

    pygame.draw.rect(screen, red, exitButton)
    pygame.draw.rect(screen, "black", exitButtonOutline, 5)

    screen.blit(regenNumText1, (510,330))
    
    screen.blit(CheckNumText1,(515,426))

    screen.blit(exitTXT1, (670, 520))
    ##################################################################

    #################Image Blits#####################################
    screen.blit(arrowLeftIMG,(220,415))

    screen.blit(arrowRightIMG,(410,415))

    ################################################################


    
    pygame.display.update()        