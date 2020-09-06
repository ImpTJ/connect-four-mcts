import pygame, time
from grid import *

WIDTH, HEIGHT = 700, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four MTCS")

def main():
	run = True
	FPS = 60
	clock = pygame.time.Clock()

	game_grid = Grid(6, 7, 0, 0, WIDTH, HEIGHT)

	def redraw_window():
		WIN.fill((255, 255, 255))

		game_grid.draw(WIN)
		pygame.display.update()

	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		redraw_window()

main()














