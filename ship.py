
class Ship:
    def __init__ (self):
        self.direction="center"
        self.xpos=200
        self.ypos=200
    
    def move(self):
        
        if self.direction=="left":
            self.xpos=self.xpos-3
            
        if self.direction=="right":
            self.xpos=self.xpos+3
        if self.direction=="UP":
            self.ypos=self.ypos-3
        if self.direction=="DOWN":
            self.ypos=self.ypos+3
        if self.direction== "center":
            self.xpos=self.xpos
            
        return(self.xpos,self.ypos)
            

