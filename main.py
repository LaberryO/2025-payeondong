import pygame
from Resource import *

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("무한 스크롤 플랫포머")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
platforms = pygame.sprite.Group()
platform_pool = []  # 플랫폼 재사용 리스트

tilemap_data = load_tilemap("tilemap.txt")
map_width = len(tilemap_data[0]) * TILE_SIZE
map_height = len(tilemap_data) * TILE_SIZE

player = Player(1500, 100, projectiles, platforms)
all_sprites.add(player)

camera = Camera(map_width, map_height)

def update_visible_platforms(platform_group, platform_pool, tilemap, camera):
    platform_group.empty()

    screen_width, screen_height = 1600, 800
    cols = len(tilemap[0])
    rows = len(tilemap)

    cam_x = -camera.camera_rect.x
    cam_y = -camera.camera_rect.y

    # 정수 타일 위치
    tile_offset_x = cam_x // TILE_SIZE
    tile_offset_y = cam_y // TILE_SIZE

    tiles_x = (screen_width // TILE_SIZE) + 6
    tiles_y = (screen_height // TILE_SIZE) + 2

    i = 0
    for row in range(tiles_y):
        for col in range(-2, tiles_x):  # 💡 왼쪽까지 타일 확보하기 위해 col을 -2부터 시작
            map_x = (tile_offset_x + col) % cols
            map_y = tile_offset_y + row

            if 0 <= map_y < rows and tilemap[map_y][map_x] == 1:
                if i < len(platform_pool):
                    platform = platform_pool[i]
                else:
                    platform = Platform()
                    platform_pool.append(platform)

                # 정확한 월드 좌표
                draw_x = (tile_offset_x + col) * TILE_SIZE
                draw_y = (tile_offset_y + row) * TILE_SIZE
                platform.set_position(draw_x, draw_y)
                platform_group.add(platform)
                i += 1

running = True
while running:
    clock.tick(60)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shoot(pygame.mouse.get_pos())

    keys = pygame.key.get_pressed()
    player.update(keys)
    projectiles.update()
    camera.update(player)

    # main.py 루프 내에서
    update_visible_platforms(platforms, platform_pool, tilemap_data, camera)


    for platform in platforms:
        screen.blit(platform.image, camera.apply(platform))
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))
    for projectile in projectiles:
        screen.blit(projectile.image, camera.apply(projectile))

    pygame.display.flip()

pygame.quit()
