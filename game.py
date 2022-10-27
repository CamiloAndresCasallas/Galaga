import pygame
import random
from sky import Sky
from ship import Ship


class Game:



    def __init__ (self):
        self.width=800
        self.height=800
        self.mySky=Sky(self.width, self.height, 1600)
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.clock=pygame.time.Clock()
        self.fps=60
        self.sprites=pygame.image.load("sprites.png")
        self.shipsprite=pygame.Surface((64,64)).convert()
        self.shipsprite.blit(self.sprites,(0,0), (250,436, 64,64))
        self.ship=Ship()
        circulo=pygame.draw.circle(self.screen,(255,255,255), (self.food.x,self.food.y),5)

    
    def checkKeys(self):
        
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]: 
            self.ship.direction="left"
        elif keys[pygame.K_RIGHT]: 
            self.ship.direction="right"
        elif keys[pygame.K_UP]: 
            self.ship.direction="UP"
        elif keys[pygame.K_DOWN]: 
            self.ship.direction="DOWN"
        else:
            self.ship.direction="center"
            
        bullets=[]
        
        def on_key_down(key):
            if key == keys.SPACE:
                bullets.append(Actor('bullet'))
                bullets[-1].x=ship.xpos
                bullets[-1].y=ship.ypos
                
            

    def run(self):

        pygame.init()

        control=True
        while control: 

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                 pygame.quit()

            self.screen.fill((0,0,0))

            #show the Sky
            for star in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen,(r,g,b), star, 1)


                    
            
            self.mySky.move()
            x=self.ship.xpos
            y=self.ship.ypos
            self.screen.blit(self.shipsprite, (x,y))
            self.clock.tick(self.fps)
            self.checkKeys()
            self.ship.move()  
            pygame.display.flip()
            



mygame=Game()
mygame.run()
