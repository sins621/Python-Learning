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

food_pos = pg.Vector2(
    random.choice(grid["x"]) + grid_size / 2, random.choice(grid["y"]) + grid_size / 2
)
head_pos = pg.Vector2(screen_width / 2, screen_height / 2)
segment_pos = pg.Vector2(screen_width / 2 + grid_size, screen_height / 2 - grid_size)
segments = []
segments.append(segment_pos)

direction = pg.Vector2(grid_size, 0)
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
            elif event.key == pg.K_e:
                segment_pos = segments[-1]
                segments.append(segment_pos)

    screen.fill(black)
    # grid["x"] = horz = 16
    # grid["y"] = vert = 12

    pg.draw.circle(screen, "red", food_pos, grid_size / 2)

    for point in grid["x"]:
        #                          s x  y  e x  y
        # pg.draw.line(screen, "#", (0, 0), (0, 0))
        pg.draw.line(screen, white, (point, 0), (point, screen_height))

    for point in grid["y"]:
        pg.draw.line(screen, white, (0, point), (screen_width, point))

    if timer <= 0:
        for i in range(len(segments) - 1, 0, -1):
            segments[i] = segments[i - 1].copy()
        segments[0] += direction
        timer = speed

    for segment in segments:
        pg.draw.rect(screen, white, (segment.x, segment.y, grid_size, grid_size))

    pg.display.flip()
    dt = clock.tick(120) / 1000
    timer -= dt

pg.quit()
