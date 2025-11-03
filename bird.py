from pico2d import *
import game_framework
import random

sprites = (
    (0, 92), (50, 92), (100, 92), (150, 92), (200, 92),
    (0, 46), (50, 46), (100, 46), (150, 46), (200, 46),
    (0, 0), (50, 0), (100, 0), (150, 0),
)

# 빨간 비둘기???
# 새의 크기: 약 21cm(공백 제외 20픽셀)
# 새의 속도: 시속 70km/h
# 날개짓 속도: 초당 5회(총 14개의 이미지)

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 70.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1 / 5.0  # 한 번 푸드덕 하는데 걸리는 시간
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION # 초당 푸드덕 5회!
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = random.randint(100, 1500)
        self.y = random.randint(350, 500)
        self.face_dir = 1
        self.frame = random.randint(0, 14)

    def draw(self):
        frame_x, frame_y = sprites[int(self.frame)]
        if self.face_dir == 1:  # right
            self.image.clip_composite_draw(frame_x, frame_y, 50, 46, 0, '', self.x, self.y, 25, 23)
        else:  # face_dir == -1: # left
            self.image.clip_composite_draw(frame_x, frame_y, 50, 46, 0, 'h', self.x, self.y, 25, 23)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x < 25:
            self.face_dir = 1
        elif self.x > 1575:
            self.face_dir = -1