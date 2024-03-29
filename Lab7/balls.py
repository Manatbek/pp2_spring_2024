import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()
fs = 60

RED = (255, 0, 0)
rad = 25
x, y = 600, 450     
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20
        
    if x < 25:
        x = 25
    if x > 1175:
        x = 1175
    if y < 25:
        y = 25
    if y > 875:
        y = 875
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, RED, (x, y), rad)
    
    pygame.display.flip()
    clock.tick(fs)