import csv
from filmAdvice.settings import APP_MAIN_CURRENT_PATH
from filmAdvice.system.constant import *
from filmAdvice.movie.models import Movie


class LoadDataSets:
    def __init__(self):
        pass

    @staticmethod
    def load_movie_data():
        with open(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_MOVIES_FILE, encoding='utf-8') as f:
            reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                    fieldnames='MovieID::Title::Genres'.split('::'), delimiter='\t')

        for row in reader:

            # movie = Movie(title=row['Title'], genre=row['Genres'])
            print(row)
            # movie.save()
        return reader

    @staticmethod
    def load_link_data():
        with open(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_LINKS_FILE, encoding='utf-8') as f:
            reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                    fieldnames='MovieID::Title::Genres'.split('::'), delimiter='\t')

        for row in reader:
            pass
        return reader

    @staticmethod
    def load_rating_data():
        with open(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_RATINGS_FILE, encoding='utf-8') as f:
            reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                    fieldnames='MovieID::Title::Genres'.split('::'), delimiter='\t')

        for row in reader:
            print(row)
            # rating = Movie(title=row['Title'], genre=row['Genres'])
            # rating.save()
        return reader

    @staticmethod
    def load_tag_data():
        with open(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_TAGS_FILE, encoding='utf-8') as f:
            reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                    fieldnames='MovieID::Title::Genres'.split('::'), delimiter='\t')

        for row in reader:
            print(row)
            # user = Movie(title=row['Title'], genre=row['Genres'])
            # user.save()
        return reader
