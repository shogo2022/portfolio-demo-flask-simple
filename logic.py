import random

from models.meme import *
from models.settings import session

def get_test_meme():
    memes = session.query(Meme).all()
    if len(memes) <= 0:
        return None
    meme = random.choice(memes)
    return meme


