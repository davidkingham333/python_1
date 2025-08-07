import pygame
import random
import sys

pygame.init()

x_pos=250
y_pos=250
snake = [[250, 250]]

direction=0

background_colour=(0,0,0)
text_colour=(255,255,255)
text_colour1=(255,0,0)
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("SNAKE")
screen.fill(background_colour)

snake_count = 1

snakeVar = pygame.font.SysFont("Arial",20)
snake_text="■"

foodVar=pygame.font.SysFont("Arial",20)
food_text ="■"


def getDirection() -> int:
    global direction
    return direction


def food_event():
    global x_pos, y_pos

    while True:
        x_pos = random.randrange(0, 499)
        y_pos = random.randrange(0, 499)
        if [x_pos, y_pos] not in snake:
            break

def collision_detected() -> bool:
    global x_pos
    global y_pos
    global snake

    if snake[0][0] == x_pos and snake[0][1] == y_pos:
        print("LOG: Had sežral jídlo.")
        return True
    
    return False

def snake_expend():
    global snake, snake_count

    snake.append(snake[-1])


food_event()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                direction=2
            elif event.key==pygame.K_DOWN:
                direction=3
            elif event.key==pygame.K_LEFT:
                direction=0
            elif event.key==pygame.K_RIGHT:
                direction=1
            else:
                print("try again")


    if direction == 0:
        new_head = [snake[0][0] - 10, snake[0][1]]
    elif direction == 1:  
        new_head = [snake[0][0] + 10, snake[0][1]]
    elif direction == 2:  
        new_head = [snake[0][0], snake[0][1] - 10]
    elif direction == 3:  
        new_head = [snake[0][0], snake[0][1] + 10] 


    if collision_detected():
        print("LOG: Hra končí.")

        running = False


        # Kontrola kolize s jídlem
    if (new_head[0] - x_pos  <= 10 and new_head[0] - x_pos >= -10) and (new_head[1] - y_pos <= 10 and new_head[1] - x_pos  >= -10):
        snake_expend()
        food_event()
    else:
        snake.pop()
            
    snake.insert(0,new_head)
    

    screen.fill(background_colour)  # Vycisteni obrazovky
    for pos in snake:
        pygame.draw.rect(screen,text_colour,pygame.Rect(pos[0],pos[1],10,10))

    screen.blit(foodVar.render(food_text, True, text_colour1), (x_pos, y_pos))
    pygame.display.flip()
    pygame.time.delay(200)

pygame.quit()
