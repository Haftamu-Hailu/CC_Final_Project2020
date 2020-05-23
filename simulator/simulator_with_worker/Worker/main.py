import boto3
import simulator_functions as worker
import initializer as init
import time
import json

queue_url_send = 'https://sqs.eu-west-2.amazonaws.com/459864568246/conf_queue'
queue_url_receive = 'https://sqs.eu-west-2.amazonaws.com/459864568246/sim_test'
sqs = boto3.client('sqs',region_name='eu-west-2',
					aws_access_key_id="",
					aws_secret_access_key="")
def main():
	while True:
		print("New While entered:::::::::::::::::::::::::::::::::::::::::::::::")
		time.sleep(1)
		queue_url = 'https://sqs.eu-west-2.amazonaws.com/459864568246/sim_test'
		response = sqs.receive_message(
		QueueUrl=queue_url,
		AttributeNames=[
			'SentTimestamp'
		],
		MaxNumberOfMessages=10,
		MessageAttributeNames=[
			'All'
		],
		VisibilityTimeout=30,
		WaitTimeSeconds=0
		)
#{"initial_data" : {"contact_tracing" : 0, "total_agents": 10, "infected_agents": 1, "office_capacity" : 5, "home_capacity" : 2, "mortality_rate":0.04, "sick_days": 21, "free_symptoms_days":14 ,"total_days":30, "risk_home": 0.1, "risk_work": 0.03}})

		try:
			for message in response['Messages']:
				receipt_handle = message['ReceiptHandle']
				print("Messages received from queue")
				argv = json.loads(message['Body'])
				if(argv['method']=='createhealthyAgent'):
					#nr, days_until_symptoms,mortality_rate
					print("createhealthyAgent")
					nr = int(argv['nr'])
					days_until_symptoms = int(argv['days_until_symptoms'])
					mortality_rate = argv['mortality_rate']
					result = init.createhealthyAgent(nr, days_until_symptoms, mortality_rate)
				if(argv['method']=='createinfectedAgent'):
					#nr, days_until_symptoms,mortality_rate
					print("createinfectedAgent")
					nr = int(argv['nr'])
					days_until_symptoms = int(argv['days_until_symptoms'])
					mortality_rate = float(argv['mortality_rate'])
					result = init.createinfectedAgent(nr, days_until_symptoms, mortality_rate)
				if(argv['method']=='assigntoHousehold'):
					#house_id,house_capacity, risk_infection_home, ids
					print("assigntoHousehold")
					house_id = int(argv['house_id'])
					house_capacity = int(argv['house_capacity'])
					risk_infection_home = float(argv['risk_infection_home'])
					ids = list(argv['array'])
					result = init.assigntoHousehold(house_id, house_capacity, risk_infection_home, ids)
				if(argv['method']=='assigntoOffice'):
					#office_id, office_capacity, risk_infection_work, ids
					print("assigntoOffice")
					office_id = int(argv['office_id'])
					office_capacity = int(argv['office_capacity'])
					risk_infection_work = float(argv['risk_infection_work'])
					ids= list(argv['array'])
					result = init.assigntoOffice(office_id, office_capacity, risk_infection_work, ids)
				if(argv['method']=='simulate_infection'):
					print("simulate_infection")
					#simulate_infection(location, array_subjects, risk, current_day)
					location=argv['location']
					array_subjects = list(argv['array_subjects'])
					risk = float(argv['risk'])
					
					current_day = int(argv['current_day'])
					result = worker.simulate_infection(location, array_subjects, risk, current_day)
				if(argv['method']=='end_of_day'):
					print("end_of_day")
					#end_of_day(contact_tracing, max_sick_time, current_day)
					contact_tracing=bool(argv['contact_tracing'])
					max_sick_time=int(argv['max_sick_time'])
					current_day=int(argv['current_day'])
					result = worker.end_of_day(contact_tracing, max_sick_time, current_day)
				if(result):
					sqs.delete_message(
					QueueUrl=queue_url,
					ReceiptHandle=receipt_handle
					)
					send_message(result, queue_url_send)
				else:
					print("Message could not be processed")
		except KeyError as e:
			print(repr(e))
			print("Queue is empty")

def send_message(message, queue_url):
	sqs.send_message(
	QueueUrl=queue_url,
	DelaySeconds=0,
	MessageAttributes={
		'R': {
			'DataType': 'String',
			'StringValue': '1'
		},
		},
	MessageBody= message
	)
	return "sent message"

if __name__ == '__main__':
	main()