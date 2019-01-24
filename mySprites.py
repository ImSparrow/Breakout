'''
Author: Jun Hao Zhang
Date: April 26 2015
Description: Sprites for the Super Break=out game
'''

# Import pygame and random
import pygame, random
pygame.init()

class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((10, 10))
        self.image.fill((142, 112, 219))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.__screen = screen
        self.__dx = random.randint(3,8)
        self.__dy = random.randint(-8,-3)
 
    def change_direction(self):
        '''This method causes the y direction of the ball to reverse.'''
        self.__dy = -self.__dy
    def reset(self):
        ''' This method resets the ball, and changes its vector'''
        self.rect.center = (self.__screen.get_width()/2,self.__screen.get_height()/2)
        self.__dx = random.randint(-8,8)
        self.__dy = random.randint(-8,8)
    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''
        # Check if we have reached the left or right end of the screen.
        # If not, then keep moving the ball in the same x direction.
        if ((self.rect.left > 0) and (self.__dx < 0)) or\
           ((self.rect.right < self.__screen.get_width()) and (self.__dx > 0)):
            self.rect.left += self.__dx
        # If yes, then reverse the x direction. 
        else:
            self.__dx = -self.__dx
             
        # Check if we have reached the top or bottom of the court.
        # If not, then keep moving the ball in the same y direction.
        if ((self.rect.top > 0) and (self.__dy > 0)) or\
           ((self.rect.bottom < self.__screen.get_height()) and (self.__dy < 0)):
            self.rect.top -= self.__dy
        # If yes, then reverse the y direction. 
        else:
            self.__dy = -self.__dy
            
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player 1 and Player 2'''
    def __init__(self, screen, player_num):
        '''This initializer takes a screen surface, and player number as
        parameters.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Creating the blocks
        self.image = pygame.Surface((70,5))
        self.image = self.image.convert()
        self.image.fill((142, 112, 219))
        self.rect = self.image.get_rect()
        self.__player_num = player_num
        # Positioning the players
        if self.__player_num == 1:
            self.rect.left = screen.get_width()/2
        elif self.__player_num == 2:
            self.rect.left = screen.get_width()/2
 
        # Placing the players at the bottom of the screen
        self.__screen = screen
        self.rect.bottom = self.__screen.get_height()
        self.__dx = 0
    def change_direction(self, xy_change):
        '''This method takes a (x,y) tuple as a parameter, extracts the 
        x element from it, and uses this to set the players x direction.'''
        self.__dx = xy_change[0]
         
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        if self.__player_num == 1:
            if ((self.rect.left > 0) and (self.__dx > 0)) or\
               ((self.rect.right < self.__screen.get_width()) and (self.__dx < 0)):
                self.rect.left -= (self.__dx*7)
        elif self.__player_num == 2:
            self.rect.left,y = pygame.mouse.get_pos()
        
class Brick(pygame.sprite.Sprite):
    '''This class define our brick class'''
    def __init__(self, screen,x_position,y_position,r,g,b):
        '''calls for the screen, x and y position and rgb colour'''
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((37,10))
        self.image.fill((r,g,b))
        self.rect = self.image.get_rect()
        self.rect.centerx = (0+x_position)
        self.rect.centery = (0+y_position)
    def move(self):
        ''' When called it will move the brick down by 2 pixels'''
        self.rect.centery += 2
class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our endzone at the bottom'''
    def __init__(self, screen):
        '''This initializer takes the screen and nothing else'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.Surface((screen.get_width(), 1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.top = screen.get_height() - 1
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load the Arial font
        self.__font = pygame.font.SysFont("Arial", 30)
        self.__player1_life = 3
        self.__player1_points = 0
    def player1_life(self):
        '''This method takes away a life from the player when it hits the end zone'''
        self.__player1_life -= 1
    def player1_points(self):
        ''' This method gives the player one point for every brick destroyed'''
        self.__player1_points += 1
     
    def loser(self):
        '''When player life reaches zero it will return a 1 to signify that the game is over.'''
        if self.__player1_life == 0:
            return 1
        else:
            return 0
    def winner(self):
        ''' When the player destroy all the brick it will signify that the game is over.'''
        if self.__player1_points == 108:
            return 1
        else:
            return 0
 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Life: %d           Points: %d " %(self.__player1_life,self.__player1_points)
        self.image = self.__font.render(message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (270, 15)
        