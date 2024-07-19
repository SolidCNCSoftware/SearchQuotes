from sqlalchemy import create_engine, Column, Integer, String, Boolean, MetaData, Table
from sqlalchemy.orm import sessionmaker, declarative_base

# Connection string
server = 'DESKTOP-9FBPMP7\\SQLEXPRESS'  # Your server name
database = 'Translate'  # Your database name
connection_string = 'mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes;'

# Create database engine
engine = create_engine(connection_string)
Base = declarative_base()

# Define table
class Translation(Base):
    __tablename__ = 'English'
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)
    line_number = Column(Integer, nullable=False)
    translatable = Column(Boolean, default=True)

# Create table
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()
