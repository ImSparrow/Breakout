'''
Author: Jun Hao Zhang
Date: April 26, 2015
Description: A remake of the Super Break-out game
'''

# I - IMPORT AND INITIALIZE
import pygame, mySprites
pygame.init()
pygame.mixer.init()

     
def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # DISPLAY
    pygame.display.set_caption("Super Break-Out")
     
    # ENTITIES
    screen = pygame.display.set_mode((640, 480))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Creating a list for the breaks
    brick = []
    # First layer of the brick
    for i in range(18):
        brick.append(mySprites.Brick(screen,i*37,70,255,0,255))
    # Second layer of the brick
    for i in range(18):
        brick.append(mySprites.Brick(screen,i*37,80,255,0,0))
    # Thrid layer of the brick
    for i in range(18):
        brick.append(mySprites.Brick(screen,i*37,90,255,255,0))
    # Fourth layer of the brick
    for i in range(18):
        brick.append(mySprites.Brick(screen,i*37,100,255,165,0))
    # Fifth layer of the brick
    for i in range(18):
        brick.append(mySprites.Brick(screen,i*37,110,0,255,0))
    # Last layer of the brick
    for i in range(18):
        brick.append(mySprites.Brick(screen,i*37,120,0,0,205))
    # Creating all the sprites
    score_keeper = mySprites.ScoreKeeper()
    player_endzone = mySprites.EndZone(screen)
    ball = mySprites.Ball(screen)
    player = mySprites.Player(screen,1)
    player2 = mySprites.Player(screen,2)
    bricksprites = pygame.sprite.Group(brick)
    allSprites = pygame.sprite.Group(ball,player,player2,brick,player_endzone,score_keeper)
    # Importing the sounds
    gameover = pygame.image.load("gameover.png")
    gameover.convert()
    pygame.mixer.music.load("music.mp3")
    bounce = pygame.mixer.Sound("bounce.wav")
    bounce.set_volume(0.1)
    pygame.mixer.music.set_volume(0.3)
    # Making the bgm loop
    pygame.mixer.music.play(-1)
    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
     
        # EVENT HANDLING: Player 1 using left and right arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Fade out time for 3 seconds
                pygame.mixer.music.fadeout(3000)
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.change_direction((-1, 0))
                if event.key == pygame.K_LEFT:
                    player.change_direction((1, 0))
                    
        # If ball reacts with player 1 it will change direction and play a sound            
        if ball.rect.colliderect(player):
            ball.change_direction()
            bounce.play()
        # If ball reacts with player 2 it will change direction and play a sound  
        if ball.rect.colliderect(player2):
            ball.change_direction()
            bounce.play()
            
        # Creating a for loop to see every single collision event    
        for brick in pygame.sprite.spritecollide(ball,bricksprites,True):
            for walls in bricksprites:
                walls.move()
            # Gain points for every brick destroyed    
            score_keeper.player1_points()
            ball.change_direction()
            bounce.play()
        # If ball reacts with the end zone, players will lose a life and the ball will reset
        if ball.rect.colliderect(player_endzone):
            ball.reset()
            score_keeper.player1_life()
        # If all the bricks are destroyed player wins, then the game ends
        if score_keeper.winner():
            pygame.mixer.music.fadeout(3000)
            keepGoing = False
        # If player loses all their life, the game ends
        if score_keeper.loser():
            pygame.mixer.music.fadeout(3000)
            keepGoing = False
            
                     
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
         
    # Unhide the mouse pointer and have a delay on the quit
    pygame.time.delay(3000)
    pygame.mouse.set_visible(True)
 
    # Close the game window
    pygame.quit()     
     
# Call the main function
main()   