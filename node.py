import random

class Node:
	def __init__(self, grid, depth, parent = None, is_root = False):
		self.current_grid = grid
		self.depth = depth
		self.parent_node = parent
		self.is_root = is_root
		self.position_over = False

		self.no_winning_nodes = 0 # Draw = 0.5
		self.child_nodes = []

	def add_node(self, grid):
		node = Node(grid, self.depth + 1, parent = self)
		self.child_nodes.append(node)
		return node

	def get_random_child_node(self):
		return self.child_nodes[random.randint(0, len(self.child_nodes) - 1)]

	# Debugging
	
	# current_count = 1 to include the parent node
	# Tested to be accurate: 7^3 + 7^2 + 7^1 + 7^0 = 400 for a depth of 3
	def get_total_nodes(self, current_count = 1):
		node_count = current_count

		for node in self.child_nodes:
			node_count = node.get_total_nodes(node_count)

		return node_count + len(self.child_nodes)

	def print_summary(self):
		print("Node with " + str(len(self.child_nodes)) + " children")
		print("Winning nodes: " + str(self.no_winning_nodes))
		print("Total nodes: " + str(self.get_total_nodes()))
		print("Depth of current node: " + str(self.depth))
		print(self.current_grid.data)

















