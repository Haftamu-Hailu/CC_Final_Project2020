import sys
import logging
import pymysql
#rds settings
rds_host = "ccbdaproject-testing-1.cadpkk0zdpr3.eu-west-1.rds.amazonaws.com"
name = 'admin'
password = 'Pr0ject'
db_name = 'ccbdaproject-testing-1'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

item_count = 0

with conn.cursor() as cur:
    cur.execute("create table 473907d4-0eb2-4dad-93f1-cda2baa5b545 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
    cur.execute('insert into Employee (EmpID, Name) values(1, "Joe")')
    cur.execute('insert into Employee (EmpID, Name) values(2, "Bob")')
    cur.execute('insert into Employee (EmpID, Name) values(3, "Mary")')
    conn.commit()
    cur.execute("select * from Employee")
    for row in cur:
        item_count += 1
        logger.info(row)
        #print(row)
conn.commit()

