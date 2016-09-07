from movieinfo import MovieInfo
from urllib2 import urlopen
from json import load

def get_movies():
	#sf open data source: film location in sf
	apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"
	#open the apiUrl and assign data to variable
	response = urlopen(apiUrl)
	json_obj = load(response)
	return json_obj

def convert_to_movieinfo(movie):
	director = movie["director"]
	release_year = movie["release_year"]
	title = movie["title"]
	actor_1 = movie["actor_1"]
	actor_2 = movie["actor_2"]
	location = movie.get("locations")
	new_movie = MovieInfo(director, release_year, title, actor_1, actor_2, location)
	return new_movie

def list_movieinfo(movie_list):
	movies = []
	for movie in movie_list:
		new_movie = convert_to_movieinfo(movie)
		movies.append(new_movie)
	return movies

# print json_obj
def film_2002(json_obj):
	film_2002 = []
	for film in json_obj:
		if film['release_year']== "2002":
			if film['title']not in film_2002:
				film_2002.append(film)

	# film_2002 = sorted(film_2002)
	return film_2002

def main():
	json_obj = get_movies()
	movie_list = film_2002(json_obj)
	movie_list_classes = list_movieinfo(movie_list)

	for movie in movie_list_classes:
		print movie.title, movie.actor_1, movie.actor_2, movie.location, movie.director, movie.release_year


if __name__ == '__main__':
	main()