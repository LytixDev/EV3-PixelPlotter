import pygame

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
WIDTH = HEIGHT = 400 
ROWS = COLS = 40
PIXEL_SIZE = WIDTH // ROWS


def init_grid(rows, cols):
    # inititalize grid of all zeros, i.e all white
    grid = []
    
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(0)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pixel = WHITE if pixel == 0 else BLACK
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))


def get_pixel(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE
    return row, col


def draw(win, grid):
    draw_grid(win, grid)
    pygame.display.update()


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint")
    grid = init_grid(ROWS, COLS)
    
    drawing = True  # if false, it will draw white pixels i.e delete
    follow = False
    running = True
    clock = pygame.time.Clock()
    # main event loop
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if space is pressed reverse from drawing to ereasing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    drawing = not drawing

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col, row = get_pixel(pos)
                if drawing:
                    grid[col][row] = 1
                else:
                    grid[col][row] = 0

            if follow:
                x, y = pygame.mouse.get_pos()
                x = x // 10
                y = y // 10
                print(x, y)
                # to-do
                # move the printers arm and paper to follow the mouse
                # when the mouse is pressed, put the pen down, and vice versa
                # this would be able to draw N I C E lines

        draw(WIN, grid)
    
    # take a screenshot of the surface before exiting
    pygame.image.save(WIN, "drawn_picture.png")
    pygame.quit()


if __name__ == "__main__":
    main()
