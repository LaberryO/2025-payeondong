import pymunk
import pymunk.pygame_util
import pygame

class Player:
    def __init__(self, screen, space):
        self.width = 100
        self.height = 100
        self.x = screen.center_x - self.width // 2
        self.y = screen.center_y // 2 - 25
        self.speed = 800
        self.can_jump = False

        self.body = pymunk.Body(1,  pymunk.moment_for_box(1, (self.width, self.height)))
        self.body.position = (self.x, self.y)
        self.shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
        self.shape.collision_type = 1  # PLAYER
        self.shape.friction = 1.0
        space.add(self.body, self.shape)

    def move(self, keys):
        vx = 0
        if keys[pygame.K_LEFT]:
            vx = -self.speed
        elif keys[pygame.K_RIGHT]:
            vx = self.speed
        self.body.velocity = (vx, self.body.velocity.y)

        if keys[pygame.K_SPACE] and self.can_jump:
            self.body.apply_impulse_at_local_point((0, -self.height*5))
            self.can_jump = False  # 점프하면 바로 False로 막음
    
    def allowJump(self):
        self.can_jump = True  # 충돌 시 외부에서 True로 설정