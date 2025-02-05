#Sierra Oliver
#November 4, 2020
#Cookie Clicker - Culminating Assignment

#importing library and setting screen size
import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#setting cookie event to be able to have cookies go up per second later
#basically making this event only go off every second
COOKIE_EVENT = pygame.USEREVENT
pygame.time.set_timer(COOKIE_EVENT, 1000)

#setting colours for the background and cookie
LBROWN = (216,170,99)
BROWN = (180,142,84)
DBROWN = (87,65,30)
BLUE = (99,204,250)
GRAYBROWN = (211,193,180)
GRAYDBROWN = (146,133,124)

#setting colours for text and menu buttons (some are used for start menu)
WHITE = (255,255,255)
LGRAY = (200,200,200)
GRAY = (145,145,145)
DGRAY = (75,75,75)
BLACK = (0,0,0)
DGREEN = (50,181,5)
GREEN = (137,247,100)
LRED = (249,141,141)
RED = (253,46,46)

#setting colours for start menu
LBLUE = (200,221,255)
SKYBLUE = (156,192,250)
SMOKE = (229,229,229) #this is light gray just ran out of names

#setting variables
chip_x = 600
chip_y = 350
total_money = 0
click_amount = 1
clicker_level = 0
cookie_speed = 0
clicker_price = 50
grandma_price = 300
grandma_moneyps = 5
fox_price = 1250
fox_moneyps = 10
farm_price = 5000
farm_moneyps = 25
factory_price = 10000
factory_moneyps = 50
grandma_level = 0
fox_level = 0
farm_level = 0
factory_level = 0
can_click = bool (True)
clock = pygame.time.Clock ()

#setting cookie animation variables
lcookie_x = 300
lcookie_y = 250
rcookie_x = 1060
rcookie_y = 250
mcookie_x = 680
mcookie_y = 250
endrcookie_x = 1300
endrcookie_y = 100
endlcookie_x = 100
endlcookie_y = 100

#format pattern for the money and the upgrade prices shown on screen
money_pattern = "${:,.2f}"
upgrade_pattern = "${:,.0f}"

#declaring fonts and making specific texts 
font1 = pygame.font.SysFont ('Times New Roman',60, False, False)
l_font = pygame.font.SysFont ('Times New Roman',100, True, False)
title = l_font.render ('Cookie Clicker', True, WHITE)
title_back = l_font.render ('Cookie Clicker', True, BLACK)
start_title = font1.render ('start',True,WHITE)
quit_title = font1.render ('quit',True,WHITE)       
font = pygame.font.SysFont ('Times New Roman',60, False, False)
s_font = pygame.font.SysFont ('Calibri',20, True, False)
upgrade_text = s_font.render ('upgrades', True, WHITE)
exit_text = s_font.render ('exit', True, WHITE)
no_money = s_font.render ('not enough money', True, RED)
highest_level = s_font.render ('upgrade is the highest it goes', True, RED)

#making a starting screen function 
def intro ():
    intro = True
    can_click = True

    #taking variables from outside this function
    global lcookie_x #left cookie
    global lcookie_y 
    global rcookie_x #right cookie
    global rcookie_y
    global mcookie_x #middle cookie
    global mcookie_y
    global endrcookie_x #very right cookie
    global endrcookie_y
    global endlcookie_x #very left cookie
    global endlcookie_y

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit ()
                
            if event.type == pygame.MOUSEBUTTONUP:#resets mouse clicking
                can_click = True #user can now click again
                
        screen.fill(LBLUE)#fills screen with blue

        #setting variables only used in this function
        start_x = 0
        start_y = 50
        end_x = 50
        end_y = 0

        #draws diagonal lines on the starting screen
        for i in range (23):
            pygame.draw.line (screen,SKYBLUE, [start_x,start_y], [end_x,end_y],15)
            start_y += 100
            end_x += 100

        pygame.draw.circle (screen, LBROWN, [lcookie_x,lcookie_y],50) #draws left cookie
        pygame.draw.circle (screen, BROWN, [lcookie_x,lcookie_y],50,2) #draws left cookie outline
        
        pygame.draw.circle (screen, LBROWN, [rcookie_x, rcookie_y],50) #draws right cookie
        pygame.draw.circle (screen, BROWN, [rcookie_x, rcookie_y],50,2) #draws right cookie outline

        pygame.draw.circle (screen, LBROWN, [mcookie_x, mcookie_y],50)#draws middle cookie
        pygame.draw.circle (screen, BROWN, [mcookie_x, mcookie_y],50,2)#draws middle cookie outline

        pygame.draw.circle (screen, LBROWN, [endrcookie_x, endrcookie_y],50)#draws end right cookie
        pygame.draw.circle (screen, BROWN, [endrcookie_x, endrcookie_y],50,2)#draws end right cookie outline

        pygame.draw.circle (screen, LBROWN, [endlcookie_x, endlcookie_y],50)#draws end right cookie
        pygame.draw.circle (screen, BROWN, [endlcookie_x, endlcookie_y],50,2)#draws end right cookie outline

        #left cookie chocolate chips
        pygame.draw.circle (screen, DBROWN, [lcookie_x + 25,lcookie_y - 25],10)
        pygame.draw.circle (screen, DBROWN, [lcookie_x,lcookie_y],10)
        pygame.draw.circle (screen, DBROWN, [lcookie_x - 10,lcookie_y + 30],10)
        pygame.draw.circle (screen, DBROWN, [lcookie_x - 20,lcookie_y - 20],10)
        pygame.draw.circle (screen, DBROWN, [lcookie_x + 30,lcookie_y + 10],10)

        #right cookie chocolate chips
        pygame.draw.circle (screen, DBROWN, [rcookie_x + 15,rcookie_y - 25],10)
        pygame.draw.circle (screen, DBROWN, [rcookie_x,rcookie_y],10)
        pygame.draw.circle (screen, DBROWN, [rcookie_x - 10,rcookie_y + 30],10)
        pygame.draw.circle (screen, DBROWN, [rcookie_x - 20,rcookie_y - 20],10)
        pygame.draw.circle (screen, DBROWN, [rcookie_x +30,rcookie_y + 10],10)

        #middle cookie chocolate chips
        pygame.draw.circle (screen, DBROWN, [mcookie_x + 15,mcookie_y - 25],10)
        pygame.draw.circle (screen, DBROWN, [mcookie_x,mcookie_y],10)
        pygame.draw.circle (screen, DBROWN, [mcookie_x - 10,mcookie_y + 30],10)
        pygame.draw.circle (screen, DBROWN, [mcookie_x - 20,mcookie_y - 20],10)
        pygame.draw.circle (screen, DBROWN, [mcookie_x +30,mcookie_y + 10],10)

        #end right cookie chocolate chips
        pygame.draw.circle (screen, DBROWN, [endrcookie_x + 15,endrcookie_y - 25],10)
        pygame.draw.circle (screen, DBROWN, [endrcookie_x,endrcookie_y],10)
        pygame.draw.circle (screen, DBROWN, [endrcookie_x - 10,endrcookie_y + 30],10)
        pygame.draw.circle (screen, DBROWN, [endrcookie_x - 20,endrcookie_y - 20],10)
        pygame.draw.circle (screen, DBROWN, [endrcookie_x +30,endrcookie_y + 10],10)

        #end left cookie chocolate chips
        pygame.draw.circle (screen, DBROWN, [endlcookie_x + 15,endlcookie_y - 25],10)
        pygame.draw.circle (screen, DBROWN, [endlcookie_x,endlcookie_y],10)
        pygame.draw.circle (screen, DBROWN, [endlcookie_x - 10,endlcookie_y + 30],10)
        pygame.draw.circle (screen, DBROWN, [endlcookie_x - 20,endlcookie_y - 20],10)
        pygame.draw.circle (screen, DBROWN, [endlcookie_x +30,endlcookie_y + 10],10)

        #moves the cookies downward
        lcookie_y += 1
        rcookie_y += 2
        mcookie_y += 3
        endrcookie_y += 1
        endlcookie_y += 2

        #if the cookies get to the bottom of the screen they reset
        if lcookie_y >= 1050:
            lcookie_y = -2

        if rcookie_y >= 1050:
            rcookie_y = -2

        if mcookie_y >=1050:
            mcookie_y = -2

        if endrcookie_y >=1050:
            endrcookie_y = -2

        if endlcookie_y >=1050:
            endlcookie_y = -2

        screen.blit(title_back, [355,200])#prints title to the screen
        screen.blit(title,[360,200])#prints title to the screen
        
        #makes start button
        pygame.draw.rect (screen,SMOKE, [475,380,400,100])
        pygame.draw.rect (screen,LGRAY, [475,380,400,100],2)
        screen.blit (start_title,[615,390])
        
        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=475 and mos_x <=875 and mos_y >= 380 and mos_y <= 480:#if mouse is in box
            pygame.draw.rect(screen,BLACK,[475,380,400,100],2)#draws black outline when hovered over the box
            
            if event.type == pygame.MOUSEBUTTONDOWN and can_click:#if mouse is clicked
                pygame.time.wait (500) #stops it for 500 milliseconds
                intro = False #breaks out of loop
                
        #makes quit button
        pygame.draw.rect (screen,SMOKE,[475,525,400,100])
        pygame.draw.rect (screen,LGRAY, [475,525,400,100],2)
        screen.blit (quit_title,[615,535])

        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=475 and mos_x <=875 and mos_y >= 525 and mos_y <= 625:#if mouse is in box
            pygame.draw.rect(screen,BLACK,[475,525,400,100],2)#draws black outline when hovered over the box
            
            if event.type == pygame.MOUSEBUTTONDOWN and can_click:#if mouse is clicked
                pygame.quit() #exits game
                exit ()
                
        
        pygame.display.update ()
    
def upgrade_window (): #defining an upgrade window to be able to call it later
    upgrade = True
    
    #takes the variables from outside this function
    #these need to be here because the variables are updated inside this function
    global total_money
    global click_amount
    global clicker_level
    global clicker_price
    global grandma_price 
    global grandma_moneyps  
    global fox_price 
    global fox_moneyps 
    global farm_price 
    global farm_moneyps
    global factory_price 
    global factory_moneyps
    global cookie_speed
    global grandma_level 
    global fox_level 
    global farm_level 
    global factory_level 
    can_click = True
    

    while upgrade:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit ()

            if event.type == pygame.MOUSEBUTTONUP:#resets mouse clicking
                can_click = True #user can now click again
                
            if event.type == COOKIE_EVENT:#allows cookie speed to only go up every second
                total_money += cookie_speed #the cookies they get per second are added to the total money
           
        #the money they get per second is updated everytime they get more money
        money_text = font.render (str(money_pattern.format(total_money)), True, WHITE)

        #resets screen so that the new amount of money will show while in upgrade window
        screen.fill (BLUE)
        screen.blit(money_text,[1000,25])
                
        pygame.draw.rect(screen, GRAY,[0,500,400,300])#draws gray upgrade screen

        price_increase = random.randrange (2,6)#generates a random number between 2-5 

        #the exit box (in the upgrade menu)
        pygame.draw.rect(screen,DGRAY, [380,500,20,20])
        pygame.draw.line(screen,RED, [380,500], [400,520],2)
        pygame.draw.line(screen,RED, [400,500], [380,520] ,2)
        
        #checks if mouse is in exit box
        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=380 and mos_x <=400 and mos_y >= 500 and mos_y <= 520:#if mouse is in box
            pygame.draw.rect(screen,BLACK, [380,500,20,20],2)#draws black outline when hovered over the box
            
            if event.type == pygame.MOUSEBUTTONDOWN and can_click:#if mouse is clicked
                can_click = False #prevents holding down of mouse button
                upgrade = False

        #clicker speed upgrade
        screen.blit(first_upgrade,[10,525])#prints the upgrade line to the screen
        pygame.draw.circle(screen,GREEN,[350,530],15)#draws circle button
        pygame.draw.circle(screen,DGREEN,[350,530],15,2)#outlines the circle
        
        #checks if mouse is on the clicker speed green button
        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=335 and mos_x <=365 and mos_y >= 515 and mos_y <= 545:#if mouse is in circle
            pygame.draw.circle(screen,WHITE,[350,530],15,2)#outlines the circle when hovered over

            if event.type == pygame.MOUSEBUTTONDOWN : #if mouse button is held down below happens
                                      
                if clicker_level == 30:#if they upgrade to level 10 they can't upgrade anymore
                    screen.blit(highest_level, [10,550]) #prints that they have reached the highest level
                                             
                elif total_money >= clicker_price: #if the user has enough money they can buy the upgrade
                    total_money -= clicker_price #the user pays for the upgrade with their money
                    clicker_level += 1 #the upgrade level goes up
                    click_amount += 0.2 
                    clicker_price += clicker_price/4
                    upgrade = False
                
                else: #if none of the above is true this happens
                    screen.blit(no_money, [10,550])#prints that they have no money

        #grandma upgrade
        screen.blit(grandma_upgrade, [10,575]) #prints grandma upgrade line to screen
        pygame.draw.circle(screen,GREEN,[350,580],15)#draws circle button
        pygame.draw.circle(screen,DGREEN,[350,580],15,2)#outlines the circle

        #checks if mouse is on the grandma green button
        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=335 and mos_x <=365 and mos_y >= 565 and mos_y <= 595:#if mouse is in circle
            pygame.draw.circle(screen,WHITE,[350,580],15,2)#outlines the circle when hovered over 
                
            if event.type == pygame.MOUSEBUTTONDOWN : #if mouse button is held down below happens

                if grandma_level == 50 :
                    screen.blit(highest_level, [10,600]) #prints that they have reached the highest level
                
                elif total_money >= grandma_price: #if user has enough money
                    total_money -= grandma_price 
                    cookie_speed += grandma_moneyps 
                    grandma_price += grandma_price /price_increase
                    grandma_level += 1
                    upgrade = False

                else: #if none of the above is true this happens
                    screen.blit (no_money, [10,600])#prints that they have no money

        #fox upgrade
        screen.blit (fox_upgrade,[10,625]) #prints fox upgrade line to the screen
        pygame.draw.circle(screen,GREEN,[350,625],15)#draws circle button
        pygame.draw.circle(screen,DGREEN,[350,625],15,2)#outlines the circle

        #checks if mouse is on the fox green button
        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=335 and mos_x <=365 and mos_y >= 610 and mos_y <= 640:#if mouse is in circle
            pygame.draw.circle(screen,WHITE,[350,625],15,2)#outlines the circle when hovered over 
                
            if event.type == pygame.MOUSEBUTTONDOWN : #if mouse button is held down below happens

                if fox_level == 50:
                    screen.blit(highest_level, [10,645]) #prints that they have reached the highest level
                
                elif total_money >= fox_price : #if user has enough money
                    total_money -= fox_price
                    cookie_speed += fox_moneyps
                    fox_price += fox_price/price_increase
                    fox_level += 1
                    upgrade = False

                else: #if none of the above is true this happens
                    screen.blit (no_money, [10,645])#prints that they have no money
            
        #farm upgrade
        screen.blit (farm_upgrade,[10,670]) #prints fox upgrade line to the screen
        pygame.draw.circle(screen,GREEN,[350,670],15)#draws circle button
        pygame.draw.circle(screen,DGREEN,[350,670],15,2)#outlines the circle

        #checks if mouse is on the farm green button
        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=335 and mos_x <=365 and mos_y >= 655 and mos_y <= 685:#if mouse is in circle
            pygame.draw.circle(screen,WHITE,[350,670],15,2)#outlines the circle when hovered over 
                
            if event.type == pygame.MOUSEBUTTONDOWN : #if mouse button is held down below happens

                if farm_level == 50:
                    screen.blit(highest_level, [10,690]) #prints that they have reached the highest level
                
                elif total_money >= farm_price : #if user has enough money
                    total_money -= farm_price
                    cookie_speed += farm_moneyps
                    farm_price += farm_price/price_increase
                    farm_level += 1
                    upgrade = False

                else: #if none of the above is true this happens
                    screen.blit (no_money, [10,690])#prints that they have no money

        #factory upgrade
        screen.blit (factory_upgrade,[10,715]) #prints fox upgrade line to the screen
        pygame.draw.circle(screen,GREEN,[350,715],15)#draws circle button
        pygame.draw.circle(screen,DGREEN,[350,715],15,2)#outlines the circle
        
        #checks if mouse is on the factory green button
        mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
        if mos_x >=335 and mos_x <=365 and mos_y >= 700 and mos_y <= 730:#if mouse is in circle
            pygame.draw.circle(screen,WHITE,[350,715],15,2)#outlines the circle when hovered over 
                
            if event.type == pygame.MOUSEBUTTONDOWN : #if mouse button is held down or clicked below happens

                if factory_level == 50:
                    screen.blit(highest_level, [10,735]) #prints that they have reached the highest level
                
                elif total_money >= factory_price : #if user has enough money
                    total_money -= factory_price
                    cookie_speed += factory_moneyps
                    factory_price += factory_price/price_increase
                    factory_level += 1
                    upgrade = False

                else: #if none of the above is true this happens
                    screen.blit (no_money, [10,735])#prints that they have no money
                    
        clock.tick (60)            
        pygame.display.update ()
    
#makes a smaller version of the cookie
def small_cookie():
    
    #draws main cookie circles
     pygame.draw.circle (screen, LBROWN, [650,400] , 200)
     pygame.draw.circle (screen, WHITE, [650,400] , 200,5)
     
     #draws outside chocolate chips
     pygame.draw.circle (screen, DBROWN, [750, 275] , 25)
     pygame.draw.circle (screen, DBROWN, [550, 275] , 25)
     pygame.draw.circle (screen, DBROWN, [500, 450] , 25)
     pygame.draw.circle (screen, DBROWN, [625, 280] , 25)
     pygame.draw.circle (screen, DBROWN, [650, 550] , 25)
     pygame.draw.circle (screen, DBROWN, [800, 450] , 25)
     
     #draws middle chocolate chips
     pygame.draw.circle (screen, DBROWN, [600, 450] , 25)
     pygame.draw.circle (screen, DBROWN, [700, 450] , 25)
     pygame.draw.circle (screen, DBROWN, [600, 350] , 25)
     pygame.draw.circle (screen, DBROWN, [700, 350] , 25)

intro() #calls the intro screen

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == COOKIE_EVENT:
            total_money += cookie_speed #the cookies they get per second are added to the total money
            
    #setting specific texts
    #this needs to be here because the fonts need to be updated as they include a variables in them (price needs to be updated)
    first_upgrade = s_font.render ('clicker speed | level - ' + str(clicker_level) + '    ' + str(upgrade_pattern.format(clicker_price)), True, WHITE)
    grandma_upgrade = s_font.render ('grandma | mps ' + str(grandma_moneyps) + '   ' + str(upgrade_pattern.format(grandma_price)),True,WHITE)
    fox_upgrade = s_font.render ('fox | mps ' + str(fox_moneyps) + '   ' + str(upgrade_pattern.format(fox_price)),True,WHITE)
    farm_upgrade = s_font.render ('farm | mps ' + str(farm_moneyps) + '   ' + str(upgrade_pattern.format(farm_price)), True, WHITE)
    factory_upgrade = s_font.render ('factory | mps ' + str(factory_moneyps) + '   ' + str(upgrade_pattern.format(factory_price)), True, WHITE)
    
    screen.fill (BLUE) #fills screen blue
    pygame.draw.circle (screen, LBROWN, [650,400] , 250) #draws cookie
    pygame.draw.circle (screen, BROWN, [650,400] , 250,5)#draws cookie outline
    
    #middle top chocolate chips
    for i in range (2):
        pygame.draw.circle (screen, DBROWN, [chip_x, chip_y] , 25)
        chip_x += 100
    chip_x = 600

    #middle bottom chocolate chips
    for i in range (2):
        chip_y = 450
        pygame.draw.circle (screen, DBROWN, [chip_x, chip_y] , 25)
        chip_x += 100
    chip_x = 600
    chip_y = 350

    #outside chocolate chips 
    pygame.draw.circle (screen, DBROWN, [750, 250] , 25)
    pygame.draw.circle (screen, DBROWN, [500, 250] , 25)
    pygame.draw.circle (screen, DBROWN, [450, 450] , 25)
    pygame.draw.circle (screen, DBROWN, [625, 200] , 25)
    pygame.draw.circle (screen, DBROWN, [650, 575] , 25)
    pygame.draw.circle (screen, DBROWN, [870, 450] , 25)

    #the exit button
    pygame.draw.rect (screen, LRED,[10,10,40,40])
    pygame.draw.rect (screen, RED,[10,10,40,40],2)
    screen.blit (exit_text, [15,22])

    #sees if mouse is in exit button
    mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
    if mos_x >=10 and mos_x <=50 and mos_y >= 10 and mos_y <= 50:#if mouse is in rectangle
        pygame.draw.rect (screen, WHITE,[10,10,40,40],2)#draws upgrade outline
    
        if event.type == pygame.MOUSEBUTTONDOWN :#if mouse is clicked
            can_click = False #prevents holding down of mouse button
            pygame.quit()#quits the game
            exit()
            
    #draws upgrade button
    pygame.draw.circle (screen, LGRAY,[60,700],50)
    pygame.draw.circle (screen, GRAY,[60,700],50,5)
    screen.blit(upgrade_text, [22,695])
    
    #prints money to the screen
    money_text = font.render (str(money_pattern.format(total_money)), True, WHITE)
    screen.blit(money_text,[1000,25])
    
    #sees if mouse is in upgrade box
    mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
    if mos_x >=10 and mos_x <=110 and mos_y >= 650 and mos_y <= 750:#if mouse is in circle
        pygame.draw.circle (screen, WHITE,[60,700],50,5)#draws upgrade outline
    
        if event.type == pygame.MOUSEBUTTONDOWN :#if mouse is clicked
            can_click = False #prevents holding down of mouse button
            upgrade_window () #calls the function

    #sees if mouse is over cookie
    mos_x, mos_y = pygame.mouse.get_pos ()#gets mouse position
    if mos_x >=400 and mos_x <=900 and mos_y >= 150 and mos_y <= 650:#if mouse is in the circle
        pygame.draw.circle (screen, WHITE, [650,400],250,6)#draws cookie outline
        
        if event.type == pygame.MOUSEBUTTONDOWN and can_click:#if mouse is clicked
            can_click = False #prevents holding down of mouse button
            total_money += click_amount #adds money when clicked

        if event.type == pygame.MOUSEBUTTONDOWN:#essentially while the mouse button is being held down the cookie gets smaller
            
            #resets the screen so the only the small cookie will show (the original sized cookie will not show)
            screen.fill (BLUE)
            pygame.draw.circle (screen, LGRAY,[60,700],50)
            pygame.draw.circle (screen, GRAY,[60,700],50,5)
            pygame.draw.rect (screen, LRED,[10,10,40,40])
            pygame.draw.rect (screen, RED,[10,10,40,40],2)
            screen.blit (exit_text, [15,22])
            screen.blit(upgrade_text, [22,695])
            screen.blit(money_text,[1000,25])
            
            small_cookie () #calls this function
            
    if event.type == pygame.MOUSEBUTTONUP:#resets mouse clicking
        can_click = True #user can now click again
        
    clock.tick (60)      
    pygame.display.flip ()
pygame.quit()
