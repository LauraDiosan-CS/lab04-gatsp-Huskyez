
def TSPCost(permutation, graph):
	
	cost = 0
	
	for i in range(len(permutation) - 1):
		cost += graph.distances[permutation[i]][permutation[i + 1]][0]
	cost += graph.distances[permutation[len(permutation) - 1]][permutation[0]][0]
	return cost


class Graph:

	def __init__(self):
		self.nrCities = 0
		self.distances = []
		self.solution = []

	def loadData(self, fileName):
		with open(fileName) as f:
			data = f.readline()
			self.nrCities = int(data)

			for i in range(self.nrCities):
				data = f.readline()
				dist = data.split(',')
				dist = [(float(x), dist.index(x)) for x in dist]
				self.distances.append(dist)


