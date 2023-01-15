import pygame


class Knives (pygame.sprite.Sprite):
    def __init__(self, x, y,speed,timestop):
        super().__init__()

        
        self.image = pygame.image.load("images/knives.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.timestop = timestop

    
        
    def update(self):
        if self.timestop:
            self.rect.x += 0
        else:
            self.rect.x += self.speed

        if self.rect.x > 1100:
            self.kill()


class Bullet (pygame.sprite.Sprite):
    def __init__(self, x, y,speed):
        super().__init__()

        
        self.image = pygame.image.load("images/shoot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        
        
        self.rect.x += self.speed
        
        if self.rect.x > 1100:
            self.kill()





class muda (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        
        

        
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
        self.muda = [muda1,muda2,muda3,muda4,muda5,muda6,muda7,muda8,muda9,muda10]
        self.muda_index = 0
        self.image = self.muda[self.muda_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.playerpos = x

    def update(self):
        self.muda_index += 0.4
        if self.muda_index >= len(self.muda): self.muda_index = 0
        self.image = self.muda[int(self.muda_index)]
        self.muda_back_index = 0
        
        self.rect.x += 4
        self.rect.y
        if self.rect.x - self.playerpos > 100:
            self.kill()


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

        #### IDLE STATE ANIMATION ####
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
        player_walk1 = pygame.image.load("images/walk1.png").convert_alpha()       
        player_walk2 = pygame.image.load("images/walk2.png").convert_alpha()
        player_walk3 = pygame.image.load("images/walk3.png").convert_alpha()
        player_walk4 = pygame.image.load("images/walk4.png").convert_alpha()
        player_walk5 = pygame.image.load("images/walk5.png").convert_alpha()
        player_walk6 = pygame.image.load("images/walk6.png").convert_alpha()
        player_walk7 = pygame.image.load("images/walk7.png").convert_alpha()
        player_walk8 = pygame.image.load("images/walk8.png").convert_alpha()
        player_walk9 = pygame.image.load("images/walk9.png").convert_alpha()
        player_walk10 = pygame.image.load("images/walk10.png").convert_alpha()
        player_walk11 = pygame.image.load("images/walk11.png").convert_alpha()
        player_walk12 = pygame.image.load("images/walk12.png").convert_alpha()
        player_walk13 = pygame.image.load("images/walk13.png").convert_alpha()
        player_walk14 = pygame.image.load("images/walk14.png").convert_alpha()
        player_walk15 = pygame.image.load("images/walk15.png").convert_alpha()
        player_walk16 = pygame.image.load("images/walk16.png").convert_alpha()
        self.player_walk = [player_walk1,player_walk2,player_walk3,player_walk4,player_walk5,player_walk6,player_walk7,player_walk8,player_walk9,player_walk10,player_walk11,player_walk12,player_walk13,player_walk14,player_walk15,player_walk16]
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
        self.barrage_sound.set_volume(0.07)
        






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

        self.knives = pygame.sprite.Group()
        self.checkmate_sound = pygame.mixer.Sound("audio/checkmate.wav")
        self.checkmate_sound.set_volume(0.1)



        #### SOME MORE INITIALIZATIONS ####
        self.rect = self.image.get_rect()
        
        self.player_walk1_scaled = pygame.transform.scale2x(player_walk1)
        
        self.movement_speed = 0
        self.dash_state = False
        self.dashbackstate = False
        self.rect.x = 100
        self.hp = 15000
        self.max_hp = 10000
        self.gravity = 0
        self.lowhp_sound = pygame.mixer.Sound("audio/lowhp.wav")
        self.lowhp_sound.set_volume(0.1)
        
        

        


        
     


    
            
    def player_input(self):
          

        ################### JUMP #########################

        if self.rect.bottom < 480:
                self.is_jumping = True
        else:
            self.is_jumping = False
        keys = pygame.key.get_pressed()

        if keys [pygame.K_w] and self.rect.bottom >= 480:
            self.gravity = -30
            

        

        


        #################### MOVE RIGHT #########################

        if keys[pygame.K_d] and not self.is_jumping:
            self.movement_speed += 0.8  # increase speed
            self.rect.x += self.movement_speed  # Move player right
            moving_right = True
            
            

        else: 
            self.movement_speed *= 0.9 
            moving_right = False


        ################ MOVE LEFT #####################################

        if keys[pygame.K_a] and not self.is_jumping:
            self.movement_speed += 0.8  #  increase speed
            self.rect.x -= self.movement_speed  # Move  player left
            moving_left = True
            
            
        
        else: 
            self.movement_speed *= 0.9
            moving_left = False 


        ###################### FALL FASTER ##############################

        if keys [pygame.K_s]:
            self.gravity = + 25

        ##################### PREVENTION OF MOVEMENT CONFLICT (RIGHT AND LEFT) ###################
        if moving_left and moving_right == True:
            self.movement_speed = 0

        ####################### MOVE RIGHT ###########################
        if keys[pygame.K_RIGHT] and not self.dash_state and not self.dashback_state and not moving_left and not moving_right:
            self.dash_state = True
            self.dash_sound.play()
            self.rect.x += 100
        
        elif not keys[pygame.K_RIGHT]:
            self.dash_state = False

        ######################## MOVE LEFT ##########################

        if keys[pygame.K_LEFT] and not self.dashback_state and not moving_left and not moving_right:
            self.dashback_state = True
            self.rect.x -= 100
            self.dash_sound.play()
        
        elif not keys[pygame.K_LEFT]:
            self.dashback_state = False



        ####################### SHOOT OUT BULLET ########################

        
        if keys[pygame.K_q]:
            if not self.bullet_fired and self.bullet_cooldown <=0:
                bullet = Bullet(self.rect.x + 10, self.rect.centery, 30)
                self.attack1.add(bullet)
                self.bullet_cooldown += 10 # Bullet has a cooldown for every 0.16 seconds (10/main game loop tick(60))(will only work once every keypress, key hold does not count :) )
                
                
                self.bullet_fired = True
        elif not keys[pygame.K_q]:
            self.bullet_fired = False

        if self.bullet_cooldown > 0:
            self.bullet_cooldown -= 1 # Minus Down the CoolDown


        ########################### ABILITY BARRAGE ##########################

        if keys[pygame.K_e]:
            if not self.barrage_fired and self.barrage_cooldown <=0:
                barrage = muda(self.rect.x , self.rect.y)
                self.barrage.add(barrage)
                self.barrage_sound.play()
                self.barrage_cooldown += 30

                self.barrage_fired = True
            
        elif not keys[pygame.K_e]:
            self.barrage_fired = False

        if self.barrage_cooldown > 0:
            self.barrage_cooldown -= 1

        ########################### ABILITY TIMESTOP ##############################

        if self.hp<10000:
            if keys[pygame.K_g] and  self.tokiotomare_index == len(self.tokiotomare)-1:
                self.timestop = True
                self.timestop_sfx.play()
                
            
            if self.knifethrow_index == len(self.knifethrow)-2 and self.timestop:
                    knives = Knives(self.rect.x,self.rect.y,30, self.timestop)
                    self.knives.add(knives)


            if self.timestop:
                current_time = pygame.time.get_ticks()
                
                if current_time - self.timestop_start_time > 10000:
                    self.timemove_sound.play()
                    self.timestop = False
                    self.timestop_start_time = pygame.time.get_ticks()
                    





        for knife in self.knives:
            knife.timestop = self.timestop
        
                
        





        

        

        
     

        

    
    def apply_gravity(self):
        self.gravity += 1.4
        self.rect.y += self.gravity
        if self.rect.bottom >= 490:
            self.rect.bottom = 490

        
            

    def update(self):
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
        if self.movement_speed > 0.5:
            
            ## WALK ANIMATION ##
            if keys[pygame.K_d] and self.movement_speed > 2 and self.rect.bottom > 479 and not keys[pygame.K_a]  :
                self.player_index += 0.4
                if self.player_index >= len(self.player_walk): self.player_index = 0
                self.image = self.player_walk[int(self.player_index)]
                self.player_back_index = 0
            
            ## BACK ANIMATION ##
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
                self.player_attack_index = len(self.player_attack)-1
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

        if self.barrage_cooldown:
            self.player_playerpose_index += 0.2
            if self.player_playerpose_index >= len(self.player_playerpose): 
                self.player_playerpose_index = len(self.player_playerpose)-1
            self.image = self.player_playerpose[int(self.player_playerpose_index)]

        elif not self.barrage_cooldown:
            self.player_playerpose_index = 0


        ## TIMESTOP ANIMATION ##
        if keys[pygame.K_g] and self.hp<10000 and not self.timestop:
                        
            
            self.tokiotomare_index += 0.2
            if self.tokiotomare_index >= len(self.tokiotomare): 
                self.tokiotomare_index = len(self.tokiotomare)-1
            self.image = self.tokiotomare[int(self.tokiotomare_index)]

            if self.tokiotomare_index == 1:
                            
                self.timestop_sound.play()

        

            


        elif not keys[pygame.K_g]:
            self.tokiotomare_index = 0

        

        ## KNIFE THROW ANIMATION ##

        if keys[pygame.K_f] and self.timestop:
            self.knifethrow_index += 0.5
            if self.knifethrow_index >= len(self.knifethrow): 
                self.knifethrow_index = len(self.knifethrow)-1
            self.image = self.knifethrow[int(self.knifethrow_index)]
            if self.knifethrow_index == 1:
                self.checkmate_sound.play()

            

        elif not keys[pygame.K_z]:
            self.knifethrow_index = 0



        
            

          
        
        