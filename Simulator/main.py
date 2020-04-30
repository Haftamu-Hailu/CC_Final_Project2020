from sys import argv
import math
import uuid
import random as rn
from agent import Agent
from simulation import simulation


#main to initialize the simulation
# python3 main.py True 1000 20 30 0.05 21 14 30 0.01 0.036
# python3  main.py <Contact tracing en> <#Agents> <#infected> <office_capacity> <mortality_rate> <# days sick> <# days in isolation> <# days simulated> <infecetion risk home> <infection risk work>

#number of Agents
nrA = int(argv[2])
#number of initially infected not quarantined agents
iI = int(argv[3])
#number of initially healthy agents
iH = nrA - iI
#number of offices (nr of agents div office_capacity)
office_capacity = int(argv[4])
nrO = math.ceil(nrA/office_capacity)
#Mortality rate
mr = float(argv[5])
#number of days sick
nrSDays = int(argv[6])
#number of days isolation
nrIDays = int(argv[7])
#number of days
nrDays = int(argv[8])
#risk of infection at home
rIH = float(argv[9])
#risk of infection at work
rIW = float(argv[10])

#initialize agents

#loop creates list with IDs for every agent
idArray = []
print("-- Generating IDs --")
for i in range(nrA):
	idArray.append(uuid.uuid4().hex)

#Loop to create healthy agents
print("-- creating healthy agents --")
for i in range(iH):
	idArray[i] = Agent(idArray[i],'H')

#Loop to create infected agents not 100%  sure this works
print("-- infected healthy agents --")
for i in range(iH, nrA):
	idArray[i] = Agent(idArray[i],'I')

#Loop to assign agents to households of 2
print("-- assign agents to households of 2 --")
counter = nrA
while counter >1:
	#generates a random integer in range 0, nrA
	i = rn.randrange(nrA)
	j = rn.randrange(nrA)
	if i != j and len(idArray[i].household) == 1 and len(idArray[j].household) == 1:
		idArray[i].household.append(idArray[j].id)
		idArray[j].household.append(idArray[i].id)
		counter-=2
print("-- assign agents to offices of "+ str(office_capacity) +" --")
#Loop assigns agents to an office
for i in idArray:
	while i.office == 0:
		j = rn.randrange(nrO)
		if  len(list(filter(lambda x : x.office == j+1, idArray))) < office_capacity:
			i.office = j+1
#print all agents initialized
#for i in range(nrA):
#	print(i)
#	print("Agent id: "+ str(idArray[i].id) + " Health: "+ str(idArray[i].health) + " office: " + str(idArray[i].office) + " region: " + str(idArray[i].region) + " household: ")
#	print(idArray[i].household)
#for i in range(nrO):
#	print( "Office " + str(i+1) + "has capacity"+str(len(list(filter(lambda x : x.office == i+1, idArray)))))
#start simulation
simulation(argv[1],nrA, iI, iH, office_capacity, nrO, mr, nrSDays, nrIDays, nrDays, rIH, rIW, idArray)