import pygame
from .projectile import Projectile
from .tilemap import TILE_SIZE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, projectile_group, platforms):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.projectile_group = projectile_group
        self.platforms = platforms

        self.speed = 10
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_power = -14
        self.on_ground = False

    def update(self, keys):
        dx = 0
        if keys[pygame.K_a]:
            dx = -self.speed
        elif keys[pygame.K_d]:
            dx = self.speed

        # 1. X축 이동
        self.rect.x += dx

        # 2. X축 충돌 처리
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:  # 오른쪽 이동 중 충돌
                    self.rect.right = platform.rect.left
                elif dx < 0:  # 왼쪽 이동 중 충돌
                    self.rect.left = platform.rect.right

        # 3. 중력 적용
        self.velocity_y += self.gravity
        if self.velocity_y > 20:  # 최대 낙하 속도 제한 (옵션)
            self.velocity_y = 20
        self.rect.y += self.velocity_y

        # 4. Y축 충돌 처리
        self.on_ground = False
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # 낙하 중일 때 바닥 충돌
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # 점프 중일 때 천장 충돌
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

        # 5. 점프 처리
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_power

    def shoot(self, target_pos):
        projectile = Projectile(self.rect.center, target_pos)
        self.projectile_group.add(projectile)