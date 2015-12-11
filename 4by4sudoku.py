from solver import *
import itertools as it

"""Size of the 2d grid representing the problem"""
size = (4,4)

"""Initialise the grid with None"""
grid = [x[:] for x in [[None]*size[0]]*size[1]]

"""Add any initial condition to the grid"""
grid[0][0] = 2
grid[1][2] = 2
grid[2][1] = 1
grid[3][3] = 4

def print_grid(g):
	print "Current State of Grid:"
	for y in range(4):
		print ' | '.join([str(k[y]) if k[y] else ' ' for k in g])
		if y < 3: print '-'*(4+3*len(' | '))
	print

"""Function to determin if a given value is legal at an index in the grid"""
def legal(grid,val,coord):
	blk_coord = (coord[0]/2, coord[1]/2)
	col = grid[coord[0]]
	row = [k[coord[1]] for k in grid]
	blk = [grid[2*blk_coord[0]+x][2*blk_coord[1]+y] for x,y in it.product(range(0,2), repeat=2)]
	if val in row: return False
	if val in col: return False
	if val in blk: return False
	return True

print_grid(grid)

"""Create and call the solver"""
solver = Solver2d(legal, range(1,5))
solver.solve(grid)


print_grid(grid)
