import os
import Simulator.Config.mysql_config as db
# Our script for setting everything up online - should not be part of the github repo as it contains sensitive data



#------------ Setting up the MySQL Database ---------------
# Creating security group for the database


host = db.host
username = db.username
password = db.password
port = db.port
dbname = db.dbname
instance_identifier = db.instance_identifier

os.system(f"aws rds create-db-instance --db-name {dbname} --engine MySQL "
          f"--db-instance-identifier {instance_identifier} --backup-retention-period 3 "
          f"--db-instance-class db.t2.micro --allocated-storage 5 --no-publicly-accessible "
          f"--master-username {username} --master-user-password {password}")

