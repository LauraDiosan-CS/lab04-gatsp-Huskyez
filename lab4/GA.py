from Chromosome import Chromosome
from Graph import Graph
from random import randint
import os


class GA:

	def __init__(self, populationSize, numberGenerations, fitnessFunction, fileName):
		self.populationSize = populationSize
		self.numberGenerations = numberGenerations
		self.population = []
		self.fitnessFunction = fitnessFunction
		self.graph = Graph()
		self.graph.loadData(fileName)
		self.outfile = os.getcwd() + "/output/" + os.path.basename(fileName)[:-4] + ".out"

	def initialise(self):
		params = {"noNodes": self.graph.nrCities}
		for _ in range(self.populationSize):
			chromosome = Chromosome(params)
			self.population.append(chromosome)
		self.evaluateGeneration()

	def evaluateGeneration(self):
		for c in self.population:
			c.fitness = self.fitnessFunction(c.repres, self.graph)

	def bestChromosome(self):
		return min(self.population, key=lambda x: x.fitness)

	def worstChromosome(self):
		return max(self.population, key=lambda x: x.fitness)

	def selection(self):
		pos1 = randint(0, self.populationSize - 1)
		pos2 = randint(0, self.populationSize - 1)

		if self.population[pos1].fitness < self.population[pos2].fitness:
			return pos1
		else:
			return pos2

	def oneGeneration(self):
		newPop = []
		for _ in range(self.populationSize):
			p1 = self.population[self.selection()]
			p2 = self.population[self.selection()]
			off = p1.crossover(p2)
			off.mutation()
			newPop.append(off)
		self.population = newPop
		self.evaluateGeneration()

	def oneGenerationElitism(self):
		newPop = [self.bestChromosome()]
		for _ in range(self.populationSize - 1):
			p1 = self.population[self.selection()]
			p2 = self.population[self.selection()]
			off = p1.crossover(p2)
			off.mutation()
			newPop.append(off)
		self.population = newPop
		self.evaluateGeneration()

	def oneGenerationSteadyState(self):
		for _ in range(self.populationSize):
			p1 = self.population[self.selection()]
			p2 = self.population[self.selection()]
			off = p1.crossover(p2)
			off.mutation()
			off.fitness = self.fitnessFunction(off.repres, self.graph)
			worst = self.worstChromosome()
			if off.fitness < worst.fitness:
				worst = off

	def run(self, generationFunction):

		with open(self.outfile, "w") as out:
			bestChromosome = Chromosome()
			for currentGeneration in range(self.numberGenerations):
				generationFunction()
				bestChromosome = self.bestChromosome()
				out.write("GENERATION " + str(currentGeneration) + ": " + str(bestChromosome.repres) + " - " + str(
					bestChromosome.fitness) + "\n")

		return bestChromosome
