import pygame
from pygame.locals import *
import main
import random


def hard():

    # brick colors
    colors = [(130, 0, 0), (31, 138, 112), (0, 66, 90),
              (231, 177, 10), (246, 0, 197), (122, 68, 149)]

    # brick strengths
    strengths = [1, 2, 3, 4, 5, 6]
    score = 0  # define score variable
    pygame.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Breakout')

    # define font
    font = pygame.font.SysFont('Instrument Serif', 30)

    # define colours
    bg = (192, 192, 192)
    # block colours
    block_red = (130, 0, 0)
    block_green = (31, 138, 112)
    block_blue = (0, 66, 90)
    block_yellow = (231, 177, 10)
    block_magenta = (246, 0, 197)
    block_peach = (122, 68, 149)
    # paddle colours
    paddle_col = (45, 45, 45)
    paddle_outline = (24, 24, 24)

    # text colour
    text_col = (0, 0, 0)

    # define game variables
    cols = 13
    rows = 6
    clock = pygame.time.Clock()
    fps = 60
    live_ball = False
    game_over = 0

    # function for outputting text onto the screen

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # brick wall class

    class wall():
        def __init__(self):
            self.width = screen_width // cols
            self.height = 50

        def create_wall(self):
            self.blocks = []
            # define an empty list for an individual block
            block_individual = []
            for row in range(rows):
                # reset the block row list
                block_row = []
                # iterate through each column in that row
                for col in range(cols):
                    # generate x and y positions for each block and create a rectangle from that
                    block_x = col * self.width
                    block_y = row * self.height
                    rect = pygame.Rect(
                        block_x, block_y, self.width, self.height)

                # append the row to the full list of blocks
                    strength = random.choice(strengths)
                    color = colors[strength-1]
                    # create a list at this point to store the rect and data
                    block_individual = [rect, strength, color]
                    # append that individual block to the block row
                    block_row.append(block_individual)
                # append the row to the full list of blocks
                self.blocks.append(block_row)
                self.blocks.append(block_row)

        def draw_wall(self):
            for row in self.blocks:
                for block in row:
                    # assign a colour based on block strength
                    if block[1] == 6:
                        block_col = block_peach
                    elif block[1] == 5:
                        block_col = block_magenta
                    elif block[1] == 4:
                        block_col = block_yellow
                    elif block[1] == 3:
                        block_col = block_blue
                    elif block[1] == 2:
                        block_col = block_green
                    elif block[1] == 1:
                        block_col = block_red

                    pygame.draw.rect(screen, block_col, block[0])
                    pygame.draw.rect(screen, bg, (block[0]), 2)

    # paddle class

    class paddle():
        def __init__(self):
            self.reset()

        def move(self):
            # reset movement direction
            self.direction = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.direction = -1
            if key[pygame.K_RIGHT] and self.rect.right < screen_width:
                self.rect.x += self.speed
                self.direction = 1

        def draw(self):
            pygame.draw.rect(screen, paddle_col, self.rect)
            pygame.draw.rect(screen, paddle_outline, self.rect, 3)

#Paddle variables

        def reset(self):
            # define paddle variables
            self.height = 20
            self.width = int(screen_width / cols)
            self.x = int((screen_width / 2) - (self.width / 2))
            self.y = screen_height - (self.height * 2)
            self.speed = 10
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.direction = 0

    class Score:

        def __init__(self):
            self.score = 0

        def update_score(self):
            # if strength == 3:
            #     self.score += 10
            # elif strength == 2:
            #     self.score += 5
            # elif strength == 1:
            #     self.score += 1
            self.score += 100

        def get_score(self):
            return self.score

    score = Score()

    # ball class
    class game_ball():
        def __init__(self, x, y):
            self.reset(x, y)

        def move(self):

            # collision threshold
            collision_thresh = 5

            # start off with the assumption that the wall has been destroyed completely
            wall_destroyed = 1
            row_count = 0
            for row in wall.blocks:
                item_count = 0
                for item in row:
                    # check collision
                    if self.rect.colliderect(item[0]):
                        # check if collision was from above
                        if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                            self.speed_y *= -1
                        # check if collision was from below
                        if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                            self.speed_y *= -1
                        # check if collision was from left
                        if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                            self.speed_x *= -1
                        # check if collision was from right
                        if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                            self.speed_x *= -1
                        # reduce the block's strength by doing damage to it
                        if wall.blocks[row_count][item_count][1] > 1:
                            wall.blocks[row_count][item_count][1] -= 1
                            score.update_score()
                        else:
                            wall.blocks[row_count][item_count][0] = (
                                0, 0, 0, 0)
                            score.update_score()
                            # if wall_destroyed:
                            # pygame.mixer.Sound("path/to/total/destruction/sound.wav").play()

                            # score += 1  # increment score when a block is destroyed
                    # check if block still exists, in whcih case the wall is not destroyed
                    if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                        wall_destroyed = 0
                    # increase item counter
                    item_count += 1
                # increase row counter
                row_count += 1
            # after iterating through all the blocks, check if the wall is destroyed
            if wall_destroyed == 1:
                self.game_over = 1

            # check for collision with walls
            if self.rect.left < 0 or self.rect.right > screen_width:
                self.speed_x *= -1

            # check for collision with top and bottom of the screen
            if self.rect.top < 0:
                self.speed_y *= -1
            if self.rect.bottom > screen_height:
                self.game_over = -1

            # look for collission with paddle
            if self.rect.colliderect(player_paddle):
                # check if colliding from the top
                if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                    self.speed_y *= -1
                    self.speed_x += player_paddle.direction
                    if self.speed_x > self.speed_max:
                        self.speed_x = self.speed_max
                    elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                        self.speed_x = -self.speed_max
                else:
                    self.speed_x *= -1

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            return self.game_over

        def draw(self):
            pygame.draw.circle(screen, paddle_col, (self.rect.x +
                                                    self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
            pygame.draw.circle(screen, paddle_outline, (self.rect.x +
                                                        self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)

        def reset(self, x, y):
            self.ball_rad = 10
            self.x = x - self.ball_rad
            self.y = y
            self.rect = pygame.Rect(
                self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
            self.speed_x = 4
            self.speed_y = -4
            self.speed_max = 5
            self.game_over = 0

    # create a wall
    wall = wall()
    wall.create_wall()

    # create paddle
    player_paddle = paddle()

    # create ball
    ball = game_ball(player_paddle.x + (player_paddle.width // 2),
                     player_paddle.y - player_paddle.height)

    paused = False

    run = True
    while run:

        clock.tick(fps)

        if not paused:
            screen.fill((192, 192, 192))
            # main.main_menu()
            # drawing objects
            wall.draw_wall()
            player_paddle.draw()
            ball.draw()

        # draw all objects
        wall.draw_wall()
        player_paddle.draw()
        ball.draw()

        if live_ball:
            # draw paddle
            player_paddle.move()
            # draw ball
            game_over = ball.move()
            if game_over != 0:
                live_ball = False

        # print player instructions
        if not live_ball:
            if game_over == 0:
                draw_text("Press any key to start", font, text_col, 250, 300)
            elif game_over == 1:
                draw_text("You Won!", font, text_col, 350, 300)
                draw_text("Press any key to restart", font, text_col, 280, 350)
            elif game_over == -1:
                draw_text("You Lost!", font, text_col, 350, 300)
                draw_text("Press any key to restart", font, text_col, 280, 350)
                draw_text("Your score is %s " % str(
                    score.get_score()), font, text_col, 280, 380)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # draw_text(score, font, text_col, 20, 20)
            if event.type == pygame.KEYDOWN and live_ball == False:
                live_ball = True
                ball.reset(player_paddle.x + (player_paddle.width // 2),
                           player_paddle.y - player_paddle.height)
                # reset score to 0
                # score.update_score(0)
            elif event.type == pygame.KEYDOWN and game_over != 0:
                # reset game when any key is pressed after game over
                live_ball = True
                ball.reset(player_paddle.x + (player_paddle.width // 2),
                           player_paddle.y - player_paddle.height)
                player_paddle.reset()
                wall.create_wall()

                # reset score to 0
                score.update_score(0)

        pygame.display.update()

    pygame.quit()


def easy():
    pygame.init()
    pygame.mixer.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Breakout')

    # initial colors
    bg = (234, 234, 234)

    # block/brick colors
    block_red = (242, 85, 96)
    block_green = (0, 255, 0)
    block_blue = (0, 0, 255)

    # paddle colors
    paddle_col = (65, 65, 65)
    paddle_outline = (0, 0, 0)

    # text colors
    text_col = (0, 0, 0)

    # define font
    font = pygame.font.SysFont('Constantia', 30)

    # define game variables
    cols = 6
    rows = 6
    clock = pygame.time.Clock()
    fps = 60
    live_ball = False
    game_over = 0

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # load sound effects
    # destory_sound = pygame.mixer.Sound(
        # "C:\\Users\\DELL\\Desktop\\Brick-Breakout\\Breakout\\pause_sound.wav")

    # brick wall class

    class wall():
        def __init__(self):
            self.width = screen_width // cols
            self.height = 50

        def create_wall(self):
            self.blocks = []
            # define empty list for an individual block
            block_individual = []
            for row in range(rows):
                # reset the block row list
                block_row = []
                # iterate through each column in that row
                for col in range(cols):
                    # generate x and y positions for each block and create a rectangle from that
                    block_x = col * self.width
                    block_y = row * self.height
                    rect = pygame.Rect(
                        block_x, block_y, self.width, self.height)
                    # assign block strength based on row
                    if row < 2:
                        strength = 3
                    elif row < 4:
                        strength = 2
                    elif row < 6:
                        strength = 1
                    # create a list at this point to store the rect and color data
                    block_individual = [rect, strength]
                    # append that individual block to the block row list
                    block_row.append(block_individual)
                # append the row to the full list of blocks
                self.blocks.append(block_row)

        def draw_wall(self):
            for row in self.blocks:
                for block in row:
                    # assign a color based on block strength
                    if block[1] == 3:
                        block_color = block_blue
                    elif block[1] == 2:
                        block_color = block_green
                    elif block[1] == 1:
                        block_color = block_red
                    pygame.draw.rect(screen, block_color, block[0])
                    pygame.draw.rect(screen, bg, (block[0]), 2)

    # paddle class

    class paddle():
        def __init__(self):
            self.reset()

        def move(self):
            # reset movement direction
            self.direction = 0
            # check key presses
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.direction = -1
            if key[pygame.K_RIGHT] and self.rect.right < screen_width:
                self.rect.x += self.speed
                self.direction = 1

        def draw(self):
            # draw paddle
            pygame.draw.rect(screen, paddle_col, self.rect)
            pygame.draw.rect(screen, paddle_outline, self.rect, 3)

        def reset(self):
            self.height = 20
            self.width = int(screen_width // cols)
            self.x = int((screen_width/2) - (self.width/2))
            self.y = screen_height - (self.height * 2)
            self.speed = 10
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.direction = 0

    class Score:

        def __init__(self):
            self.score = 0

        def update_score(self):
            self.score += 100

        def get_score(self):
            return self.score

    score = Score()
    # ball  class
    # print(score.get_score())

    class game_ball():
        def __init__(self, x, y):
            self.reset(x, y)

        def move(self):

            # collision threshold
            collision_thresh = 5

            # start off with the assumption that the wall has been destroyed
            wall_destroyed = 1
            row_count = 0
            for row in wall.blocks:
                item_count = 0
                for item in row:
                    # check collision
                    if self.rect.colliderect(item[0]):
                        # check if collision was from above
                        if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                            self.speed_y *= -1
                        # check if collision was from below
                        if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                            self.speed_y *= -1
                        # check if collision was from left
                        if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                            self.speed_x *= -1
                        # check if collision was from right
                        if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                            self.speed_x *= -1
                        # reduce the block's strength
                        if wall.blocks[row_count][item_count][1] > 1:
                            wall.blocks[row_count][item_count][1] -= 1
                            score.update_score()
                            # play sound effect
                            # destroy_sound.play()
                        else:
                            wall.blocks[row_count][item_count][0] = (
                                0, 0, 0, 0)
                            score.update_score()
                            # if wall_destroyed:
                            # pygame.mixer.Sound("path/to/total/destruction/sound.wav").play()

                    # check if block still exists
                    if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                        wall_destroyed = 0
                    # increase item count
                    item_count += 1
                # increase row count
                row_count += 1

            # after iterating through all blocks, check if wall is destroyed
            if wall_destroyed == 1:
                self.game_over = 1

            # collision check with walls
            if self.rect.left < 0 or self.rect.right > screen_width:
                self.speed_x *= -1  # reverse the x direction i.e, change the direction with the walls
            if self.rect.top < 0:
                # reverse the y direction i.e, change the direction with the top of the screen
                self.speed_y *= -1
            if self.rect.bottom > screen_height:
                self.game_over = -1

            # collision with the paddle

            # if self.rect.colliderect(player_paddle.rect):
            #     # collision from the top
            #     if abs(self.rect.bottom - player_paddle.rect.top) < 10 and self.speed_y > 0:
            #         self.speed_y *= -1
            #     # collision from the left
            #     elif abs(self.rect.right - player_paddle.rect.left) < 10 and self.speed_x > 0:
            #         self.speed_x  *= -1
            #     # collision from the right
            #     elif abs(self.rect.left - player_paddle.rect.right) < 10 and self.speed_x < 0:
            #         self.speed_x *= -1
            #     # collision from the bottom
            #     elif abs(self.rect.top - player_paddle.rect.bottom) < 10 and self.speed_y < 0:
            #         self.speed_y *= -1

            if self.rect.colliderect(player_paddle):
                # check if colliding from the top
                if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                    self.speed_y *= -1
                    self.speed_x += player_paddle.direction
                    if self.speed_x > self.speedmax:
                        self.speed_x = self.speedmax
                elif self.speed_x < 0 and self.speed_x < self.speedmax:
                    self.speed_x = self.speedmax
                else:
                    self.speed_x *= -1

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            return self.game_over

        def draw(self):
            pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_radius,
                                                    self.rect.y + self.ball_radius), self.ball_radius)
            pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_radius,
                                                        self.rect.y + self.ball_radius), self.ball_radius, 3)

        def reset(self, x, y):
            self.ball_radius = 10
            self.x = x - self.ball_radius
            self.y = y
            self.rect = pygame.Rect(
                self.x, self.y, self.ball_radius * 2, self.ball_radius * 2)
            self.speed_x = 4
            self.speed_y = -4
            self.speedmax = 5
            self.game_over = 0

    # create a wall
    wall = wall()
    wall.create_wall()

    # create paddle
    player_paddle = paddle()

    # create ball
    ball = game_ball(player_paddle.x + (player_paddle.width // 2),
                     player_paddle.y - player_paddle.height)

    paused = False

    # score measures

    run = True
    while run:

        clock.tick(fps)
        # clock.stopped = False

        if not paused:
            screen.fill(bg)
            # main.main_menu()
            # drawing objects
            wall.draw_wall()
            player_paddle.draw()
            ball.draw()

        if live_ball:
            player_paddle.move()
            game_over = ball.move()
            if game_over != 0:
                live_ball = False
                # final_score = score.get_score()

        # instructions
        if not live_ball:
            if game_over == 0:
                draw_text("Press any key to start", font, text_col, 250, 300)
            elif game_over == 1:
                draw_text("You Won!", font, text_col, 350, 300)
                draw_text("Press any key to restart", font, text_col, 280, 350)
            elif game_over == -1:
                draw_text("You Lost!", font, text_col, 350, 300)
                draw_text("Press any key to restart", font, text_col, 280, 350)
                draw_text("Your score is %s " % str(
                    score.get_score()), font, text_col, 280, 380)

                # display final score
                # draw_text("Final Score: " + str(final_score),
                #           font, text_col, 280, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # draw_text(score, font, text_col, 20, 20)
            if event.type == pygame.KEYDOWN and live_ball == False:
                live_ball = True
                ball.reset(player_paddle.x + (player_paddle.width // 2),
                           player_paddle.y - player_paddle.height)
                # reset score to 0
                # score.update_score(0)
            elif event.type == pygame.KEYDOWN and game_over != 0:
                # reset game when any key is pressed after game over
                live_ball = True
                ball.reset(player_paddle.x + (player_paddle.width // 2),
                           player_paddle.y - player_paddle.height)
                player_paddle.reset()
                wall.create_wall()

                # reset score to 0
                score.update_score(0)

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # paused = not paused

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            #     paused = not paused

            # pause the game loop
            # while paused:
            #     for event in pygame.event.get():
            #         if event.type == pygame.KEYDOWN:
            #             if event.key == pygame.K_ESCAPE:
            #                 paused = not paused
            #                 break

        # pygame.display.update()

        pygame.display.update()

    pygame.quit()


def main():

    hard()
    #easy()


if __name__ == '__main__':
    main()
