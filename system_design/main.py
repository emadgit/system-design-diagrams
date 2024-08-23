# set GROQ_API_KEY in the secrets
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB, Route53


def start():
    print("The basic starter design")
    with Diagram("Web Service", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")


def clusteredWebSerivce():
    with Diagram("Clustered Web Services", show=False):
        dns = Route53("dns")
        lb = ELB("lb")

        with Cluster("Services"):
            svc_group = [ECS("web1"), ECS("web2"), ECS("web3")]

        with Cluster("DB Cluster"):
            db_primary = RDS("userdb")
            db_primary - [RDS("userdb ro")]

        memcached = ElastiCache("memcached")

        dns >> lb >> svc_group
        svc_group >> db_primary
        svc_group >> memcached
