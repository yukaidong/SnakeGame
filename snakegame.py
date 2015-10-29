#! /usr/bin/env python
#encoding utf-8

from character import *

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
