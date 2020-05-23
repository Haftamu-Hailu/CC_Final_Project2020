import math
import uuid
import random as rn

from agent import Agent
from Locations.home import Home
from Locations.office import Office

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqs_handler import send_message, receive_message, delete_message
import json

host = "sim-database.cum3wdeshheg.eu-west-2.rds.amazonaws.com"
username = ""
password = ""
port = 3306
dbname = "simdatabase"
engine = create_engine("mysql+pymysql://" + username +":" + password +"@"+host + "/"+dbname,echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

queue_url_receive = 'https://sqs.eu-west-2.amazonaws.com/459864568246/conf_queue'
queue_url_send = 'https://sqs.eu-west-2.amazonaws.com/459864568246/sim_test'

def initialize(total_agents, initially_infected_agents, initially_healthy_agents, office_capacity,
               house_capacity, mortality_rate, total_days_sick, days_until_symptoms, total_days_simulated,
               risk_infection_home, risk_infection_work):
    
    
    #Create tables
    agent_array = [i for i in range(0, total_agents)]
    Agent.createAgentTable(engine)
    Home.createHomeTable(engine)
    Office.createOfficeTable(engine)

    batchsize = 100
    number_of_batchesHagents = 0
    number_of_batchesIagents = 0
    nr_iter = 0
    if initially_healthy_agents >= 100:
        number_of_batchesHagents = int(initially_healthy_agents/batchsize)

    extraBatchH = initially_healthy_agents%batchsize
    if initially_healthy_agents >= 100:
        number_of_batchesIagents = int(initially_infected_agents/batchsize)
    extraBatchI = initially_infected_agents%batchsize

    #from initialize import createhealthyAgent, createinfectedAgent, assigntoHousehold, assigntoOffice
    
    # Create agents
    print("-- Creating healthy agents --")
    print("Number of Batches: ", number_of_batchesHagents)
    if extraBatchH != 0:
        nr_iter +=1
        message = json.dumps({'method':'createhealthyAgent','nr' : extraBatchH , 'days_until_symptoms': days_until_symptoms, 'mortality_rate': mortality_rate}) 
        send_message(message, queue_url_send)
    for i in range(number_of_batchesHagents):
        message = json.dumps({'method':'createhealthyAgent','nr' : batchsize , 'days_until_symptoms': days_until_symptoms, 'mortality_rate': mortality_rate}) 
        send_message(message, queue_url_send)
        print("Batch sent nr. :", i)
        #createhealthyAgent(session, days_until_symptoms ,mortality_rate)
    
    print("-- Creating infected agents --")
    print("Number of Batches: ", number_of_batchesIagents)
    if extraBatchI != 0:
        nr_iter +=1
        message = json.dumps({'method':'createinfectedAgent','nr' : extraBatchI , 'days_until_symptoms': days_until_symptoms, 'mortality_rate': mortality_rate}) 
        send_message(message, queue_url_send)
    for i in range(number_of_batchesIagents):
        message = json.dumps({'method':'createinfectedAgent','nr' : batchsize , 'days_until_symptoms': days_until_symptoms, 'mortality_rate': mortality_rate}) 
        print("Batch sent nr. :", i)
        send_message(message, queue_url_send)
        #createhealthyAgent(session, days_until_symptoms ,mortality_rate)

    #Waitall
    nr_iter += number_of_batchesHagents+number_of_batchesIagents
    print("nr_iter ", nr_iter)
    nr_msg = 0
    while nr_msg < nr_iter:
        
        print("nr_msg agent creation = ", nr_msg, "exptected :", nr_iter)
        try:
            response = receive_message(queue_url_receive, 1000)
            for message in response['Messages']:
                print(message)
                if message['MessageAttributes']['R']['StringValue']=='1':
                    nr_msg+=1
                    delete_message(message, queue_url_receive)

        except KeyError as e:
            print(repr(e))
            print("Queue is empty")
    
    
    # Shuffle the list to mix infected and healthy agents
    rn.shuffle(agent_array)
    
    # Create locations


    number_of_homes = math.ceil(total_agents / house_capacity)
    number_of_offices = math.ceil(total_agents / office_capacity)


    print("-- Assign agents to households --")
    array = []
    house_id=1
    for nr in agent_array:
        array.append(nr+1)
        if len(array) == house_capacity or nr == agent_array[-1]:
            message = json.dumps({'method':'assigntoHousehold','house_id' : house_id , 'house_capacity': house_capacity, 'risk_infection_home': risk_infection_home, 'array': array}) 
            send_message(message, queue_url_send)
            #assigntoHousehold(house_id, house_capacity, risk_infection_home, array)
            array.clear()
            house_id+=1
    array.clear()

    
    # Shuffle again to mix households
    rn.shuffle(agent_array)
    
    #Waitall
    nr_msg = 0
    while nr_msg < number_of_homes:
        
        print("nr_msg homecreation = ", nr_msg, "exptected :", number_of_homes)
        response = receive_message(queue_url_receive, 1000)
        try:
            for message in response['Messages']:
                if message['MessageAttributes']['R']['StringValue']=='1':
                    nr_msg+=1
                    delete_message(message, queue_url_receive)

        except KeyError as e:
            print(repr(e))
            print("Queue is empty")
    

    print("-- Assign agents to offices --")
    office_id = 1
    for nr in agent_array:
        array.append(nr+1)
        if len(array) == office_capacity or nr == agent_array[-1]:
            message = json.dumps({'method':'assigntoOffice','office_id' : office_id , 'office_capacity': office_capacity, 'risk_infection_work': risk_infection_work, 'array': array}) 
            send_message(message, queue_url_send)
            #assigntoOffice(office_id, office_capacity, risk_infection_work, array)
            array.clear()
            office_id+=1
    
    #Waitall
    nr_msg = 0
    while nr_msg < number_of_offices:
        
        response = receive_message(queue_url_receive, 1000)
        print("nr_msg office creation = ", nr_msg, "exptected :", number_of_offices)
        try:
            for message in response['Messages']:
                if message['MessageAttributes']['R']['StringValue']=='1':
                    nr_msg+=1
                    delete_message(message, queue_url_receive)

        except KeyError as e:
            print(repr(e))
            print("Queue is empty")
    

    return number_of_offices, number_of_homes