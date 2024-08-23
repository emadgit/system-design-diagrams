# set GROQ_API_KEY in the secrets
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def start():
    print("The basic starter design")
    with Diagram("Web Service", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")
