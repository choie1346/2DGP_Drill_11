import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_collision_pair('grass:ball', grass, None)

    boy = Boy()
    game_world.add_object(boy, 1)
    game_world.add_collision_pair('zombie:boy', None, boy)

    # 바닥에 공을 배치
    global balls
    balls = [Ball(random.randint(300, 1600), 60, 0) for i in range(20)]
    for b in balls:
        game_world.add_object(b, 1)

    # 충돌 검사가 필요한 페어 등록
    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)


    global zombies
    zombies = [Zombie() for i in range(4)]
    for zombie in zombies:
        game_world.add_object(zombie, 1)
        game_world.add_collision_pair('zombie:ball', zombie, None)
        game_world.add_collision_pair('zombie:boy', zombie, None)

def update():
    game_world.update()
    # 게임 내 모든 객체가 업데이트가 끝났기 떄문에 충돌검사를 해야함.
    #for ball in balls.copy():
    #    if game_world.collide(boy, ball):
    #        print("COLLISION boy:ball")
    #        boy.ball_count += 1
    #        game_world.remove_object(ball)
    #        balls.remove(ball)
    game_world.handle_collision()



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

