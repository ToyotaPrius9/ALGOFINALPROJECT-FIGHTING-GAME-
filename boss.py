import pygame
import random


class ora (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        ############################### SELF ANIMATIONS ###################3333
        self.ora = []## empty list ##
        self.ora.append(pygame.image.load("images/ora1.png").convert_alpha()) ## append list with all these ##
        self.ora.append(pygame.image.load("images/ora2.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora3.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora4.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora5.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora6.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora7.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora8.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora9.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora10.png").convert_alpha())
        self.ora.append(pygame.image.load("images/ora11.png").convert_alpha()) 
        self.ora.append(pygame.image.load("images/ora12.png").convert_alpha())  
        
        self.ora_index = 0
        self.image = self.ora[self.ora_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bosspos = x
        

    def update(self):
        self.ora_index += 0.4 ## Change through images, making itself look animated ##
        if self.ora_index >= len(self.ora): self.ora_index = 0 ## if length goes out of list, restart from 0 ##
        self.image = self.ora[int(self.ora_index)] ## Set this image to self.image ##
        
        
        self.rect.x -= 4 ## move 4 to left constantly ##
        
        if self.rect.x < self.bosspos - 300: ## if goes 300 pixels to the left from the attack position of the boss, remove from the screen ##
            self.kill()
            




class Attack1(pygame.sprite.Sprite):
    ## Similiar to Bullet for the player class but some changes, this thing can go not only straght, but also northwest! ##
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/shoot.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.x_velocity = random.uniform(-10, -8)
        self.y_velocity = random.uniform(0 , -4)
        self.prob_straight = 0.8 # Prob of going straight
        self.prob_nw = 0.2 # Prob of going northwest
    def update(self):
        random_num = random.random() ## Generates between 0 and 1 ##
        
        if random_num < self.prob_straight:
            self.rect.x -= 20 ## bullet will go straight ##
        else:
            self.rect.x -= 20 ## bullet will go northwest ##
            self.rect.y -= 1  ## How far up to northwest? This -1 holds that fate ##
        
        if self.rect.x == 60: ## If goes this far, remove from screen ##
            self.kill()
       
class Attack2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/roadsign.png").convert_alpha() ## questionable choice of image/attack, but why not? ##
        self.rect = self.image.get_rect(center=(x, y))
        self.prob_straight = 0.8 # Prob of going straight
        self.prob_nw = 0.2 # Prob of going northwest
    def update(self):
        random_num = random.random() #Generates between 0 and 1
        
        if random_num < self.prob_straight: # Depending on the result of random number:
            self.rect.x -= 10 ## bullet will go straight ##
        else:
            self.rect.x -= 20 ## bullet will go northwest ##
            self.rect.y -= 10
        
        if self.rect.x == 60: ## Goes too far? Disappear from the screen! ##
            self.kill()



class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        


        ########################## BOSS IDLE ANIMATION & RECT ##########################
        self.bossidle = []
        self.bossidle.append(pygame.image.load("images/bossidle1.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle2.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle3.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle4.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle5.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle6.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle7.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle8.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle9.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle10.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle11.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle12.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle13.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle14.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle15.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle16.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle15.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle14.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle13.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle12.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle11.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle10.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle9.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle8.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle7.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle6.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle5.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle4.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle3.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle2.png").convert_alpha())
        self.bossidle.append(pygame.image.load("images/bossidle1.png").convert_alpha())
        self.bossidle_index = 0
        self.image = self.bossidle[self.bossidle_index]
        self.rect = self.image.get_rect()


        ############################ BOSS JUMP ANIMATION ###########################
        self.bossjump = []
        self.bossjump.append(pygame.image.load("images/bossjump1.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump2.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump3.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump4.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump5.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump6.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump7.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump8.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump9.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump10.png").convert_alpha())
        self.bossjump.append(pygame.image.load("images/bossjump11.png").convert_alpha())
        self.bossjump_index = 0


        ############################## BOSS BARAGE ANIMATION###################
        self.bosspose = []
        self.bosspose.append(pygame.image.load("images/bosspose1.png").convert_alpha())
        self.bosspose.append(pygame.image.load("images/bosspose2.png").convert_alpha())
        self.bosspose.append(pygame.image.load("images/bosspose3.png").convert_alpha())
        self.bosspose.append(pygame.image.load("images/bosspose4.png").convert_alpha())
        self.bosspose.append(pygame.image.load("images/bosspose5.png").convert_alpha())
        self.bosspose_index = 0

        ############################## BOSS MOVE BACKWARDS ANIMATION #################
        
        self.bossback = []
        self.bossback.append(pygame.image.load("images/bossback1.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback2.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback3.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback4.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback5.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback6.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback7.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback8.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback9.png").convert_alpha())
        self.bossback.append(pygame.image.load("images/bossback10.png").convert_alpha())
        self.bossback_index = 0

        ########################## BOSS MOVE FORWARDS ANIMATION ######################
        
        self.bosswalk = []
        self.bosswalk.append(pygame.image.load("images/bosswalk1.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk2.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk3.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk4.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk5.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk6.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk7.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk8.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk9.png").convert_alpha())
        self.bosswalk.append(pygame.image.load("images/bosswalk10.png").convert_alpha())
        self.bosswalk_index = 0
        

        
        
        ################## DECLARE AND INITIATE #######################
        
        ## BOSS ATTACKS ##
        self.attack1 = False
        self.attack2 = False
        self.attack3 = False

        ## BOSS MOVEMENT FOR X ##
        self.moveleft = False
        self.moveright = False
        self.jumpup = False
        self.movement_speed = 0
        self.accel = 6 # FOR ACCELLERATION OF MOVEMENT #
        
        ## BOSS HEALTH POINTS ##
        self.max_hp = 15000 
        self.hp = 40000
        

        ## BOSS RECT PLACEMENTS, ALTHOUGH THE MAIN GAME LOOP ALREADY DOES THIS ##
        self.rect.x = 1000
        self.rect.y = 490

        ## BOSS GRAVITY ##
        self.gravity = 0



        

        
        ## INITIATE PLAYER'S TIME STOP ABILITY STATUS (TRUE OR FALSE)  [MODIFIED IN THE MAIN GAME LOOP] ##
        self.time_stopped = False

        ## INITIATE VARIABLES CONTAINING THE SPRITES THE BOSS COULD SHOOT OUT ##
        self.attack1_group = pygame.sprite.Group()
        self.attack2_group = pygame.sprite.Group()
        self.barrage = pygame.sprite.Group()
        
    ## FIRST ATTACK FUNCTION, A BULLET SHOT ##
    def attack_1(self):
        self.attack1 = True
        
        self.attack1_group.add(Attack1(self.rect.centerx, self.rect.centery))
        
    ## SECOND ATTACK FUNCTION, A STREET SIGN SHOT ##
    def attack_2(self):
        self.attack2 = True
        self.attack2_group.add(Attack2(self.rect.centerx, self.rect.centery))
        
    ## THIRD ATTACK FUNCTION, A PAINFUL BARRAGE ##
    def attack_3(self):
        self.attack3 = True
        self.barrage.add(ora(self.rect.centerx,self.rect.y-30))
        
        
        


    ## FUNCTION FOR THE BOSS TO JUMP ##
    def jump(self):
        self.jumpup = True # CHANGES JUMP BOOLEAN STATE TO TRUE FROM FALSE #

        # MAKES THE BOSS JUMP, ONLY IF THEY ARE ON THE GROUND ( RECT BOTTOM 490 ) #
        if self.rect.bottom == 490:
            self.gravity = -30

        
        
            

        


    ## FUNCTION FOR THE APPLIANCE OF GRAVITY ##
    def apply_gravity(self):
        self.gravity += 1.3 # DROPS THE BOSS DOWN AT THE SPEED OF 1.3 PER FRAME #
        self.rect.y += self.gravity # Y VALUE OF BOSS MINUSES BY GRAVITY VALUE #

        # KEEPS THE BOSS FFROM FALLING OFF THE SCREEN AND STAY ON THE GROUND, IF RECT BOTTOM AT 490, STAYS AT 490 #
        if self.rect.bottom >= 490:
            self.rect.bottom = 490
            self.jumpup = False
            

       
    ## FUNCTION FOR THE BOSS TO MOVE LEFT ##
    def move_left(self):
        self.moveleft = True # CHANGES BOOLEAN VALUE OF MOVELEFT STATE, CAN BE USED TO KEEP TRACK IF MOVING LEFT OR NOT #

        if self.moveleft:
            self.movement_speed += self.accel # MOVEMENT SPEED ADDS BY ACCELERATION VALUE #
            self.rect.x -= self.movement_speed # APPLIES THIS ACCELERATION TO MOVE LEFT (WHICH IS FORWARD TO THE BOSS) #
        else:
            self.movement_speed *= 0.9 # IF NOT MOVING LEFT, SLOWS DOWN ACCEL, CHANGES STATUS #
            self.moveleft = False
        
        # LIMITS THE MOVEMENTS SPEED OF THE BOSS #
        if self.movement_speed>14:  
            self.movement_speed = 14
           #self.moveleft = False ## FOR ANIMATION NOT TO LOOK WEIRD ##
            


    ## FUNCTION TO MOVE RIGHT ( OR BACK, IN BOSS PERSPECTIVE ) ##
    def move_right(self):
        self.moveright = True # KEEPS TRACK OF IF MOVING RIGHT OR NOT #

        # ADDS ACCELERATION TO SPEED AND APPLIES THIS SPEED TO THE BOSS GOING RIGHT (OR BACK) #
        if self.moveright:
            self.movement_speed += self.accel
            self.rect.x += self.movement_speed

        # IF NOT MOVING RIGHT ANYMORE, SLOW DOWN ACCEL AND CHANGE STATUS #
        else:
            self.movement_speed *= 0.9
            self.moveright = False
        
        # CAPS MOVEMENT SPEED  #
        if self.movement_speed>14:
            self.movement_speed = 14

      
            
        
        
        
        
        



    def update(self,playerpos, bulletpos): ######### UPDATE TAKES IN PLAYER POSITION AND BULLET POSITION AS ARGUEMENTS ###########

        #### APPLY GRAVITY INTO ACTION #####
        self.apply_gravity()

        ##### APPLY ALL MOVEMENT ACTIONS ONLY IF PLAYER HAS NOT STOPPED TIME #########
        if not self.time_stopped:
            ## IDLE ANIMATION ##
            if self.rect.y <= 490 and not self.moveleft and not self.moveright and not self.jumpup:
                self.bossidle_index += 0.2
                if self.bossidle_index >= len(self.bossidle): self.bossidle_index = 0
                self.image = self.bossidle[int(self.bossidle_index)]

            ## JUMP ANIMATION ##
            if self.gravity < 30:
                self.bossjump_index += 0.2
                if self.bossjump_index >= len(self.bossjump): self.bossjump_index = 0
                self.image = self.bossjump[int(self.bossjump_index)]

            ## BARRAGE POSE ANIMATION ##
            if self.attack3:
                
                self.bosspose_index += 0.3
                if self.bosspose_index >= len(self.bosspose): 
                    self.bosspose_index = 0
                    self.attack3 = False
                self.image = self.bosspose[int(self.bosspose_index)]
            
            
            ## WALKBACK ANIMATION ##
            if self.moveright and not self.moveleft and not self.jumpup:

                self.bossback_index += 0.2
                if self.bossback_index >= len(self.bossback): 
                    self.bossback_index = 0
                    
                self.image = self.bossback[int(self.bossback_index)]


            ## WALK ANIMATION ##
            if self.moveleft and not self.jumpup and not self.moveright:

                self.bosswalk_index += 0.2
                if self.bosswalk_index >= len(self.bosswalk): 
                    self.bosswalk_index = 0
                    
                self.image = self.bosswalk[int(self.bosswalk_index)]
            
            
            ## CREATE A VARIABLE CONTAINING RANDOM INTEGERS, FOR RANDOM ATTACK CHANCES [SIDE NOTE: THIS INT CHANGES EVERY FRAME, CHANGES REALLY FAST]##
            attack_chance = random.randint(0,200) # RANDOM INTS RANGING FROM 0,200 #

            if attack_chance <= 8 : # IF THE RANDOM INT OUT OF 200 IS LESS OF EQUAL TO 8, PERFORM ATTACK 1 [SHOOT] #
                self.attack_1()
                
                attack_chance = random.randint(0,200) # REFRESH THE RANDOM INT #
                

            elif attack_chance == 15: # IF RAND INT COMES TO 15, PERFORM ATTACK 2 
                self.attack_2()
                
                attack_chance = random.randint(0,200) # REFRESH RANDOM INT #

            elif attack_chance <= 14 : # IF RANDINT LOWER THAN 14 AND PLAYER IS LOWER 500 X PIXELS AWAY, PERFORM ATTACK 3 [BARRAGE]
                if self.rect.x - 500 < playerpos:
                    self.attack_3()
                
                    attack_chance = random.randint(0,200) # REFRESH RANDOM INT #
                    
                    
                

            elif attack_chance > 0: # IF RANDINT IS ANY NUMBER AT ALL HIGHER THAN 0 AND BOSS HP IS BELOW 1000 AND PLAYER IS LOWER THAN 300 X PIXELS AWAY, SPAM ATTACK 3 [BARRAGE]
                if self.hp < 1000:
                    if self.rect.x - 200 < playerpos:
                        self.attack_3()

                        attack_chance = random.randint(0,200) # REFRESH RANDOM INT #




            

            
           
            ## NOW A NEW VARIABLE CONTAINING RANDINT VALUES EXCLUSIVE FOR JUST BOSS MOVEMENTS, NOTHING TO DO WITH ATTACKS, WORKS IN A SIMILIAR WAY ##
            move_chance = random.randint(0,200)
            if move_chance < 2 :

                if self.rect.x > playerpos:

                    self.move_left()
                    move_chance = random.randint(0,200)

            if move_chance < 20 :
                if self.rect.x -1000 < playerpos: 
                    self.move_left()
                    move_chance = random.randint(0,200)
            
            if move_chance < 200 :
                if self.rect.x < playerpos:  # AT ALL COSTS, BOSS WILL MOVE RIGHT IF PLAYER IS BEHIND HIM! nothing boss can do if time is stopped doe :( #
                    self.move_right()
                    self.moveright = False ## Dont want the animation to play when this happens, to achieve this, we can set moveright to False ##
                    move_chance = random.randint(0,200)

            
            if move_chance < 200 :
                closest_bullet = None ## TO COUNTER MEASURE THE BULLET SPRITES OF PLAYER BEING A LIST FORMAT ##
                min_distance = float("inf")
                for bullet_x, _ in bulletpos:
                    distance = abs(self.rect.x - bullet_x)
                    if distance < min_distance:
                        min_distance = distance
                        closest_bullet = bullet_x
                if closest_bullet is not None and min_distance > 50:
                    self.jump()
                move_chance = random.randint(0,200)
                
            if self.rect.x >1100:
                self.move_left()

        
            



        

        




        
        



        

        
        
            


            


        
