import pygame
import random

pygame.init()

#surface 
screen_width,screen_height=500,500
game_display=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("The Snake Game")

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
ORANGE=(255,165,0)

clock=pygame.time.Clock()
snake_size=10
snake_speed=15

message_font=pygame.font.SysFont('ubuntu',30)
score_font=pygame.font.SysFont('ubuntu',25)

def print_score(score):
    text=score_font.render('Score: '+str(score),True,ORANGE)
    game_display.blit(text,[0,0])
def draw_snake(snake_size,snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display,GREEN,[pixel[0],pixel[1],snake_size,snake_size])

def run_game():

    game_over=False
    game_close=False

    x=screen_width/2
    y=screen_height/2

    x_speed=0
    y_speed=0

    snake_pixels=[]
    snake_lenght=1

    target_x=round(random.randrange(50,screen_width-50-snake_size) / 10.0)*10.0
    target_y=round(random.randrange(50,screen_height-50-snake_size) / 10.0)*10.0
    while not game_over:
        while game_close:
            game_display.fill(BLACK)
            game_over_message=message_font.render("Game over!",True,RED)
            game_over_message2=message_font.render(f"Your Score:{str(snake_lenght-1)}",True,BLUE)
            game_display.blit(game_over_message,[screen_width/3,screen_height/3])
            game_display.blit(game_over_message2,[screen_width/3,screen_height/2])
            print_score(snake_lenght-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        game_over=True
                        game_close=False
                    if event.type == pygame.K_a:
                        run_game()
            if event.type == pygame.QUIT:
                game_over=True
                game_close=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_speed=snake_size
                    y_speed=0
                if event.key == pygame.K_LEFT:
                    x_speed=-snake_size
                    y_speed=0
                if event.key == pygame.K_UP:
                    x_speed=0
                    y_speed=-snake_size
                if event.key == pygame.K_DOWN:
                    x_speed=0
                    y_speed=snake_size
        if x>=screen_width-20 or x<20 or y>=screen_height-20 or y<20:
            game_close=True
        
        x+=x_speed
        y+=y_speed

        game_display.fill(WHITE)
        pygame.draw.line(game_display, BLACK, (495, 0), (495, 500), 20)
        pygame.draw.line(game_display, BLACK, (5, 0), (5, 495 ), 20)
        pygame.draw.line(game_display, BLACK, (0, 5), (495, 5 ), 20)
        pygame.draw.line(game_display, BLACK, (0, 495), (500, 495), 20)
        pygame.draw.rect(game_display,ORANGE,[target_x,target_y,snake_size,snake_size])

        snake_pixels.append([x,y])
        if len(snake_pixels)>snake_lenght:
            del snake_pixels[0]
        for pixel in snake_pixels[:-1]:
            if pixel==[x,y]:
                game_close=True
        draw_snake(snake_size,snake_pixels)
        print_score(snake_lenght-1)
        pygame.display.update()

        if x==target_x and y==target_y:
            target_x=round(random.randrange(0,screen_width-snake_size) / 10.0)*10.0
            target_y=round(random.randrange(0,screen_height-snake_size) / 10.0)*10.0
            snake_lenght+=1
        
        clock.tick(snake_speed)
    pygame.quit()
    quit()
run_game()



pygame.quit()
