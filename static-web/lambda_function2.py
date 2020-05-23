import sys
import logging
import pymysql
import json

#rds settings
rds_host = "ccbdaproject-testing-1.cadpkk0zdpr3.eu-west-1.rds.amazonaws.com"
name = "admin"
password = "Pr0ject1"
db_name = "innodb"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded.")


def respond(err, res=None):
    if not err:
        logger.info('SUCCESS: Results fetched from db.')

    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps(str(err) if err else res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }


def lambda_handler(event, context):
    operation = event['requestContext']['http']['method']
    if operation == 'POST':
        body_dict = json.loads(event['body'])
        simulation_id = body_dict['simulation_id']
        query = "select * from innodb.`Overview-{}`".format(simulation_id)
        records = []
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
            for row in cur:
                record = {
                    'day': row[0],
                    'currently_infected': row[1],
                    'total_infected': row[2],
                    'sympt': row[3],
                    'total_isolated': row[4],
                    'total_dead': row[5],
                }
                records.append(record)
        return respond(None, records)
    else:
        return respond(ValueError('Unsupported method {}'.format(operation)))