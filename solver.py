import itertools as it

class Solver2d:
	"""Basic constraint solver for 2d grids"""
	
	legal = None
	values = []
	
	def __init__(self, legal, values):
		self.legal = legal
		self.values = values
	
	def solve(self, grid):
		progress = True
		while progress:
			progress = False
			for x,y in it.product(xrange(len(grid)), xrange(len(grid[0]))):
				if not grid[x][y]:
					num_legal = 0
					for val in self.values:
						if self.legal(grid, val, (x, y)):
							num_legal += 1
							solution = val
					if num_legal == 1:
						grid[x][y] = solution
						progress = True
					elif num_legal == 0:
						print "ERROR: No solution possible for %d,%d".format(x,y)
						return
