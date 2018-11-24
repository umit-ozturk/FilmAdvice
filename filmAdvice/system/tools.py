import csv
from filmAdvice.settings import APP_MAIN_CURRENT_PATH
from filmAdvice.system.constant import *


def find_imdb_link_for_movie_id(movie_id):
    with open(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_LINKS_FILE, encoding='utf-8') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='movieId,imdbId,tmdbId'.split(','), delimiter='\t')
    for row in reader:
        if row["movieId"][0] == movie_id:  # imdb_link = "https://www.imdb.com/title/tt" + str(imdb_id) + "/"
            imdb_id = 'tt' + str(row["movieId"].split(",")[1])
            return imdb_id
    return None