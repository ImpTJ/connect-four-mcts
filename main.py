import pygame, time
from grid import *
from player import *

# Constants
WIDTH, HEIGHT = 700, 600
DISC_COLOURS = [
	(255, 255, 51 ), # yellow
	(255, 0,   102)  # red
]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four MTCS")

# Main program
def main():
	run = True
	game_over = False
	FPS = 60
	clock = pygame.time.Clock()

	ACTIVE_KEYS = np.array([pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7])

	game_grid = Grid(6, 7, 0, 0, WIDTH, HEIGHT)
	players = [
		PlayerUser(1, DISC_COLOURS[0]),
		PlayerUser(2, DISC_COLOURS[1])
	]
	active_player = players[0]

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

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if not game_over:
					if np.isin(event.key, ACTIVE_KEYS):
						# '1' has unicode 49 -> column index 0
						valid_move = active_player.make_move(game_grid, event.key - 49)

						if valid_move:
							if game_grid.check_win(active_player.ID):
								print("Player " + str(active_player.ID) + " wins")
								game_over = True
							elif game_grid.check_full():
								print("Draw")
								game_over = True
							else:
								# Game is not over. Continue playing
								active_player = next_player(active_player)

		redraw_window()

main()














