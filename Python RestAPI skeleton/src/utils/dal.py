from .app_config import AppConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Dal:

    @staticmethod
    def create_session():

        # Create the engine obj which handles the connection
        engine = create_engine(AppConfig.mongo_connection)

        # Create the session factory which activating it creates the session
        session_factory = sessionmaker(bind=engine)

        # Create the session obj
        session = session_factory()
        
        return session