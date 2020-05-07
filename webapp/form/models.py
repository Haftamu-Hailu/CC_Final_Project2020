from django.db import models
import logging

logger = logging.getLogger(__name__)


class Simulator(models.Model):

    def get_initial_data(self, post_data):
        initial_data = self.str_2_initial_data(post_data)
        return initial_data

    def str_2_initial_data(self, post_data):
        initial_data = {}
        initial_data['contact_tracing'] = True if post_data['contact_tracing'] == 'Yes' else False
        initial_data['total_agents'] = int(post_data['total_agents'])
        initial_data['infected_agents'] = int(post_data['infected_agents'])
        initial_data['office_capacity'] = int(post_data['office_capacity'])
        initial_data['home_capacity'] = int(post_data['home_capacity'])
        initial_data['mortality_rate'] = float(post_data['mortality_rate'])
        initial_data['risk_home'] = float(post_data['risk_home'])
        initial_data['risk_work'] = float(post_data['risk_work'])
        initial_data['sick_days'] = int(post_data['sick_days'])
        initial_data['free_symptoms_days'] = int(post_data['free_symptoms_days'])
        initial_data['total_days'] = int(post_data['total_days'])
        return initial_data
