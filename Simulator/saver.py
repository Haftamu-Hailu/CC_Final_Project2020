from collections import defaultdict
import matplotlib.pyplot as plt

class Saver:
	def __init__(self, verbose):
		self.verbose = verbose
		self.overview = defaultdict(lambda: [])
		self.infections = []

	def save_overview(self, key, value):
		self.overview[key].append(value)

	def save_infection_data(self, infecter, infected, location, day):
		self.infections.append((infecter, infected, location, day))

	def print_overview(self):
		for key in self.overview:
			plt.plot(self.overview[key])
			plt.title(key)
			plt.show()
