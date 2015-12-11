import itertools as it

class solver2d:
	"""Basic constraint solver for 2d grids"""
	
	this.legal = None
	this.values = []
	
	def __init___(self, legal, values):
		this.legal = legal
		this.values = values
	
	def solve(grid):
		for x,y in it.product(xrange(len(grid)), xrange(len(grid[0]))):
			if not grid[x][y]:
				num_legal = 0
				for val in values:
					if legal(val, (x, y)):	
						num_legal += 1
						solution = val
						
				if num_legal == 1:
					grid[x][y] = solution
				elif num_legal == 0:
					print "ERROR: No solution possible for %d,%d".format(x,y)
					return
