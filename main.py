import pygame
import os
import pymunk
import pymunk.pygame_util

from Resource import *

class Game:
    def __init__(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        pygame.display.set_caption("2025-payeondong")

        self.clock = pygame.time.Clock()
        self.screen = Screen(1600, 900) # 1600 : 900 이 기본값
        self.display = pygame.display.set_mode(self.screen.size)

        self.running = True

        # 충돌 타입
        self.PLAYER = 1
        self.GROUND = 2

        # Space
        self.space = pymunk.Space()
        self.space.gravity = (0, 1300)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.display)

        self.floor = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.floor.position = (0, self.screen.height - 64)
        self.floor_shape = pymunk.Segment(self.floor, (0, 0), (self.screen.width, 0), 1)
        self.floor_shape.collision_type = 2 # GROUND

        self.space.add(self.floor, self.floor_shape)
    
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.keys = pygame.key.get_pressed()

    def handleStates(self):
        state_method = {
            "game" : self.game,
        }

        def default():
            print("Unknown State")

        state_method.get(self.state, default)()

    # 메인 루프
    def game(self):
        self.handleEvents()

        self.display.fill((255, 255, 255))

        self.player.move(self.keys)

        self.space.debug_draw(self.draw_options)

        self.space.step(self.delta_time)

    # 엔진 구동
    def run(self):
        self.load()

        self.state = "game" # 임시 값
        while self.running:
            self.delta_time = self.clock.tick(60) / 1000.0

            self.handleStates()

            pygame.display.update()

    # 로딩
    def load(self):
        self.reset()

    # 리셋
    def reset(self):
        self.player = Player(self.screen, self.space)
        handler = self.space.on_collision(collision_type_a=self.PLAYER, collision_type_b=self.GROUND, begin=self.onGroundContact, data=self.player)

    # 지면 접촉 여부
    def onGroundContact(self, arbiter, space, data):
        self.player.allowJump()
        return True
        
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()