from sqlalchemy import MetaData
from sqlalchemy import create_engine

metadata = MetaData()
engine = create_engine('mysql+pymysql://root:root@localhost/book_catalogue?charset=utf8')
connection = engine.connect()
metadata.create_all(engine)

from sqlalchemy import Column,Table
from sqlalchemy import Integer,String

BookCatalogue = Table('BookCatalogue',metadata,
                      Column('id',Integer(),primary_key=True,autoincrement=True),
                      Column('user_id', Integer()),
                      Column('title',String(200)),
                      Column('author',String(200)),
                      Column('page_count',String(200)),
                      Column('average_rating',String(200)))
Users = Table('Users',metadata,
              Column('id',Integer(),primary_key=True,autoincrement=True),
              Column('username',String(200)),
              Column('password',String(200)))