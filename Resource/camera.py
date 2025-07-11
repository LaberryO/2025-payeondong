import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, target):
        # 스프라이트 등 위치 보정용 (카메라 좌표 기준으로)
        return target.rect.move(self.camera_rect.topleft)

    def update(self, target):
        # 카메라가 플레이어 중심에 위치하도록 계산
        x = -target.rect.centerx + 1600 // 2
        y = -target.rect.centery + 800 // 2

        self.camera_rect = pygame.Rect(x, y, self.width, self.height)
