class Board:
	board = None
	yRange = 0
	xRange = 0
	def __init__(self, file):
		self.board = parse(file)
		
	# Parse a file and return a board 
	def parse(file):
	
	def boardDisplay():
		for y in xrange(yRange + 1):
			for x in xrange(xRange + 1):
			if board[y][x] == 'START':
				sys.stdout.write('S')
			if board[y][x] == 'OPEN':
				sys.stdout.write('.')
			if board[y][x] == 'GOAL':
				sys.stdout.write('G')
			if board[y][x] == 'BARRIER':
				sys.stdout.write('*')
			sys.stdout.write('\n')
			
	def isBarrier(position):
		if board[position[0]][position[1]] == 'BARRIER':
			return True
	def isGoal(position):
		if board[position[0]][position[1]] == 'GOAL':
			return True