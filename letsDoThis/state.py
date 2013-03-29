class State:

	x = 0
	y = 0
	die = None
	action = ""

	def __init__(self,x,y,die,action):
		self.x = x
		self.y = y
		self.die = die
		self.action = action

	def valid(self,puzzle,state):
		return self.validLocation(puzzle,state.x,state.y) and state.die[1] != 6

	def validLocation(self,puzzle,x,y):
		#print("____________________________")
		#print([x,len(puzzle)])
		#print(0 <= x < len(puzzle))
		#print([y,len(puzzle[0])])
		#print(0 <= y < len(puzzle[0]))
		return(0<= x <len(puzzle) 
				and 0<=y < len(puzzle[0]) 
				and puzzle[x][y] != "*")

	def neighbors(self,puzzle):
		#print("In Die")
		#print(self.die)
		#print([self.x,self.y])
		dieVertical = self.die[0][:]
		dieMiddle = self.die[1][:]
		
		dieNorth = [dieVertical[:],dieMiddle[:]]
		dieSouth = [dieVertical[:],dieMiddle[:]]
		dieEast  = [dieVertical[:],dieMiddle[:]]
		dieWest  = [dieVertical[:],dieMiddle[:]]
		
		dN = dieNorth[0].pop(0)
		dieNorth[1].pop()
		dieNorth[0].append(dN)
		dieNorth[1].append(dieNorth[0][3])
		dieNorth[1][1] = dieNorth[0][1]
		
		dS = dieSouth[0].pop()
		dieSouth[1].pop()
		dieSouth[0].insert(0,dS)
		dieSouth[1].append(dieSouth[0][3])
		dieSouth[1][1] = dieSouth[0][1]
		
		dE = dieEast[1].pop()
		dieEast[0].pop()
		dieEast[1].insert(0,dE)
		dieEast[0].append(dieEast[1][3])
		dieEast[0][1] = dieEast[1][1]
		
		dW = dieWest[1].pop(0)
		dieWest[0].pop()
		dieWest[1].append(dW)
		dieWest[0].append(dieWest[1][3])
		dieWest[0][1] = dieWest[1][1]
		x = self.x + 0
		y = self.y + 0

#		print(dieNorth)
#		print(dieSouth)
#		print(dieEast)
#		print(dieWest)
		
		neighbors = [State(x,(y - 1), dieNorth, "N"),
					State(x,(y + 1), dieSouth, "S"),
					State((x + 1),self.y, dieEast, "E"),
					State((x -1), self.y, dieWest, "W")]
		
		s = 0
		while s < len(neighbors):
			if(not self.valid(puzzle,neighbors[s])):
				neighbors.pop(s)
				s -= 1
			s += 1
#		print("===================")
#		for neighbor in neighbors:
#			print(neighbor.die)
#			print(neighbor.action)
#		print("+++++++++++++++++++")
		return neighbors
