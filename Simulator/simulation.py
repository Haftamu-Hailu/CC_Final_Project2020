import random as rn
#function determines whether an agents gets sick with given probability
def decision(prob):
    return rn.random() < prob

#simulation
def simulation(c_tracing,nrA, iI, iH, office_capacity, nrO, mr, nrSDays, nrIDays, nrDays, rIH, rIW, idArray):
	#Total number of infected
	total_infected = iI
	#number of max isolated
	peak_isolation = 0
	print('-'*20+ '\n')
	print("Contact tracing: " + str(c_tracing) +  " Number of agents: " + str(nrA))
	print("Day: "+ str(0) +" total infected: "+ str(total_infected) + " currently infected: "+ str(len(list(filter(lambda x : x.health =='I' or x.health =='II' or x.health =='ID', idArray)))) + " currently isolated: "+ str(len(list(filter(lambda x : x.health =='HI' or x.health =='II' or x.health =='ID', idArray)))) + " dead: " + str(len(list(filter(lambda x : x.health =='D', idArray)))))
	print('-'*20+ '\n')
	#Loop for number of days nrDays
	for d in range(nrDays):

		#change status of infected to infected and isolated, determine whether agent will die and send out contact tracing notifications
		for i in list(filter(lambda x : x.sick_days == 5, idArray)):
			#will die?
			if decision(mr):
				i.health = 'ID'
				#print("Day: "+ str(d + 1) +" Agent id: "+ str(i.id) + " Health: "+ str(i.health)+ " Sickdays: "+ str(i.sick_days))
			#else person will be infected and isolated
			else:
				i.health = 'II'
				#print("Day: "+ str(d + 1) +" Agent id: "+ str(i.id) + " Health: "+ str(i.health)+ " Sickdays: "+ str(i.sick_days))
			#contact tracing
			if c_tracing:
				#print("Contact")
				for j in list(filter(lambda x : x.office == i.office or x.household == i.household, idArray)):
					#healthy agents change status to healthy and isolated at home
					if j.health == 'H':
						j.health = 'HI'
					elif j.health =='I':
						j.health = 'II'
					#print('notification sent to ' + str(j.id) + ' health status of ' + j.id + ' set to ' + str(j.health))
		#for all agents who have been sick for the number of days change status to immune IM or dead D
		for i in list(filter(lambda x : x.sick_days == nrSDays, idArray)):
			#print("Day: "+ str(d + 1) +" Agent id: "+ str(i.id) + " Health: "+ str(i.health))
			if i.health == 'II':
				i.health = 'IM'
				i.sick_days = 0
			elif i.health == 'ID':
				i.health = 'D'
				i.sick_days = 0

		
		for i in list(filter(lambda x : x.isolation_days == nrIDays and x.health == 'HI', idArray)):
			#print("Day: "+ str(d + 1) +" Agent id: "+ str(i.id) + " Health: "+ str(i.health))
			i.health = 'H'


		#change status of all agents to work
		for i in list(filter(lambda x : x.health == 'H' or x.health == 'IM' or x.health == 'I', idArray)):
			i.region = 'work'
			#print("Day: "+ str(d + 1) +" Agent id: "+ str(i.id) + " region: "+ str(i.region))
		
		#is someone in the office infected? yes calculate whether agent is now infected
		for i in list(filter(lambda x : x.health == 'I', idArray)):
			for j in list(filter(lambda x : x.office == i.office and x.health != 'I' and x.health !='IM'and x.health !='ID'and x.health !='II', idArray)):
				#print("Day: "+ str(d + 1) +" Agent id: "+ str(j.id) + " region: "+ str(j.office))
				if decision(rIW):
					j.health = 'I'
					total_infected +=1
		
		#change status of all agents to home 
		for i in  list(filter(lambda x : x.region == 'work', idArray)):
			i.region = 'home'
			#print("Day: "+ str(d + 1) +" Agent id: "+ str(i.id) + " region: "+ str(i.region))
		
		#is someone at home infected? yes calculate whether agent is now infected
		for i in list(filter(lambda x : x.health == 'I', idArray)):
			for j in list(filter(lambda x : x.household == i.household and x.health != 'I' and x.health !='IM'and x.health !='ID'and x.health !='II', idArray)):
				#print("Day: "+ str(d + 1) +" Agent id: "+ str(j.id) + " region: "+ str(j.office))
				if decision(rIH):
					j.health = 'I'
					total_infected +=1

		#for i in range(nrA):
			#print("Day: "+ str(d + 1) +" Agent id: "+ str(idArray[i].id) + " Health: "+ str(idArray[i].health))
		#increase the number of days sick for infected by 1
		for i in list(filter(lambda x : x.health == 'I' or x.health =='II'or x.health =='ID', idArray)):
			i.sick_days +=1
			#print(i.sick_days)
		#increase the number of days in isolation by 1
		for i in list(filter(lambda x : x.health == 'HI', idArray)):
			i.isolation_days+=1
			#print(i.sick_days)
		peak_isolation = max(len(list(filter(lambda x : x.health =='HI' or x.health =='II' or x.health =='ID', idArray))), peak_isolation)
		print("Day: "+ str(d + 1) +" total infected "+ str(total_infected) +
			" currently infected: "+ str(len(list(filter(lambda x : x.health =='I' or x.health =='II' or x.health =='ID', idArray)))) +
			" currently isolated: "+ str(len(list(filter(lambda x : x.health =='HI' or x.health =='II' or x.health =='ID', idArray)))) +
			" dead: " + str(len(list(filter(lambda x : x.health =='D', idArray))))+
			", peak isolation" + str(peak_isolation))

	print('-'*20 + '\n')
	print("Over " + str(nrDays) + " days " + str(total_infected) + " agents were infected.")
	print(str(len(list(filter(lambda x : x.health =='D', idArray)))) + " agents died, peak isolation was at " + str(peak_isolation)+ ", " + str(len(list(filter(lambda x : x.health =='IM', idArray)))) + " recovered.")