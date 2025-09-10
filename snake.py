import pygame
import random
import sys

pygame.init()

x_pos = 250
y_pos = 250
snake = [[250, 250]]

direction = 0

background_colour = (0, 0, 0)
text_colour = (255, 255, 255)
text_colour1 = (255, 0, 0)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SNAKE")
screen.fill(background_colour)


foodVar = pygame.font.SysFont("Arial", 20)
food_text = "■"

clock = pygame.time.Clock()


def getDirection() -> int:
    global direction
    return direction

def food_event():
    global x_pos, y_pos
    global snake
    while True:
        x_pos = random.randrange(0, 500, 10)
        y_pos = random.randrange(0, 500, 10)
        if [x_pos, y_pos] not in snake:
            break

def snake_expend():
    global snake, snake_count
    snake.append(snake[-1])

food_event()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 2
            elif event.key == pygame.K_DOWN and direction != 2:
                direction = 3
            elif event.key == pygame.K_LEFT and direction != 1:
                direction = 0
            elif event.key == pygame.K_RIGHT and direction != 0:
                direction = 1
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

    if new_head[0] < 0 or new_head[0] >= 500 or new_head[1] < 0 or new_head[1] >= 500:
        print("LOG: you crashed into wall.")
        running = False

    if new_head in snake:
        print("LOG: you crashed into itself.")
        running = False

    if new_head[0] == x_pos and new_head[1] == y_pos:
        snake_expend()
        food_event()
    else:
        snake.pop()

    snake.insert(0, new_head)
    
    clock.tick(5)

    screen.fill(background_colour)
    for pos in snake:
        pygame.draw.rect(screen, text_colour, pygame.Rect(pos[0], pos[1], 10, 10))


    screen.blit(foodVar.render(food_text, True, text_colour1), (x_pos, y_pos))
    pygame.display.flip()


pygame.quit()
