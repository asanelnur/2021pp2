import pygame
import random

pygame.init()

#surface 
screen_width,screen_height=600,600
game_display=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("The Hungry Lion Game")
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
ORANGE=(255,165,0)

clock=pygame.time.Clock()
FPS=60



score_font=pygame.font.SysFont('ubuntu',25)

def print_score(score):
    text=score_font.render('Score: '+str(score),True,ORANGE)
    game_display.blit(text,[0,0])
def draw_lion(x,y):
    pygame.draw.rect(game_display,BLUE,(x,y,20,20))

foods= []
block= []

for i in range(10):
    x1=random.randint(20,580)
    y1=random.randint(20,580)
    foods.append([x1,y1])
def draw_foods():
    for i,val in enumerate(foods):
        x1=foods[i][0]
        y1=foods[i][1]
        pygame.draw.rect(game_display,GREEN,(x1,y1,20,20))
    
for i in range(15):
    x1=random.randint(20,580)
    y1=random.randint(20,580)
    block.append([x1,y1])
def draw_block():
    for i,val in enumerate(block):
        x1=block[i][0]
        y1=block[i][1]+5
        pygame.draw.rect(game_display,RED,(x1,y1,20,20))

def run_game():
    game_over=False
    
    x=screen_width-random.randint(30,570)
    y=screen_height-30

    score=0
    

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RIGHT,pygame.K_d]:
                    x=x+5
                if event.key in [pygame.K_LEFT,pygame.K_a]:
                    x=x-5
                if event.key in [pygame.K_UP,pygame.K_w]:
                    y=y-5
                if event.key in [pygame.K_DOWN,pygame.K_x]:
                    y=y+5
        for i,val in enumerate(block):
             block[i][1]+=3
             if block[i][1]>600:
                 block[i][0]=random.randint(20,580)
                 block[i][1]=0
        for i,val in enumerate(foods):
             c=foods[i][0]
             foods[i][0]=random.randint(c-2,c+2)
             
        game_display.fill(WHITE)
        draw_lion(x,y)
        draw_foods()
        draw_block()
        print_score(score)
        for i,val in enumerate(foods):
            if foods[i][0] in range(x-5,x+5) and foods[i][1] in range(y-5,y+5):
                score+=1
                foods.remove(foods[i])
                foods[i]=[random.randint(20,580),random.randint(20,580)]
        for i,val in enumerate(block):
            if block[i][0] in range(x-5,x+5) and block[i][1] in range(y-5,y+5):
                score-=1
                block.remove(block[i])
                block[i]=[random.randint(20,580),random.randint(20,580)]
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
run_game()



pygame.quit()
