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
	def __init__(self, ID, colour, search_depth, ips):
		Player.__init__(self, ID, colour, "AI")
		self.root_node = None
		self.current_node = self.root_node
		self.leaf_nodes = [] # Only includes leaf nodes that needs simulation
		self.iteration_count = 0
		self.search_depth = search_depth
		self.iterations_per_second = ips

	def get_max_iterations(self, cols):
		count = 0

		for i in range(self.search_depth + 1):
			count += cols ** i

		return count

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
		node.absolute_weight += weight_value
		node.total_simulations += 1

		if not node.is_root:
			self._propagate_recursively(node.parent_node, weight_value)

	def back_propagate(self, node):
		weight_value = 0

		if node.current_grid.check_win(self.ID):
			weight_value = 1
		elif node.current_grid.check_win(self.opponent.ID):
			# Forces AI to not play very aggressively
			if node.depth == 2:
				weight_value = -100
			else:
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
				child_node = node.add_node(child_grid, col)

				if child_node.current_grid.check_game_over(self.ID, self.opponent.ID):
					# Back propagation
					self.back_propagate(child_node)
				elif child_node.depth < max_depth:
					self.create_full_branches(child_node, grid, max_depth)
				elif child_node.depth == max_depth:
					self.leaf_nodes.append(child_node)

	def simulate_full_game(self, node):
		current_depth = node.depth - 1

		game_over = False

		while not game_over:
			self.make_valid_random_move(node.current_grid, self.get_player_id(current_depth))

			if node.current_grid.check_game_over(self.ID, self.opponent.ID):
				game_over = True
				# Back propagation
				self.back_propagate(node)

			current_depth += 1

	def get_chosen_col(self):
		chosen_col = None
		highest_weighting = self.root_node.child_nodes[0].get_weighting()


		for node in self.root_node.child_nodes:
			#print(str(node.get_weighting()))

			if node.get_weighting() > highest_weighting:
				highest_weighting = node.get_weighting()
				chosen_col = node.move_col

				if chosen_col == None:
					print("Error: Fetched column from a root node / expansion node")

		return chosen_col

	def think_move_mcts(self, grid):
		move_made = False

		# Initialise the tree
		if(self.iteration_count == 0):
			self.leaf_nodes = []
			self.root_node = Node(copy.deepcopy(grid), 0, is_root = True)

			# Create the tree first
			self.create_full_branches(self.root_node, grid, self.search_depth)

			self.iteration_count += 1
		else:
			for i in range(self.iterations_per_second):
				self.iteration_count += 1

				# 1st iteration is initialising the tree
				current_node_index = self.iteration_count - 2 # We start on the 2nd iteration

				if current_node_index < len(self.leaf_nodes):
					# Selection
					self.current_node = self.leaf_nodes[current_node_index]

					# Expansion
					child_grid = copy.deepcopy(self.current_node.current_grid)
					expansion_node = self.current_node.add_node(child_grid)

					# Simulation (and back propagation)
					self.simulate_full_game(expansion_node)

		# Iteration limit reached
		if(self.iteration_count >= self.get_max_iterations(grid.no_cols)):

			# Make best move
			chosen_col = self.get_chosen_col()
			self.make_move(grid, chosen_col)
			move_made = True
			self.iteration_count = 0

			# Debugging
			self.root_node.print_summary(len(self.leaf_nodes))

		return move_made













