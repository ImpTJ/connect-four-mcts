import random, copy
from node import *

class Player:
	def __init__(self, ID, colour, tag):
		self.ID = ID
		self.colour = colour
		self.tag = tag
		self.opponent = None

	def set_opponent(self, player):
		self.opponent = player

	# Makes a move: returns True only if move is valid
	def make_move(self, grid, col, ID = -1):
		if ID == -1:
			ID = self.ID

		for i, row in enumerate(grid.data):
			if grid.data[i, col] == 0:
				grid.data[i, col] = ID
				return True

			if i == grid.no_cols - 1:
				return False

class PlayerUser(Player):
	def __init__(self, ID, colour):
		Player.__init__(self, ID, colour, "user")


class PlayerAI(Player):
	def __init__(self, ID, colour):
		Player.__init__(self, ID, colour, "AI")
		self.root_node = None
		self.current_node = self.root_node
		self.iteration_count = 0

	def make_valid_random_move(self, grid, ID = -1):
		if ID == -1:
			ID = self.ID

		# Safety net to prevent infinite loop if board is full
		if not grid.check_full():
			move_made = False

			while not move_made:
				move_made = self.make_move(grid, random.randint(0, grid.no_cols - 1), ID)

	# Depth of 0 is AI's turn
	def get_player_id(self, depth):
		if depth % 2 == 0:
			return self.ID
		else:
			return self.opponent.ID

	def _propagate_recursively(self, node, weight_value):
		node.no_winning_nodes += weight_value

		if not node.is_root:
			self._propagate_recursively(node.parent_node, weight_value)

	def back_propagate(self, node):
		weight_value = 0

		if node.current_grid.check_win(self.ID):
			weight_value = 1
		elif node.current_grid.check_win(self.opponent.ID):
			weight_value = 0
		elif node.current_grid.check_full():
			weight_value = 0.5
		else:
			print("Error: This should never be printed.")

		self._propagate_recursively(node, weight_value)

	def create_full_branches(self, node, grid, max_depth):
		child_node = None

		for col in range(grid.no_cols):
			child_grid = copy.deepcopy(node.current_grid)

			if self.make_move(child_grid, col, self.get_player_id(node.depth)):
				child_node = node.add_node(child_grid)

				if child_node.current_grid.check_game_over(self.ID, self.opponent.ID):
					# Back propagation
					self.back_propagate(child_node)
				elif child_node.depth < max_depth:
					self.create_full_branches(child_node, grid, max_depth)

				# Debugging
				child_node.print_summary()

	def think_move_mcts(self, grid):
		move_made = False

		self.iteration_count += 1

		# Initialise the MCTS
		if(self.iteration_count == 1):
			self.root_node = Node(copy.deepcopy(grid), 0, is_root = True)

			# Create the tree first
			tree_depth = 3
			self.create_full_branches(self.root_node, grid, tree_depth)

		'''
		# Selection
		self.current_node = self.root_node

		while len(self.current_node.child_nodes) != 0:
			self.current_node = self.current_node.get_random_child_node()

		# Expansion
		child_grid = copy.deepcopy(self.current_node.current_grid)

		self.make_valid_random_move(child_grid)
		self.current_node.add_node(child_grid)
		'''

		# Time limit reached
		if(self.iteration_count >= 60 * 1):
			self.make_valid_random_move(grid)
			move_made = True
			self.iteration_count = 0

			# Debugging
			self.root_node.print_summary()

		return move_made













