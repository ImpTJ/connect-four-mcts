import random

class Node:
	def __init__(self, grid, depth, move_col = None, parent = None, is_root = False):
		self.current_grid = grid
		self.depth = depth
		self.move_col = move_col # Root nodes and expansion nodes do not have a stored move
		self.parent_node = parent
		self.is_root = is_root
		self.position_over = False

		self.absolute_weight = 0 # Draw = 0.5
		self.total_simulations = 0 # Including all child nodes
		self.child_nodes = []

	def add_node(self, grid, move_col = None):
		node = Node(grid, self.depth + 1, move_col = move_col, parent = self)
		self.child_nodes.append(node)
		return node

	def get_random_child_node(self):
		return self.child_nodes[random.randint(0, len(self.child_nodes) - 1)]

	def get_weighting(self):
		return self.absolute_weight / self.total_simulations

	# Debugging
	
	# current_count = 1 to include the parent node
	# Tested to be accurate: 7^3 + 7^2 + 7^1 + 7^0 = 400 for a depth of 3
	def get_total_nodes(self, current_count = 1):
		node_count = current_count

		for node in self.child_nodes:
			node_count = node.get_total_nodes(node_count)

		return node_count + len(self.child_nodes)

	def get_total_nodes_has_simulated(self, no_leaf_nodes):
		# Since each leaf node has an expansion node, the leaf nodes are counted twice.
		return self.get_total_nodes() - no_leaf_nodes

	def print_summary(self, no_leaf_nodes = 0):
		print("Node with " + str(len(self.child_nodes)) + " children")
		print("Total simulations: " + str(self.total_simulations))

		total_nodes = -1

		if self.is_root:
			print("Assuming simulation has been complete: ")
			total_nodes = self.get_total_nodes_has_simulated(no_leaf_nodes)
		else:
			total_nodes = self.get_total_nodes()

		print("Total nodes: " + str(total_nodes))
		print("Depth of current node: " + str(self.depth))
		print(self.current_grid.data)

















