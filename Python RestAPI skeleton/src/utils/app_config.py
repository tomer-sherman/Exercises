from dotenv import load_dotenv
from os import environ

load_dotenv()

class AppConfig():
    mongo_connection = str(environ.get("CONNECTION_STRING"))