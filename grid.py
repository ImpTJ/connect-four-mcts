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

	def disc_width(self):
		return self.width / self.no_cols

	def disc_height(self):
		return self.height / self.no_rows

	def draw_disc(self, x, y, colour, surface):
		pygame.draw.rect(surface, colour, (x, y, self.disc_width(), self.disc_height()))

	def draw(self, surface, players):
		for i, row in enumerate(self.data):
			for j, cell in enumerate(row):

				if cell == players[0].ID or cell == players[1].ID:
					x = j * self.disc_width()
					y = self.height - (i + 1) * self.disc_height()

				if cell == players[0].ID:
					self.draw_disc(x, y, players[0].colour, surface)
				if cell == players[1].ID:
					colour = (0, 0, 255)
					self.draw_disc(x, y, players[1].colour, surface)














