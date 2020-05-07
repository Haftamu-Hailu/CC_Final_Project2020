from simulator.initializer import initialize
from simulator.simulator import Simulator
from simulator.saver import Saver


def start_simulation(initial_data, verbose=True):
    enable_contact_tracing = initial_data['contact_tracing']  # Enable contact tracing
    total_agents = initial_data['total_agents']  # Number of Agents
    initially_infected_agents = initial_data['infected_agents']  # Number of initially infected agents
    initially_healthy_agents = total_agents - initially_infected_agents  # Number of initially healthy agents
    office_capacity = initial_data['office_capacity']  # Capacity of agents per office
    house_capacity = initial_data['home_capacity']  # Capacity of agents per house
    mortality_rate = initial_data['mortality_rate']  # Mortality rate
    total_days_sick = initial_data['sick_days']  # Number of days sick
    days_until_symptoms = initial_data['free_symptoms_days']  # Number of days until symptoms
    total_days_simulated = initial_data['total_days']  # Number of days of simulation
    risk_infection_home = initial_data['risk_home']  # Risk of infection at home
    risk_infection_work = initial_data['risk_work']  # Risk of infection at work
    verbose = verbose  # If we want printing during simulator run

    locations, agent_array = initialize(total_agents, initially_infected_agents, initially_healthy_agents,
                                        office_capacity, house_capacity, mortality_rate, total_days_sick,
                                        days_until_symptoms, total_days_simulated, risk_infection_home,
                                        risk_infection_work)

    saver = Saver(verbose)
    simulator = Simulator(enable_contact_tracing, locations, agent_array, saver)

    while simulator.current_day <= total_days_simulated:
        simulator.step()

    return 200, saver.overview
