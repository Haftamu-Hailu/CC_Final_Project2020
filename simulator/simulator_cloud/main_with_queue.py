import boto3
import time
import json
from initializer import initialize
from simulator import Simulator
from saver import Saver

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

    simulation_id = initial_data['simulation_id'].replace("-", "_")

    locations, agent_array = initialize(total_agents, initially_infected_agents, initially_healthy_agents,
                                        office_capacity, house_capacity, mortality_rate, total_days_sick,
                                        days_until_symptoms, total_days_simulated, risk_infection_home,
                                        risk_infection_work)

    saver = Saver(verbose, simulation_id)
    simulator = Simulator(enable_contact_tracing, locations, agent_array, saver, simulation_id)

    saver.initialize_db(locations, agent_array)

    while simulator.current_day <= total_days_simulated:
        simulator.step()

    return 200, saver.overview


def send_message(message):
    sqs = boto3.client('sqs',region_name='eu-west-2',
                    aws_access_key_id="AKIAWWEQQOG3FWVNHG4V", 
                    aws_secret_access_key="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")
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
                    aws_access_key_id="AKIAZBFSLRGGYX7XKBDO",
                    aws_secret_access_key="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")
    

    while True:
        time.sleep(3)
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
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            print("Message deleted from queue")
            initial_data = json.loads(response['Messages'][0]['Body'])["initial_data"]
            simulation_id = response["Messages"][0]['MessageAttributes']["Simulation_id"]['StringValue']

            initial_data["simulation_id"] = simulation_id
            start_simulation(initial_data)
            print("Simulation started")

        except KeyError as e:
            print(repr(e))
            print("Queue is empty")

if __name__ == '__main__':
    main()