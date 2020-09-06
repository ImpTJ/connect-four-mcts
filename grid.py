import pygame
import numpy as np

class Grid:
	def __init__(self, no_rows, no_cols, x, y, width, height):
		self.no_rows = no_rows
		self.no_cols = no_cols
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.data = np.empty((self.no_rows, self.no_cols), dtype = int)
		self.data.fill(0)

		# Testing random data
		self.data[0, 0] = 1
		self.data[0, 1] = 2
		self.data[0, 6] = 1

	def disc_width(self):
		return self.width / self.no_cols

	def disc_height(self):
		return self.height / self.no_rows

	def draw_disc(self, x, y, colour, surface):
		pygame.draw.rect(surface, colour, (x, y, self.disc_width(), self.disc_height()))

	def draw(self, surface):
		for i, row in enumerate(self.data):
			for j, cell in enumerate(row):
				if cell == 1:
					colour = (255, 0, 0)
					self.draw_disc(j * self.disc_width(), i * self.disc_height(), colour, surface)
				if cell == 2:
					colour = (0, 0, 255)
					self.draw_disc(j * self.disc_width(), i * self.disc_height(), colour, surface)
