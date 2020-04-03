import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#  안가져오고 싶을때 빈 {}
# movie_list = list(db.movies.find({}, {'_id': False}))
# for movie in movie_list:
#     print(movie)

avengers = db.movies.find_one({"title": '어벤져스: 엔드게임'})
same_stars = list(db.movies.find({'star': avengers['star']}))
for movie in same_stars:
    print(movie)

db.movies.update_many({'star': avengers['star']},{'$set': {'star': 0}})
