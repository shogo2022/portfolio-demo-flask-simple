from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base


# mysqlのDBの設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    "meme_user",
    "supersecretpassword",
    "172.16.0.246",
    "memedb",
)
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

# Sessionの作成
session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
