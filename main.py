####################################

# Connect 4
# AI vs Player
# (Can customise to Player vs Player, AI vs AI, Player vs AI easily)


# Using Monte Carlo Tree Search
# Customisable iterations and search depth

# Made in ~10 hours (over 4 days)
# With NO online help on the MCTS algorithm (only previous knowledge)

# Author: Freddy JIANG

####################################






import pygame, time
import numpy as np
from grid import *
from player import *

# Constants
WIDTH, HEIGHT = 700, 600
DISC_COLOURS = [
	(255, 255, 51 ), # yellow
	(255, 0,   102)  # red
]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four MCTS")

# Main program
def main():
	run = True
	game_over = False
	FPS = 60
	clock = pygame.time.Clock()

	ACTIVE_KEYS = np.array([pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7])

	game_grid = Grid(6, 7, 0, 0, WIDTH, HEIGHT)
	players = [
		PlayerAI(1, DISC_COLOURS[0], search_depth = 3, ips = 10),
		PlayerUser(2, DISC_COLOURS[1])
	]
	active_player = players[0]
	move_made = False

	# Initialisation
	players[0].set_opponent(players[1])
	players[1].set_opponent(players[0])

	# Functions
	def next_player(prev_player):
		if prev_player == players[0]:
			# Apparently, Python creates a new local variable 'active_player'
			# Instead of fetching the previously created 'active_player'
			active_player = players[1]
		else:
			active_player = players[0]

		return active_player

	def redraw_window():
		WIN.fill((255, 255, 255))

		game_grid.draw(WIN, players)
		pygame.display.update()

	# Main loop
	while run:
		clock.tick(FPS)

		move_made = False

		# Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if np.isin(event.key, ACTIVE_KEYS) and active_player.tag == "user" and not move_made and not game_over:
					# User makes move
					# '1' has unicode 49 -> column index 0
					move_made = active_player.make_move(game_grid, event.key - 49)

		if not game_over:
			# AI makes move
			if active_player.tag == "AI":
				move_made = active_player.think_move_mcts(game_grid)

			# If a player makes a move
			if move_made:
				if game_grid.check_win(active_player.ID):
					print("Player " + str(active_player.ID) + " wins")
					game_over = True
				elif game_grid.check_full():
					print("Draw")
					game_over = True
				else:
					# Game is not over. Continue playing
					active_player = next_player(active_player)

		# GUI
		redraw_window()

main()














