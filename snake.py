# make a snake game


import pygame
import sys
import random
import time


# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# initialize pygame
pygame.init()


# create the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# set the title of the window
pygame.display.set_caption("Snake Game")


# create a game clock
clock = pygame.time.Clock()


# create a game font
font = pygame.font.SysFont(None, 25)


# create a game score
score = 0


# create a game speed
speed = 1


# create a game over flag
game_over = False


# create a game over text
game_over_text = font.render("Game Over", True, red)


# create a game over text position
game_over_text_position = game_over_text.get_rect()
game_over_text_position.center = (400, 300)




# create a snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]


# create a food
food_position = [random.randrange(1, screen_width/10)*10, random.randrange(1, screen_height/10)*10]
food_spawn = True


# create a direction
direction = "RIGHT"
change_to = direction


# create a function to change the direction
def change_direction(event):
    global change_to
    if event.key == pygame.K_LEFT and direction != "RIGHT":
        change_to = "LEFT"
    if event.key == pygame.K_RIGHT and direction != "LEFT":
        change_to = "RIGHT"
    if event.key == pygame.K_UP and direction != "DOWN":
        change_to = "UP"
    if event.key == pygame.K_DOWN and direction != "UP":
        change_to = "DOWN"


# create a function to spawn the food
def spawn_food():
    global food_spawn
    global food_position
    food_spawn = True
    food_position = [random.randrange(1, screen_width/10)*10, random.randrange(1, screen_height/10)*10]


# create a function to check if the snake has eaten the food
def check_eat():
    global score
    global food_spawn
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        spawn_food()


# create a function to check if the snake has hit the wall
def check_hit_wall():
    global game_over
    if snake_position[0] == -10 or snake_position[0] == screen_width or snake_position[1] == -10 or snake_position[1] == screen_height:
        game_over = True


# create a function to check if the snake has hit itself
def check_hit_self():
    global game_over
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True


# create a function to move the snake
def move():
    global direction
    global change_to
    direction = change_to

    # move the head in the direction of the direction variable
    if direction == "RIGHT":
        snake_position[0] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10

    # move the body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
    else:
        snake_body.pop()


# create a function to draw the snake
def draw_snake():
    for block in snake_body:
        pygame.draw.rect(screen, green, [block[0], block[1], 10, 10])


# create a function to draw the food
def draw_food():
    pygame.draw.rect(screen, blue, [food_position[0], food_position[1], 10, 10])


# create a function to draw the score
def draw_score():
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [10, 10])


# create a function to draw the game over text
def draw_game_over():
    screen.blit(game_over_text, game_over_text_position)


# create a function to draw the screen
def draw_screen():
    screen.fill(white)
    draw_snake()
    draw_food()
    draw_score()
    pygame.display.update()


# create a function to check if the game is over
def check_game_over():
    global game_over
    if game_over:
        pygame.quit()
        sys.exit()


# create a function to reset the game
def reset_game():
    global direction
    global change_to
    global snake_position
    global snake_body
    global score
    global speed
    global food_spawn

    direction = "RIGHT"
    change_to = direction
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    score = 0
    speed = 1
    food_spawn = True


# create a function to start the game
def start_game():
    global game_over
    global speed
    game_over = False
    reset_game()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                change_direction(event)

        check_game_over()
        check_eat()
        check_hit_wall()
        check_hit_self()
        move()
        draw_screen()

        if score < 4:
            speed = 5 
            clock.tick(speed)
        else:
            speed = score * 1.5
            clock.tick(speed)


# start the game
start_game()


# close the game
pygame.quit()
sys.exit()


# end of the program
