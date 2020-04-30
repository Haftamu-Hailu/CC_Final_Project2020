class Agent:
	#initializes an Agent with custom variables
	def __init__(self,id,health_status):
		#id
		self.id = id
		#health state
		self.health = health_status
		#lives with
		self.household = [self.id]
		#work place
		self.office = 0
		#Region state starts at home for every agen
		self.region = 'home'
		#days sick
		self.sick_days = 0
		#days in isolation
		self.isolation_days = 0