from pico2d import *
import game_framework

sprites = (
    (0, 92), (50, 92), (100, 92), (150, 92), (200, 92),
    (0, 46), (50, 46), (100, 46), (150, 46), (200, 46),
    (0, 0), (50, 0), (100, 0), (150, 0),
)

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 1 / 10.0  # 한 번 푸드덕 하는데 걸리는 시간
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION # 초당 푸드덕 15회!
FRAMES_PER_ACTION = 10

class Bird:
    image = None

    def __init__(self, x = 400, y = 400):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.face_dir = 1
        self.frame = 0

    def draw(self):
        frame_x, frame_y = sprites[int(self.frame)]
        if self.face_dir == 1:  # right
            self.image.clip_composite_draw(frame_x, frame_y, 50, 46, 0, '', self.x, self.y, 50, 46)
        else:  # face_dir == -1: # left
            self.image.clip_composite_draw(frame_x, frame_y, 50, 46, 0, 'h', self.x, self.y, 50, 46)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x < 25:
            self.face_dir = 1
        elif self.x > 1575:
            self.face_dir = -1