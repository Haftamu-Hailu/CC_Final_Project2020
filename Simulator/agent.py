import random as rn

class Agent:
	def __init__(self, id, is_infected, days_until_symptoms, total_days_sick, mortality_rate):
		self.id = id

		self.is_alive = True
		self.has_symptoms = False
		self.is_isolated = False
		self.is_infected = is_infected
		self.has_been_infected = is_infected

		self.day_infected = 0 if is_infected else float("-inf")
		self.day_isolated = float("-inf")

		self.days_until_symptoms = days_until_symptoms
		self.total_days_sick = total_days_sick
		self.mortality_rate = mortality_rate

		self.home = None
		self.office = None

	def get_id(self):
		return self.id

	def set_home(self, home):
		self.home = home

	def set_office(self, office):
		self.office = office

	def can_get_infected(self):
		if self.is_infected or self.has_been_infected:
			return False
		return True

	def set_infected(self, current_day):
		self.is_infected = True
		self.has_been_infected = True
		self.day_infected = current_day

	def update_status(self, current_day):
		if not self.is_alive:
			return

		if self.is_infected:
			if self.dies():
				self.is_alive = False
				self.is_infected = False
				self.has_symptoms = False
				self.is_isolated = True
				return

			if self.day_infected + self.days_until_symptoms == current_day:
				self.has_symptoms = True
				self.is_isolated = True

			if self.day_infected + self.total_days_sick == current_day:
				self.is_infected = False
				self.is_isolated = False
				self.has_symptoms = False

		if not self.is_infected and self.is_isolated:
			if self.day_isolated + self.total_days_sick == current_day:
				self.is_isolated = False

	def update_location(self, current_time):
		pass

	def dies(self):
		return rn.random() < self.mortality_rate

	def set_in_isolation(self, current_day):
		if not self.is_isolated:
			self.is_isolated = True
			self.day_isolated = current_day
