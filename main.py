import pygame
from Resource import *

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("플랫포머 with 카메라 스크롤")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# 타일맵 로드
tilemap_data = load_tilemap("tilemap.txt")

map_width = len(tilemap_data[0]) * TILE_SIZE
map_height = len(tilemap_data) * TILE_SIZE

for row_index, row in enumerate(tilemap_data):
    for col_index, tile in enumerate(row):
        if tile == 1:
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            platform = Platform(x, y)
            platforms.add(platform)
            all_sprites.add(platform)

player = Player(100, 100, projectiles, platforms)
all_sprites.add(player)

camera = Camera(map_width, map_height)

running = True
while running:
    clock.tick(60)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shoot(event.pos)

    keys = pygame.key.get_pressed()
    player.update(keys)

    projectiles.update()
    camera.update(player)

    # 화면에 스프라이트 그리기 (카메라 좌표 적용)
    for sprite in all_sprites:
        cam_pos = camera.apply(sprite)
        print(f"Sprite {sprite} original: {sprite.rect.topleft}, after camera: {cam_pos}")
        screen.blit(sprite.image, cam_pos)

    for projectile in projectiles:
        screen.blit(projectile.image, camera.apply(projectile))

    pygame.display.flip()

pygame.quit()