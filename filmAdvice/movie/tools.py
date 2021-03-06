from filmAdvice.settings import APP_MAIN_CURRENT_PATH
from filmAdvice.system.constant import *
from apiclient.discovery import build
from datetime import datetime
from imdbpie import Imdb


DEVELOPER_KEY = "AIzaSyCKSsxs6Xzxl5tHEOS9RRU5S_2NRGRXvRs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(q, year, max_results=1, order="relevance", token=None, location=None, location_radius=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=q + str(year) + str(" trailer"),
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",  # Part signifies the different types of data you want
        maxResults=max_results,
        location=location,
        locationRadius=location_radius).execute()

    title = []
    videoId = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            title.append(search_result['snippet']['title'])
            videoId.append(search_result['id']['videoId'])

    youtube_dict = {'title': title, 'videoId': videoId}

    return youtube_dict


def get_client():
    client = Imdb()
    return client


def popular_movies():
    return get_client().get_popular_movies()


def crew_info(imdb_id):
    return get_client().get_title_top_crew(imdb_id)


def movie_info(imdb_id):
    return get_client().get_title_credits(imdb_id)['base']


def movie_ratings(imdb_id):
    return get_client().get_title_ratings(imdb_id)


def movie_video(imdb_id):
    return get_client().get_title_videos(imdb_id)


def movie_genres(imdb_id):
    return get_client().get_title_genres(imdb_id)


def save_rate_to_csv(user, movie_id, rate):
    timestamp = int(datetime.now().timestamp())
    writer = open(APP_MAIN_CURRENT_PATH + SYSTEM_APP_PATH + DATASET_TMP_RATINGS_FILE, 'a', encoding='utf-8')
    string = str(user.id) + "," + str(movie_id) + "," + rate + ".0," + str(timestamp) + "\n"
    writer.writelines(str(string))
    writer.close()
