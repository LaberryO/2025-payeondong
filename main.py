import os, pygame, sys;

from Resource.Data.Screen import Screen;
from Resource.Data.Color import Color;

from Resource.System.PathLoader import imageLoader;

class Game:
    def __init__(self):
        # main.py를 기준으로 경로 설정
        os.chdir(os.path.dirname(os.path.abspath(__file__)));
        
        # 기초 설정
        pygame.init();
        pygame.display.set_caption("2025-payeondong");

        # 설정용 변수
        self.clock = pygame.time.Clock();
        self.screen = pygame.display.set_mode(Screen().getSize());
        self.running = True;
    
        # 이미지
        self.tempImage = pygame.image.load(imageLoader("temp.png")); # 임시 이미지

    # 리셋
    def reset(self):
        pass;

    # 이벤트 처리
    def handleEvents(self):
        # 창 닫기
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                self.running = False;
                pygame.quit();
                sys.exit();

    # 메인 루프
    def update(self, deltaTime):
        self.screen.blit(self.tempImage, (
            Screen().getCenterX() - self.tempImage.get_width() / 2,
            Screen().getCenterY() - self.tempImage.get_height() / 2
        ));

    # 물리적 루프
    def run(self):
        while self.running:
            # DeltaTime (델타 타임)
            deltaTime = self.clock.tick(60) / 1000.0;

            self.handleEvents();

            self.screen.fill(Color().white());
            self.update(deltaTime);

            pygame.display.update();

# main.py가 직접 실행되어야 게임 루프 시작
if __name__ == "__main__":
    game = Game();
    game.run();