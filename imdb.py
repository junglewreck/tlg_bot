from imdbpie import Imdb
import random
imdb = Imdb()
film =  imdb.top_250()
rnd = (random.randint(0,249))
full = film[rnd]
title = film[rnd].get('title')
poster_full = film[rnd].get('image')
poster_img = poster_full.get('url')
print full
