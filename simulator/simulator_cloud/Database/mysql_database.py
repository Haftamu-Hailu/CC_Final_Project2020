import pymysql
import logging
import Config.mysql_config as config

UNKNOWN_DATABASE_ERROR = 1049
TABLE_ALREADY_EXISTS_ERROR = 1050


class MySQLDatabase:
    """Database connection class."""

    def __init__(self, simulation_id):
        self.host = config.host
        self.username = config.username
        self.password = config.password
        self.port = config.port
        self.dbname = config.dbname
        self.conn = None

        self.simulation_id = simulation_id

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(self.host,
                                            user=self.username,
                                            passwd=self.password,
                                            db=self.dbname,
                                            connect_timeout=5)
        except pymysql.MySQLError as e:
            logging.error(e)
            if e.args[0] is UNKNOWN_DATABASE_ERROR:
                # The database is not configured properly in the intialization
                logging.error("ERROR IN CONFIGURATION OF DBS, DATABASE INSTANCE NOT CREATED")
        finally:
            logging.info('Connection opened successfully.')

    def create_overview_table(self):
        """
        Create the Overview table in our database
        This should only be run the very first time database is set up
        Looks like: (Day, CurrInfectedA, TotInfectedA, Sympt_A, TotIsolatedA, TotDeadA)
        """
        try:
            self.open_connection()
            create_overview_query = f"CREATE TABLE Overview_{self.simulation_id}(" + \
                                                """Day int(11) NOT NULL,
                                                 CurrInfectedA int(11) NOT NULL,
                                                 TotInfectedA int(11) NOT NULL,
                                                 Sympt_A int(11) NOT NULL,
                                                 TotIsolatedA int(11) NOT NULL,
                                                 TotDeadA int(11) Not NULL,
                                                 PRIMARY KEY (Day)) """
            cursor = self.conn.cursor()
            cursor.execute(create_overview_query)
            logging.info("Overview Table created successfully")

        except pymysql.MySQLError as e:
            logging.error(e)
            if e.args[0] == TABLE_ALREADY_EXISTS_ERROR:
                logging.error("Overview table has already been created")

    def create_agent_table(self):
        """
        Create the Agent table in our database
        This should only be run the very first time database is set up
        Looks like: (Id, CurrInfectedA, TotInfectedA, Sympt_A, TotIsolatedA, TotDeadA)
        """
        try:
            self.open_connection()
            create_agent_table_query = f"CREATE TABLE {self.simulation_id}Agent(" + \
                                              """Id Varchar(40) NOT NULL,
                                                 IsAlive bool NOT NULL,
                                                 HasSymptoms bool NOT NULL,
                                                 IsIsolated bool NOT NULL,
                                                 IsInfected bool NOT NULL,
                                                 HasBeenInfected bool NOT NULL,
                                                 DayInfected VARCHAR(11) NOT NULL,
                                                 DayIsolated VARCHAR(11) NOT NULL,
                                                 Office VARCHAR(11) NOT NULL,
                                                 Home VARCHAR(11) NOT NULL,
                                                 PRIMARY KEY (Id)) """
            cursor = self.conn.cursor()
            cursor.execute(create_agent_table_query)
            logging.info("Agent Table created successfully")

        except pymysql.MySQLError as e:
            logging.error(e)
            if e.args[0] == TABLE_ALREADY_EXISTS_ERROR:
                logging.error("Agent table has already been created")

    def create_location_table(self):
        """
        Create the Location table in our database
        This should only be run the very first time database is set up
        Looks like: (Id, CurrInfectedA, TotInfectedA, Sympt_A, TotIsolatedA, TotDeadA)
        """
        try:
            self.open_connection()
            create_location_table_query = f"CREATE TABLE {self.simulation_id}Location(" + \
                                              """Id VARCHAR(20) NOT NULL,
                                                 Capacity int NOT NULL,
                                                 InfectionRisk float(11) NOT NULL,
                                                 PRIMARY KEY (Id)) """
            cursor = self.conn.cursor()
            cursor.execute(create_location_table_query)
            logging.info("Location Table created successfully")

        except pymysql.MySQLError as e:
            logging.error(e)
            if e.args[0] == TABLE_ALREADY_EXISTS_ERROR:
                logging.error("Location table has already been created")

    def insert_agent(self, agent):
        """ Inserting Agent Into Overview Table """
        try:
            self.open_connection()

            insert_query = f"INSERT INTO {self.simulation_id}Agent(Id, IsAlive, HasSymptoms, IsIsolated, IsInfected, HasBeenInfected, DayInfected, DayIsolated, Office, Home) " \
                           f"VALUES ('{agent.id}',{agent.is_alive},{agent.has_symptoms}, {agent.is_isolated},{agent.is_infected},{agent.has_been_infected},'{agent.day_infected}','{agent.day_isolated}', '{agent.office.id}', '{agent.home.id}')"
            cursor = self.conn.cursor()
            result = cursor.execute(insert_query)
            self.conn.commit()
            logging.info("Data Inserted successfully")

        except pymysql.MySQLError as e:
            logging.error(e)

    def insert_location(self, location):
        """ Inserting Location"""
        try:
            self.open_connection()

            insert_query = f"INSERT INTO {self.simulation_id}Location(Id, Capacity, InfectionRisk) " \
                           f"VALUES ('{location.id}',{location.capacity},{location.infection_risk})"
            cursor = self.conn.cursor()
            result = cursor.execute(insert_query)
            self.conn.commit()
            logging.info("Data Inserted successfully")

        except pymysql.MySQLError as e:
            logging.error(e)

    def insert_overview_data(self, day, currently_infected_agents, total_infected_agents, currently_symptomatic_agents, total_isolated_agents, dead_agents):
        """ Inserting Data Into Overview Table """
        try:
            self.open_connection()
            insert_query = f"INSERT INTO Overview_{self.simulation_id}(Day, CurrInfectedA, TotInfectedA, Sympt_A, TotIsolatedA, TotDeadA) " \
                           f"VALUES ({day},{currently_infected_agents},{total_infected_agents}, {currently_symptomatic_agents},{total_isolated_agents},{dead_agents}) "

            cursor = self.conn.cursor()
            result = cursor.execute(insert_query)
            self.conn.commit()
            logging.info("Data Inserted successfully")

        except pymysql.MySQLError as e:
            logging.error(e)









