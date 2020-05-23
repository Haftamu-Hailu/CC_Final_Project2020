import pymysql
import logging
import Config.mysql_config as config

UNKNOWN_DATABASE_ERROR = 1049
TABLE_ALREADY_EXISTS_ERROR = 1050


class MySQLDatabase:
    """Database connection class."""

    def __init__(self):
        self.host = config.host
        self.username = config.username
        self.password = config.password
        self.port = config.port
        self.dbname = config.dbname
        self.conn = None

        self.create_overview_table()
        self.insert_overview_data(155, 300, 50, 60, 10, 4)

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
            create_overview_query = """CREATE TABLE Overview( 
                                                 Day int(11) NOT NULL,
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


    def insert_overview_data(self, day, currently_infected_agents, total_infected_agents, currently_symptomatic_agents, total_isolated_agents, dead_agents):
        """ Inserting Data Into Overview Table """
        try:
            self.open_connection()
            insert_query = f"INSERT INTO Overview(Day, CurrInfectedA, TotInfectedA, Sympt_A, TotIsolatedA, TotDeadA) " \
                           f"VALUES ({day},{currently_infected_agents},{total_infected_agents}, {currently_symptomatic_agents},{total_isolated_agents},{dead_agents}) "

            cursor = self.conn.cursor()
            result = cursor.execute(insert_query)
            self.conn.commit()
            logging.info("Data Inserted successfully")

        except pymysql.MySQLError as e:
            logging.error(e)