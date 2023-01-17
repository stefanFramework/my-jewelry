from config import current_config
from flask_sqlalchemy import SQLAlchemy

database_uri = current_config.SQLALCHEMY_DATABASE_URI
pool_size = current_config.SQLALCHEMY_DATABASE_POOL_SIZE



# from flask_sqlalchemy_session import flask_scoped_session, current_session
# from config import current_config
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# database_uri = current_config.SQLALCHEMY_DATABASE_URI
# pool_size = current_config.SQLALCHEMY_DATABASE_POOL_SIZE
#
# engine = create_engine(database_uri, pool_size=pool_size)
#
# session_factory = sessionmaker(bind=engine)
#
#
def register_session(app):
    db = SQLAlchemy()
    db.init_app(app)

#
#
# def get_session():
#     return current_session()
