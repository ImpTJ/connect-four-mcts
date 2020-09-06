class Player:
	def __init__(self, ID, colour):
		self.ID = ID
		self.colour = colour

	# Makes a move: returns True only if move is valid
	def make_move(self, grid, col):
		for i, row in enumerate(grid.data):
			if grid.data[i, col] == 0:
				grid.data[i, col] = self.ID
				return True

			if i == grid.no_cols - 1:
				return False

class PlayerUser(Player):
	def __init__(self, ID, colour):
		Player.__init__(self, ID, colour)


class PlayerAI(Player):
	def __init__(self, ID, colour):
		Player.__init__(self, ID, colour)
