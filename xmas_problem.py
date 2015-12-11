from solver import *
import itertools as it

"""Size of the 2d grid representing the problem"""
size = (25,25)

"""Initialise the grid with None"""
grid = [x[:] for x in [[None]*size[0]]*size[1]]
constraints = [[[25]]*size[0],
               [[25]]*size[1]]
print constraints
"""Add any initial condition to the grid"""

"""Function that returns the number of solutions that are legal"""
def solutions(line, runs, mid_run=False):
	res = 0
	in_run = mid_run
	runs_left = runs
	line_left = line
	if sum(runs) == len(line):
		for x in line:
			if x == 0:
				return 0
		return 1
	while len(line_left):
		if line_left[0] == 1:
			in_run = 1
			if len(runs_left) == 0:
				return 0
			runs_left[0] -=1
		elif line_left[0] == 0:
			if in_run and runs_left[0] != 0: 
				return 0
			runs_left = runs_left[1:]
			in_run = 0
		else:
			if len(line_left[1:]) >= sum(runs):
				res += solutions([0]+line_left[1:], runs_left, in_run)
			res += solutions([1]+line_left[1:], runs_left, in_run)
		line_left = line_left[1:]
	if len(runs_left) > 0 and runs_left[-1] != 0:
		return 0
	return res

"""Function to determin if a given value is legal at an index in the grid"""
def legal(grid,val,coord):
	row = grid[coord[0]]
	col = [row[coord[1]] for row in grid]
	row[coord[1]] = val
	col[coord[0]] = val
	num  = solutions(row, constraints[0][coord[0]])
	num += solutions(col, constraints[1][coord[1]])
	return True if num > 0 else False

"""Create and call the solver"""
solver = Solver2d(legal, [0,1])
solver.solve(grid)

print grid
