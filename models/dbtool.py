# import sqlite3
# import random

# db_path = 'static/hello.sqlite3'

# # ランダムでDBからgreetingを一つ取得
# def get_random_greeting():
#   table = 'greetings'
#   id_list = get_id_list(table)
#   # id一覧からランダムで一つ選びだす
#   random_id = random.choice(id_list)['id']
#   sql = 'SELECT greeting,image_path FROM ' + table + ' WHERE id=' + str(random_id)
#   greeting = execute_sql(sql)
#   # 取得データは一つだけなのでここで0を指定しておく
#   return greeting[0]

# # DBに接続してsqlを実行
# def execute_sql(sql):
#   con = sqlite3.connect(db_path)
#   con.row_factory = sqlite3.Row
#   cur = con.cursor()
#   cur.execute(sql)
#   result = cur.fetchall()
#   con.close()
#   return result

# # 指定したtableのID一覧を取得
# def get_id_list(table):
#   sql = 'SELECT id FROM ' + table
#   id_list = execute_sql(sql)
#   return id_list

meme_list = [
    {
        'description': 'Bug, Panic',
        'image_path': 'https://portfoliopublicimages.s3.amazonaws.com/funny/meme-engineer01.gif'
    },
    {
        'description': 'Due date is getting closer',
        'image_path': 'https://portfoliopublicimages.s3.amazonaws.com/funny/meme-engineer02.gif'
    
    },
    {
        'description': 'First time to give a presentation',
        'image_path': 'https://portfoliopublicimages.s3.amazonaws.com/funny/meme-engineer03.gif'
    
    },
    {
        'description': 'Production deployment without test',
        'image_path': 'https://portfoliopublicimages.s3.amazonaws.com/funny/meme-engineer04.gif'
    
    },
    {
        'description': 'Expect unexpect',
        'image_path': 'https://portfoliopublicimages.s3.amazonaws.com/funny/meme-engineer05.gif'
    
    },
    {
        'description': 'Fix on the fly',
        'image_path': 'https://portfoliopublicimages.s3.amazonaws.com/funny/meme-engineer06.gif'
    
    },
    {
        'description': 'Do not touch anything, it somehow works',
        'image_path': 'https://portfoliopublicimages.s3.amazonaws.com/funny/meme-engineer07.gif'
    
    }
]

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

import random

def get_test_meme():
    memes = session.query(Meme).all()
    if len(memes) <= 0:
        return None
    meme = random.choice(memes)
    return meme

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

