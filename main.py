import pygame
from sys import exit
from player2 import Player as Player

from boss import Boss as Boss
from boss import Attack1 as Attack1

pygame.init()
## Set A Clock ##
clock = pygame.time.Clock()

## Screen Display Size And Caption Set ##
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("untitled fighting game")

## Icon Of Window Set ##
icon_image = pygame.image.load("images/knifethrow8.png")
pygame.display.set_icon(icon_image)

## Background Set ##
background = pygame.image.load("images/bg.png")
ground = pygame.image.load("images/1333.jpg")

## Player Set ##
player = pygame.sprite.GroupSingle() ## Adds The Player Class To The player Sprite Variable  ##
player.add(Player())

## Boss Set ##
boss = pygame.sprite.GroupSingle() ## Adds The Boss Class To The Boss Sprite Variable ##
boss.add(Boss())

## FUNCTION TO DRAW THE HP BAR ##
def draw_hp_bar(screen, x, y, current_hp, max_hp):
    hp_percent = current_hp / max_hp
    pygame.draw.rect(screen, (255,255,255), (x, y, 375, 20)) ## Draws a White Bar Sized Of 375 pixels Wide and 20 Pixels Tall ##
   
    ## Low HP? Draws Red, Mid HP? Draws Yellow, High HP? Draws Green ##
    if hp_percent <= 0.25:
        color = (255,0,0) ## red ##
    elif hp_percent <= 0.55:
        color = (255,255,0) ## yellow ##
    else:
        color = (0,255,0) ## green ##
        
    pygame.draw.rect(screen, color, (x, y, hp_percent*250, 20)) ## Draw the health bar with the varying colors ##


## STORE DIFFERENT SOUNDS IN DIFFERENT VARIABLES, AND ADJUST IT'S VOLUMES ##
enemylow_sound = pygame.mixer.Sound("audio/enemylow.wav")
enemylow_sound.set_volume(0.1)
playerwin_sound = pygame.mixer.Sound("audio/win.wav")
playerwin_sound.set_volume(0.1)
playerline1_sound = pygame.mixer.Sound("audio/wry.wav")
playerline1_sound.set_volume(0.1)



## DECLARE 3 STATES ##
lobby = True
running = False
over = False




## THE START SCREEN ##
while lobby:
    ## ABILITY TO QUIT GAME ##
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        exit()
    
    ## FILL BACKGROUND WITH WHITE ##
    screen.fill((255,255,255)) 
    ## FILL IN FONT ##
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    ## RENDER TEXT AND PLACE INSIDE VARIABLE##
    text_surface = my_font.render('Welcome to da untitled fighting game', False, (0, 0, 0))
    ## TAKE THAT TEXT VARIABLE AND PLACE IT ON THE SCREEN ##
    screen.blit(text_surface,(200,200))
    
    ## DRAW AND UPDATE THE PLAYER ON THE START SCREEN ##
    player.draw(screen)
    player.update()

    ## PLACE THE BOSS AT A PARTICULAR POSITION BEFORE STARTING OFF TO THE MAIN GAME LOOP ##
    boss.sprite.rect.x = 1000
    
    ## FRAME REFRESH ##
    clock.tick(60)
    ## SCREEN REFRESH ##
    pygame.display.flip()
    ## PROCEED TO GAME IF CLICKED ##
    if event.type == pygame.MOUSEBUTTONDOWN:
        if running == False:
            running = True 
            lobby = False
            
            
    
    


########################## GAME START ##################################
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    

    

        
    ## PLACE THE BACKGROUND ##
    screen.blit(background, (0, -50))

    ## PLACE THE GROUND ##
    screen.blit(ground, (0, 480))

    ## PLACE THE HP BAR OF PlAYER AND BOS ##
    draw_hp_bar(screen, 20, 5, player.sprite.hp, player.sprite.max_hp)
    draw_hp_bar(screen, 600, 5, boss.sprite.hp, boss.sprite.max_hp)



            ## BOSS SHOOT DAMAGE AND KNOCKBACK ##
    for attack in boss.sprite.attack1_group.sprites():
        if pygame.sprite.collide_rect(player.sprite, attack):
            player.sprite.rect.x -= 5
            player.sprite.hp -= 60
            attack.kill()
            
            ## BOSS SECONDARY SHOOT DAMAGE AND KNOCKBACK ##
    for attack in boss.sprite.attack2_group.sprites(): 
        if pygame.sprite.collide_rect(player.sprite, attack):
            player.sprite.rect.x -= 10
            player.sprite.hp -= 100
            attack.kill()


            ## BOSS BARRAGE DAMAGE AND KNOCKBACK ##
    for attack in boss.sprite.barrage.sprites():
        if pygame.sprite.collide_rect(player.sprite, attack):
            player.sprite.rect.x-=5
            player.sprite.hp -= 30


             ## PLAYER SHOOT DAMAGE AND KNOCKBACK ##
    for attack2 in player.sprite.attack1.sprites(): 
        if pygame.sprite.collide_rect(boss.sprite, attack2):
            boss.sprite.rect.x += 40
            boss.sprite.hp -= 100
            attack2.kill()

             ## PLAYER BARRAGE DAMAGE AND KNOCKBACK ##
    for attack2 in player.sprite.barrage.sprites():
        if pygame.sprite.collide_rect(boss.sprite, attack2):
            boss.sprite.rect.x+=10
            boss.sprite.hp -= 100


                ## PLAYER TIME STOP KNIVES DAMAGE AND KNOCKBACK ##
    for attack2 in player.sprite.knives.sprites():
        if pygame.sprite.collide_rect(boss.sprite, attack2):
            boss.sprite.rect.x+=10
            boss.sprite.hp -= 140



        ## READ BULLET SPRITE POSITIONS FROM THE PLAYER AND STORE IT IN bullet_pos ##
    bullet_pos = [(bullet.rect.x, bullet.rect.y) for bullet in player.sprite.attack1.sprites()]


        ## PREVENT PLAYER FROM GOING OUT OF SCREEN ##
    if player.sprite.rect.x > 1120:
        player.sprite.rect.x = 1120
    if player.sprite.rect.x < 10:
        player.sprite.rect.x = 10

        ## PREVENT BOSS FROM GOING OUT OF SCREEN ##
    if boss.sprite.rect.x > 1120:
        boss.sprite.rect.x = 1120
    if boss.sprite.rect.x < 10:
        boss.sprite.rect.x = 10


        
    ## PLAY WINNING DIALOGUE OF PLAYER ##
    if boss.sprite.hp <= 0:
        playerwin_sound.play()

    ## MOVE FORWARDS TO THE GAME OVER SCREEN WHEN EITHER BOSS OR PLAYER REACHES 0 HP ##
    if player.sprite.hp <= 0 or boss.sprite.hp <= 0:
        running = False
        over = True
    



    ## TELL THE BOSS CLASS THAT PLAYER HAS STOPPED TIME, AND THE SCREEN WILL FILL WITH YELLOW ##
    if player.sprite.timestop:
        boss.sprite.time_stopped = True
        transparent_yellow = (255, 255, 102, 150)
        pygame.draw.rect(screen, transparent_yellow, (0, 0, 1200, 600))
    

    ## TELL THE BOSS THAT PLAYER TIMESTOP HAS NOW ENDED, SCREEN FILL YELLOW WILL AUTOMATICALLY DISAPPEAR ##
    elif not player.sprite.timestop:
        boss.sprite.time_stopped = False


    ## PLAY THE LINE OF PLAYER WHEN BOSS HEALTH REACHES TO A CERTAIN VALUE ##
    if boss.sprite.hp == 6000:
        enemylow_sound.play()

    ## PLAY ANOTHER LINE OF PLAYER WHEN BOSS HEALTH REACHES TO A CERTAIN VALUE ##
    if boss.sprite.hp == 9000:
        playerline1_sound.play()

    ## UPDATE THE PLAYER ALONG WITH ALL OF THE SPRITES INSIDE OF THE PLAYER CLASS, ALONG WITH DRAWAING THEM ON THE SCREEN ##
    player.update()  
    player.draw(screen)  
    player.sprite.attack1.update()
    player.sprite.attack1.draw(screen)
    player.sprite.barrage.update()
    player.sprite.barrage.draw(screen)
    player.sprite.knives.draw(screen)
    player.sprite.knives.update()
  


    ## UPDATE THE BOSS ALONG WITH ALL OF THE SPRITES INSIDE OF THE BOSS CLASS, ALONG WITH DRAWING THEM ON THE SCREEN ##
    boss.draw(screen)
    boss.update(player.sprite.rect.x,bullet_pos)
    boss.sprite.attack1_group.update()
    boss.sprite.attack1_group.draw(screen)
    boss.sprite.attack2_group.update()
    boss.sprite.attack2_group.draw(screen)
    boss.sprite.barrage.update()
    boss.sprite.barrage.draw(screen)

    
    ## SET THE FRAME REFRESH ##
    clock.tick(60)
    
    
    ## INITIATE SCREEN REFRESH ##
    pygame.display.flip()
    


############### GAME OVER STATE ##################
while over:
    
    ## EXIT THE GAME ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            exit()

    ## FILL THE SCREEN WITH WHITE ##   
    screen.fill((255,255,255)) 

  

    ## FONT STYLE, TYPICAL CHOICE OF STYLE? (COMIC SANS) ##
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    ## IF THE PLAYER LOST, DISPLAY "YOU LOSE" ##
    if player.sprite.hp <=0:
        text_surface = my_font.render('You Lose', False, (0, 0, 0))
    
    ## IF THE PLAYER WON, DISPLAY "YOU WIN" ##
    elif boss.sprite.hp <=0:
        text_surface = my_font.render('You Win', False, (0, 0, 0))
    


    ## PLACE THE DISPLAY OF WIN OR LOSE ##
    screen.blit(text_surface,(200,200))


    
    ## DRAW AND UPDATE PLAYER ON THE SCREEN, CUZ WHY NOT? ##
    player.draw(screen)
    player.update()
    
    ##FRAME REFRESH##
    clock.tick(60)
    ##DISPLAY REFRESH##
    pygame.display.flip()

    
    

