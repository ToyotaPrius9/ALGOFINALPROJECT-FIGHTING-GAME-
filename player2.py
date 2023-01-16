import pygame

## Class For the Knives ##
class Knives (pygame.sprite.Sprite):
    def __init__(self, x, y,speed,timestop): ## Three arguements, player x position, player y position, and timestop status of player ##
        super().__init__()

        
        self.image = pygame.image.load("images/knives.png").convert_alpha() ## initialize image ##
        self.rect = self.image.get_rect()
        self.rect.x = x  ## Put Self's x position same as arguement "x" ##
        self.rect.y = y  ## Put Self's y position same as arguement "y" ##
        self.speed = speed ## Set Speed To Arguement Value ##
        self.timestop = timestop ## Store TimeStop Status ##

    
        
    def update(self):
        if self.timestop:
            self.rect.x += 0 ## DO NOT MOVE WHEN TIME IS STOPPED ##
        else:
            self.rect.x += self.speed ## IF TIME NOT STOPPED, MOVE ACCORDING TO SPEED ##

        if self.rect.x > 1000:
            self.kill() ## REMOVE FROM SCREEN WHEN REACHES MORE THAN 1000 (why 1000? if it werent 1000, this move could be an exploit easy win) ##


class Bullet (pygame.sprite.Sprite): ## make shooting bullet (it's not really a bullet but let's just call it that) ##
    def __init__(self, x, y,speed): ## takes x and y along with speed value as arguements ##
        super().__init__()

        
        self.image = pygame.image.load("images/shoot.png").convert_alpha()
        self.rect = self.image.get_rect() ## initialize rect value of self according to image ##
        self.rect.x = x ## set self x value according to arguement ##
        self.rect.y = y ## set self y value according to arguement ##
        self.speed = speed ## set speed value and store it here ##

    def update(self):
        
        
        self.rect.x += self.speed ## Move self X position according to speed ##
        
        if self.rect.x > 1100: ## If goes off screen, remove from screen ##
            self.kill()





class muda (pygame.sprite.Sprite): ## barrage attack sprite ##
    def __init__(self, x, y): ## takes it's x and y value as arguement, no speed this time ##
        super().__init__()

        
        

        ############## SELF ANIMATION IMAGES ############################
        muda1 = pygame.image.load("images/zawarudo1.png").convert_alpha()
        muda2 = pygame.image.load("images/zawarudo2.png").convert_alpha()
        muda3 = pygame.image.load("images/zawarudo3.png").convert_alpha()
        muda4 = pygame.image.load("images/zawarudo4.png").convert_alpha()
        muda5 = pygame.image.load("images/zawarudo5.png").convert_alpha()
        muda6 = pygame.image.load("images/zawarudo6.png").convert_alpha()
        muda7 = pygame.image.load("images/zawarudo7.png").convert_alpha()
        muda8 = pygame.image.load("images/zawarudo8.png").convert_alpha()
        muda9 = pygame.image.load("images/zawarudo9.png").convert_alpha()
        muda10 = pygame.image.load("images/zawarudo10.png").convert_alpha()
        self.muda = [muda1,muda2,muda3,muda4,muda5,muda6,muda7,muda8,muda9,muda10] ## Store Animations As A List
        self.muda_index = 0 ## Store an index value of which animation to play ##
        self.image = self.muda[self.muda_index] ## Update It's Image To Whatever The Index Says So ##
        self.rect = self.image.get_rect() ## Initiate Rect Values Based Off Image ##
        self.rect.x = x ## Take Arguement X As Selve's X value
        self.rect.y = y ## Take Arguement Y As Selve's Y Value
        self.playerpos = x ## Store Player Position ##

    def update(self):
        ############## CHNAGE THROUGH IMAGES (ANIMATES SELF) ############
        self.muda_index += 0.4 ## Cycle Through All Images 0.4 Times For Each Frame (WHICH IS 60 AT THE GAMELOOP) ##
        if self.muda_index >= len(self.muda): self.muda_index = 0 ## If the index goes out of total list length, restart from 0 ##
        self.image = self.muda[int(self.muda_index)] ## Put The Animation Into Play And Update self's image based on index values from the list ##
        
        
        self.rect.x += 4 ## Move 4 Pixels Front Continously ##
        
        if self.rect.x - self.playerpos > 100: ## If Went 100 Pixels Too Far From The Poisiton Of The Player's Attack Position, Remove From Screen##
            self.kill()


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

        #### IDLE STATE ANIMATION #### [ Append Technique ]
        self.player_idle = []
        self.player_idle.append(pygame.image.load("images/idle1.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle2.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle3.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle4.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle5.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle6.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle5.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle4.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle3.png").convert_alpha())
        self.player_idle.append(pygame.image.load("images/idle2.png").convert_alpha())
        self.player_idle_index = 0
        self.image = self.player_idle[self.player_idle_index]

        #### WALK STATE ANIMATION ####
        self.player_walk = []
        self.player_walk.append(pygame.image.load("images/walk1.png").convert_alpha())       
        self.player_walk.append(pygame.image.load("images/walk2.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk3.png").convert_alpha())
        self.player_walk.append(pygame.image.load("images/walk4.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk5.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk6.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk7.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk8.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk9.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk10.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk11.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk12.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk13.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk14.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk15.png").convert_alpha())    
        self.player_walk.append(pygame.image.load("images/walk16.png").convert_alpha())        
        self.player_index = 0
        self.image = self.player_walk[self.player_index]

        #### BACKWARDS STATE ANIMATION ####
        player_back1 = pygame.image.load("images/back1.png").convert_alpha()
        player_back2 = pygame.image.load("images/back2.png").convert_alpha()
        player_back3 = pygame.image.load("images/back3.png").convert_alpha()
        player_back4 = pygame.image.load("images/back4.png").convert_alpha()
        player_back5 = pygame.image.load("images/back5.png").convert_alpha()
        player_back6 = pygame.image.load("images/back6.png").convert_alpha()
        player_back7 = pygame.image.load("images/back7.png").convert_alpha()
        player_back8 = pygame.image.load("images/back8.png").convert_alpha()
        player_back9 = pygame.image.load("images/back9.png").convert_alpha()
        player_back10 = pygame.image.load("images/back10.png").convert_alpha()
        player_back11 = pygame.image.load("images/back11.png").convert_alpha()
        player_back12 = pygame.image.load("images/back12.png").convert_alpha()
        player_back13 = pygame.image.load("images/back13.png").convert_alpha()
        player_back14 = pygame.image.load("images/back14.png").convert_alpha()
        player_back15 = pygame.image.load("images/back15.png").convert_alpha()
        player_back16 = pygame.image.load("images/back16.png").convert_alpha()
        
        self.player_back = [player_back1,player_back2,player_back3,player_back4,player_back5,player_back6,player_back7,player_back8,player_back9,player_back10,player_back11,player_back12,player_back13,player_back14,player_back15,player_back16]
        self.player_back_index = 0
        self.image = self.player_back[self.player_back_index]

        #### JUMP STATE ANIMATION ####
        self.player_jump = []
        self.player_jump.append(pygame.image.load("images/jump1.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump2.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump3.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump4.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump5.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump6.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump7.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump8.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump9.png").convert_alpha())
        self.player_jump.append(pygame.image.load("images/jump10.png").convert_alpha())
        self.player_jump_index = 0
        self.image = self.player_jump[self.player_jump_index]
        

        #### ATTACK STATE ANIMATION & INITIALIZATIOIN####
        self.player_attack = []
        self.player_attack.append(pygame.image.load("images/attack1.png").convert_alpha())
        self.player_attack.append(pygame.image.load("images/attack2.png").convert_alpha())
        self.player_attack.append(pygame.image.load("images/attack3.png").convert_alpha())
        self.player_attack.append(pygame.image.load("images/attack4.png").convert_alpha())
        self.player_attack.append(pygame.image.load("images/attack5.png").convert_alpha())
        self.player_attack.append(pygame.image.load("images/attack6.png").convert_alpha())
        self.player_attack.append(pygame.image.load("images/attack7.png").convert_alpha())
        self.player_attack.append(pygame.image.load("images/attack8.png").convert_alpha())
        self.player_attack_index = 0
        self.image = self.player_attack[self.player_attack_index]
        self.attack1 = pygame.sprite.Group()
        self.bullet_cooldown = 10
        self.bullet_fired = False




        #### DASH STATE ANIMATION ####
        
        self.player_dashforward = []
        self.player_dashforward.append(pygame.image.load("images/dashforward1.png").convert_alpha())
        self.player_dashforward.append(pygame.image.load("images/dashforward2.png").convert_alpha())
        self.player_dashforward.append(pygame.image.load("images/dashforward3.png").convert_alpha())
        self.player_dashforward.append(pygame.image.load("images/dashforward4.png").convert_alpha())
        self.player_dashforward.append(pygame.image.load("images/dashforward5.png").convert_alpha())
        self.player_dashforward.append(pygame.image.load("images/idle1.png").convert_alpha())
        self.player_dashforward_index = 0
        self.image = self.player_dashforward[self.player_dashforward_index]



        #### BACKDASH STATE ANIMATION ####

        self.player_dashback = []
        self.player_dashback.append(pygame.image.load("images/dashback1.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback2.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback3.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback4.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback5.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback6.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback7.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback8.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/dashback9.png").convert_alpha())
        self.player_dashback.append(pygame.image.load("images/idle1.png").convert_alpha())
        self.player_dashback_index = 0
        self.image = self.player_dashback[self.player_dashback_index]

        self.dash_sound = pygame.mixer.Sound("audio/dash.wav")
        self.dash_sound.set_volume(0.1)


        #### BARRAGE STATE ANIMATION AND INITIALIALIZATION####

        self.player_playerpose = []
        self.player_playerpose.append(pygame.image.load("images/playerpose1.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose2.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose3.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose4.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose5.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose6.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose7.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose8.png").convert_alpha())
        self.player_playerpose.append(pygame.image.load("images/playerpose9.png").convert_alpha())
        self.player_playerpose_index = 0
        self.barrage_sound = pygame.mixer.Sound("audio/mudamuda.wav")
        self.barrage_sound.set_volume(0.03)
        






        self.barrage = pygame.sprite.Group()
        self.barrage_cooldown = 0
        self.barrage_fired = False



        ##### STOP TIME STATE ANIMATION AND INITIALIZATION ########

        self.tokiotomare = []
        self.tokiotomare.append(pygame.image.load("images/tokiotomare1.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare2.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare3.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare4.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare5.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare6.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare7.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare8.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare9.png").convert_alpha())
        self.tokiotomare.append(pygame.image.load("images/tokiotomare10.png").convert_alpha())
        self.tokiotomare_index = 0
        

        
        
        self.timestop = False
        self.timestop_start_time = pygame.time.get_ticks()
        self.timestop_sound = pygame.mixer.Sound("audio/timestop.wav")
        self.timestop_sound.set_volume(0.1)
        self.timestop_sfx = pygame.mixer.Sound("audio/timestopsfx.wav")
        self.timestop_sfx.set_volume(0.3)
        self.timemove_sound = pygame.mixer.Sound("audio/timemove.wav")
        self.timemove_sound.set_volume(0.6)






        ########## ABILITY KNIFE THROW ANIMATION (ONLY WHEN TIME STOP) AND INITIALIZATION #################################

        self.knifethrow = []
        self.knifethrow.append(pygame.image.load("images/knifethrow1.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow2.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow3.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow4.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow5.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow6.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow7.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow8.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow9.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow10.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow12.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow13.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow14.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow15.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow16.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow17.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow18.png").convert_alpha())
        self.knifethrow.append(pygame.image.load("images/knifethrow19.png").convert_alpha())
        self.knifethrow_index = 0

        self.knives = pygame.sprite.Group() ## Create variable containing Knives Sprite
        self.checkmate_sound = pygame.mixer.Sound("audio/checkmate.wav") ## Voiceline When Threw Knife ##
        self.checkmate_sound.set_volume(0.1) ## Too Loud?, Lowering Da Volume ##



        #### SOME MORE INITIALIZATIONS ####
        self.rect = self.image.get_rect() ## Sets Self's rect value based off current image of self ##
        
        
        
        self.movement_speed = 0 ## Variable For Movement Speed ##
        self.dash_state = False ## Variable For Dash State Status (boolean) ##
        self.dashbackstate = False ## Variable For Back Dash State Status (boolean) ##
        self.rect.x = 100 ## Set Spawning X Point of Player ##
        self.hp = 15000 ## Set Starting Off HP of the Player (I Gave It A Higher Value Than Max HP.. The Player Will Need It..) ##
        self.max_hp = 10000 ## Set Max HP of Player ##
        self.gravity = 0 ## Set Variable Of Gravity ##
        self.lowhp_sound = pygame.mixer.Sound("audio/lowhp.wav") ## Voiceline For Low Health ##
        self.lowhp_sound.set_volume(0.1) ## Yeah It's Loud.. Gotta Lower The Volume ##
        
        

        


        
     


    
    ############################ INPUTS FOR THE PLAYER ############################3
    def player_input(self):
          

        ################### JUMP #########################

        if self.rect.bottom < 480: ## If Player Is Above Surface, Set Jump Status To True ##
                self.is_jumping = True 
        else:
            self.is_jumping = False  ## If Not, Jump Status is False ##
        keys = pygame.key.get_pressed() ## Just To Make Things Easer, store all the pressed keys in a variable "keys" ##

        if keys [pygame.K_w] and self.rect.bottom >= 480: ## If Player On Surface, Give Them The Ability To Jump If W  key is pressed ##
            self.gravity = -30 ## JUMP!, player gravity will be minused by 30 and the player will be on the air. More mechanics Explained In Apply Gravity Function ##
            

        

        


        #################### MOVE RIGHT #########################

        if keys[pygame.K_d] and not self.is_jumping: ## If Input is D and player isn't jumping, let em walk front, Dio Can't Walk On Air ##
            self.movement_speed += 0.8  ## increase speed gradually, it will increase the longer player holds down d key. ##
            self.rect.x += self.movement_speed  ## Move player right ##
            moving_right = True ## Set The Status Of Moving Right, Useful For Fixing The Issue Of Conflicts On Pressing Both Right And left (What happened without this was, player can shoot front like sonic the hedgehod if held both right and left walk and released one of the key)
            
            

        else: 
            self.movement_speed *= 0.9  ## IF Not Moving Right, Decrease Movement Speed Gradually, but not instantly. Since its... *0.9, kinda proud of this thought ##
            moving_right = False ## Set Status Of Moving Right To False, cuz you know.. you're not moving anymore... ##


        ################ MOVE LEFT #####################################

        if keys[pygame.K_a] and not self.is_jumping: ## Same Thing Now but for moving left, by the A key ##
            self.movement_speed += 0.8  #  increase speed
            self.rect.x -= self.movement_speed  # Move  player left
            moving_left = True ## Set Status ##
            
            
        
        else: 
            self.movement_speed *= 0.9 ## Slow Down Gradually, But Not Instantly; If Key isnt pressed anymore... ##
            moving_left = False 


        ###################### FALL FASTER ##############################

        if keys [pygame.K_s]: ## If You Hold S, Gravity becomes stronger, maybe an unnecessary movement mechanic but nice to have imo ##

            self.gravity = + 25 ## Increase that gravity, did i defy the law of physics? Who knows... ##

        ##################### PREVENTION OF MOVEMENT CONFLICT (RIGHT AND LEFT) ###################

        if moving_left and moving_right == True: ## This is for an unwanted glitch to be fixed, player wont shoot front if both A and D were pressed and then one key gets released ##

            self.movement_speed = 0 ## Yeah, you aint going anywhere with 0 movement speed... ##

        ####################### DASH RIGHT ###########################
        if keys[pygame.K_RIGHT] and not self.dash_state and not self.dashback_state and not moving_left and not moving_right: ## If player isnt walking front or back, or is in the process of dashing, the player will dash front if right key pressed, this prevents the player from holding dash key and dashing uncontrollably ##
            self.dash_state = True ## Set the dash state status ##
            self.dash_sound.play() ## Play the Dash Sound, sorry for the ear bleed... ##
            self.rect.x += 100 ## Move a hundred pixels to the right ##
        
        elif not keys[pygame.K_RIGHT]:
            self.dash_state = False ## If no dash key is being pressed, set the dash status to false

        ######################## DASH LEFT ##########################

        if keys[pygame.K_LEFT] and not self.dashback_state and not moving_left and not moving_right: ## Same thing, but for left this time ##
            self.dashback_state = True ## Status Set ##
            self.rect.x -= 100 ## minus now, not plus, since we're dashing left ##
            self.dash_sound.play() ## plays the same sound as dashing right ##
        
        elif not keys[pygame.K_LEFT]:
            self.dashback_state = False



        ####################### SHOOT OUT BULLET ########################

        
        if keys[pygame.K_q]: ## if q key is pressed, and the cooldown of the bullet is equal or less than 0, and bullet_fired status is False, add the bullet sprite to the previously created variable for holding this bullet, and spawn em ##
            if not self.bullet_fired and self.bullet_cooldown <=0:
                bullet = Bullet(self.rect.x + 10, self.rect.centery, 30) ## Set the bullet position to a but infront of the player and player's Y position, speed will be 30 ##
                self.attack1.add(bullet) ## Add the bullet class to the created variable for this bullet in the innit
                self.bullet_cooldown += 10 # Bullet has a cooldown for every 0.16 seconds (10/main game loop tick(60))(will only work once every keypress, key hold does not count :) )
                
                
                self.bullet_fired = True ## Set Fired Status ##
        elif not keys[pygame.K_q]:
            self.bullet_fired = False

        if self.bullet_cooldown > 0: # If cooldown is higher than 0, minus it by 1 every tick frame
            self.bullet_cooldown -= 1 # Minus Down the CoolDown


        ########################### ABILITY BARRAGE ##########################

        if keys[pygame.K_e]: ## if key is E, and the cooldown is less or equal to 0, add the muda class to the variable decalred for it in the init ##
            if not self.barrage_fired and self.barrage_cooldown <=0:
                barrage = muda(self.rect.x , self.rect.y) ## Store the muda class along with it's arguements inside of a variable ##
                self.barrage.add(barrage) ## Put this variable inside the variable of barrage inside the init ##
                self.barrage_sound.play() ## Sound for barrage ability, gets annoying when heard too much ##
                self.barrage_cooldown += 30 ## Set the cooldown for barrage, it will be 30/60 seconds.

                self.barrage_fired = True ## Set Status For Barrage, True edition ##
            
        elif not keys[pygame.K_e]:
            self.barrage_fired = False ## Set Status For Barrage, False edition ##

        if self.barrage_cooldown > 0: ## If the cooldown is higher than 0, minus it by 1, constantly ##
            self.barrage_cooldown -= 1

        ########################### ABILITY TIMESTOP ##############################

        if self.hp<10000: ## Only happens If HP Is Below 10k ##
            if keys[pygame.K_g] and  self.tokiotomare_index == len(self.tokiotomare)-1: ## If animation reaches to a certain point and g is pressed, set timestop status ##
                self.timestop = True
                self.timestop_sfx.play() ## Play the Sound At the Start Of When Time is Stopped
                
            
            if self.knifethrow_index == len(self.knifethrow)-2 and self.timestop: ## If Animation Reaches To A Certain Point, and time has been stopped, spawn the knives ##
                    knives = Knives(self.rect.x,self.rect.y,30, self.timestop) ## sets the Knives Class along with it's arguements inside of a variable ##
                    self.knives.add(knives) ## Adds that variable to a variable inside of the init ##


            if self.timestop:
                current_time = pygame.time.get_ticks() ## Takes the current time of pygame ##
                
                if current_time - self.timestop_start_time > 10000: ## If the current time and the start time of timestop subtracted is now higher than 10k milliseconds (10 Seconds), stoptime ends, time will now move again ##
                    self.timemove_sound.play() ## Play the Sound for time moving ##
                    self.timestop = False ## Timestop is now no more True ##
                    self.timestop_start_time = pygame.time.get_ticks() ## refresehs timestops_start_time, the starting time of time stop is refreshed. RIP brain cells ##
                    
                    





        for knife in self.knives: ## REFRESHES THE TIMESTOP STATE FOR KNIVES, SINCE IT DOES NOT REFRESH EVEN WITH ALL THE PREVIOUS CODE ##
            knife.timestop = self.timestop
        
                
        





        

        

        
     

        

    ########################## FUNCTION TO APPLY GRAVITY ################
    def apply_gravity(self): 
        self.gravity += 1.4  ## Player always falls on this speed to the ground, if this speed is increased, player falls faster. if they hold S key, this value increases temporarily till the time they dont press S key anymore ##
        self.rect.y += self.gravity ## Apply the gravity to player's Y position ##
        if self.rect.bottom >= 490: ## If player is on the gorund, keep them there. If this code werent there, player would fall off the screen and right to the underworld. ##
            self.rect.bottom = 490

        
            

    def update(self): ## UPDATE ALL THE DECLARED FUNCTIONS IN THIS CLASS ##
        self.player_input()
        self.apply_gravity()
        self.animation_state()

        ## PREVENT FOR GOING OUT OF SCREEN ##
        if self.rect.x >1200:
            self.rect.x = 1200

        if self.rect.x <30:
            self.rect.x = 30

        ## PLAY LOW HEALTH VOICE ##

        if self.hp == 600:
            self.lowhp_sound.play()



        
        
        
        
        

        
        
        

    def animation_state(self):
        keys = pygame.key.get_pressed()
        if self.movement_speed > 0.5: # I couldve used the true or false state for chekcing movements but this way just works better, i see walking states based off movement speed this time #
            
            ## WALK ANIMATION ##
            if keys[pygame.K_d] and self.movement_speed > 2 and self.rect.bottom > 479 and not keys[pygame.K_a]  :
                self.player_index += 0.4
                if self.player_index >= len(self.player_walk): self.player_index = 0
                self.image = self.player_walk[int(self.player_index)]
                self.player_back_index = 0
            
            ## WALK BACK ANIMATION ##
            elif keys[pygame.K_a] and self.movement_speed > 2 and self.rect.bottom > 479 and not keys[pygame.K_d]:
                self.player_back_index += 0.4
                if self.player_back_index >= len(self.player_back): self.player_back_index = 0
                self.image = self.player_back[int(self.player_back_index)]
                self.player_index = 0

            
        
        ## IDLE ANIMATION ##
        elif self.movement_speed < 1 and self.rect.bottom > 479:
            self.player_idle_index += 0.1
            if self.player_idle_index >= len(self.player_idle): self.player_idle_index = 0
            self.image = self.player_idle[int(self.player_idle_index)]

        ## JUMP ANIMATION ##
        elif self.rect.bottom < 479:
                
                self.player_jump_index += 0.3
                if self.player_jump_index >= len(self.player_jump): self.player_jump_index = len(self.player_jump)-1
                self.image = self.player_jump[int(self.player_jump_index)]
        
        if self.rect.bottom >479:
            self.player_jump_index = 0

        ## ATTACK ANIMATION ##
        
        if keys[pygame.K_q]:
            self.player_attack_index += 0.4
            if self.player_attack_index >= len(self.player_attack): 
                self.player_attack_index = len(self.player_attack)-1 ## STAY ON THE LAST ANIMATION IF GOES OUT OF LENGTH ##
            self.image = self.player_attack[int(self.player_attack_index)]

        elif not keys[pygame.K_q]:
            self.player_attack_index = 0


        ## DASH FORWARD ANIMATION ##

        if keys[pygame.K_RIGHT] and self.movement_speed < 1:
            self.player_dashforward_index += 0.6
            if self.player_dashforward_index >= len(self.player_dashforward): 
                self.player_dashforward_index = len(self.player_dashforward)-1
            self.image = self.player_dashforward[int(self.player_dashforward_index)]

        elif not keys[pygame.K_RIGHT]:
            self.player_dashforward_index = 0

        ## DASH BACK ANIMATION ##

        if keys[pygame.K_LEFT] and self.movement_speed < 1:
            self.player_dashback_index += 0.6
            if self.player_dashback_index >= len(self.player_dashback): 
                self.player_dashback_index = len(self.player_dashback)-1
            self.image = self.player_dashback[int(self.player_dashback_index)]

        elif not keys[pygame.K_LEFT]:
            self.player_dashback_index = 0

        ## BARRAGE ANIMATION ##

        if self.barrage_cooldown: ## I USE COOLDOWNS ON THIS CASE, TO DECIDE WHETHER TO PLAY THIS ANIMATION OR NOT ##
            self.player_playerpose_index += 0.2
            if self.player_playerpose_index >= len(self.player_playerpose): 
                self.player_playerpose_index = len(self.player_playerpose)-1
            self.image = self.player_playerpose[int(self.player_playerpose_index)]

        elif not self.barrage_cooldown:
            self.player_playerpose_index = 0


        ## TIMESTOP ANIMATION ##
        if keys[pygame.K_g] and self.hp<10000 and not self.timestop: ## ONLY HAPPENS BELOW 10K HP, KINDA INEFFECIENT SINCE CHANGING IT WILL BE DIFFICULT, BUT WORKS ##
                        
            
            self.tokiotomare_index += 0.2
            if self.tokiotomare_index >= len(self.tokiotomare): 
                self.tokiotomare_index = len(self.tokiotomare)-1
            self.image = self.tokiotomare[int(self.tokiotomare_index)]

            if self.tokiotomare_index == 1:
                            
                self.timestop_sound.play() ## Play the voiceline for time stop if the animation index is on the second index, this does not necessarily mean that if this voiceline is player, time has stopped, since time does not stop at the second index value ##

        

            


        elif not keys[pygame.K_g]:
            self.tokiotomare_index = 0

        

        ## KNIFE THROW ANIMATION ##

        if keys[pygame.K_f] and self.timestop: 
            self.knifethrow_index += 0.5
            if self.knifethrow_index >= len(self.knifethrow): 
                self.knifethrow_index = len(self.knifethrow)-1
            self.image = self.knifethrow[int(self.knifethrow_index)]
            if self.knifethrow_index == 1: ## Play Voiceline When At Second Index Value Of Animation
                self.checkmate_sound.play()

            

        elif not keys[pygame.K_f]:
            self.knifethrow_index = 0



        
            

          
        
        
