import pygame 
from pygame.locals import *
import sys
import time
import random
import pyjokes

class Game:
    
    def __init__(self):
        self.w = 750
        self.h = 500
        self.rest = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = "0%"        
        self.results = 'Time:0 Accuracy:0 WPM:0'
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)
        
        pygame.init()
        self.open_image = 