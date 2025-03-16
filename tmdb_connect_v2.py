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
    download_images(movie_list)
    save_movie_data(movie_list)

def get_popular_movies():
    movies = tmdb.Movies()
    popular_movies = movies.popular(page=1)
    return popular_movies["results"]

def download_images(movie_list):
    for movie in movie_list:
        if not movie["poster_path"]:
            continue
        image_downloader(f"{POSTER_ROOT}{movie['poster_path']}")

        if not movie["backdrop_path"]:
            continue

        image_downloader(f"{BACKDROP_ROOT}{movie['backdrop_path']}")

def image_downloader(image_url):
    image_file_path = f"{IMAGE_LOCAL_CACHE}/{image_url.split('/')[-1]}"
    if os.path.exists(image_file_path):
        return
    
    print(f"Downloading {image_url}...")
    image_data = requests.get(image_url).content

    with open(image_file_path, "wb") as file:
        file.write(image_data)

def save_movie_data(movie_list):
    pass


main()