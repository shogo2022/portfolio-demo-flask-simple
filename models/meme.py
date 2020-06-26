import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from models.dbtool import Base
from models.dbtool import ENGINE

class Meme(Base):
    """
    meme item
    """
    __tablename__ = 'item'
    id = Column('id', Integer, primary_key = True)
    description = Column('description', String(20))
    image_path = Column('imaage_path', String(80))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)