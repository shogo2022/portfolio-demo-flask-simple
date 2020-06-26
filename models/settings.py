from flask import Flask

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_pyfile('../config.py')


# mysql db connection
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    app.config['DB_USER'],
    app.config['DB_PASSWD'],
    app.config['DB_IPADDRESS'],
    app.config['DB_NAME'],
)
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

# Session
session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

# use in models
Base = declarative_base()
Base.query = session.query_property()
