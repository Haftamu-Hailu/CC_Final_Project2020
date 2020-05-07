from django.db import models
import boto3
import os
import logging

# STARTUP_SIGNUP_TABLE = os.environ['STARTUP_SIGNUP_TABLE']
# AWS_REGION = os.environ['AWS_REGION']
# NEW_SIGNUP_TOPIC = os.environ['NEW_SIGNUP_TOPIC']
# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

logger = logging.getLogger(__name__)


class Simulator(models.Model):

    def get_initial_data(self, post_data):
        initial_data = self.str_2_initial_data(post_data)
        return 200

    def str_2_initial_data(self, post_data):
        initial_data = {}
        initial_data['total_agents'] = int(post_data['total_agents'])
        initial_data['infected_agents'] = int(post_data['infected_agents'])
        initial_data['office_capacity'] = int(post_data['office_capacity'])
        initial_data['mortality_rate'] = float(post_data['mortality_rate'])
        initial_data['risk_home'] = float(post_data['risk_home'])
        initial_data['risk_work'] = float(post_data['risk_work'])
        initial_data['sick_days'] = int(post_data['sick_days'])
        initial_data['isolated_days'] = int(post_data['isolated_days'])
        initial_data['total_days'] = int(post_data['total_days'])
        return initial_data
