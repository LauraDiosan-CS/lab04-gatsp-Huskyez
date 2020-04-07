from random import randint


def generateARandomPermutation(n):
	# perm = [i for i in range(n)]
	# pos1 = randint(0, n - 1)
	# pos2 = randint(0, n - 1)
	# perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
	# return perm
	pool = [x for x in range(n)]
	permutation = []

	while len(pool) > 0:
		index = randint(0, len(pool) - 1)
		permutation.append(pool[index])
		del pool[index]

	return permutation


class Chromosome:
	def __init__(self, problParam=None):
		if problParam is not None:
			self.__problParam = problParam  # problParam has to store the number of nodes/cities
			self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
		else:
			self.__repres = []
		self.__fitness = 0.0

	@property
	def repres(self):
		return self.__repres

	@property
	def fitness(self):
		return self.__fitness

	@repres.setter
	def repres(self, l=None):
		if l is None:
			l = []
		self.__repres = l

	@fitness.setter
	def fitness(self, fit=0.0):
		self.__fitness = fit

	def crossover(self, c):
		# order XO
		pos1 = randint(-1, self.__problParam['noNodes'] - 1)
		pos2 = randint(-1, self.__problParam['noNodes'] - 1)
		if pos2 < pos1:
			pos1, pos2 = pos2, pos1
		k = 0
		newrepres = self.__repres[pos1: pos2]
		for el in c.__repres[pos2:] + c.__repres[:pos2]:
			if el not in newrepres:
				if len(newrepres) < self.__problParam['noNodes'] - pos1:
					newrepres.append(el)
				else:
					newrepres.insert(k, el)
					k += 1

		offspring = Chromosome(self.__problParam)
		offspring.repres = newrepres
		return offspring

	def mutation(self):
		# insert mutation
		pos1 = randint(0, self.__problParam['noNodes'] - 1)
		pos2 = randint(0, self.__problParam['noNodes'] - 1)
		if pos2 < pos1:
			pos1, pos2 = pos2, pos1
		el = self.__repres[pos2]
		del self.__repres[pos2]
		self.__repres.insert(pos1 + 1, el)

	def __str__(self):
		return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

	def __repr__(self):
		return self.__str__()

	def __eq__(self, c):
		return self.__repres == c.__repres and self.__fitness == c.__fitness


if __name__ == "__main__":
	print(generateARandomPermutation(6))
