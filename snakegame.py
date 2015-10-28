#! /usr/bin/env python
#encoding utf-8

import sys
from random import randrange

import pygame

#class Snake 

def init_ui():
	pygame.init()
	pygame.display.set_mode((400,400)) #block size 20
	pygame.mouse.set_visible(0)
	pygame.display.set_caption('Snake Game')
	return pygame.display.get_surface()

def update_ui(screen, snake, food):
	block_size = 20
	snake_color = (0,255,0)
	food_color = (255,0,0)
	for snake_pos in snake:
		snake_area = pygame.Rect((20*snake_pos[0], 20*snake_pos[1]), (20,20))
		pygame.draw.rect(screen, snake_color, snake_area)
	food_area = pygame.Rect((20*food[0], 20*food[1]), (20,20))
	pygame.draw.rect(screen, food_color, food_area)
	pygame.display.update()

def operate(snake, food):
	return


def main():
	snake = [(10,10), (9,10), (8,10)]
	food = (randrange(20), randrange(20))
	screen = init_ui();
	while True:
		operate(snake, food)
		update_ui(screen, snake, food)


if __name__ == '__main__':
	main()