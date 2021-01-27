import pygame
import random
                        
pygame.init() 
# Definig colours
white = (255,255,255)
red = (255,0,0)
black =(0)
blue = (0,0,255)
dark_blue = (28,32,204)
green = (8,233,9)
screen_width = 900
screen_hight = 600
#Creating window
game_window = pygame.display.set_mode((screen_width,screen_hight))

pygame.display.set_caption("Snakes game")
pygame.display.update()

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])
def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,black,[x,y,snake_size,snake_size])

font = pygame.font.SysFont(None,55) 
clock = pygame.time.Clock()
def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(green)
        text_screen("Welcome to Snakes",blue,260,250)
        text_screen("Press Enter to play",blue,232,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(60)

#Main game loop
def gameloop():
        # Game spefic variables
    exit_game = False
    gameOver = False
    snake_x = 45
    snake_y = 55
    velosityX = 0
    velosityY = 0
    snake_size = 1
    snk_list = [ ]
    snk_length = 1
    with open("hiscore.txt","r") as f:
        hiscore = f.read( ) 

    foodX = random.randint(20,screen_width/2)
    foodY = random.randint(20,screen_hight/2)
    score = 0
    velosity = 8
    snake_size = 30
    fps = 30
    while not exit_game:
        if gameOver:
            game_window.fill(blue)  
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
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
                        velosityX = velosity
                        velosityY = 0
                    if event.key == pygame.K_LEFT:
                        velosityX = -velosity
                        velosityY = 0
                    if event.key == pygame.K_UP:
                        velosityY = -velosity
                        velosityX = 0
                    if event.key == pygame.K_DOWN:
                        velosityY = velosity
                        velosityX = 0
            snake_x += velosityX     
            snake_y += velosityY
            
            if abs(snake_x - foodX) < 12 and abs(snake_y- foodY) < 12:
                score+=10
                foodX = random.randint(20,screen_width/2)
                foodY = random.randint(20,screen_hight/2)
                snk_length += 5
                if score > int(hiscore) :
                    hiscore = score                 
            game_window.fill(dark_blue)
            text_screen("Score : "+str(score)+" Highscore : "+str(hiscore),red,5,5)
            pygame.draw.rect(game_window,red,[foodX,foodY ,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)   
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if snake_x < 0 or snake_x>screen_width or snake_y<0 or snake_y>screen_hight:
                gameOver = True
            if head in snk_list[:-1]:
                gameOver = True 
            # pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(game_window,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit() 
    quit()
welcome()
