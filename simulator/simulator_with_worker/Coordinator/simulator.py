import math
import random as rn
from sqlalchemy import create_engine, or_, and_, MetaData, Table
from sqlalchemy.sql import select
import json 

from sqs_handler import receive_message, send_message, delete_message

class Simulator:
    def __init__(self, enable_contact_tracing, saver, numberofHomes, numberofOffices, numberofAgents, infection_risk_Office, infection_risk_Home, total_days_sick):
        self.enable_contact_tracing = enable_contact_tracing
        self.current_day = 0
        self.step_size = 1
        self._sick = total_days_sick
        self.saver = saver
        self.nrHomes= numberofHomes
        self.nrOffices = numberofOffices
        self.nrAgents = numberofAgents
        self.inf_Office = infection_risk_Office
        self.inf_Home = infection_risk_Home
        self.batchsize = 10
        self.queue_url_receive = 'https://sqs.eu-west-2.amazonaws.com/459864568246/conf_queue'
        self.queue_url_send = 'https://sqs.eu-west-2.amazonaws.com/459864568246/sim_test'
        self.number_of_batchesOffices = math.ceil(self.nrOffices/self.batchsize)
        self.number_of_batchesHomes = math.ceil(self.nrHomes/self.batchsize)

    # Amount of  per step
    def step(self):
        # Simulate infections in each location

        array = []
        for office in range(self.nrOffices):
            array.append(office+1)
            if len(array) == self.batchsize or office+1 == self.nrOffices:
                #simw.simulate_infection('office', array, self.inf_Office, self.current_day)
                message = json.dumps({'method':'simulate_infection', 'location': 'office', 'array_subjects': array, 'risk': self.inf_Office, 'current_day': self.current_day})
                send_message(message,self.queue_url_send)
                array.clear()
        
        #wait all   
        nr_msg = 0
        while nr_msg < self.number_of_batchesOffices:
            
            response = receive_message(self.queue_url_receive, 1000)
            print("nr_msg office infections = ", nr_msg, "exptected :", self.nrOffices)
            try:
                for message in response['Messages']:
                    if message['MessageAttributes']['R']['StringValue']=='1':
                        nr_msg+=1
                        delete_message(message, self.queue_url_receive)

            except KeyError as e:
                print(repr(e))
                print("Queue is empty")
        
        array.clear()

        for home in range(self.nrHomes):
            array.append(home+1)
            if len(array) == self.batchsize or home+1 == self.nrHomes:
                #simw.simulate_infection('home', array, self.inf_Home, self.current_day)
                message = json.dumps({'method':'simulate_infection', 'location': 'home', 'array_subjects': array, 'risk': self.inf_Home, 'current_day': self.current_day})
                send_message(message,self.queue_url_send)
                array.clear()
        
        #wait all
        nr_msg = 0
        while nr_msg < self.number_of_batchesHomes:
            
            print("nr_msg office infections = ", nr_msg, "exptected :", self.nrHomes)
            response = receive_message(self.queue_url_receive, 1000)
            try:
                for message in response['Messages']:
                    if message['MessageAttributes']['R']['StringValue']=='1':
                        nr_msg+=1
                        delete_message(message, self.queue_url_receive)
            except KeyError as e:
                print(repr(e))
                print("Queue is empty")
        
        #End of day update       
        message = json.dumps({'method':'end_of_day', 'contact_tracing': int(self.enable_contact_tracing), 'max_sick_time':self._sick,'current_day': self.current_day})
        send_message(message,self.queue_url_send)
        
        #wait end_of_day
        reply = ''
        while reply is not 'end_of_day':
            
            print("waiting for end_of_day")
            response = receive_message(self.queue_url_receive, 1)
            try:
                reply = response['Messages'][0]['Body']
                print(reply)
                if response['Messages'][0]['MessageAttributes']['R']['StringValue']=='1':
                    delete_message(response['Messages'][0], self.queue_url_receive)
                    reply = 'end_of_day'

            except KeyError as e:
                print(repr(e))
                print("Queue is empty")
        
        self.save_status()
        self.current_day += 1

    def save_status(self):
        host = "sim-database.cum3wdeshheg.eu-west-2.rds.amazonaws.com"
        username = ""
        password = ""
        port = 3306
        dbname = "simdatabase"
        engine = create_engine("mysql+pymysql://" + username +":" + password +"@"+host + "/"+dbname,echo = True)
        meta = MetaData(engine)
        conn = engine.connect()
        table = Table('Agent_Table', meta, autoload=True, autoload_with=engine)
        select_o= table.select()
        agent_array= conn.execute(select_o)
        currently_infected_agents = sum(1 if agent.is_infected else 0 for agent in agent_array)
        agent_arra= conn.execute(select_o)
        total_infected_agents = sum(1 if agent.has_been_infected else 0 for agent in agent_arra)
        agent_arr= conn.execute(select_o)
        currently_symptomatic_agents = sum(1 if agent.has_symptoms else 0 for agent in agent_arr)
        agent_ar= conn.execute(select_o)
        total_isolated_agents = sum(1 if agent.is_isolated else 0 for agent in agent_ar)
        agent_a= conn.execute(select_o)
        dead_agents = sum(1 if not agent.is_alive else 0 for agent in agent_a)
        self.saver.save_overview(self.current_day, currently_infected_agents, total_infected_agents, currently_symptomatic_agents,total_isolated_agents, dead_agents)

