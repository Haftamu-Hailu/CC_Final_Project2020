import boto3
import time
import json
from initializer import initialize
from simulator import Simulator
from saver import Saver
import os

def start_simulation(initial_data, verbose=True):
    enable_contact_tracing = bool(initial_data['contact_tracing'])  # Enable contact tracing
    total_agents = int(initial_data['total_agents'])  # Number of Agents
    initially_infected_agents = int(initial_data['infected_agents'])  # Number of initially infected agents
    initially_healthy_agents = int(total_agents - initially_infected_agents)  # Number of initially healthy agents
    office_capacity = int(initial_data['office_capacity'])  # Capacity of agents per office
    house_capacity = int(initial_data['home_capacity'])  # Capacity of agents per house
    mortality_rate = float(initial_data['mortality_rate'])  # Mortality rate
    total_days_sick = int(initial_data['sick_days'])  # Number of days sick
    days_until_symptoms = int(initial_data['free_symptoms_days'])  # Number of days until symptoms
    total_days_simulated = int(initial_data['total_days'])  # Number of days of simulation
    risk_infection_home = float(initial_data['risk_home'])  # Risk of infection at home
    risk_infection_work = float(initial_data['risk_work'])  # Risk of infection at work
    verbose = bool(verbose)  # If we want printing during simulator run

    simulation_id = "local_testing "# TODO: initial_data['simulation_id']

    locations, agent_array = initialize(total_agents, initially_infected_agents, initially_healthy_agents,
                                        office_capacity, house_capacity, mortality_rate, total_days_sick,
                                        days_until_symptoms, total_days_simulated, risk_infection_home,
                                        risk_infection_work)

    saver = Saver(verbose, simulation_id)
    simulator = Simulator(enable_contact_tracing, locations, agent_array, saver)

    saver.initialize_db(locations, agent_array)

    while simulator.current_day <= total_days_simulated:
        simulator.step()

    return 200, saver.overview


def send_message(message):
    sqs = boto3.client('sqs',region_name='eu-west-2',
                    aws_access_key_id=os.environ['access_id'],
                    aws_secret_access_key=os.environ['access_key'])
    queue_url = 'https://sqs.eu-west-2.amazonaws.com/459864568246/conf_queue'
    sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Email': {
            'DataType': 'String',
            'StringValue': 'Simulation Start successful'
        },
        },
    MessageBody= message
    )
    print("sent message")

def main():
    sqs = boto3.client('sqs',region_name='eu-west-1',
                    aws_access_key_id=os.environ['access_id'],
                    aws_secret_access_key=os.environ['access_key'])
    
    #ditc = json.dumps({"initial_data" : {"contact_tracing" : 0, "total_agents": 10, "infected_agents": 1, "office_capacity" : 5, "home_capacity" : 2, "mortality_rate":0.04, "sick_days": 21, "free_symptoms_days":14 ,"total_days":30, "risk_home": 0.1, "risk_work": 0.03}})
    #send_message(ditc)

    while True:
        time.sleep(10)
        queue_url = 'https://sqs.eu-west-1.amazonaws.com/620996823437/CCBDAProject-Queue.fifo'
        response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=30,
        WaitTimeSeconds=0
        )

        #print(response)
        try:
            receipt_handle = response['Messages'][0]['ReceiptHandle']
            print("Message received from queue")
            #print(response['Messages'][0])
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            print("Message deleted from queue")
            #print(response['Messages'][0]['Body'])
            argv = json.loads(response['Messages'][0]['Body'])
            #print(argv)
            #print(argv)
            #for i in argv['initial_data']:
            #        print(argv['initial_data'][i])
            start_simulation(argv['initial_data'])
            print("Simulation started")
            #send_message(argv)
            #continue
        except KeyError as e:
            print(repr(e))
            print("Queue is empty")

if __name__ == '__main__':
    main()
