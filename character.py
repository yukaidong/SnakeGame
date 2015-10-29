#! /usr/bin/env python
#encoding utf-8

import random
from random import randrange

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