import os

image_id = "ami-0c207044c8e195b8a"  # Final simulator
security_group = "sg-14e85758"
key_name = "ccbda-project-simulator-key"

boot_ec2_command = f"aws ec2 run-instances --image-id {image_id} --count 1 --instance-type t2.micro " \
                   f"--key-name {key_name} --security-group-ids {security_group}"
os.system(boot_ec2_command)