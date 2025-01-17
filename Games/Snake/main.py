import random

import pygame as pg

pg.init()
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Snake")
grid_size = 40
clock = pg.time.Clock()
running = True
black = "#282828"
white = "#ebdbb2"

grid = {
    "x": [i - 1 for i in range(screen_width) if i % grid_size == 1],
    "y": [i - 1 for i in range(screen_height) if i % grid_size == 1],
}

speed = 0.5

# grid
# (640x480)/40
# 16x12
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - -

food_pos = pg.Vector2(random.choice(grid["x"]), random.choice(grid["y"]))
head_pos = pg.Vector2(screen_width / 2, screen_height / 2)
direction = pg.Vector2(0, 0)

timer = speed

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                direction = (-grid_size, 0)
            elif event.key == pg.K_d:
                direction = (grid_size, 0)
            elif event.key == pg.K_s:
                direction = (0, grid_size)
            elif event.key == pg.K_w:
                direction = (0, -grid_size)

    screen.fill(black)
    # grid[0] = horz = 16
    # grid[1] = vert = 12
    pg.draw.rect(screen, "red", (food_pos.x, food_pos.y, grid_size, grid_size))
    pg.draw.rect(screen, white, (head_pos.x, head_pos.y, grid_size, grid_size))

    for point in grid["x"]:
        #                          s x  y  e x  y
        # pg.draw.line(screen, "#", (0, 0), (0, 0))
        pg.draw.line(screen, white, (point, 0), (point, screen_height))

    for point in grid["y"]:
        pg.draw.line(screen, white, (0, point), (screen_width, point))

    if timer <= 0:
        head_pos += direction
        timer = speed

    pg.display.flip()
    dt = clock.tick(120) / 1000
    timer -= dt

pg.quit()
