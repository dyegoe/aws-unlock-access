from flask import Flask, request
import boto3
import random
import string

app = Flask(__name__)

s = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(256))


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/unlock/<code>")
def app_unlock(code):
    if code == s:
        ip_address = "{}/32".format(request.environ.get("HTTP_X_REAL_IP", request.remote_addr))
        print(ip_address)
        ip_address = "82.131.117.224/32"
        session = boto3.Session(region_name="sa-east-1", profile_name="brx-dyego")
        ec2 = session.resource("ec2")
        security_group = ec2.SecurityGroup("sg-01c19652d60c0ba8a")
        response = security_group.authorize_ingress(
            IpPermissions=[
                {
                    "FromPort": 443,
                    "ToPort": 443,
                    "IpProtocol": "TCP",
                    "IpRanges": [
                        {
                            "CidrIp": ip_address,
                            "Description": "string"
                        }
                    ]
                }
            ]
        )
        print(response)
        return "Access granted"
        # return request.environ.get("HTTP_X_REAL_IP", request.remote_addr)
    else:
        return "Wrong code"


if __name__ == "__main__":
    print(f"http://127.0.0.1:5000/unlock/{s}")
    app.run(host="0.0.0.0", debug=True)
