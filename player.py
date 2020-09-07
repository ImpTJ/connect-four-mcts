import random

class Player:
	def __init__(self, ID, colour, tag):
		self.ID = ID
		self.colour = colour
		self.tag = tag

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
		Player.__init__(self, ID, colour, "user")


class PlayerAI(Player):
	def __init__(self, ID, colour):
		Player.__init__(self, ID, colour, "AI")
		self.iteration_count = 0

	def make_valid_random_move(self, grid):
		# Safety net to prevent infinite loop if board is full
		if not grid.check_full():
			move_made = False

			while not move_made:
				move_made = self.make_move(grid, random.randint(0, grid.no_cols - 1))

	def think_move_mcts(self, grid):
		move_made = False

		self.iteration_count += 1

		if(self.iteration_count >= 60 * 1):
			self.make_valid_random_move(grid)
			move_made = True
			self.iteration_count = 0

		return move_made













