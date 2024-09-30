import pygame

banyakRect = 500
# Initializing Pygame
pygame.init()
# clock = pygame.time.Clock()
 
# Initializing surface
screen = pygame.display.set_mode((400,300))
max_width = 400
max_height = 300
scroll_x = 0
scroll_y = 0

# Initializing Color
color = (0,0,255)

running = True

initX = 10
initY = 10
width = 40
height = 40

created = 0

rect_surface = pygame.Surface((50000, 50000))
rect_surface.fill((255, 255, 255))
font = pygame.font.SysFont('Arial', 12)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Continuous scrolling based on mouse movement
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # Left mouse button pressed
                scroll_x += event.rel[0]
                scroll_y += event.rel[1]
                
    screen.blit(font.render('Hello!', True, (255,0,0)), (200, 100))
    if (created < banyakRect):
        for i in range(banyakRect):       
            pygame.draw.rect(rect_surface, color, (initX, initY, width, height), 2)
            
            created += 1

            text_surface = font.render('{}'.format(created), True, color)
            rect_surface.blit(text_surface, (initX + width + 5, initY + height - 20))

            initX += width
            initY += height
            print(created)

    screen.blit(rect_surface, (-scroll_x, -scroll_y))
    pygame.display.update()
# Drawing Rectangle
