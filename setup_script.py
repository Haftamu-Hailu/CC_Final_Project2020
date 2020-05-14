import os

# Our script for setting everything up online - should not be part of the github repo as it contains sensitive data



# Setting up the MySQL Database
host = "ccbda-rds.cpwaeopvnmcx.eu-west-1.rds.amazonaws.com"
username = "admin"
password = "ccbdadatabase"
port = 3306
dbname = "test"
instance_identifier = "test"

os.system(f"aws rds create-db-instance --db-name {dbname} --engine MySQL "
          f"--db-instance-identifier {instance_identifier} --backup-retention-period 3 "
          f"--db-instance-class db.t2.micro --allocated-storage 5 --no-publicly-accessible "
          f"--master-username {username} --master-user-password {password}")
