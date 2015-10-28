#! /usr/bin/env python
#encoding utf-8

import sys
import random
from random import randrange

import pygame
from pygame.locals import *

class Snake:
	def  __init__(self):
		self.pos = [(10,10), (9,10), (8,10)]
		self.direction = 'right'

	def head(self):
		return self.pos[0]

	def tail(self):
		return self.pos[-1]

	def die(self, shit):
		if self.head() in shit.pos: return True
		if self.head() in self.pos[1:]: return True
		if self.head()[0] not in range(20): return True
		if self.head()[1] not in range(20): return True
		return False

	def eat(self, food):
		return self.head() in food.pos

	def move(self, direction):
		snake_head = self.head()
		if direction is 'left':
			snake_head = (self.head()[0]-1, self.head()[1])
			self.direction = 'left'
		if direction is 'right':
			snake_head = (self.head()[0]+1, self.head()[1])
			self.direction = 'right'
		if direction is 'up':
			snake_head = (self.head()[0], self.head()[1]-1)
			self.direction = 'up'
		if direction is 'down':
			snake_head = (self.head()[0], self.head()[1]+1)
			self.direction = 'down'
		self.pos.insert(0, snake_head)
		
	def defecate(self, shit):
		if random.choice([True, False]):
			shit.pos.append(self.tail())
			self.pos.pop()

	def not_grow(self):
		self.pos.pop()

class Food:
	def __init__(self):
		self.pos = []

	def new(self, snake):
		pos = (randrange(20), randrange(20))
		while pos in snake.pos:
			pos = (randrange(20), randrange(20))
		self.pos = [pos]


class Shit:
	def __init__(self):
		self.pos = []

def init_ui():
	pygame.init()
	pygame.display.set_mode((400,400)) #block size 20
	pygame.mouse.set_visible(0)
	pygame.display.set_caption('Snake Game')
	return pygame.display.get_surface()

def draw(screen, obj, color):
	for pos in obj.pos:
		area = pygame.Rect((20*pos[0], 20*pos[1]), (20,20))
		pygame.draw.rect(screen, color, area)

def update_ui(screen, snake, food, shit):
	block_size = 20
	snake_color = (0,255,0)
	food_color = (255,0,0)
	shit_color = (255,255,0)
	screen.fill((0, 0, 0))
	draw(screen, snake, snake_color)
	draw(screen, food, food_color)
	print shit.pos
	draw(screen, shit, shit_color)
	pygame.display.update()
	pygame.time.Clock().tick(10)


def operate(snake, food, shit):
	direction = snake.direction
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT and snake.direction is not 'right':
				direction = 'left'
			if event.key == K_RIGHT and snake.direction is not 'left': 
				direction = 'right'
			if event.key == K_UP and snake.direction is not 'down': 
				direction = 'up'
			if event.key == K_DOWN and snake.direction is not 'up': 
				direction = 'down'
	snake.move(direction)
	if snake.die(shit):
		pygame.quit()
		sys.exit()
	if snake.eat(food): 
		snake.defecate(shit)
		food.new(snake)
	else:
		snake.not_grow()


def main():
	snake = Snake()
	food = Food()
	food.new(snake)
	shit = Shit()
	screen = init_ui()
	while True:
		operate(snake, food, shit)
		update_ui(screen, snake, food, shit)


if __name__ == '__main__':
	main()
