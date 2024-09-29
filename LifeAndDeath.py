import pygame
import sys
from Grid import Grid

def DrawPixel(coordinate):
   pygame.draw.rect(screen, WHITE, (coordinate[0]*PIXEL_SIZE,coordinate[1]*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def ToggleCell(x,y):
    x = x // PIXEL_SIZE
    y = y // PIXEL_SIZE
    grid.ToggleCell(grid.GetCellAtPos(x,y))

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 80
PIXEL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Grid")

# Create Grid
grid = Grid(GRID_SIZE,GRID_SIZE)

# Timer variables
timer_event = pygame.USEREVENT + 1  # Custom event
pygame.time.set_timer(timer_event, 100)  # Set the timer to 500 milliseconds (0.5 seconds)


isSimulating = False
WindowRunning = True

print("Mouse1 to toggle a cell \nSpacebar to start/stop simulation")

# Main loop
while WindowRunning:
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            WindowRunning = False
        # Timer event
        if event.type == timer_event and isSimulating:
            grid = grid.NextIteration()

        # Mousebutton 1 pressed, toggle cell at mouse pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                ToggleCell(mouse_x, mouse_y)

        # pause or play simulation
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            isSimulating = not isSimulating
        
        # manually get next iteration 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            rid = grid.NextIteration()
                
    
    # Clear the screen
    screen.fill(BLACK)

    # Draw The alive cells
    gridList = grid.GetGrid()
    counter = 0
    for x in range(0, GRID_SIZE):
        for y in range(0, GRID_SIZE):
            counter+=1
            if(gridList[counter-1]):
                DrawPixel((x,y))
    

    # Draw the lines of the grid
    for x in range(0, WIDTH, PIXEL_SIZE):
        pygame.draw.line(screen, (50,50,50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, PIXEL_SIZE):
        pygame.draw.line(screen, (50,50,50), (0, y), (WIDTH, y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

 
