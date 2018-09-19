import boto3

session = boto3.Session(region_name='sa-east-1', profile_name='brx-dyego')
ec2 = session.resource('ec2')
security_group = ec2.SecurityGroup('sg-6a72b80d')
print(security_group.ip_permissions)
