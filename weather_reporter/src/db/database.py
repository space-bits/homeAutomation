import sqlalchemy as sa
import config
from datetime import datetime


engine = sa.create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
# Disable echoing of statements in production
if config.ENV == 'production':
  engine = sa.create_engine(config.SQLALCHEMY_DATABASE_URI)

connection = engine.connect()
metadata = sa.MetaData()

temperatures = sa.Table(
                'temperatures',
                metadata,
                sa.Column('id', sa.Integer(), primary_key=True),
                sa.Column('location', sa.String(255), nullable=False), # Location of sensor
                sa.Column('temperature', sa.Float(), nullable=False), #temperature in celsius
                # Use GMT datetime as yyyy-mm-dd HH:MM:ss+Z
                sa.Column('time', sa.String(50), default=datetime.utcnow().strftime('%Y-%m-%d %H-%M-%S%z+0000'))
              )

""" Creates the connection to a database - either on cloud sql or sqlite3 - and
then creates the required tables and metadata for the app
"""
def init_db():
  metadata.create_all(engine)
