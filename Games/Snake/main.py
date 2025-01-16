# Example file showing a basic pygame "game loop"
import pygame as pg

# pg setup
pg.init()
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))
grid_size = 40
clock = pg.time.Clock()
running = True
grid = [
    [i - 1 for i in range(screen_width + grid_size) if i % grid_size == 1],
    [i - 1 for i in range(screen_height + grid_size) if i % grid_size == 1],
]

print(grid)

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    dt = clock.tick(120) / 1000  # limits FPS to 60

pg.quit()
