from GA import GA
from Graph import TSPCost
import os

if __name__ == '__main__':

	population = 200
	generations = 200

	files = os.listdir("test")

	for file in files:
		path = os.getcwd() + "/test/" + file

		alg = GA(population, generations, TSPCost, path)
		alg.initialise()
		best = alg.run(alg.oneGenerationElitism)

		print("Best for " + file + ": ")
		print(best.repres, best.fitness, sep=" - ")
