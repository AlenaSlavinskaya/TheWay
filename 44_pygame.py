import pygame
import random

pygame.init()

blue = (0, 0, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
black = (0, 0, 0)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Snake')

game_over = False

x1 = 300
y1 = 400

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [10, 0])

def Your_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

snake_list = []
Length_of_snake = 1

foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, 500 - snake_block) / 10.0) * 10.0

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)
    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)
    if len(snake_list) > Length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_Head:
            game_over = True

    Your_snake(snake_block, snake_list)
    Your_score(Length_of_snake - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, 500 - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    clock.tick(20)

pygame.quit()
quit()