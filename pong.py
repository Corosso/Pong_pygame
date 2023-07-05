#Import libraries
import pygame, sys
#Initialize pygame
pygame.init()
#Colors (RGB)
black=(0,0,0)
white=(255,255,255)
#Screen size
size=(800,500)
#Creating screen
screen=pygame.display.set_mode(size)
#Creating clock
clock=pygame.time.Clock()
#Hide cursor
pygame.mouse.set_visible(0)
#Boolean variable to end the game
game_over=False
#Player height and widht
player_widht=10
player_height=50
#Window name
pygame.display.set_caption('Pong')
#Font for the score
font = pygame.font.SysFont("Arial", 30)
#Function that draw on the screen the score
def draw_text(text, font, text_col,X,Y):
    img = font.render(text,True,text_col)
    screen.blit(img,(X,Y))
score_p1=0
score_p2=0
#player 1 coords & speed
cord1_x=10
cord1_y=250-(player_height/2)
speed1_y=0
#player 2 coords
cord2_x=780
cord2_y=250-(player_height/2)
speed2_y=0
#ball speed/cords
speedb_x=3
speedb_y=3
cordb_x=400
cordb_y=250
#Principal cicle
while not game_over:
    #Background color
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
            sys.exit()
                #Keybord inputs
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                speed1_y=-3
            if event.key==pygame.K_s:
                speed1_y=3  
            if event.key==pygame.K_UP:
                speed2_y=-3  
            if event.key==pygame.K_DOWN:
                speed2_y=3  
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                speed1_y=0
            if event.key==pygame.K_s:
                speed1_y=0  
            if event.key==pygame.K_UP:
                speed2_y=0 
            if event.key==pygame.K_DOWN:
                speed2_y=0
        
    
    
    #Ball code
    if cordb_y>490 or cordb_y<10:
        speedb_y*=-1
    
    if cordb_x>799 :
        score_p1+=1
        cordb_x=400
        cordb_y=250
        speedb_y*=-1
        speedb_x*=-1
        
    if cordb_x<1:
        score_p2+=1
        cordb_x=400
        cordb_y=250
        speedb_y*=-1
        speedb_x*=-1
    draw_text(str(score_p1), font, white,300, 50)
    draw_text(str(score_p2), font, white,500, 50)
 
    cord1_y+=speed1_y
    cord2_y+=speed2_y    
    cordb_x+=speedb_x
    cordb_y+=speedb_y

    #Ball and player figures
    player1=pygame.draw.rect(screen, white, (cord1_x,cord1_y,player_widht,player_height))
    player2=pygame.draw.rect(screen, white, (cord2_x,cord2_y,player_widht,player_height))
    ball=pygame.draw.circle(screen, white, (cordb_x,cordb_y),6)


    #Colissions
    if ball.colliderect(player1) or ball.colliderect(player2):
        speedb_x*=-1

    pygame.display.flip()
    clock.tick(60)
pygame.display.update()    
pygame.quit()