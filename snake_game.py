import pygame
import random
import os
pygame.mixer.init()


pygame.init()

white= (255,255,255)
red = (255,0,0)
black = (0,0,0)

scrin_width=900
scrin_hight=600

gameWindow = pygame.display.set_mode((scrin_width,scrin_hight))
bgimage=pygame.image.load("C:\\Users\\Gopal Mali\\Pictures\\snake.jpg")
bgimage=pygame.transform.scale(bgimage,(scrin_width,scrin_hight)).convert_alpha()

bgimg=pygame.image.load("C:\\Users\\Gopal Mali\\Pictures\\game-over2.jpg")
bgimg=pygame.transform.scale(bgimg,(scrin_width,scrin_hight)).convert_alpha()

strimg=pygame.image.load("C:\\Users\\Gopal Mali\\Pictures\\start.jpg")
strimg=pygame.transform.scale(strimg,(scrin_width,scrin_hight)).convert_alpha()

pygame.display.set_caption("SnakesWithGopal")

pygame.display.update()



clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def welcome():
    exit_game=False
    while not exit_game:
        #gameWindow.fill((40,240,50))
        gameWindow.blit(strimg,(0,0))
        text_scrin("Welcome To SnakeWithGopal",red,75,75)
        text_scrin("Press Space Bar To Play",(40,240,50),130,520)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('C:\\Users\\Gopal Mali\\Music\\Luis Fonsi .mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def text_scrin(text,color,x,y):
    scrin_text = font.render(text,True,color)
    gameWindow.blit(scrin_text,[x,y])

def plot_snake(gameWindow,color,snk_lst,snake_size):
    for x,y in snk_lst:
         if x>10 and y>10:
             pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])



def gameloop():
    exit_game=False
    game_over=False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    if (not os.path.exists("HiScore.txt")):
        with open("HiScore.txt","w") as f:
            f.write("0")
    with open("HiScore.txt","r") as f:
        hiscore=f.read()
    food_x = random.randint(20,scrin_width/2)
    food_y = random.randint(20,scrin_hight/2)
    snk_lst=[]
    snk_length=1
    score =0
    init_velocity=5
    velocity_x=0
    velocity_y=0
    fps = 60
    while not exit_game:
        if game_over:
            with open("HiScore.txt","w") as f:
                f.write(str(hiscore))
            #gameWindow.fill((40,240,50))
            gameWindow.blit(bgimg,(0,0))
            text_scrin(" Press Enter To Continue",red,200,400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =init_velocity
                        velocity_y =0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y =0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x =0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_g:
                        score +=10


            snake_x +=velocity_x
            snake_y +=velocity_y

            if abs(snake_x - food_x)<13 and abs(snake_y - food_y)<13:
                score +=10
                food_x = random.randint(20,scrin_width/2)
                food_y = random.randint(20,scrin_hight/2)
                snk_length +=5
                if score > int(hiscore):
                    hiscore=score

            #gameWindow.fill((40,240,50))
            gameWindow.blit(bgimage,(0,0))
            text_scrin(f"Score: {str(score)}  HiScore:{str(hiscore)} ",red,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)

            if len(snk_lst) > snk_length :
                del snk_lst[0]

            if head in snk_lst[ :-1]:
                game_over=True
                #gameWindow.blit(bgimg,(0,0))
                pygame.mixer.music.load('C:\\Users\\Gopal Mali\\Music\\Car Accident.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>scrin_width or snake_y <0 or snake_y >scrin_hight:
                game_over = True
               # gameWindow.blit(bgimg,(0,0))
                pygame.mixer.music.load('C:\\Users\\Gopal Mali\\Music\\Car Accident.mp3')
                pygame.mixer.music.play()
            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_lst,snake_size )
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()   
welcome()

