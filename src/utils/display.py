from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg
from src.algorithms.sort import Sort
import time, sys


class Display():

    def __init__(self, algorithm, width=800, height=600, bg_color=(255, 255, 255), data_color=(80, 0, 255), first_color=(0,255,0), second_color=(255,0,0)):
        if not isinstance(algorithm, (Sort, )):
            raise ValueError('algorithm must be derived from Sort')
        if not width:
            raise ValueError('width must be a greater than 0 ')
        if not height:
            raise ValueError('height must be a greater than 0 ')
        self.__algo=algorithm
        self.__width=width
        self.__height=height
        self.__bg_color=bg_color
        self.__data_color=data_color
        self.__first_color=first_color
        self.__second_color=second_color
        self.__speed=0.05
        self.__on()
        
    def __on(self, ):
        pg.init()
        self.__font = pg.font.SysFont('Arial', 13)
        self.__display=pg.display.set_mode((self.__width, self.__height))
        self.__running=True
        self.__start_time=time.time()
        self.__algo.sort(display=self)
        end_time=time.time()-self.__start_time
        while self.__running:
            if self.__close():
                break

    def update(self, first=None, second=None):
        if not self.__running:
            return
        data=self.__algo.get_data()
        pg.display.set_caption('{} [{}] [{}] [Speed {}%]'.format(self.__algo.get_name(), time.strftime('%H:%M:%S', time.gmtime(time.time()-self.__start_time)), len(data), 100-round(round(self.__speed, 2)*100/0.30), 2))
        self.__display.fill(self.__bg_color)
        rect_width = self.__width/(len(data))
        for i in range(len(data)):
            colour = self.__data_color
            text_color=(0, 0, 0)
            if first == data[i]:
                colour = self.__first_color
                text_color=self.__first_color
            elif second == data[i]:
                colour = self.__second_color
                text_color=self.__second_color
            # Rect(left, top, width, height)
            pg.draw.rect(self.__display, colour, (i*rect_width, self.__height, rect_width*0.75, -data[i]))
            # pg.draw.polygon(self.__display, (0, 0, 0), (
            #     (i*rect_width + rect_width*0.75/2, self.__height-20-data[i]),
            #     (i*rect_width, self.__height-30-data[i]),
            #     (i*rect_width, self.__height-50-data[i]),
            #     (i*rect_width+rect_width*.96, self.__height-50-data[i]),
            #     (i*rect_width+rect_width*.96, self.__height-30-data[i]),
            # ))
            self.__display.blit(self.__font.render('%d'%data[i], True, text_color), (i*rect_width, self.__height-20-data[i]))
        if not self.__close():
            pg.display.update()
            time.sleep(self.__speed)

    def __close(self, ):
        if not self.__running:
            return True
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                self.__running=False
                return True
            elif event.type==pg.KEYDOWN:
                if event.key==pg.K_DOWN:
                    self.__decrease_speed()
                elif event.key==pg.K_UP:
                    self.__increase_speed()
        return False

    def __decrease_speed(self, delta=0.01):
        if round(self.__speed+delta, 2) <= 0.29:
            self.__speed=round(self.__speed+delta, 2)
    
    def __increase_speed(self, delta=0.01):
        if round(self.__speed-delta, 2) >= 0:
            self.__speed=round(self.__speed-delta, 2)
