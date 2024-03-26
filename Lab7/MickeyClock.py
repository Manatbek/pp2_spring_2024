import pygame
import sys
import datetime


pygame.init()
screen = pygame.displ.set_mode((1200, 900))
clock = pygame.time.Clock()

mickey = pygame.image.load("mickey.png")
hour_hand = pygame.image.load("hour.png")
minute_hand = pygame.image.load("min.png")

mickey_rect = mickey.get_rect(center=(600, 450))
hour_hand_rect = hour_hand.get_rect(center=mickey_rect.center)
minute_hand_rect = minute_hand.get_rect(center=mickey_rect.center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.datetime.now() 
    hour_angle = (current_time.minute * 6) - 90
    minute_angle = (current_time.second * 6) - 90

    # Rotate the hands
    rotated_hour_hand = pygame.transform.rotate(hour_hand, -hour_angle)
    rotated_minute_hand = pygame.transform.rotate(minute_hand, -minute_angle)
    hour_hand_rect = rotated_hour_hand.get_rect(center=mickey_rect.center)
    minute_hand_rect = rotated_minute_hand.get_rect(center=mickey_rect.center)

    screen.fill((255, 255, 255))
    screen.blit(mickey, mickey_rect)
    screen.blit(rotated_hour_hand, hour_hand_rect)
    screen.blit(rotated_minute_hand, minute_hand_rect)

    pygame.displ.update()
    clock.tick(60)