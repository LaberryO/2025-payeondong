import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, target):
        cam_x, cam_y = self.camera_rect.topleft
        # move 대신 직접 튜플 좌표 계산 후 반환
        return (target.rect.x + cam_x, target.rect.y + cam_y)


    def update(self, target):
        x = -target.rect.centerx + 1600 // 2
        y = -target.rect.centery + 800 // 2

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - 1600), x)
        y = max(-(self.height - 800), y)

        self.camera_rect = pygame.Rect(x, y, self.width, self.height)
