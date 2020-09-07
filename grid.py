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

	def _check_win_horizontal(self, ID):
		win_found = False

		for row in self.data:
			for j in range(self.no_cols - 3):
				is_win = True

				for k in range(4):
					if row[j + k] != ID:
						is_win = False
						break

				if is_win:
					win_found = True

		return win_found

	def _check_win_vertical(self, ID):
		win_found = False

		for j in range(0, self.no_cols):
			for i in range(0, self.no_rows - 3):
				is_win = True

				for k in range(4):
					if self.data[i + k, j] != ID:
						is_win = False
						break

				if is_win:
					win_found = True

		return win_found

	def _check_win_diagonal_up(self, ID):
		win_found = False

		for j in range(0, self.no_cols - 3):
			for i in range(0, self.no_rows - 3):
				is_win = True

				for k in range(4):
					if self.data[i + k, j + k] != ID:
						is_win = False
						break

				if is_win:
					win_found = True

		return win_found

	def _check_win_diagonal_down(self, ID):
		win_found = False

		for j in range(0, self.no_cols - 3):
			for i in range(3, self.no_rows):
				is_win = True

				for k in range(4):
					if self.data[i - k, j + k] != ID:
						is_win = False
						break

				if is_win:
					win_found = True

		return win_found

	def _check_win_diagonal(self, ID):
		return self._check_win_diagonal_up(ID) or self._check_win_diagonal_down(ID)

	def check_win(self, ID):
		return (self._check_win_horizontal(ID) or self._check_win_vertical(ID) or self._check_win_diagonal(ID))

	def check_full(self):
		return not np.isin(0, self.data)

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














