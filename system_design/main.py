# set GROQ_API_KEY in the secrets
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, ECS
from diagrams.aws.database import ElastiCache, RDS, Dynamodb
from diagrams.aws.network import ELB, Route53, APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.aws.general import User
from diagrams.aws.analytics import Quicksight


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


def languageAppPrototype():
    with Diagram("Spaced Repetition App Architecture", show=False):
        user = User("User")

        # Frontend Interaction
        user_frontend = user >> APIGateway("API Gateway")

        # Load Balancer and Backend Servers
        lb = ELB("Load Balancer")
        backend = [
            EC2("Auth Service"),
            EC2("User Profile Service"),
            EC2("Content Delivery Service"),
            EC2("Spaced Repetition Engine"),
            EC2("Notification Service"),
            EC2("Progress Tracker"),
            EC2("Analytics Service"),
        ]

        user_frontend >> lb >> backend

        # Data Storage
        db = RDS("Relational DB (PostgreSQL)")
        nosql_db = Dynamodb("NoSQL DB (DynamoDB)")
        static_storage = S3("Content Storage (S3)")

        backend >> db
        backend >> nosql_db
        backend >> static_storage

        # Monitoring and Analytics
        monitoring = Cloudwatch("Monitoring (CloudWatch)")
        analytics = Quicksight("Analytics (QuickSight)")

        backend >> monitoring
        backend >> analytics
