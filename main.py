import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Pygame Window')

WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((600,400))

player_image = pygame.image.load('cat.png')
floor_image = pygame.image.load('check.png')
FLOOR_TILE = floor_image.get_width()
shelf_image = pygame.image.load('shelf.png')
SHELF_TILE = shelf_image.get_width()



game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','2','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]


moving_right = False
moving_left = False

player_location = [50,50]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())
test_rect = pygame.Rect(100, 100, 100,50)
while True:
    display.fill((146,244,255))

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(floor_image, (x * FLOOR_TILE, y * FLOOR_TILE))
            if tile == '2':
                display.blit(shelf_image, (x * SHELF_TILE, y * SHELF_TILE))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * SHELF_TILE, y * SHELF_TILE, SHELF_TILE, SHELF_TILE))

            x += 1

        y += 1

    display.blit(player_image,player_location)

    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum


    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen,(255,0,0),test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)

    for event in pygame.event.get():
        if event.type == QUIT:

            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf,(0,0))
    pygame.display.update()
    clock.tick(60)