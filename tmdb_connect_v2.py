import tmdbsimple as tmdb
import os, requests, json
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

POSTER_ROOT = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
BACKDROP_ROOT = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
IMAGE_LOCAL_CACHE = r"C:\Work\PythonSuli\tmdb_images"
MOVIE_DATA_CACHE = os.path.join(IMAGE_LOCAL_CACHE, "movie_data.json")

def main():
    movie_list = get_popular_movies()
    download_posters(movie_list)
    download_backdrops(movie_list)
    save_movie_data(movie_list)

def get_popular_movies():
    pass

def download_posters(movie_list):
    pass

def download_backdrops(movie_list):
    pass

def image_downloader(image_url):
    pass

def save_movie_data(movie_list):
    pass


main()